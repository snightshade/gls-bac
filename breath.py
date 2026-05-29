import serial
import re
from print import bacReport

RESULT_RX = r"^TEST RESULT: +(\.[0-9]*)"

s = serial.Serial("/dev/ttyUSB1", baudrate=9600, stopbits=serial.STOPBITS_TWO, rtscts=True, timeout=5)
p = re.compile(RESULT_RX, re.MULTILINE)
while True:
	try:
		l = s.readline().decode()
	except:
		continue
	matches = p.findall(l)
	if len(matches) > 0:
		print("got BAC:", matches[0])
		bacReport(float(matches[0]))
s.close()
# TODO: make it possible to exit this without kill -9'ing it lol


# length of this is 499 chars
example = b'\r\n------------------------------\r\n  Lifeloc Technologies, Inc.\r\n  FC20               v3.10c \r\n  Serial No.          00905\r\n------------------------------\r\nUnits:                     BAC\r\n\r\nMANUAL TEST #            00191\r\n\r\nTEST RESULT:              .007\r\nTime:                    00:00\r\nDate:               00/00/0000\r\n\r\n\r\n\r\n______________________________\r\n           Subject\r\n\r\n\r\n______________________________\r\n             I.D.\r\n\r\n\r\n______________________________\r\n           Operator\r\n\r\n\r\n\r\n\r\n\r\n'
