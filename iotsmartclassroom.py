import time
import serial
ser = serial.Serial('COM3',9600)
import thingspeak
import time
channel_id = 1108445  # PUT CHANNEL ID HERE
write_key = 'QET05Z7EWG5Y9SXS'  # PUT YOUR WRITE KEY HERE

channel = thingspeak.Channel(id=channel_id, api_key=write_key)
while 1:
    text = ser.readline()
    if text == b'student id 1\r\n':
        print('student id 1')
        response = channel.update({'field1': '1'})
        print(response)
        time.sleep(15)
    elif text == b'student id 2\r\n':
        print('student id 2')
        response = channel.update({'field1': '2'})
        print(response)
        time.sleep(15)
    elif text == b'student id 3\r\n':
        print('student id 3')
        response = channel.update({'field1': '3'})
        print(response)
        time.sleep(15)
    elif text == b'student id 4\r\n':
        print('student id 4')
        response = channel.update({'field1': '4'})
        print(response)
        time.sleep(15)
    elif text == b'student id 5\r\n':
        print('student id 5')   
        response = channel.update({'field1': '5'})
        print(response)
        time.sleep(15)
    else:
        response = channel.update({'field1': '0'})
        print(response)