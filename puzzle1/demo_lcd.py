#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
import sys
from time import sleep

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()

# Main body of code

def show_lines(message, long):
       if(long<=20):
            display.lcd_display_string(message,1)
       elif(long<=40):
            display.lcd_display_string(message[:20],1)
            display.lcd_display_string(message[20:long],2)
       elif(long<=60):
            display.lcd_display_string(message[:20],1)
            display.lcd_display_string(message[20:40],2)
            display.lcd_display_string(message[40:long],3)
       elif(long<=80):
            display.lcd_display_string(message[:20],1)
            display.lcd_display_string(message[20:40],2)
            display.lcd_display_string(message[40:60],3)
            display.lcd_display_string(message[60:long],4)
           
            
            
if __name__ == "__main__":
    try:
            # Remember that your sentences can only be 16 characters long!
           statement = "Escribe lo que quieras imprimir: "
           show_lines(statement,len(statement))
           message=input(statement)
           display.lcd_clear()
           long = len(message)
           show_lines(message,long)
           
            # Give time for the message to be read
    except KeyboardInterrupt:
        # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()
        
    

