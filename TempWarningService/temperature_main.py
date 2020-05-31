import Adafruit_DHT
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from temperature_config import email,password,smtp,port,location,templimit
from recipients import recipients

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def sendmail_func(temperature):
    time = datetime.datetime.now()
    #email = email
    pas = password
    sms_gateway = recipients
    # The server we use to send emails in our case it will be gmail but every email provider has a different smtp
    # and port is also provided by the email provider.
    #smtp = smtp
    #port = port
    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pas)

    # Now we use the MIME module to structure our message.
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = ", ".join(sms_gateway)
    # Make sure you add a new line in the subject
    msg['Subject'] = "Temperature Warning From " + location
    # Make sure you also add new lines to your body
    body = "The Temperature in the " + location + " is {} at {}\n".format(temperature,time)
    # and then attach that body furthermore you can also send html content.
    msg.attach(MIMEText(body, 'plain'))

    sms = msg.as_string()

    server.sendmail(email,sms_gateway,sms)

    # lastly quit the server
    server.quit()
def sleep_minutes(minutes):
    time.sleep(minutes * 60)

def tempcheck():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            fahrenheit = (temperature * 9/5) + 32
            print("Temp={0:0.1f}*C, Temp={1:0.4}*F, Humidity={2:0.1f}%".format(temperature,fahrenheit,humidity))
            if fahrenheit > templimit:
                print('{0:.04}'.format(fahrenheit))
                sendmail_func(fahrenheit)
                sleep_minutes(30)
            time.sleep(2)
        else:
            print("Failed to retrieve data from humidity sensor")
while True:
    try:
        tempcheck()
    except Exception as exc:
        print(exc)