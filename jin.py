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
beat = 0.2

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
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*2)

    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*2)

    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(g)
    light(beat)
    p.ChangeFrequency(c)
    light(beat)
    p.ChangeFrequency(d)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*4)

    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(f)
    light(beat)

    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*.5)
    p.ChangeFrequency(e)
    light(beat*.5)

    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(d)
    light(beat)
    p.ChangeFrequency(d)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)

    p.ChangeFrequency(d)
    light(beat*2)
    p.ChangeFrequency(g)
    light(beat)
    p.stop()
    light(beat)
    p.start(50)

    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*2)

    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*2)

    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(g)
    light(beat)
    p.ChangeFrequency(c)
    light(beat)
    p.ChangeFrequency(d)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*4)

    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(f)
    light(beat)

    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat)
    p.ChangeFrequency(e)
    light(beat*0.5)
    p.ChangeFrequency(e)
    light(beat*0.5)

    p.ChangeFrequency(g)
    light(beat)
    p.ChangeFrequency(g)
    light(beat)
    p.ChangeFrequency(f)
    light(beat)
    p.ChangeFrequency(d)
    light(beat)
    p.ChangeFrequency(c)
    light(beat*4)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()

