from digitalio import DigitalInOut, Direction
import audioio
import touchio
import board
import time
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()

bpm = 120 #beats per minute for sustained hold, change this to suit your tempo
simpleCircleDemo = 1

# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = False

# make the input cap sense pads
capPins = (board.A1, board.A2, board.A3, board.A4, board.A5,
           board.A6, board.A7)

touchPad = []
for i in range(7):
    touchPad.append(touchio.TouchIn(capPins[i]))

# The seven files assigned to the touchpads
audiofiles = ["chewy_roar.wav", "R2D2-yeah.wav", "blaster-firing.wav",
               "jabba-the-hutt-laughing.wav", "light-saber-off.wav", "light-saber-on.wav",
               "yodalaughing.wav"]

def play_file(filename):
    print("playing file "+filename)
    f = open(filename, "rb")
    a = audioio.AudioOut(board.A0, f)
    a.play()
#    time.sleep(bpm/960) #sixteenthNote delay

def simpleCircle(wait):
    RED = 0x100000 # (0x10, 0, 0) also works
    BLACK = (0, 0, 0)

    for i in range(len(pixels)):
        pixels[i] = RED
        time.sleep(wait)
    time.sleep(1)

    for i in range(len(pixels)):
        pixels[i] = BLACK
        time.sleep(wait)
    time.sleep(1)

while True:

    for i in range(7):
        if touchPad[i].value:
            play_file(audiofiles[i])
            simpleCircle(.02)
