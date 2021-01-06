from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

load_dotenv(verbose = True)

class GMILAdapter:
    def __init__(self, host:str, port:int, username:str, passworrd:str):
        self.username = username
        self.password = passworrd
        # print(f'User: {self.username} hasło: {self.password}')
        self.server = smtplib.SMTP_SSL(host, port)

    def login(self):
        self.server.ehlo()
        self.server.login(self.username, self.password)
    def send_mail(self, email: str, title: str, content: str):
        messege = self._creatin_Email(content, email, title)
        self.server.sendmail(self.username, email, messege.as_string())

    def _creatin_Email(self, content, email, title):
        messege = MIMEMultipart('alternative')
        messege['Subject'] = title
        messege['From'] = self.username
        messege['To'] = email
        messege.attach(MIMEText(content, "HTML"))
        return  messege

    def __del__(self):
        self.server.close()