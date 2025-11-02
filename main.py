import pygame


# Pygame setup
pygame.init() #
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set the window size
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock() # Create a clock object to manage frame rate
running = True 

#Paddle setup
paddle_x = 400
paddle_y = 500
paddle_width = 30
paddle_height = 10
paddle_speed = 5

# Brick setup
brick_rows = 8
brick_cols = 14
brick_width = 40
brick_height = 10
brick_padding = 5 # Space between bricks
start_x = 100
stop_y = 100

# Brick colors: red, orange, green, yellow
brick_colors = [(255, 0, 0), (255, 165, 0), (0, 255, 0), (255, 255, 0)]



# Main game loop
while running:
    for event in pygame.event.get(): #
        if event.type == pygame.QUIT:
            running = False

    # Handle paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    screen.fill((0, 0, 0))  # Clear screen with black

    # Draw bricks
    for row in range(brick_rows):
        color_index = row // 2  # Change color every two rows
        brick_color = brick_colors[color_index % len(brick_colors)] # Get color based on row
        for col in range(brick_cols):
            x = start_x + col * (brick_width + brick_padding)
            y = stop_y + row * (brick_height + brick_padding)
            pygame.draw.rect(screen, brick_color, (x, y, brick_width, brick_height))


    # Draw paddle 
    pygame.draw.rect(screen, (0, 0, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.display.flip() # puts the updated screen contents on display
    clock.tick(60) # Limit to 60 FPS

pygame.quit() # Quit Pygame

