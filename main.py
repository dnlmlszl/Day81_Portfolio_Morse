import pygame
import time

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("beep.mp3")

morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'}


user_text = input("Enter text here: \n").upper()
print("Morse Code: ", end="")

for char in user_text:
    print(morse_code.get(char) or char, end=" ")

frequency = 1000

for set in morse_code:
    for symbol in set:
        if symbol == '.':
            sound.play(frequency, 100)
        elif symbol == '-':
            sound.play(frequency, 700)
    print()
    time.sleep(0.2)
