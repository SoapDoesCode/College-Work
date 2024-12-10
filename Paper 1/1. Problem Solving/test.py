import asyncio
from random import randint as rng
import pygame
import sys

pygame.init()

WIDTH = 1500
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bloons Click Shooter")
score = 0
reset_timer = False  # A flag to reset the timer
elapsed_time = 0

# Set up fonts for drawing text
font = pygame.font.Font(None, 36)  # None for default font, 36 is the font size

async def stop(time_limit):
    global reset_timer
    global elapsed_time
    while elapsed_time < time_limit:
        await asyncio.sleep(1)  # Wait for 1 second
        if reset_timer:
            elapsed_time = 0  # Reset the timer on target click
            reset_timer = False
        else:
            elapsed_time += 1
    pygame.quit()
    print(f"Total Score: {score}")
    sys.exit()  # Quit the game after 60 seconds

def generate_target(x, y, size, is_real):
    """Generate a target. If `is_real` is True, it's the real target."""
    color = (255, 0, 0) if is_real else (250, 0, 0)
    pygame.draw.circle(screen, color, (x, y), size)
    pygame.draw.circle(screen, (200, 0, 0), (x, y), 1)

def handle_click(pos, targets):
    global score, reset_timer  # Use global variables
    for target in targets:
        x, y, size, is_real = target
        farx = x - size
        fary = y - size
        closex = x + size
        closey = y + size

        if farx <= pos[0] <= closex and fary <= pos[1] <= closey:
            if is_real:  # Only increment score if the real target was clicked
                score += 1
                reset_timer = True  # Reset the timer on successful real target click
                return True  # Return True to generate new targets
            else:
                print("Wrong target clicked!")
    return False

async def main_game():
    global reset_timer, score

    screen.fill((255, 255, 255))

    # Generate initial targets
    targets = []
    num_targets = round(score / 3) if score > 3 else 1
    for i in range(num_targets):
        size = rng(25, 75)
        x = rng(size, WIDTH - size)
        y = rng(size, HEIGHT - size)
        is_real = i == 0  # Make the first target the real one
        targets.append((x, y, size, is_real))

    # Draw the initial targets
    for target in targets:
        x, y, size, is_real = target
        generate_target(x, y, size, is_real)

    # Start the asynchronous timer
    asyncio.create_task(stop(60))

    while True:
        screen.fill((255, 255 - min(score * 3, 255), 255 - min(score * 3, 255)))  # Update background color

        # Redraw the existing targets (they shouldn't move unless clicked)
        for target in targets:
            x, y, size, is_real = target
            generate_target(x, y, size, is_real)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()

                # Handle the mouse click
                gen_new = handle_click(mouse_pos, targets)

                if gen_new:  # Only generate new targets if the real target was clicked
                    targets = []  # Clear old targets

                    # Generate new targets (one real and others fake)
                    num_targets = round(score / 3) if score > 3 else 1
                    for i in range(num_targets):
                        size = rng(25, 75)
                        x = rng(size, WIDTH - size)
                        y = rng(size, HEIGHT - size)
                        is_real = i == 0  # Make the first target the real one
                        targets.append((x, y, size, is_real))

        # Render the timer and score on the screen
        timer_text = font.render(f"Time: {60 - elapsed_time} seconds", True, (0, 0, 0))
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))

        # Display the timer and score
        screen.blit(timer_text, (10, 10))  # Draw the timer at the top left
        screen.blit(score_text, (10, 50))  # Draw the score below the timer

        # Update the game state and draw the screen
        pygame.display.flip()

        # Yield control to asyncio for handling async tasks
        await asyncio.sleep(0)  # This gives control to asyncio to handle other async tasks like `stop()`

# Run the game using asyncio event loop
asyncio.run(main_game())