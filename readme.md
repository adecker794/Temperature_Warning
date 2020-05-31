## Temperature Warning
Simple Python3 script meant to notify a user through text if a temperature exceeds a set limit.

## What it does
It runs a script and checks the temperature every few seconds, once the temperature exceeds a set limit it sends a warning via text message to specified recipients.

It is set to start at boot up and run continuously unless stopped. It uses a Linux systemd service to do so.

## How to run it
First you must connect your DHT22 up to your raspberry pi, you can find many guides online. For a Raspberry Pi Zero connect pin 1 on the DHT22 to pin 2 on the Zero, pin 2 on the DHT22 to pin 6 on the Zero, pin 3 is null(this is for a 4 pin DHT22), pin 4 connects to pin 7 on the Zero.(If you have a 3 pin DHT22, you will want to connect pin 3 to pin 7 on the Zero)

Next you must install the necessary packages:
Optional beforehand (mandatory if fresh install of Raspberry Pi OS):
```
sudo apt-get update
sudo apt-get upgrade
```

Mandatory:
```
sudo apt-get install python3-dev python3-pip git -y
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
```

Clone this git repo, edit the config.ini and recipients.py and run setup.py
```
git clone https://github.com/adecker794/Temperature_Warning
cd ~/Temperature_Warning/TempWarningService
Edit config.ini and recipients.py ( you can use nano or vim, whatever you like )
cd back into ~/Temperature_Warning
sudo python3 setup.py
```

Afterwards you can check the status of the service by running
```
Systemctl status TempWarningService.service
```
