# Eping Filters

## Introduction

This project allows users to:
- Pull SBS and TBT notifications from Eping
- Apply both inclusion and exclusion filters
- Output to .csv file

It uses an undocumented JSON API the web search relies on, though it shouldn't break it's at the mercy of Eping changing their website around. There are numerous checks in place to stop the script and alert users if this happens.

## Why

WTO Technical Barrier Group decided that the best mechanism for handling large volumes of notifications is emails. Yes, they provide server side filtering, but if you need more control you're gonna have to get to scraping those emails...

Or you could use the undocumented API they use for their search functionality on the website, which helpfully supports JSON (thanks). That's the approach this script uses.

"Why don't you just use their server side filters and the email service"
- Because if you want multiple distinct filters you must create multiple subscriptions
- Can't process historical data, emails come in then and now
- Can't automate pulling data out of emails
- Open-ness includes the ability to create scripts and applications, like this, that process said open data.

## To use

- Install Python 3.x (this has been tested with 3.7) from [here](https://www.python.org/downloads/).
- Download this repository, by clicking **Code** in the top right and **Download Zip**. Alternatively use `git clone https://github.com/DavidFair/eping_filter.
- Open *parse_eping_data.py* in a text editor, change the dates to a range your interested in
- Run the script using Python 3, either `python3 parse_eping_data.py` in a CLI, or by Right Clicking and running with Python
- This will produce a single file *included_{dates}.csv* with the date range specified and all data.
- If filters are specified an *excluded_{dates}.csv* is also produced with excluded notifications.
- These CSV files are optimised to be opened in OpenOffice Calc or Microsoft Excel.

## Filtering
- To filter data simply open *filters.py* in a text editor. The example filter shows how new entries can be set
- Filters will match any word in the user set, with any word provided by the result. 

For example, the following will match with "United States of America", "United Kingdom", "United Arab Emirates"...etc. and "France".

```
IssuingCountry: Set[str] = {"United", "France"}
```

- If not entries are provided, or returned from Eping (i.e. the issuing country is empty) it will **not** be filtered out.

### Boolean values

Boolean values, such as true or false, should use the original types instead of bug-prone strings. For example to only look at SPS notifications:

```
IsSPS: Set[str] = {False}  # Notice no " " characters
```

### ExcludeFilter
Any keywords entered within this filter will cause the entry to be removed if they appear anywhere in the entry.  If the category is blank the entry is kept regardless of any included keywords.

Note:
A *keyword* is delimited by "", that is to say:

```
IssuingCountry: Set[str] = {"United Kingdom"}
```

Will only filter out records containing "United Kingdom", not United States for example. Whilst

```
IssuingCountry: Set[str] = {"United", "Kingdom"}
```
Will filter out any country with the words United, or Kingdom anywhere in the issuing country name.


### IncludeFilter
Any keywords entered within this filter must appear in the record for it to be kept. The IncludeFilter follows the same rules as the ExcludeFilter; blank categories are kept and words are delimited by " ".
