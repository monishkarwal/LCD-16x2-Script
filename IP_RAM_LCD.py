#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.

import time
import Adafruit_CharLCD as LCD

# Raspberry Pi pin configuration:
lcd_rs        = 26  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 19
lcd_d4        = 13
lcd_d5        = 6
lcd_d6        = 5
lcd_d7        = 11
lcd_backlight = 4

# BeagleBone Black configuration:
# lcd_rs        = 'P8_8'
# lcd_en        = 'P8_10'
# lcd_d4        = 'P8_18'
# lcd_d5        = 'P8_16'
# lcd_d6        = 'P8_14'
# lcd_d7        = 'P8_12'
# lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
#lcd.message('MK\nExtreme-Machine')
# Wait 5 seconds
#time.sleep(5.0)


# Demo scrolling message right/left.
#lcd.clear()
#message = 'Scroll'
#lcd.message(message)
#for i in range(lcd_columns-len(message)):
#    time.sleep(0.5)
#   lcd.move_right()
#for i in range(lcd_columns-len(message)):
#    time.sleep(0.5)
#    lcd.move_left()

# Return RAM information (unit=kb) in a list                                       
# Index 0: total RAM                                                               
# Index 1: used RAM                                                                 
# Index 2: free RAM

#!/usr/bin/python

import os
import Adafruit_CharLCD
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

 
cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output
 
while 1:
        lcd.clear()
        ipaddr = run_cmd(cmd)
        #lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
        lcd.message('     MK NAS\n')
        lcd.message('IP:%s' % ( ipaddr ) )
        sleep(30)

        lcd.clear()

        RAM_stats = getRAMinfo()
        RAM_used = round(int(RAM_stats[1]) / 1000,1)
        RAM_free = round(int(RAM_stats[2]) / 1000,1)
        lcd.message('RAM Used %sMB   \n' % (RAM_used))
        lcd.message('RAM Free  %sMB   ' % (RAM_free))
        sleep(10)
