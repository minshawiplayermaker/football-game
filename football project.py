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

        # Draw the left leg
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (self.x + 8, self.y + 45),
            (self.x + 8, self.y + 65),
            5
        )

        # Draw the right leg
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (self.x + 22, self.y + 45),
            (self.x + 22, self.y + 65),
            5
        )

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


# These are player objects
player1 = Player(200, 300, (255, 0, 0))
player2 = Player(600, 300, (0, 0, 255))


# Player 1 controls: A, D, W, S
player1_controls = [
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s
]

# Player 2 controls: Left, Right, Up, Down
player2_controls = [
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN
]


# The ball starts in the middle
ball_x = 400
ball_y = 350

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gets the keys being pressed
    keys = pygame.key.get_pressed()

    # Move both players
    player1.move(keys, player1_controls)
    player2.move(keys, player2_controls)

    # Make the ball follow Player 1
    if abs(player1.x - ball_x) < 50 and abs(player1.y - ball_y) < 60:
        ball_x = player1.x + 40
        ball_y = player1.y + 40

    # Make the ball follow Player 2
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
# 3. Keep the players' heads on their bodies