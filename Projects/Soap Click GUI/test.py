from keyboard_utils import start_hold, stop_hold, tap_button, write
from mouse_utils import get_mouse_pos, move_to, start_mouse_hold, stop_mouse_hold, click, auto_click, click_location, scroll

import time

# start_hold("windows")
# write("r")
# stop_hold("all"); time.sleep(0.025)
# write("https://www.marktechpost.com/2024/09/14/onegen-an-ai-framework-that-enables-a-single-llm-to-handle-both-retrieval-and-generation-simultaneously/")
# write("\n")

# start_hold("windows")
# stop_hold("all")

time.sleep(5)

for i in range(5):
    click_location("left", (2818, 701))
    time.sleep(0.001)
    click_location("left", (2858, 694))
    time.sleep(0.001)
    click_location("left", (2911, 705))
    time.sleep(0.001)
    click_location("left", (2908, 752))
    time.sleep(0.001)
    click_location("left", (2852, 749))
    time.sleep(0.001)
    click_location("left", (2811, 747))
    time.sleep(0.001)
    click_location("left", (2810, 801))
    time.sleep(0.001)
    click_location("left", (2870, 804))
    time.sleep(0.001)
    click_location("left", (2914, 812))
    time.sleep(0.001)

# auto_click("left", delay=0.01, num_times=500)

# tap_button("windows", then_wait=1)
# click_location("left", (2910, 74))
# time.sleep(0.1)
# write("discord")