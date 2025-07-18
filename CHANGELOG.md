# Version History

## As of yet unversioned changes
# 3.0.5
- Bugfix for identifying strains
- Extend log length

## 3.0.4
- Added basic logging (logs/repeatanalyzer.log)

## 3.0.3
- Bugfix: build will now expect files to be in the executable directory (rather than hidden system dir)

## 3.0.2
* Build macOS app with py2app

## 3.0.1

* Refactoring and cleanup (no functional changes)
* Build with pyinstaller

## 3.0.0

* Import code to github and reformat readme
* Move version log to its own file
* Convert code to python 3
* Update Geocoding to using geopy (rather than google maps) for less restrictive rate limits
* Bugfixes lingering from transition (file encoding, changes to mapping and geocoding)
* Unit tests for geocoding utils and Location class

## 2.8

* Improvements on DNA reading
  * Incorrect codons are now replaced with X Rather than individual incorrect nucleotides being removed
  * Added reverse frames
* General updates to AllData for accuracy
*Please be sure to reload from scratch (delete RepeatAnalyzer.dat)*

## 2.7.7

* Minor bug fixes
* Repeat search can now support multiple repeats in Fasta
* Note: This is one of the last version releases before publication.
  In the near future, updates will largely be bug fixes*

## 2.7.6

* Added frequency printout in genetic diversity results
  * Genetic Diversity Search results are now in a new window
  * Minor Tweaks to Genetic diversity plot

## 2.7.5

* Added support for coordinate locations. now you can enter locations for strains as either country, province, county or coordinates.
* For best results, delete RepeatAnalyzer.dat and reload all data. (This prevents duplicate country names)
  *Note: All locations now only go down to the granularity of county for consistency. This may be changed in the future, if necessary.*

## 2.7.4

*!!NOTE!! If you experience issues, delete RepeatAnalyzer.dat and load data from source files again"

* Added supersets and similar repeats to repeat search
  * supersets shows any repeats the searched repeat is a subset of
  * for similar repeats, enter a number for the maximum distance on the search window
    and all repeats within that edit distance will be shown (0 will return no matches)
* Fixed minor offset bug introduced to species selection in 2.7.2

## 2.7.3

* Filenames no longer require an extension (unless it is something other than .txt)
  *note: program assumes any file name with '.' includes extension*
* New windowed interface on the 'search by' functions for ease of copy/pasting
* all windows open new processes (meaning they can be left open after the parent window closes, and multiple can be run at once)
* locations are now selected by dropdown (alphabetical a-z)

## 2.7.2

* popup windows now (almost all) run in separate processes
* allowed more flexible input y or Y for y/n options
* species can be added from the change species menu
* identify strain starts on the correct species

## 2.7.1

* Fixed a conflict causing searched not to return full results
* Added global uniformity value
* Added local uniformity value
* Clarified some user output
* Added functionality to show all repeats unique to a region
* Changed 'calculate genetic diversity' to 'regional diversity analysis'
!It is highly recommended you use this version over earlier versions!

## 2.7 One major bug fix on data input

* Several QoL fixes including the ability to identify the repeats from multiple isolates in one go (must be in FASTA),
crash prevention on erroneous input, and correction of some errors in the data.
It is highly recommended you use this version over earlier versions and reload any data you are using (as it may have mistakes).
You can still use the same input file.

## 2.6.2

* Corrected coordinate reference system (crs) of map so that state and country borders align properly.

## 2.6.1

* Added more flexibility when entering location names. Search now accepts strings like "usa, texas" in place of "U. S. A., Texas"
