import pygame
import asyncio
import sys, os

from random import randint as rng
from random import choice as choose

from configparser import ConfigParser

import pygame_menu

configFilePath = os.path.join(os.path.dirname(__file__), 'config.ini')
config = ConfigParser()
config.read(configFilePath)

pygame.init()
clock = pygame.time.Clock()

### GAME SETTINGS ###
WIDTH = config.getint("Settings", "window_width")
HEIGHT = config.getint("Settings", "window_height")
refresh_rate = config.getint("Settings", "refresh_rate")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
font = pygame.font.Font(None, 36)

grid_size = list(map(int, config.get('Settings', 'grid_size').removeprefix("(").removesuffix(")").split(',')))
grid_padding = config.getint("Settings", "grid_padding")
### GAME SETTINGS ###

### INITIAL SETUP ###
border_colour = list(map(int, config.get('Settings', 'init_border_colour').removeprefix("(").removesuffix(")").split(',')))
grid_colour = list(map(int, config.get('Settings', 'init_grid_colour').removeprefix("(").removesuffix(")").split(',')))
snake_head_colour = list(map(int, config.get('Settings', 'init_snake_head_colour').removeprefix("(").removesuffix(")").split(',')))
snake_body_colour = list(map(int, config.get('Settings', 'init_snake_body_colour').removeprefix("(").removesuffix(")").split(',')))
target_colour = list(map(int, config.get('Settings', 'init_target_colour').removeprefix("(").removesuffix(")").split(',')))

playing = True
snake_alive = True
moving_dir = None
score = 0

snake_head = []
snake_head.append((grid_size[0]//5))
snake_head.append((grid_size[1]//2))

snake_body = []
snake_body.append([snake_head[0]-2, snake_head[1]])
snake_body.append([snake_head[0]-1, snake_head[1]])

target_locations = []
### INITIAL SETUP ###

def complement(rgb: list):
    r = 255 - rgb[0]
    g = 255 - rgb[1]
    b = 255 - rgb[2]

    rgb_values = [r, g, b]

    return rgb_values

def draw_grid(grid_size: list, screen_size: list, padding: int, grid_colour: list) -> None:
    s_width = (screen_size[0] - (2*padding)) // grid_size[0]
    s_height = (screen_size[1] - ((2*padding)+30)) // grid_size[1]

    # print(f"Width: {s_width}px\nHeight: {s_height}px")

    alt_offset = 10
    alt_grid_colour = (grid_colour[0]+alt_offset, grid_colour[1]+alt_offset, grid_colour[2]+alt_offset)

    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            color = grid_colour if (x + y) % 2 == 0 else alt_grid_colour
            pygame.draw.rect(screen, color, pygame.Rect(
                padding + (x * s_width), 
                padding + 30 + (y * s_height), 
                s_width, 
                s_height
            ))
            
def draw_targets(locations: list):
    t_width = (WIDTH - (2*grid_padding)) // grid_size[0]
    t_height = (HEIGHT - ((2*grid_padding)+30)) // grid_size[1]

    for target in locations:
        pygame.draw.rect(screen, target_colour, pygame.Rect(
            (grid_padding + (target[0] * t_width)),
            (grid_padding + 30 + (target[1] * t_height)),
            t_width,
            t_height
        ))

def generate_target(snake_body: list, target_locations: list) -> tuple:
    grid = []
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            grid.append((x, y))
    
    for part in snake_body:
        try:
            grid.remove(tuple(part))
        except:
            pass
    
    for target in target_locations:
        grid.remove(tuple(target))
    
    return choose(grid)

def draw_snake(snake_head: list, snake_body: list) -> None:
    s_width = (WIDTH - (2*grid_padding)) // grid_size[0]
    s_height = (HEIGHT - ((2*grid_padding)+30)) // grid_size[1]

    pygame.draw.rect(screen, snake_head_colour, pygame.Rect(
            (grid_padding + (snake_head[0] * s_width)),
            (grid_padding + 30 + (snake_head[1] * s_height)),
            s_width,
            s_height
        ))
    
    for coord in snake_body:
        if coord != snake_head:
            pygame.draw.rect(screen, snake_body_colour, pygame.Rect(
                (grid_padding + (coord[0] * s_width)),
                (grid_padding + 30 + (coord[1] * s_height)),
                s_width,
                s_height
            ))

def step_snake(snake_head: list, snake_body: list, direction: str) -> None:
    global score
    # Append the current head to the body as the new segment
    snake_body.append(snake_head[:]) # Use a copy of the head
    
    # Move the snake's head based on the direction
    match direction:
        case "up":
            snake_head[1] -= 1
        case "down":
            snake_head[1] += 1
        case "left":
            snake_head[0] -= 1
        case "right":
            snake_head[0] += 1

    if ((snake_head[0] >= grid_size[0])
        or (snake_head[0] < 0)
        or (snake_head[1] >= grid_size[1]
        or (snake_head[1] < 0))
        ):
        global moving_dir, snake_alive
        moving_dir = None
        snake_alive = False

    print(snake_head)
    print(target_locations)
    if tuple(snake_head) in target_locations:
        print("Nom")
        score += 1
        target_locations.remove(tuple(snake_head))
        snake_body.append(snake_head)
        target_locations.append(generate_target(snake_body, target_locations))
    
    # Remove the last part of the tail to simulate movement
    snake_body.pop(0)

async def start_snake():
    global playing
    while snake_alive:
        if moving_dir != None:
            # await asyncio.sleep(0.3) # slow
            # await asyncio.sleep(0.21) # medium
            await asyncio.sleep(0.12) # fast
            step_snake(snake_head, snake_body, moving_dir)
        else:
            await asyncio.sleep(0)
    playing = False
    pygame.quit() # Quit the game after 60 seconds of no pops
    print(f"You died!\nFinal Score: {score}")

async def main_game():
    global playing, border_colour, grid_colour, moving_dir

    screen.fill(border_colour)

    # Start the snake moving
    asyncio.create_task(start_snake())

    target_locations.append(generate_target(snake_body, target_locations))

    while playing:
        screen.fill((border_colour))
        
        draw_grid(grid_size, (WIDTH, HEIGHT), grid_padding, grid_colour)
        draw_snake(snake_head, snake_body)
        draw_targets(target_locations)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # playing = False
                pygame.quit()
                print(f"Final Score: {score}")
                # update_config()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # step_snake(snake_head, snake_body, direction="up")
                ...
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and moving_dir != "down":
                    # step_snake(snake_head, snake_body, direction="up")
                    moving_dir = "up"
                elif event.key == pygame.K_DOWN and moving_dir != "up":
                    # step_snake(snake_head, snake_body, direction="down")
                    moving_dir = "down"
                elif event.key == pygame.K_LEFT and moving_dir != "right":
                    # step_snake(snake_head, snake_body, direction="left")
                    moving_dir = "left"
                elif event.key == pygame.K_RIGHT and moving_dir != "left":
                    # step_snake(snake_head, snake_body, direction="right")
                    moving_dir = "right"

        text_rgb = complement(border_colour)
        score_text = font.render(f"Score: {score}", True, text_rgb)
        # timer_text = font.render(f"Time: {time_limit - elapsed_time} seconds", True, text_rgb)

        screen.blit(score_text, (10, 5))
        # screen.blit(timer_text, (10, 10))

        # sets the refresh rate (fps)
        clock.tick(refresh_rate)

        # update the game state and draw the screen
        pygame.display.flip()

        await asyncio.sleep(0) # this is needed, DO NOT REMOVE

# def start_game():
#     asyncio.run(main_game())

asyncio.run(main_game())