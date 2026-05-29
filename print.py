from escpos import *
import datetime

LINE_WIDTH=32 # mode 0 default
granted="""       ╔═══════════════╗
       ║ Entry Granted ║
       ╚═══════════════╝"""
denied="""         ╔════════════╗
         ║Entry Denied║
         ╚════════════╝"""

def centerText(txt: str) -> str:
	if len(txt) > LINE_WIDTH:
		return "" #TODO: impl line wrap
	if len(txt) == LINE_WIDTH:
		return txt # well, that was easy
	remainder = LINE_WIDTH - len(txt)
	return (int(remainder/2)*" ")+txt

def rightText(txt: str) -> str:
	if len(txt) > LINE_WIDTH:
		return ""
	if len(txt) == LINE_WIDTH:
		return txt
	return ((LINE_WIDTH - len(txt))*" ")+txt

def lrText(l: str, r: str) -> str:
	# text to the left and right
	if (len(l) + len(r)) >= LINE_WIDTH:
		return l + "\n" + rightText(r)
	rem = LINE_WIDTH - (len(l) + len(r))
	return l+(rem*" ")+r

p = printer.Serial(devfile="/dev/ttyUSB0", baudrate=9600, bytesize=8, parity=None, stopbits=2, dsrdtr=False, profile="simple")
p.text('\x00'*50) # this particular printer needs to be woken up
p.text("\n")
p.text('\x00'*50)
#p.text("greetings, earthling\n")
p.image("/home/philo/Downloads/logo.png", high_density_vertical=True, high_density_horizontal=False, impl="bitImageColumn")
#p.set(align="center")
p.textln(centerText("CERTIFICATE OF BAC"))
now = datetime.datetime.now()
p.textln(lrText("Date:", str(now.day)+"."+str(now.month)+"."+str(now.year)))
p.textln(lrText("Time:", str(now.hour)+":"+str(now.minute)))
p.textln(lrText("BAC:", "0.123"))
p.textln(lrText("MICROPLASTICS:", "666"))
p.textln(rightText("nanostone/stone"))
p.textln(granted)
