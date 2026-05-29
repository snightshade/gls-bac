from escpos import *
import datetime
import random

LINE_WIDTH=32 # mode 0 default
BAC_THRESH=0.003
granted="""       ╔═══════════════╗
       ║ Entry Granted ║
       ╚═══════════════╝"""
denied="""        ╔══════════════╗
        ║ Entry Denied ║
        ╚══════════════╝"""

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

def bacReport(bac: float) -> None:
	p = printer.Serial(devfile="/dev/ttyUSB0", baudrate=9600, bytesize=8, parity=None, stopbits=2, dsrdtr=False, profile="simple")
	p.text('\x00'*50) # this particular printer needs to be woken up
	p.text("\n")
	p.text('\x00'*50)
	p.image("logo.png", high_density_vertical=True, high_density_horizontal=False, impl="bitImageColumn")
	#p.set(align="center")
	p.textln(centerText("CERTIFICATE OF BAC"))
	now = datetime.datetime.now()
	p.textln(lrText("Date:", str(now.day)+"."+str(now.month)+"."+str(now.year)))
	p.textln(lrText("Time:", str(now.hour)+":"+str(now.minute)))
	p.textln(lrText("BAC:", str(bac)))
	p.textln(lrText("MICROPLASTICS:", str(random.randrange(300,900))))
	p.textln(rightText("nanostone/stone"))
	if bac >= BAC_THRESH:
		p.textln(granted)
	else:
		p.textln(denied)
