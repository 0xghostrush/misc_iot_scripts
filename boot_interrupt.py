import serial
import time

port = "/dev/ttyUSB0"

serial_port = serial.Serial(port, baudrate=115200, timeout=1,stopbits=serial.STOPBITS_ONE)

serial_string = ""

serial_port.reset_input_buffer()
serial_port.reset_output_buffer()

serial_port.write(b"reboot\r\b")
time.sleep(0.5)

# works on tplink
# change to something else if needed
for i in range(1000):
    serial_port.write(b"tpl \r\b")
    print("writing tpl #: " + str(i))

while True:
    serial_string = serial_port.readline()
    print(serial_string.decode("Ascii"))

# Can add other stuff here - md etc