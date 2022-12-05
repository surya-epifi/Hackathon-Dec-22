# Hackathon-Dec-22
## Keynote
https://docs.google.com/presentation/d/1XCEqgdK15OP_k05TNkmDgH1Dx98PM_MQh8OX3UqF8Vk/edit?usp=sharing
 
## Problem statement: 
https://docs.google.com/document/d/1-NKEs5yQ6TSa-c-5OlnNXGH9dvGDNRylW59zX37csAY/edit

## Pre-requisites
#### -> Image Processing
`pip3.9 install -r requirements.txt`
#### -> Image Processing
`brew install tesseract`
#### -> Sentiment analysis
`pip3.9 install -U textblob`
`python3.9 -m textblob.download_corpora`
#### -> Phone number analysis
`pip3.9 install phonenumbers`
#### -> SNScrape
`pip3.9 install git+https://github.com/JustAnotherArchivist/snscrape.git`
#### -> Django
`python3.9 -m pip install django`

## Run 
`python3.9 manage.py shell < start.py`

## Generate CSV
`python3.9 manage.py shell < present.py`
Output Path: `ScammerHunt/scammers_list.csv`

## Useful commands
#### -> Install python 3.8
`brew update`
`brew install pyenv`
`pyenv install 3.9.0`
#### -> Save new requirements
`pip3.9 freeze > requirements.txt`
#### -> uninstall all modules
`pip3.9 freeze | xargs pip uninstall -y`
#### -> Runserver
`python3.9 manage.py runserver 0.0.0.0:2200`
#### -> Django admin
`http://0.0.0.0:2200/admin/`
username: `team`
password: `team`
