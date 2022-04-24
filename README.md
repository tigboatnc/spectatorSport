# Spectator Sport
what in the love of god is media doing? 

> NLP based analysis and insight experiments on the US media and its reporting on the Russian invasion of Ukraing (2022)

## Notebooks 
|Notebook|Description|Date|
|-|-|-|
|[1-raw_processing](./notebooks/1-raw_processing.ipynb)|Cleaning raw data and adding reporting time column|04-11-22|
|[2-find_reporting](./notebooks/2-find_reporting.ipynb)|EDA|04-11-22|
|[3-2-corpus_generation_selenium](./notebooks/3-2-corpus_generation_selenium.ipynb)|Scraping references from website|04-11-22|

## Data
|Data|Description|Date|
|-|-|-|
|[Raw Scrape](./data/raw/)|Raw data from telegram, twitter, facebook etc. which is geotagged|04-11-22|
|[input-data.csv](./data/processed/input-data.csv)|Processing of Raw Scrape Data|04-11-22|
|[articles/*.csv](./data/processed/articles/)|Scraped Articles Per Reference |04-11-22|


## Todo 
- [] Sync notebook 1 for operating on new file names `samarth` <_only mac support rn_>
## People 
Neg [git](https://github.com/tigboatnc) <br/>
Geog [git](https://github.com/SwagYangJH) <br/>
Overtak [git](https://github.com/HenryVarro666) <br/>


```shell 
python -m spacy download en_core_web_md
python -m spacy download en_core_web_sm

```

## Good References 
|Type|Link|Reference|Thoughts|
|-|-|-|-|
|`paper`|[Detection of hyperpartisan news articles using natural language processing technique](./literature_review/Detection%20of%20hyperpartisan%20news%20articles%20using%20natural%20language%20processing%20technique.pdf)|[Elsevier](https://reader.elsevier.com/reader/sd/pii/S2667096822000088?token=A954ACDD1DD6A04D8CB01231618FCF95062684BC29388056A2A2387BD71B569D1F287C61EDB98424E8519326768CD3C2&originRegion=us-east-1&originCreation=20220424203741)|NA|