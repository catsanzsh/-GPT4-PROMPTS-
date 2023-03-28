import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions and create a screen
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Paddle dimensions
paddle_width, paddle_height = 20, 100

# Paddle speed
paddle_speed = 5

# Create paddles, ball, and font
paddle_a = pygame.Rect(10, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)
paddle_b = pygame.Rect(screen_width - 30, screen_height / 2 - paddle_height / 2, paddle_width, paddle_height)
ball = pygame.Rect(screen_width / 2 - 10, screen_height / 2 - 10, 20, 20)
font = pygame.font.Font(None, 36)

# Ball velocity
ball_speed = [3, 3]

# Scores
score_a, score_b = 0, 0

def reset_ball():
    ball.x = screen_width / 2 - 10
    ball.y = screen_height / 2 - 10
    ball_speed[0] = -ball_speed[0]
    ball_speed[1] = -ball_speed[1]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_UP] and paddle_a.top > 0:
        paddle_a.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_a.bottom < screen_height:
        paddle_a.y += paddle_speed
    if keys[pygame.K_w] and paddle_b.top > 0:
        paddle_b.y -= paddle_speed
    if keys[pygame.K_s] and paddle_b.bottom < screen_height:
        paddle_b.y += paddle_speed

    # Move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Collision with walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed[1] = -ball_speed[1]

    # Collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed[0] = -ball_speed[0]

    # Ball out of bounds
    if ball.left <= 0:
        score_b += 1
        reset_ball()
    if ball.right >= screen_width:
        score_a += 1
        reset_ball()

    # Update the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Render and display scores
    score_text = font.render(f"{score_a} - {score_b}", True, GREEN)
    screen.blit(score_text, (screen_width / 2 - score_text.get_width() / 2, 10))

    pygame.display.flip()
    pygame.time.delay(16)
