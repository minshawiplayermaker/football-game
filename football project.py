import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Football Game")

clock = pygame.time.Clock()

green = (50, 170, 70)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (30, 50, 200)
yellow = (255, 220, 0)

# Players
player1 = pygame.Rect(100, 230, 40, 50)
player2 = pygame.Rect(660, 230, 40, 50)

# Ball
ball = pygame.Rect(390, 240, 20, 20)

score1 = 0
score2 = 0
ball_speed = 0
game_over = False

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if game_over == False:

        # Player 1 controls
        if keys[pygame.K_w]:
            player1.y = player1.y - 3
        if keys[pygame.K_s]:
            player1.y = player1.y + 3
        if keys[pygame.K_a]:
            player1.x = player1.x - 3
        if keys[pygame.K_d]:
            player1.x = player1.x + 3

        # Player 2 controls
        if keys[pygame.K_UP]:
            player2.y = player2.y - 3
        if keys[pygame.K_DOWN]:
            player2.y = player2.y + 3
        if keys[pygame.K_LEFT]:
            player2.x = player2.x - 3
        if keys[pygame.K_RIGHT]:
            player2.x = player2.x + 3

        # Player 1 kick
        if keys[pygame.K_SPACE]:
            if player1.colliderect(ball):
                ball_speed = 6

        # Player 2 kick
        if keys[pygame.K_RETURN]:
            if player2.colliderect(ball):
                ball_speed = -6

        # Keep players on the field
        if player1.x < 25:
            player1.x = 25
        if player1.x > 735:
            player1.x = 735
        if player1.y < 120:
            player1.y = 120
        if player1.y > 400:
            player1.y = 400

        if player2.x < 25:
            player2.x = 25
        if player2.x > 735:
            player2.x = 735
        if player2.y < 120:
            player2.y = 120
        if player2.y > 400:
            player2.y = 400

        # Move the ball
        ball.x = ball.x + ball_speed

        # Goal for Barcelona
        if ball.x < 0:
            score2 = score2 + 1
            ball.x = 390
            ball.y = 240
            ball_speed = 0

        # Goal for Real Madrid
        if ball.x > 780:
            score1 = score1 + 1
            ball.x = 390
            ball.y = 240
            ball_speed = 0

        # Check winner
        if score1 == 3:
            game_over = True

        if score2 == 3:
            game_over = True

    # Draw field
    screen.fill(green)

    pygame.draw.rect(screen, white, (20, 100, 760, 350), 4)
    pygame.draw.line(screen, white, (400, 100), (400, 450), 3)
    pygame.draw.circle(screen, white, (400, 275), 60, 3)

    # Goals
    pygame.draw.rect(screen, white, (0, 220, 20, 110), 3)
    pygame.draw.rect(screen, white, (780, 220, 20, 110), 3)

    # Real Madrid player
    pygame.draw.circle(screen, white, (120, 218), 15)
    pygame.draw.rect(screen, white, player1)

    # Barcelona player
    pygame.draw.circle(screen, black, (680, 218), 15)
    pygame.draw.rect(screen, blue, player2)

    # Ball
    pygame.draw.circle(screen, white, ball.center, 10)
    pygame.draw.circle(screen, black, ball.center, 10, 2)

    # Score
    font = pygame.font.Font(None, 40)

    score_text = font.render(
        "Real Madrid " + str(score1) + " - " + str(score2) + " Barcelona",
        True,
        white
    )

    screen.blit(score_text, (230, 40))

    # Game over
    if game_over:
        big_font = pygame.font.Font(None, 70)

        game_text = big_font.render(
            "GAME OVER",
            True,
            yellow
        )

        screen.blit(game_text, (270, 180))

        if score1 == 3:
            winner = font.render(
                "Real Madrid wins!",
                True,
                white
            )
        else:
            winner = font.render(
                "Barcelona wins!",
                True,
                white
            )

        screen.blit(winner, (300, 260))

    pygame.display.update()
    clock.tick(60)

pygame.quit()