import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getData import getData
import os
from dotenv import load_dotenv


load_dotenv()

data = getData()


def sendEmail():
    try:
        sender_address = os.getenv('EMAIL_ID')
        sender_pass = os.getenv('PASSWORD')
        receiver_address = os.getenv('RECEIVER_EMAIL_ID')
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'COVID Data for the day'

        # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
        htmlData = """\
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <p>Here is the COVID data. Please wear a mask and if eligible take your vaccine shots</p>
            <table border="1px solid black">
                <tr>
                    <td>
                        Bangalore Count
                    </td>
                <th>
                    {0}
                </th>
                </tr>
                <tr>
                    <td>
                        Mangalore Count
                    </td>
                <th>
                    {1}
                </th>
                </tr>
                <tr>
                    <td>
                        Udupi Count
                    </td>
                <th>
                    {2}
                </th>
                </tr>
                 <tr>
                    <td>
                        Kasargod Count
                    </td>
                <th>
                    {3}
                </th>
                </tr>
                 <tr>
                    <td>
                        Mangalore Death Count
                    </td>
                <th>
                    {4}
                </th>
                </tr>
                <tr>
                    <td>
                        Karnataka Count
                    </td>
                <th>
                    {5}
                </th>
                </tr>
                <tr>
                    <td>
                        India Count
                    </td>
                <th>
                    {6}
                </th>
                </tr>
            </table>
            <p>Stay safe and indoors.</p>
        </body>
        </html>
        """.format(data['bangaloreCount'], data['mangaloreCount'], data['udupiCount'], data['kasargodCount'], data['mangaloreDeath'], data['karnatakaCount'], data['indiaDailyConfirmed'])
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
