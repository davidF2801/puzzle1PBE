#! /usr/bin/env python
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers #Importem la carpeta drivers
display = drivers.Lcd()
#La següent funció la usaré per a que el string entrat es col·loqui a les files corresponents per ordre, sense fer això, 
#quan un string ocupa més de 20 caracters, es coloca en l'order incorrecte
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
           statement = "Escribe lo que quieras imprimir: " #primer de tot treiem el missatge per pantalla de que s'escrigui el que es vol imprimir
           show_lines(statement,len(statement))
           message=input(statement)
           display.lcd_clear() #Un cop entrat el missatge es neteja la pantalla
           show_lines(message,len(message)) #Finalment es mostra el missatge per pantalla
    except KeyboardInterrupt: #Quan es prem ctrl + c, es neteja la pantalla i s'acaba l'execució del programa
        print("Cleaning up!")
        display.lcd_clear()
        
    

