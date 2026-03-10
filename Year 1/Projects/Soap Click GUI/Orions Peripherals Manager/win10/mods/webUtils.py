"""A Specific Set Of Utilities Built for the web"""
from typing import Literal
import sys
from asyncio import run, sleep as asyncWait


path = "peripherals"
if path not in sys.path:
    sys.path.append(path)


import peripherals.keyboardControl as keyboard
import peripherals.mouseControl as mouse


async def open_URL(url:str, browser:Literal["Chrome", "Edge", "Firefox"], fullscreen:bool = False) -> None:
    """Opens a URL in preferred Browser (Optional Fullscreen)

    Args:
        url (str): URL to navigate to
        browser (Literal[&quot;Chrome&quot;, &quot;Edge&quot;, &quot;Firefox&quot;]): Preferred Browser
        fullscreen (bool, optional): Fullscreen Option. Defaults to False.

    Returns:
        None
    """
    keyboard.keyboard.tap(keyboard.Key.cmd)
    await asyncWait(1) # Waiting on system
    await keyboard.write(browser)
    await asyncWait(0.99) # Waiting on system
    await mouse.go_to(120, 300)
    await mouse.left_click()
    await asyncWait(0.99) # Waiting on system
    if fullscreen:
        await keyboard.press_key("F11")
        await asyncWait(0.99) # Waiting on system
        await mouse.go_to(0, 0)
        await asyncWait(1) # Waiting on system
    await mouse.go_to(300, 50)
    await mouse.left_click()
    await keyboard.write(url)
    return None