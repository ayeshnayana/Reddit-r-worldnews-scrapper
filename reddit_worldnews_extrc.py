# Web scrapping from reddit for worldnews
# This program will webscrape the subreddit r/worldnews and send an automated email with the links to the stories

import requests  # For http requests

from bs4 import BeautifulSoup  # For web scraping

import smtplib  # To send the email

# To create the email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import csv

# For system date and time manipulation
import datetime

# when sending the email we need the appropriate date on the heading
# To do that we need to get the current date and time
# Also, we can make sure now that the same email will not be repeated everyday
now = datetime.datetime.now()

# Create a empty python string object
# This is a placeholder for the email content
content = ''

def extract_worldnews(url):
    print('Extracting Hacker News Stories')
    # Create a placeholder for the content
    cnt = ''
    # create the email heading by passing the heading into the placeholder
    cnt += ('<b>r\worldnews:</b>\n'+'<br>'+'-'*50+'<br>')
    # Create the body of the email

    # get the content in the url using the requests and store the info in response
    response = requests.get(url)
    # In the object response there is a method called content.
    # We use the method content to get the content in the response
    content = response.content # This content is a local field inside the request class

    soup = BeautifulSoup(content, 'html.parser') # Create a soup of text from the website

    # We want to extract only the table (tb) and the title
    # Using valign we can seperate from one link to another link
    # Since python starts from zero, we need "i+1"
    #cards = soup.find_all('div', {'data-click-id':'body'})
    #print(len(cards))
    #card = cards[0]
    #print(card.a.get('href'))
    #atag = card.find_all('a').get('href')
    #print(card.h3.text.strip())
    for i, tag in enumerate(soup.find_all('div', {'data-click-id':'body'})):
        # To format the output nicely we use "::"
        # We dont want the "more" art the end of the website so tag.text != 'More'
        cnt +=((str(i+1)+' :: '+tag.h3.text.strip() + tag.a.get('href') + "\n" + '<br>'))
    return(cnt)

url = 'https://www.reddit.com/r/worldnews/'
content = extract_worldnews(url)
print(content)