"""Simple Prebuilt Mouse Control Functions"""
import math
from typing import Literal
from subprocess import run
try:
    from pynput.mouse import Button, Controller
except ImportError:
    run(["python","-m", "install", "pynput"])
    from pynput.mouse import Button, Controller
    
from asyncio import sleep as wait

mouse = Controller()

button_mapping = {
    "left": Button.left,
    "right": Button.right,
}

def read_location() -> tuple:
    """Returns the current mouse position as a tuple"""
    return mouse.position

# Global variables to control mouse locking
fix_mouse_pos = False
fixed_position = (0, 0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Mouse Lockers~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

async def lock_mouse() -> None:
    """Start locking the mouse."""
    global fix_mouse_pos
    fix_mouse_pos = True

async def unlock_mouse() -> None:
    """Stop locking the mouse."""
    global fix_mouse_pos
    fix_mouse_pos = False

async def mouse_lock_detector() -> None:
    """Continuously lock the mouse position to the last set position."""
    global fix_mouse_pos
    while True:
        if fix_mouse_pos:
            mouse.position = fixed_position
        await wait(0)

async def lock_mouse_to(x: int, y: int) -> None:
    """Start locking the mouse to a specific position."""
    global fix_mouse_pos, fixed_position
    fixed_position = (x, y)
    fix_mouse_pos = True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Default Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

async def go_to(x:int, y:int) -> None:
    """Instantly Move to New Position (Doesn't count as an action)"""
    mouse.position = (x, y)
    await wait(0)

async def glide_to(x: int, y: int) -> None:
    """Move the mouse to a new position in a straight line (with natural timing)"""
    current_x, current_y = mouse.position
    distance = math.hypot(x - current_x, y - current_y)
    steps = int(distance / 20)  # Adjust this to change the speed/smoothness
    for step in range(1, steps + 1):
        # Linear interpolation for the new position
        new_x = current_x + (x - current_x) * (step / steps)
        new_y = current_y + (y - current_y) * (step / steps)
        mouse.position = (new_x, new_y)
        await wait(0.01)  # Add delay between movements to make it smoother
    # Ensure the final position is correct
    mouse.position = (x, y)
    await wait(0)

async def left_click() -> None:
    """Click Once at current position"""
    mouse.click(Button.left)
    await wait(0.01)

async def left_click_at(x:int, y:int) -> None:
    """Click Once at defined X and Y position"""
    await go_to(x, y)
    mouse.click(Button.left)
    await wait(0.01)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Auto Clickers~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

async def auto_click(button:Literal["left", "right"]) -> None:
    """Auto Click at 100 cps (fixed) for time (in seconds)"""
    global button_mapping
    selected_button = button_mapping[button]
    while True:
        mouse.click(selected_button, 1)
        await wait(0.01)

async def timed_auto_click(button:Literal["left", "right"], time:int = 10) -> None:
    """Auto Click at 100 cps (fixed) for time (in seconds)"""
    global button_mapping
    selected_button = button_mapping[button]
    for x in range(0, (time*100)):
        mouse.click(selected_button, 1)
        await wait(0.01)

async def unsafe_auto_click(button:Literal["left", "right"], cps:int = 100, time:int = 10) -> None:
    """Auto Click at any cps for time (in seconds) (Setting CPS too high can cause lag)"""
    global button_mapping
    selected_button = button_mapping[button]
    for x in range(0, time*cps):
        mouse.click(selected_button, 1)
        await wait(1/cps)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Locked Controller~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

async def go_to_and_lock(x:int, y:int) -> None:
    """Instantly Move to New Position and LOCK (Doesn't count as an action)"""
    await go_to(x, y)
    await lock_mouse_to(x, y)
    await wait(0)

async def glide_to_and_lock(x: int, y: int) -> None:
    """Move the mouse to a new position in a straight line and LOCK(with natural timing)"""
    await(glide_to(x, y))
    await lock_mouse_to(x, y)
    await wait(0)
