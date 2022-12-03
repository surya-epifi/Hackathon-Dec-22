## update requirement
pip3 freeze > requirements.txt

## Install all requrements
pip3 install -r requirements.txt


## Install python 3.8
brew update
brew install pyenv
pyenv install 3.9.0

## SNScrape
pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

## uninstall all modules
pip3 freeze | xargs pip uninstall -y