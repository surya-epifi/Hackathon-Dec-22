import re
import io
import requests
from ScammerHuntCore.models import Scammer, ScrapeData
import pytesseract
from PIL import Image
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from textblob import TextBlob

def get_phone_number(text):
    result = []
    numbers = re.findall(r'(?:\+\s*\d{2}[\s-]*)?(?:\d[-\s]*){10}', text)
    for number in numbers:
        number = ''.join(number.split())
        number = number.replace('\r\n', ' $ ')
        number = number.replace('-', '')
        result.append(number[-10:])
    return result

# testing
# numbers = get_phone_number("I recieved a message from +91 81471 21834 for Bescom payment and asked me to install team viewer quicksupport to take control of my phone. This seems to be a fraud")
# print(numbers)

def imageToText(url):
    # Defining paths to tesseract.exe
    # and the image we would be using
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get(url, headers=headers)

    img = Image.open(io.BytesIO(r.content))

    text = pytesseract.image_to_string(img)
    #
    return text

  
# testing
# text = imageToText("https://pbs.twimg.com/media/FiZ8PQKVQAEOkaC?format=jpg&name=small")
# print(text)

def get_upi_ids(text):
    upiHandles = ["apl", "yapl", "abfspay", "abfspay", "fbl", "axisb", "idfcbank", "icici", "okaxis", "okhdfcbank", "okicici", "oksbi", "axisbank", "jupiteraxis", "icici", "indus", "ikwik", "ybl", "ibl", "axl", "pingpay", "icici", "sliceaxis", "kmbl", "tapicici", "timecosmos", "yesbank", "idfcbank", "waicici", "icici", "waaxis", "wahdfcbank", "wasbi", "yesbank"]
    words = text.split(' ')
    identifiedUpiHandles = []
    for word in words:
        word = word.replace('.', '')
        upi = word.split('@')
        try:
            if upi[1] in upiHandles:
                identifiedUpiHandles.append(word)            
        except IndexError:
            pass
    return identifiedUpiHandles

# Testing
# upires = get_upi_ids("Hello my upi id is abc@okhdfcbank.")            
# print(upires)

def get_sentiment_score(content):
    blob = TextBlob(content)
    total_sentiment_polarity = 0
    for sentence in blob.sentences:
        total_sentiment_polarity += sentence.sentiment.polarity
    average_sentiment_polarity = total_sentiment_polarity / len(blob.sentences)
    return average_sentiment_polarity

def get_info_from(phone_number):
    mobileNo=phonenumbers.parse(phone_number)
    timezone_value = timezone.time_zones_for_number(mobileNo)
    carrier_value = carrier.name_for_number(mobileNo,"en")
    geocoder_value = geocoder.description_for_number(mobileNo,"en")
    
    return (timezone_value, carrier_value, geocoder_value)
    

def clearAllData():
    ScrapeData.objects.all().delete()
    Scammer.objects.all().delete()

clearAllData()