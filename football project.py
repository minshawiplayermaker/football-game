import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Football Game")

clock = pygame.time.Clock()


# This function draws the football on the screen
def draw_ball(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)


# A class is like a blueprint for making players
class Player:

    # This sets up the player's starting information
    def __init__(self, x, y, shirt_color):
        self.x = x
        self.y = y
        self.shirt_color = shirt_color

    # This function draws the player
    def draw(self):

        # Draw the player's body
        pygame.draw.rect(
            screen,
            self.shirt_color,
            (self.x, self.y, 30, 45)
        )

        # Draw the player's head
        pygame.draw.circle(
            screen,
            (255, 200, 150),
            (self.x + 15, self.y - 10),
            12
        )

        # Draw the player's left leg
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (self.x + 8, self.y + 45),
            (self.x + 8, self.y + 65),
            5
        )

        # Draw the player's right leg
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (self.x + 22, self.y + 45),
            (self.x + 22, self.y + 65),
            5
        )


# These are objects made from the Player class
# Each object represents one player
player1 = Player(200, 300, (255, 0, 0))
player2 = Player(600, 300, (0, 0, 255))


# This keeps the game running
running = True

while running:

    # Checks if the player closes the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Makes the football field green
    screen.fill((40, 150, 40))

    # Draws both players
    player1.draw()
    player2.draw()

    # Draws the football
    draw_ball(400, 350)

    # Updates the screen
    pygame.display.update()

    # Keeps the game running at 60 frames per second
    clock.tick(60)

pygame.quit()


# Things I need to add:
# 1. Make the players dribble the ball
# 2. Make the players block
# 3. Keep there heads on their bodies