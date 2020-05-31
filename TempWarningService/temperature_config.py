from configparser import ConfigParser

parser = ConfigParser()
parser.read('/usr/local/bin/TempWarningService/config.ini')

#print(parser.sections())
#print(parser.options('Config'))
#print(parser.get('Config', 'email'))

email = parser.get('Config', 'Email')
password = parser.get('Config', 'Password')
smtp = parser.get('Config', 'SMTP')
port = int(parser.get('Config', 'Port'))
templimit = int(parser.get('Config', 'Temperature_Limit'))
location = parser.get('SMSConfig', 'Location')



#print(email,password,smtp,port,location)