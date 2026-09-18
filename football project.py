import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Football Game")

clock = pygame.time.Clock()


# This function draws the football
def draw_ball(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)


# This class is like a blueprint for making players
class Player:

    # This sets up the player's starting information
    def __init__(self, x, y, shirt_color):
        self.x = x
        self.y = y
        self.shirt_color = shirt_color
        self.speed = 5
        self.blocking = False

    # This function moves the player
    def move(self, keys, controls):

        if keys[controls[0]]:
            self.x -= self.speed

        if keys[controls[1]]:
            self.x += self.speed

        if keys[controls[2]]:
            self.y -= self.speed

        if keys[controls[3]]:
            self.y += self.speed

    # This function lets the player block
    def block(self, keys, block_key):

        if keys[block_key]:
            self.blocking = True
        else:
            self.blocking = False

    # This function draws the player
    def draw(self):

        # Draw the body
        pygame.draw.rect(
            screen,
            self.shirt_color,
            (self.x, self.y, 30, 45)
        )

        # Draw the head
        pygame.draw.circle(
            screen,
            (255, 200, 150),
            (self.x + 15, self.y - 10),
            12
        )

        # Draw the legs
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (self.x + 8, self.y + 45),
            (self.x + 8, self.y + 65),
            5
        )

        pygame.draw.line(
            screen,
            (0, 0, 0),
            (self.x + 22, self.y + 45),
            (self.x + 22, self.y + 65),
            5
        )

        # Draw arms when the player is blocking
        if self.blocking:

            pygame.draw.line(
                screen,
                (0, 0, 0),
                (self.x, self.y + 15),
                (self.x - 15, self.y + 30),
                5
            )

            pygame.draw.line(
                screen,
                (0, 0, 0),
                (self.x + 30, self.y + 15),
                (self.x + 45, self.y + 30),
                5
            )


# Player objects
player1 = Player(200, 300, (255, 0, 0))
player2 = Player(600, 300, (0, 0, 255))


# Player 1 controls
player1_controls = [
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s
]

# Player 2 controls
player2_controls = [
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN
]


# Ball starting position
ball_x = 400
ball_y = 350


# Game loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are being pressed
    keys = pygame.key.get_pressed()

    # Move players
    player1.move(keys, player1_controls)
    player2.move(keys, player2_controls)

    # Player 1 blocks with SPACE
    player1.block(keys, pygame.K_SPACE)

    # Player 2 blocks with ENTER
    player2.block(keys, pygame.K_RETURN)

    # Ball follows Player 1
    if abs(player1.x - ball_x) < 50 and abs(player1.y - ball_y) < 60:
        ball_x = player1.x + 40
        ball_y = player1.y + 40

    # Ball follows Player 2
    if abs(player2.x - ball_x) < 50 and abs(player2.y - ball_y) < 60:
        ball_x = player2.x - 10
        ball_y = player2.y + 40

    # Green football field
    screen.fill((40, 150, 40))

    # Draw players
    player1.draw()
    player2.draw()

    # Draw ball
    draw_ball(ball_x, ball_y)

    pygame.display.update()

    clock.tick(60)

pygame.quit()


# Things I need to add:
# 1. Make the players dribble the ball
# 2. Make the players block
# 3. Keep their heads on their bodies