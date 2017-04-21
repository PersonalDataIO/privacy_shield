# Privacy Shield scraper

This is a scraper for the data held by the [privacyshield.gov](http://www.privacyshield.gov) website. 
The scraper was originally developed by Petter Reinholdtsen, and has been uploaded to GitHub by Paul-Olivier Dehaye. 

## Privacy Shield arrangement

Privacy Shield is a transatlantic arrangement between the United States and the European Union (actually, the European Economic Area and separately Switzerland), meant to ensure data transferred from Europe would be adequately protected once it landed in the US. It is also the name of the corresponding programme (actually two-fold, with one for the EEA and one from Switzerland), under which US companies can commit in front of the Federal Trade Commission to respect the Privacy Shield principles. A [similar scraper](https://github.com/pdehaye/safe-harbor) has been built by Dehaye for the previous arrangement, Safe Harbor.

## Running the scraper

Make sure to install the requirements first `pip install -r requirements.txt`. The scraper can be run very simply by running `privacy_shield.py`, and simply outputs a stream of JSON files. Ideally a separate repository would hold the historical data. 



