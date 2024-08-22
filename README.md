# MusicData
I scraped the Boston Symphony Orchestra performance history 
API to obtain a complete performance history of the orchestra. 

I analyzed the data using pandas in a Jupyter notebook.

Here are some results

Top 5 Most Played Works:

| Rank | Performances | Composer and Work                                                       |
|------|--------------|-------------------------------------------------------------------------|
| 1    | 506          | Johannes Brahms, Symphony No.   2 in D major, Op. 73                    |
| 2    | 496          | Ludwig van Beethoven, Symphony No.  7 in A major, Op. 92                |
| 3    | 486          | Ludwig van Beethoven, Symphony No.  5 in C minor, Op. 67                |
| 4    | 483          | Ludwig van Beethoven, Symphony No.  3 in E-flat major, Op. 55, "Eroica" |
| 5    | 475          | Johannes Brahms, Symphony No.   1 in C minor, Op. 68                    |

Top 5 Most Played Violin Concertos:

| Rank | Performances | Composer and Work                                                |
|------|--------------|------------------------------------------------------------------|
| 1    | 235          | Ludwig van Beethoven, Concerto for Violin in D major, Op. 61     |
| 2    | 209          | Johannes Brahms, Concerto for Violin in D major, Op. 77          |
| 3    | 177          | Pyotr Ilyich Tchaikovsky, Concerto for Violin in D Major, Op. 35 |
| 4    | 165          | Felix Mendelssohn, Concerto for Violin in E minor, Op. 64        |
| 5    | 117          | Jean Sibelius, Concerto for Violin in D minor, Op. 47            |

## Symphonies with APIs/Interfaces
- BSO: https://archives.bso.org
- NyPhil: https://github.com/nyphilarchive/PerformanceHistory/
- Amsterdam Orchestra: https://archief.concertgebouworkest.nl/en/archive/search/
- Cleveland: https://www.clevelandorchestra.com/discover/archives/ (reached out)
- LA: https://www.laphil.com/about/la-phil/archives-services (reached out)
- Phil Orch: (reached out)
- Inspiration: https://www.reddit.com/r/classicalmusic/comments/1apv9qo/100_mostfrequently_performed_symphonies_at/

## Useful Links
- Python json library: https://docs.python.org/3/library/json.html
- Waiting on specific element in selenium: https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python?noredirect=1&lq=1
- Exclude none from json/dict: https://stackoverflow.com/questions/4255400/exclude-empty-null-values-from-json-serialization
- Pandas dataframes (for future): https://stackoverflow.com/questions/57067551/how-to-read-multiple-json-files-into-pandas-dataframe
- More Pandas dataframes: https://avithekkc.medium.com/how-to-convert-nested-json-into-a-pandas-dataframe-9e8779914a24
- Count Occurrences of Value in Column https://www.geeksforgeeks.org/how-to-count-occurrences-of-specific-value-in-pandas-column/

## Libraries Used
- Selenium Wire: https://pypi.org/project/selenium-wire/#response-objects
- Selenium: https://pypi.org/project/selenium/