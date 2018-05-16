import serial
import time

ser = serial.Serial("/dev/ttyACM0")
while True:
    ser.write(b"1000\n")
    time.sleep(1)
    ser.write(b"0000\n")
    time.sleep(1)
    
    
ser.close()
