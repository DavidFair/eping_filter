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

from implementation import request_data, FilterResults, write_out_csv_data
from filters import ExcludeFilter, IncludeFilter

if __name__ == "__main__":
    # This must me DD/MM/YY - you can thank eping for not using ISO Standards ....
    start_date = "02/02/21"
    end_date = "03/02/21"

    data = request_data(start_date, end_date)
    filterer = FilterResults(ExcludeFilter(), IncludeFilter())
    included, excluded = filterer.filter_data(raw_data=data)

    # Append -Start_date-end_date
    suffix = f"-{start_date.replace('/', '_')}-{ end_date.replace('/', '_')}"
    write_out_csv_data(included, f"included-{suffix}.csv")
    write_out_csv_data(excluded, f"excluded-{suffix}.csv")
