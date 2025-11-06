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
paddle_width = 40
paddle_height = 10
paddle_speed = 5

# Brick setup
brick_rows = 8
brick_cols = 14
brick_width = 40
brick_height = 10
brick_padding = 5 # Space between bricks
start_x = 100
start_y = 100

# Brick colors: red, orange, green, yellow
brick_colors = [(255, 0, 0), (255, 165, 0), (0, 255, 0), (255, 255, 0)]



# Ball setup
x_ball = 400 # Initial x position of the ball
y_ball = 400 # Initial y position of the ball
delta_x = 2.5 # Horizontal speed of the ball
delta_y = 2.5 # Vertical speed of the ball
radius_ball = 5 # Radius of the ball
ball_respawn_delay = 1000  # milliseconds

bricks = []
for row in range(brick_rows):
    color_index = row // 2  # Change color every two rows
    brick_color = brick_colors[color_index % len(brick_colors)] # Get color based on row
    for col in range(brick_cols):
        x = start_x + col * (brick_width + brick_padding)  # Calculate x position
        y = start_y + row * (brick_height + brick_padding) # Calculate y position
        bricks.append((x, y, brick_color))  # Store brick position and color

# Set up font for score and lives display
font = pygame.font.Font(None, 36)
score = 0
lives = 3

# Brick points
brick_points = {(255, 0, 0): 7, (255, 165, 0): 5, (0, 255, 0): 3, (255, 255, 0): 1}


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

    # Store ball's current position
    prev_x_ball = x_ball
    prev_y_ball = y_ball

    # Create Rect objects for paddle and ball
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    ball_rect = pygame.Rect(x_ball - radius_ball, y_ball - radius_ball, radius_ball * 2, radius_ball * 2)

    # Check for collision between ball and paddle
    if ball_rect.colliderect(paddle_rect):
        delta_y = -delta_y  # Reverse ball direction on collision
         

    screen.fill((0, 0, 0))  # Clear screen with black

    # List to hold bricks to be removed
    bricks_to_remove = [] 
    
    for brick in bricks:
        x, y, brick_color = brick
        brick_rect = pygame.Rect(x, y, brick_width, brick_height)
        pygame.draw.rect(screen, brick_color, brick_rect)
        if ball_rect.colliderect(brick_rect):
            prev_y_ball = y_ball - delta_y
            prev_x_ball = x_ball - delta_x
            if prev_y_ball + radius_ball <= brick_rect.top or prev_y_ball - radius_ball >= brick_rect.bottom:
                delta_y = -delta_y  # Reverse ball direction on collision
            if prev_x_ball + radius_ball <= brick_rect.left or prev_x_ball - radius_ball >= brick_rect.right:
                delta_x = -delta_x  # Reverse ball direction on collision
            bricks_to_remove.append(brick)  # Remove the brick on collision
            score += brick_points[brick_color]  # Update score based on brick color

    # Remove collided bricks
    for brick in bricks_to_remove:
        bricks.remove(brick)
            
    

    # Draw ball
    x_ball += delta_x
    y_ball += delta_y
    if x_ball > WIDTH - radius_ball or x_ball < radius_ball:
        delta_x = -delta_x
    if y_ball < radius_ball:
        delta_y = -delta_y
    if y_ball > HEIGHT - radius_ball:
        lives -= 1
        x_ball = 400
        y_ball = 400
        delta_y = -delta_y

        if lives <= 0:
            # Game Over - draw final screen
            screen.fill((0, 0, 0))
            
            game_over_surface = font.render("GAME OVER", True, (255, 0, 0))
            game_over_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
            screen.blit(game_over_surface, game_over_rect)
            
            final_score_surface = font.render(f"Final Score: {score}", True, (255, 255, 255))
            final_score_rect = final_score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
            screen.blit(final_score_surface, final_score_rect)
            
            pygame.display.flip()
            pygame.time.delay(3000)  # Show game over screen for 3 seconds
            
            # Wait for user to close the window
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
                        running = False
        else:
            # Respawn ball if lives remaining
            x_ball = 400
            y_ball = 400
            delta_y = -delta_y

        # Draw everything BEFORE the delay 
        pygame.draw.rect(screen, (0, 0, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
        
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        
        lives_surface = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(lives_surface, (WIDTH - 120, 10))
        
        pygame.draw.circle(screen, (255, 255, 255), (x_ball, y_ball), radius_ball)

        pygame.display.flip()  # Show updated lives/ball position
        pygame.time.delay(1000)  # 1 second delay before ball respawns

    # Draw paddle 
    pygame.draw.rect(screen, (0, 0, 255), (paddle_x, paddle_y, paddle_width, paddle_height))

    # Update and draw score
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))  # White color
    screen.blit(score_surface, (10, 10))  # Draw at position (10, 10)

    # Update and draw lives
    lives_surface = font.render(f"Lives: {lives}", True, (255, 255, 255))  # White color
    screen.blit(lives_surface, (WIDTH - 120, 10))  # Draw at top-right corner

    pygame.draw.circle(screen, (255, 255, 255), (x_ball,y_ball), radius_ball)
    
    pygame.display.flip() # puts the updated screen contents on display

    clock.tick(60) # Limit to 60 FPS

pygame.quit() # Quit Pygame

