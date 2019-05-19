import random

# Data
NOTES = [
    "C",
    "D",
    "E",
    "F",
    "G",
    "A",
    "B",
    "C#",
    "D#",
    "E#",
    "F#",
    "G#",
    "A#",
    "B#",
    "Cb",
    "Db",
    "Eb",
    "Fb",
    "Gb",
    "Ab",
    "Bb"
]

# Functions
def getRandomIndexExclusive(size):
    return int(random.random() * size)

def generateNote():
    randomNumber = getRandomIndexExclusive(len(NOTES))
    return NOTES[randomNumber]

def displayNote(note):
    print("< " + note + " >", end = " ")

def confirmMusicianPlayed(note):
    return input("")

def playTheNote():
    note = generateNote()
    displayNote(note)
    confirmMusicianPlayed(note)

def promptMusicianToContinue():
    musicianResponse = input("... ")
    isEnter = len(musicianResponse.strip()) == 0
    return isEnter

# Main
print("Play the notes!...")
try:
    keepPlaying = True
    while keepPlaying:
        playTheNote()

        keepPlaying = promptMusicianToContinue()

finally:
    print("Good work! Stay diligent in practice!")
