import numpy as np
import random
from gpiozero import LED, LEDBoard
from time import sleep
pins = LEDBoard(a = 23, b = 18, c = 22, d = 27, e = 17, f = 24, g = 25 )
segDict = {
'0':    [0,1,2,3,4,5],    
'1':	[1,2],
'2':	[0,1,3,4,6],	
'3':	[0,1,2,3,6],	
'4':	[1,2,5,6],	
'5':	[0,2,3,5,6],	
'6':	[0,2,3,4,5,6],
'7':	[0,1,2],
'8':	[0,1,2,3,4,5,6],	
'9':    [0,1,2,3,5,6] }

# print(segDict[str(num)])
while True:
    num = random.randint(0,5)
    print(num)
    pinlist = segDict[str(num)]
    pins.off()
    for i in range(len(pinlist)):
        pins.on(pinlist[i])
    sleep(2)

# num =1
# if num == 1:
# while True:
#     pins.off()
#     pins.on(0,1,5,6)
#     sleep(1)
#     pins.on(2,3,4,6)
#     sleep(1)
