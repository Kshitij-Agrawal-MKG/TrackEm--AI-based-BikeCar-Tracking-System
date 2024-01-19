from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import requests
bot_token = # enter your bot token
chat_id =  # enter your chat_id


def mailSend(mail, userid, emailreader, dbData):
    for currentMail in emailreader:
        print("Sending mail: ", currentMail)
        link = MIMEMultipart()
        link["To"] = currentMail
        link["From"] = f"TRACK'EM<{userid}>"
        link["Subject"] = "[URGENT] Suspicious Vehicle Detected"
        nowtime = datetime.now()
        current_time = nowtime.strftime("%d/%m/%Y, %H:%M:%S")
        sendMessageData = f"""A Vehicle is detected that may have been involved in some criminal activity.
Details:
License plate number: {dbData[0]}
Name: {dbData[1]}
Crime: {dbData[2]}
Time: {current_time}
Location: MNIT, Jaipur"""

        msg1 = MIMEText(sendMessageData, "plain")
        link.attach(msg1)

        imgopn = open("Image.jpg", "rb").read()
        imgmsg = MIMEImage(imgopn, ".jpg", name="Image.jpg")#namr on necessary

        link.attach(imgmsg)

        mail.sendmail(userid, currentMail, link.as_string())

        print("Mail sent successfully...")

    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    files = {'photo': open("Image.jpg", 'rb')}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print('Image sent successfully!')
    else:
        print('Failed to send image.')
        print(response.text)
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    message_text = sendMessageData
    params = {
        'chat_id': chat_id,
        'text': message_text
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message:', response.text)