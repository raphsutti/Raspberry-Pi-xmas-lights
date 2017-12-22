#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#physical location
BZRPin = 11
ledPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BZRPin, GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(BZRPin, GPIO.LOW)
GPIO.output(ledPin, GPIO.HIGH)

p = GPIO.PWM(BZRPin, 50)
p.start(50)
beat = 1

cL = 129
cLS = 139
dL = 146
dLS= 156
eL= 163
fL= 173
fLS= 185
gL= 194
gLS= 207
aL= 219
aLS= 228
bL= 232
c= 261
cS= 277
d= 294
dS= 311
e= 329
f= 349
fS= 370
g= 391
gS= 415
a= 440
aS= 455
b= 466
cH= 523
cHS= 554
dH= 587
dHS= 622
eH= 659
fH= 698
fHS= 740
gH= 784
gHS= 830
aH= 880
aHS= 910
bH= 933

def light(pause):
  GPIO.output(ledPin, GPIO.LOW)
  time.sleep(pause/2)
  GPIO.output(ledPin, GPIO.HIGH)
  time.sleep(pause/2)

try:
  #while True:
    p.ChangeFrequency(a)
    light(beat*.5)
    p.ChangeFrequency(a)
    light(beat*.5)
    p.ChangeFrequency(a)
    light(beat*.5)
    p.ChangeFrequency(f)
    light(beat*.35)
    p.ChangeFrequency(cH)
    light(beat*.15)

    p.ChangeFrequency(a)
    light(beat*0.5)
    p.ChangeFrequency(f)
    light(beat*.35)
    p.ChangeFrequency(cH)
    light(beat*.15)
    p.ChangeFrequency(a)
    light(beat)
    p.ChangeFrequency(eH)
    light(beat*.5)

    p.ChangeFrequency(eH)
    light(beat*.5)
    p.ChangeFrequency(eH)
    light(beat*.5)
    p.ChangeFrequency(fH)
    light(beat*.35)
    p.ChangeFrequency(cH)
    light(beat*.15)
    p.ChangeFrequency(gS)
    light(beat*0.5)

    p.ChangeFrequency(f)
    light(beat*.35)
    p.ChangeFrequency(cH)
    light(beat*.15)
    p.ChangeFrequency(a)
    light(beat)
    p.ChangeFrequency(aH)
    light(beat*.5)
    p.ChangeFrequency(a)
    light(beat*.35)

    p.ChangeFrequency(a)
    light(beat*.15)
    p.ChangeFrequency(aH)
    light(beat*0.5)
    p.ChangeFrequency(gHS)
    light(beat*.25)
    p.ChangeFrequency(gH)
    light(beat*.25)
    p.ChangeFrequency(fHS)
    light(beat*0.125)

    p.ChangeFrequency(fH)
    light(beat*.125)
    p.ChangeFrequency(fHS)
    light(beat*.25)

    p.stop()
    light(beat*.25)
    p.start(50)

    p.ChangeFrequency(aS)
    light(beat*.25)
    p.ChangeFrequency(dHS)
    light(beat*0.5)
    p.ChangeFrequency(dH)
    light(beat*.25)
    p.ChangeFrequency(cHS)
    light(beat*.25)
    p.ChangeFrequency(cH)
    light(beat*.125)

    p.ChangeFrequency(b)
    light(beat*0.125)
    p.ChangeFrequency(cH)
    light(beat*.25)

    p.stop()
    light(beat*.25)
    p.start(50)

    p.ChangeFrequency(f)
    light(beat*.125)
    p.ChangeFrequency(gS)
    light(beat*.5)
    p.ChangeFrequency(f)
    light(beat*0.375)
    p.ChangeFrequency(a)
    light(beat*.125)
    p.ChangeFrequency(cH)
    light(beat*.5)

    p.ChangeFrequency(a)
    light(beat*.375)
    p.ChangeFrequency(cH)
    light(beat*.125)
    p.ChangeFrequency(eH)
    light(beat)
    p.ChangeFrequency(aH)
    light(beat*.5)
    p.ChangeFrequency(a)
    light(beat*.35)

    p.ChangeFrequency(a)
    light(beat*.15)
    p.ChangeFrequency(aH)
    light(beat*.5)
    p.ChangeFrequency(gHS)
    light(beat*0.25)
    p.ChangeFrequency(gH)
    light(beat*.25)
    p.ChangeFrequency(fHS)
    light(beat*.125)

    p.ChangeFrequency(fH)
    light(beat*.125)
    p.ChangeFrequency(fHS)
    light(beat*.25)

    p.stop()
    light(beat*.25)
    p.start(50)

    p.ChangeFrequency(aS)
    light(beat*.25)
    p.ChangeFrequency(dHS)
    light(beat*.5)
    p.ChangeFrequency(dH)
    light(beat*0.25)
    p.ChangeFrequency(cHS)
    light(beat*.25)
    p.ChangeFrequency(cH)
    light(beat*.125)

    p.ChangeFrequency(b)
    light(beat*.125)
    p.ChangeFrequency(cH)
    light(beat*.25)

    p.stop()
    light(beat*.25)
    p.start(50)

    p.ChangeFrequency(f)
    light(beat*0.25)
    p.ChangeFrequency(gS)
    light(beat*.5)
    p.ChangeFrequency(f)
    light(beat*.375)
    p.ChangeFrequency(cH)
    light(beat*.125)
    p.ChangeFrequency(a)
    light(beat*.5)

    p.ChangeFrequency(f)
    light(beat*0.375)
    p.ChangeFrequency(c)
    light(beat*.125)
    p.ChangeFrequency(a)
    light(beat)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

