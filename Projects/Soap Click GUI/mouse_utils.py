import time

from pynput.mouse import Button, Controller

mouse = Controller()

bindings = {
    "left": Button.left,
    "right": Button.right,
    "middle": Button.middle
}

def get_mouse_pos() -> tuple:
    return mouse.position

def move_to(location: tuple, glide_steps: int = 0, move_time: int = 0) -> None:
    """If glide_steps is zero then move_time will be ignored"""
    current_pos = get_mouse_pos()

    if glide_steps != 0:
        diff_x, diff_y = location[0]-current_pos[0], location[1]-current_pos[1]
        step_dist_x, step_dist_y = diff_x // glide_steps, diff_y // glide_steps
        step_delay = move_time / glide_steps

    for i in range(glide_steps):
        mouse.move(step_dist_x, step_dist_y)
        time.sleep(step_delay)

    mouse.position = location

def start_mouse_hold(button: str) -> None:
    mouse.press(bindings[button])

def stop_mouse_hold(button: str) -> None:
    mouse.release(bindings[button])

def click(button: str) -> None:
    mouse.click(bindings[button])

def auto_click(button: str, delay: float, num_times: int = 10) -> None:
    for i in range(num_times):
        mouse.click(bindings[button])
        time.sleep(delay)

def click_location(button: str, location: tuple, glide_steps: int = 0, move_time: int = 0) -> None:
    """If glide_steps is zero then move_time will be ignored"""
    move_to(location, glide_steps, move_time)
    click(button)

def scroll(direction: str, amount: int) -> None:
    match direction.lower():
        case "up":
            mouse.scroll(0, amount)
        case "down":
            mouse.scroll(0, -amount)
        case "left":
            mouse.scroll(amount, 0)
        case "right":
            mouse.scroll()