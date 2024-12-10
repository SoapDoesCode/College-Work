"""Simple Prebuilt Keyboard Control Functions"""
from subprocess import run
try:
    from pynput.keyboard import Key, Controller
except ImportError:
    run(["python","-m", "install", "pynput"])
    from pynput.keyboard import Key, Controller


from asyncio import sleep as wait


keyboard = Controller()

key_mappings = {
    'Esc': Key.esc,
    'F1': Key.f1,
    'F2': Key.f2,
    'F3': Key.f3,
    'F4': Key.f4,
    'F5': Key.f5,
    'F6': Key.f6,
    'F7': Key.f7,
    'F8': Key.f8,
    'F9': Key.f9,
    'F10': Key.f10,
    'F11': Key.f11,
    'F12': Key.f12,
    'Print Screen': Key.print_screen,
    'Scroll Lock': Key.scroll_lock,
    'Pause': Key.pause,
    'Insert': Key.insert,
    'Home': Key.home,
    'End': Key.end,
    'Page Up': Key.page_up,
    'Page Down': Key.page_down,
    'Left Arrow': Key.left,
    'Up Arrow': Key.up,
    'Right Arrow': Key.right,
    'Down Arrow': Key.down,
    'Tab': Key.tab,
    'Enter': Key.enter,
    'Backspace': Key.backspace,
    'Shift': Key.shift,
    'Control': Key.ctrl,
    'Alt': Key.alt,
    'Caps Lock': Key.caps_lock,
    'Num Lock': Key.num_lock,
    'Space': Key.space,
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': 'i',
    'j': 'j',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'o': 'o',
    'p': 'p',
    'q': 'q',
    'r': 'r',
    's': 's',
    't': 't',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'y': 'y',
    'z': 'z'
}


async def select_all() -> None:
    """The Ctrl+A Function"""
    with keyboard.pressed(Key.ctrl):
        keyboard.tap('a')
        await wait(0.01)
    return None

async def paste() -> None:
    """The Ctrl+V Function"""
    with keyboard.pressed(Key.ctrl):
        keyboard.tap('v')
    await wait(0.01)
    return None

async def special_paste() -> None:
    """The Ctrl+Shift+V Function"""
    with keyboard.pressed(Key.shift):
        await paste()
    return None

async def write(string: str = "") -> None:
    """Allows for typing emulation of any string, and pressing enter after"""
    keyboard.type(string)
    keyboard.tap(Key.enter)
    await wait(0.01)
    return None

async def close_tab() -> None:
    """The Ctrl+W Function"""
    with keyboard.pressed(Key.ctrl):
        keyboard.tap('w')
    await wait(0.01)
    return None

async def press_key(key: str = "esc") -> None:
    """Press a specified key"""
    if key in key_mappings:
        keyboard.tap(key_mappings[key])
        await wait(0.01)
    else:
        print(f"Key '{key}' is not mapped.")