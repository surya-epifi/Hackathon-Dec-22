# Hackathon-Dec-22
https://docs.google.com/presentation/d/1XCEqgdK15OP_k05TNkmDgH1Dx98PM_MQh8OX3UqF8Vk/edit?usp=sharing

Ref: 
Problem statement: https://docs.google.com/document/d/1-NKEs5yQ6TSa-c-5OlnNXGH9dvGDNRylW59zX37csAY/edit


## update requirement
pip3 freeze > requirements.txt

## Install all requrements
pip3 install -r requirements.txt

## other modules
brew install tesseract

## Sentiment analysis
pip install -U textblob
python -m textblob.download_corpora

## Phone number analysis
pip3.9 install phonenumbers

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

## Django admin
http://0.0.0.0:2200/admin/
username: team
password: team

## Run 
python3.9 manage.py shell < start.py

## Run presenter
python3.9 manage.py shell < present.py

