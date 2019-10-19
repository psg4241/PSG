#coder :- Salman Faris

import sys
import time
import telepot
import RPi.GPIO as GPIO  
from time import sleep           
#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
def blink(pin):
    while 1:
        GPIO.output(pin,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(pin,GPIO.LOW)
        sleep(0.5)
    return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'On':
       bot.sendMessage(chat_id, on(11))
    elif command =='Off':
       bot.sendMessage(chat_id, off(11))
    elif command =='Blink':
       bot.sendMessage(chat_id, blink(11))
bot = telepot.Bot('965718651:AAFt1jJbuCzNen7CLjhff8MySnnFVZ1kV2s')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
