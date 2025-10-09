import serial
import time

port = "/dev/ttyUSB0"
serial_port = serial.Serial(port, baudrate=115200, timeout=1,stopbits=serial.STOPBITS_ONE)

serial_string = ""

while True:
    time.sleep(10)
    serial_port.write(b"ps \r\b")
    serial_string = serial_port.read_until("ps")

    print(serial_string.decode("Ascii"))

    with open("ps_log.txt", "a") as f:
        f.write(serial_string.decode("Ascii"))

    print("Waiting 10 seconds......")