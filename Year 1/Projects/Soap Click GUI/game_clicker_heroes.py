from keyboard_utils import start_hold, stop_hold, tap_button, write
from mouse_utils import get_mouse_pos, move_to, start_mouse_hold, stop_mouse_hold, click, auto_click, click_location, scroll

import time

left = (3156, 600)
right = (3562, 600)

def sweep_coins():
    move_to(left)
    time.sleep(0.001)
    move_to(right)

def attack_for(num_clicks, delay):
    for i in range(num_clicks):
        if i % 50 == 0:
            click_location("left", left, glide_steps=20, move_time=0.075)
        elif i % 25 == 0:
            click_location("left", right, glide_steps=20, move_time=0.075)
        else:
            click("left")
        time.sleep(delay)

# time.sleep(3)

# attack_for(2000, 0.01)

from pynput import keyboard

def on_press(key):
    print(f"Pressed: {key}")
    if key == keyboard.Key.enter:
        print("Enter pressed")
        attack_for(1000, 0.01)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Stopping program...")
        exit(0)

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    time.sleep(0)