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

from typing import NamedTuple, Set

"""
class ExampleIncludeFilter(NamedTuple):
    # This is provided as an example of how to use a filter, if a word matches anywhere we will include (in this case)
    # We must match one of these to keep an entry
    IsSPS = {False}  # We only want non-sps entries
    AffectedCountries = {"United"}  # Must have United anywhere in the name, e.g. United States, United Kingdom...etc.
    AffectedCountriesIDs: Set[str] = {}
    AffectedCountriesAlternativeNames: Set[str] = {}
    # <Empty fields omitted for brevity>
    ProductsFreeText = {"banana", "pesticides", "chemicals"}  # If ANY of banana, pesticides or chemicals appears we keep it 
    HasInternationalActivity = {True}  # We only want entries with international activity
"""


class ExcludeFilter(NamedTuple):
    # If any of these match we discard
    ID: Set[str] = {}
    DocumentSymbol: Set[str] = {}
    IsSPS: Set[str] = {}
    DocumentTitle: Set[str] = {}
    NotificationTypeName: Set[str] = {}
    NotificationType: Set[str] = {}
    DescriptionOfContent: Set[str] = {}
    NotifyingCountryName: Set[str] = {}
    NotifyingCountryID: Set[str] = {}
    DateOfDistribution: Set[str] = {}
    FinalDateForComment: Set[str] = {}
    DateModified: Set[str] = {}
    LinkEN: Set[str] = {}
    LinkFR: Set[str] = {}
    LinkES: Set[str] = {}
    AgencyReponsible: Set[str] = {}
    Keywords: Set[str] = {}
    KeywordsIDs: Set[str] = {}
    Objectives: Set[str] = {}
    ObjectivesIDs: Set[str] = {}
    AffectedCountries: Set[str] = {}
    AffectedCountriesIDs: Set[str] = {}
    AffectedCountriesAlternativeNames: Set[str] = {}
    AlternativeCountryNames: Set[str] = {}
    HSProducts: Set[str] = {}
    ICSProducts: Set[str] = {}
    ProductsFreeText: Set[str] = {}
    IsUserNotified: Set[str] = {}
    DocumentLinks: Set[str] = {}
    ExtractedDocumentLinks: Set[str] = {}
    RelatedNotifications: Set[str] = {}
    EnquiryPoints: Set[str] = {}
    InterfaceLanguage: Set[str] = {}
    IsTranslation: Set[str] = {}
    IsAdminRegistered: Set[str] = {}
    HasInternationalActivity: Set[str] = {}


class IncludeFilter(NamedTuple):
    # We must match at least one of these to be included
    ID: Set[str] = {}
    DocumentSymbol: Set[str] = {}
    IsSPS: Set[str] = {}
    DocumentTitle: Set[str] = {}
    NotificationTypeName: Set[str] = {}
    NotificationType: Set[str] = {}
    DescriptionOfContent: Set[str] = {}
    NotifyingCountryName = {}
    NotifyingCountryID: Set[str] = {}
    DateOfDistribution: Set[str] = {}
    FinalDateForComment: Set[str] = {}
    DateModified: Set[str] = {}
    LinkEN: Set[str] = {}
    LinkFR: Set[str] = {}
    LinkES: Set[str] = {}
    AgencyReponsible: Set[str] = {}
    Keywords: Set[str] = {}
    KeywordsIDs: Set[str] = {}
    Objectives: Set[str] = {}
    ObjectivesIDs: Set[str] = {}
    AffectedCountries: Set[str] = {}
    AffectedCountriesIDs: Set[str] = {}
    AffectedCountriesAlternativeNames: Set[str] = {}
    AlternativeCountryNames: Set[str] = {}
    HSProducts: Set[str] = {}
    ICSProducts: Set[str] = {}
    ProductsFreeText: Set[str] = {}
    IsUserNotified: Set[str] = {}
    DocumentLinks: Set[str] = {}
    ExtractedDocumentLinks: Set[str] = {}
    RelatedNotifications: Set[str] = {}
    EnquiryPoints: Set[str] = {}
    InterfaceLanguage: Set[str] = {}
    IsTranslation: Set[str] = {}
    IsAdminRegistered: Set[str] = {}
    HasInternationalActivity: Set[str] = {}
