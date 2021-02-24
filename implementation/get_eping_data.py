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

import requests

# Upper bound for how many items we will request per query
ENDPOINT_URL = r"https://www.epingalert.org/api/Notifications/SearchNotifications"
MAX_ITEMS_PER_REQ = 1000


def create_template_request_headers():
    return {"Accept-Language": "en",
            "Accept": "application/json"}


def create_post_request(start_date, end_date):
    # Where None == Wildcard
    return {"Title": None,
            "Issued": f"{start_date}-{end_date}",
            "FilterSPS": None,
            "PageNumber": 1,
            "PageSize": MAX_ITEMS_PER_REQ
            }


def request_data(start_date, end_date):
    # Assumes all entries between given dates are required
    post_request = create_post_request(start_date, end_date)
    req = requests.post(url=ENDPOINT_URL,
                        data=post_request,
                        headers=create_template_request_headers())
    parsed_data = req.json()
    print(f"Found {len(parsed_data.get('Notifications', []))} notifications")
    return parsed_data
