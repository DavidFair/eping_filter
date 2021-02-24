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

import csv
from typing import Dict, List


def write_out_csv_data(to_write: List[Dict], file_name):
    if len(to_write) == 0:
        return

    headers = to_write[0].keys()
    with open(file_name, newline='', mode='w') as csv_handle:
        writer = csv.DictWriter(csv_handle, dialect='excel', fieldnames=headers, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for entry in to_write:
            writer.writerow(entry)