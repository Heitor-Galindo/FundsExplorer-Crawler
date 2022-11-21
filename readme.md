# FundsExplorer Crawler

***DISCLAIMER! THIS CRAWLER IS ONLY FOR STUDY PURPOSES!***

## FII Ranking ETL

Extract data from <https://www.fundsexplorer.com.br/ranking> \
Transform/Clean simbols and latib characters \
Load data to `database/fii_table.csv` \

## Install instructions

``` sh
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Running

Print a dataframe with the csv content.

```sh
python3 runner.py
```
