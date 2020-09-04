#-*- coding: utf-8 -*-　
import tm1637 #led
import time 

if __name__ == "__main__":
	display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)
	display.Clear()
	display.ShowDoublepoint(False)
	try:
			while True:
				display.showtmp(8)
				time.sleep(3)
	except KeyboardInterrupt:
		print("stop")
	finally:
		display.cleanup()
