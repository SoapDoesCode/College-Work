import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

bindings = {
    "windows": Key.cmd,
    "ctrl": Key.ctrl,
    "shift": Key.shift,
    "alt": Key.alt,
    "enter": Key.enter,
    "backspace": Key.backspace
}

def start_hold(*keys, then_wait: float = 0) -> None:
    for button in keys:
        keyboard.press(bindings[button.lower()])
        time.sleep(then_wait)

def stop_hold(*keys, then_wait: float = 0) -> None:
    for button in keys:
        button = button.lower()
        if button == "all":
            for binding in bindings.values():
                keyboard.release(binding)
                # print(f"Stopped holding: {binding}")
        else:
            keyboard.release(bindings[button])
            # print(f"Stopped holding: {button}")
        time.sleep(then_wait)

def tap_button(button, then_wait: float = 0) -> None:
    keyboard.tap(bindings[button.lower()])
    time.sleep(then_wait)

def write(text: str, then_wait: float = 0) -> None:
    keyboard.type(text)
    time.sleep(then_wait)