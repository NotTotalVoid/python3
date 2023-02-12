import pygame

# Initialize Pygame
pygame.init()

# Define color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the width and height of the window
dimensions = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(dimensions)

pygame.display.set_caption("Draggable Label")

# Create the label
text = "Drag me!"
font = pygame.font.Font(None, 36)
label_rend = font.render(text, True, BLACK)
label = pygame.Rect(100, 100, label_rend.get_width(), label_rend.get_height())

# Variable to keep track of the label's initial position
initial_position = (label.x, label.y)

# Function to draw the label on the screen
def draw_label():
    pygame.draw.rect(screen, WHITE, label)
    screen.blit(label_rend, label)

# Main game function
def game():
    done = False
    dragging = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if label.collidepoint(event.pos):
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    label.x += event.rel[0]
                    label.y += event.rel[1]
        screen.fill(BLACK)
        draw_label()
        pygame.display.flip()

    pygame.quit()

game()
