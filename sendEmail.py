import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getData import getData
import os
from dotenv import load_dotenv

load_dotenv()


def sendEmail(email, data):
    try:
        sender_address = os.getenv('EMAIL_ID')
        sender_pass = os.getenv('PASSWORD')
        receiver_address = email
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'COVID Data for the day'

        # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        htmlData = """
        <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=PT+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap"
      rel="stylesheet"
    />
  </head>
  <body style="font-family: 'PT Sans', sans-serif;">
    <p>
      Here is the COVID data. Please wear a mask and if eligible take your
      vaccine shots
    </p>
    <table border="1px solid black">
      <tr>
        <td style="font-weight: bold">Data Description</td>
        <th style="font-weight: bold">Count</th>
      </tr>
      <tr>
        <td
          style="font-weight: bold; background-color: #ff6666; color: #ffffff"
        >
          Karnataka Places Counts
        </td>
      </tr>
      <tr>
        <td>Bangalore Count</td>
        <th>{0}</th>
      </tr>
      <tr>
        <td>Mangalore Count</td>
        <th>{1}</th>
      </tr>
      <tr>
        <td>Udupi Count</td>
        <th>{2}</th>
      </tr>
      <tr>
        <td>Shimoga Count</td>
        <th>{3}</th>
      </tr>
      <tr></tr>
      <tr>
        <td>Mysuru Count</td>
        <th>{4}</th>
      </tr>
      <tr></tr>
      <tr>
        <td>Kodagu Count</td>
        <th>{5}</th>
      </tr>
      <tr>
        <td>Karnataka Total Count</td>
        <th>{6}</th>
      </tr>
      <tr>
        <td style="font-weight: bold; background-color: #ff6666; color: #ffffff">Kerala Places Counts</td>
      </tr>
      <tr>
        <td>Kasargod Count</td>
        <th>{7}</th>
      </tr>
      <tr>
        <td>Wayanad Count</td>
        <th>{8}</th>
      </tr>
      <tr>
        <td>Kerala Total Count</td>
        <th>{9}</th>
      </tr>
      <tr>
        <td
          style="font-weight: bold; background-color: #ff6666; color: #ffffff"
        >
          Death Count across Karnataka
        </td>
      </tr>
      <tr>
        <td>Mangalore Deaths</td>
        <th>{10}</th>
      </tr>
      <tr>
        <td>Bangalore Urban Deaths</td>
        <th>{11}</th>
      </tr>
      <tr>
        <td>Mysuru Deaths</td>
        <th>{12}</th>
      </tr>
      <tr>
        <td>Shimoga Deaths</td>
        <th>{13}</th>
      </tr>
      <tr>
        <td>Kodagu Deaths</td>
        <th>{14}</th>
      </tr>
     
      <tr>
        <td
          style="font-weight: bold; background-color: #ff6666; color: #ffffff"
        >
          India Overall Count
        </td>
      </tr>
      <tr>
        <td>India Count</td>
        <th>{15}</th>
      </tr>
    </table>
    <p>Stay safe and indoors.</p>
  </body>
</html>


        """.format(data['bangaloreCount'], data['mangaloreCount'], data['udupiCount'], data["shimogaCount"], data["mysoreCount"], data["kodaguCount"], data["karnatakaCount"], data['kasargodCount'], data["wayanadCount"], data["keralaCount"], data["mangaloreDeath"], data["bangaloreUrbanDeath"], data["mysoreDeath"], data["shimogaDeath"], data["kodaguDeath"], data['indiaDailyConfirmed'])
        # part1 = MIMEText(text, 'plain')
        # part2 = MIMEText(html, 'html')
        message.attach(MIMEText(htmlData, 'html'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.connect("smtp.gmail.com", 587)
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print("Email sent successfully")
    except:
        print("Email delivery failed.")
