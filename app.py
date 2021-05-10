from sendEmail import sendEmail
from analysis import dataAnaly
from getData import getData
from dotenv import load_dotenv
import os

load_dotenv()

data = getData()

dataAnaly(data)

emails = os.getenv('RECEIVER_EMAILS')
emails = emails.split(' ')

for email in emails:
    sendEmail(email, data)
