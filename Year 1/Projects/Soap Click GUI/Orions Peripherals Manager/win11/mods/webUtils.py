"""A Specific Set Of Utilities Built for the web"""
from typing import Literal
import sys
from asyncio import run, sleep as asyncWait, create_task as task
from time import sleep as wait
import screeninfo  # Add this library to get screen dimensions

path = "peripherals"
if path not in sys.path:
    sys.path.append(path)

import peripherals.keyboardControl as keyboard
import peripherals.mouseControl as mouse

# Get screen dimensions
screen = screeninfo.get_monitors()[0]  # Get the primary monitor
screen_width = screen.width
screen_height = screen.height

# Define constants for mouse positions based on screen dimensions
MOUSE_BROWSER_POSITION = (screen_width * 0.4, screen_height * 0.3)  # Center top
MOUSE_URL_INPUT_POSITION = (screen_width * 0.3, screen_height * 0.06)  # Center for URL input

async def open_URL(url: str, browser: Literal["Chrome", "Edge", "Firefox"], fullscreen: bool = False) -> None:
    """Opens a URL in preferred Browser (Optional Fullscreen)

    Args:
        url (str): URL to navigate to
        browser (Literal["Chrome", "Edge", "Firefox"]): Preferred Browser
        fullscreen (bool, optional): Fullscreen Option. Defaults to False.

    Returns:
        None
    """
    task(mouse.mouse_lock_detector())
    keyboard.keyboard.tap(keyboard.Key.cmd)
    await asyncWait(1)  # Waiting on system
    await keyboard.write(browser)
    await asyncWait(0.99)  # Waiting on system
    await mouse.go_to_and_lock(*MOUSE_BROWSER_POSITION)
    await mouse.left_click()
    await asyncWait(0.49)  # Waiting on system

    if fullscreen:
        await keyboard.press_key("F11")
        await asyncWait(0.49)  # Waiting on system
        await mouse.unlock_mouse()
        await mouse.go_to(0, 0)  # Cannot lock (Won't open UI)
        await asyncWait(1)  # Waiting on system
    await mouse.lock_mouse_to(*MOUSE_URL_INPUT_POSITION)
    await asyncWait(0.49)
    await mouse.left_click()
    await asyncWait(0.49)
    await keyboard.write(url)
    await asyncWait(0.49)
    await mouse.unlock_mouse()
    return None

async def new_tab() -> None:
    with keyboard.keyboard.pressed(keyboard.Key.ctrl):
        keyboard.keyboard.tap("t")

async def new_tab_to_url(url:str) -> None:
    await new_tab()
    await mouse.go_to(0, 0)  # Cannot lock (Won't open UI)
    await asyncWait(1)  # Waiting on system
    await mouse.lock_mouse()
    await mouse.go_to_and_lock(*MOUSE_URL_INPUT_POSITION)
    await keyboard.write(url)
    await mouse.unlock_mouse()