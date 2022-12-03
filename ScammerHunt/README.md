## update requirement
pip3 freeze > requirements.txt

## Install all requrements
pip3 install -r requirements.txt

## other modules
brew install tesseract

## Sentiment analysis
pip install -U textblob
python -m textblob.download_corpora

## Install python 3.8
brew update
brew install pyenv
pyenv install 3.9.0

## SNScrape
pip3.9 install git+https://github.com/JustAnotherArchivist/snscrape.git

## uninstall all modules
pip3.9 freeze | xargs pip uninstall -y

## Django
python3.9 -m pip install django

## Runserver
python3.9 manage.py runserver 0.0.0.0:2200

## Run 
python3.9 manage.py shell < start.py

## Run presenter
python3.9 manage.py shell < present.py

