# MusicData

## Symphonies with APIs/Interfaces
- BSO: https://archives.bso.org
- NyPhil: https://github.com/nyphilarchive/PerformanceHistory/
- Amsterdam Orchestra: https://archief.concertgebouworkest.nl/en/archive/search/
- Cleveland: https://www.clevelandorchestra.com/discover/archives/ (reached out)
- LA: https://www.laphil.com/about/la-phil/archives-services (reached out)
- Phil Orch: Reached out to anna
- Inspiration: https://www.reddit.com/r/classicalmusic/comments/1apv9qo/100_mostfrequently_performed_symphonies_at/
- 
## Next Steps
- Read JSON from BSO website and put it into a single JSON file
- Write each season to a separate file (will use subprocess), then combine later with Python
- Work with JSON file (or part of the file using Pandas)
- Season runs ~October to May

1. Gather Data
2. Clean data

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

## Thoughts

To recreate most popular symphonies chart, simply create list of all works in dataframe and then get the count for each one

## Questions
Who are the most popular composers? Works of those composers?
Most popular solo instrument?
Trends in performances over time?

```json
{
      "orchestra": "New York Philharmonic",
      "season": "2014-15",
      "concerts": [
        {
          "eventType": "Subscription Season",
          "Location": "Manhattan, NY",
          "Venue": "Avery Fisher Hall",
          "Date": "2014-11-29T05:00:00Z",
          "Time": "8:00PM"
        }
      ],
      "works": [
        {
          "ID": "11196*",
          "composerName": "Wagenaar,  Johan",
          "workTitle": "CYRANO DE BERGERAC, OVERTURE, OP. 23",
          "conductorName": "van Zweden, Jaap",
          "soloists": []
        },
        {
          "ID": "3500*",
          "composerName": "Korngold,  Erich",
          "workTitle": "CONCERTO, VIOLIN, D MAJOR, OP.35",
          "conductorName": "van Zweden, Jaap",
          "soloists": [
            {
              "soloistName": "Hahn, Hilary",
              "soloistInstrument": "Violin",
              "soloistRoles": "S"
            }
          ]
        }
      ]
    }
```