import os
import time

os.system("cls")

CSI = '\x1b['

ZERO = f"{CSI}0G"
ERASE = f"{CSI}2K"

frames = [
    "◯ ● ● ●",
    "● ◯ ● ●",
    "● ● ◯ ●",
    "● ● ● ◯"
]

def draw_animation(frames):
    while True:
        for f in frames:
            print(f"{ZERO}{ERASE}{f}", end="", flush=True)
            time.sleep(0.3)

draw_animation(frames)