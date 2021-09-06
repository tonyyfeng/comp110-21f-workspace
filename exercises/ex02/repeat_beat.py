"""Repeating a beat in a loop."""

__author__ = "730410711"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
i: int = 1
whole_beat: str = beat
if repeat > 0:
    while i < repeat:
        i = i + 1
        whole_beat = whole_beat + " " + beat
    print(whole_beat)
else:
    print("No beat...")

    