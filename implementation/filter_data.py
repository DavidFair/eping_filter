#
# This file is part of the eping_filter package (https://github.com/DavidFair/eping_filter).
# Copyright (c) 2021 David Fairbrother.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from enum import Enum
from typing import Set, List, Dict


class FilterMethod(Enum):
    INCLUDE = 1
    EXCLUDE = 2


class FilterResults:
    def __init__(self, exclude_filter, include_filter):
        self._exclude_filter = exclude_filter
        self._include_filter = include_filter

    def filter_data(self, raw_data: dict):
        notifications = raw_data.get("Notifications", [])
        if len(notifications) == 0:
            return

        notifications = self._convert_raw_data_to_list(notifications)
        included, excluded = self._apply_filter(self._include_filter, FilterMethod.INCLUDE, notifications)
        print(f"After include filter: Excluded {len(excluded)}\t Included {len(included)}")

        included, excluded_tmp = self._apply_filter(self._exclude_filter, FilterMethod.EXCLUDE, included)
        excluded.extend(excluded_tmp)
        print(f"After exclude filter: Excluded {len(excluded)}\t Included {len(included)}")
        print(f"Kept {len(included)}, {round(len(included) / len(notifications) * 100)}%")

        assert (len(notifications) == len(included) + len(excluded)), \
            "Partitioned number of items out does not match the number of items in!"

        included = self._convert_to_singular_items(included)
        excluded = self._convert_to_singular_items(excluded)

        return included, excluded

    @staticmethod
    def _convert_raw_data_to_list(notifications: List[Dict]):
        # Convert mixed types all to List[mixed] - I know we should keep typing info but lets keep only string filtering
        for i in notifications:
            for key, val in i.items():
                if not isinstance(val, List):
                    i[key] = [val]
        return notifications

    @staticmethod
    def _convert_to_singular_items(processed: List[Dict]):
        # Flatten out empty lists + 1 items lists to both None and scalar types
        for entry in processed:
            for key, val in entry.items():
                if len(val) == 0:
                    entry[key] = None
                elif len(val) == 1:
                    entry[key] = val[0]
        return processed

    @staticmethod
    def _should_keep_item(method_select: FilterMethod, user_keywords: Set[str], data_item, field_name):
        to_search = data_item[field_name]
        if not to_search or not user_keywords:
            return True  # We can't tell so always keep it

        assert isinstance(user_keywords, Set), f"Expected a set of filters, got a {repr(user_keywords)} instead"
        # Yes, we could do this with filters and fancy code, but complexity == bugs...
        is_in_result = any(str(user_word) in str(external_data)
                           for user_word in user_keywords
                           for external_data in to_search)
        if method_select is FilterMethod.EXCLUDE:
            # If we are excluding we should not keep the item if we matched
            is_in_result = not is_in_result
        return is_in_result

    def _apply_filter(self, filter_object, filter_type: FilterMethod, included_list: List[Dict]):
        excluded = []
        for field_name in filter_object._fields:
            if len(included_list) == 0:
                break  # Nothing left to do
            self._check_format_matches(field_name, included_list)
            user_selection = getattr(filter_object, field_name)

            # Filter item by item
            for item in included_list:
                should_keep = self._should_keep_item(filter_type, user_selection, item, field_name)
                if not should_keep:
                    excluded.append(item)
            # Pop excluded items out, when were not in the loop
            included_list = [i for i in included_list if i not in excluded]
        return included_list, excluded

    @staticmethod
    def _check_format_matches(field_name, notifications):
        assert field_name in notifications[0], \
            f"The returned result is missing {field_name}, key names are \n" \
            f"{notifications[0].keys()}"
