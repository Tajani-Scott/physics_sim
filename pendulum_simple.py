import pygame
import math

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
LIGHT_DIRECTION = pygame.Vector3(0.5, 0.5, -0.5).normalize()

def calculate_lighting(normal):
    intensity = LIGHT_DIRECTION.dot(normal)
    return max(intensity, 0)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

g = 9.81
L = 450
theta0 = math.pi/2  # (radians)
omega0 = 0.0  # (rad/s)

RECTANGLE_WIDTH = 80
RECTANGLE_HEIGHT = 40
STATS_WIDTH = 200
STATS_HEIGHT = 100

dt = 0.6

theta = theta0
omega = omega0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pendulum Simulation")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    alpha = -g / L * math.sin(theta)
    omega += alpha * dt
    theta += omega * dt
    omega *= 0.995

    font = pygame.font.SysFont('Garamond', 16)

    screen.fill(BLACK)

    rect_stats_x = SCREEN_WIDTH // 2 - STATS_WIDTH
    rect_stats_y = SCREEN_HEIGHT // 2 - STATS_HEIGHT
    pygame.draw.rect(screen, WHITE, (50, 50, 250, 150), 1)

    kinetic_energy_text = f"Kinetic Energy: {0.5 * L **2 * omega **2:.2f} J"
    potential_energy_text = f"Potential Energy: {g * L * (1 - math.cos(theta)):.2f} J"
    time_text = f"Time: {pygame.time.get_ticks() / 1000:.2f} seconds"
    angle_text = f"Angle: {math.degrees(theta):.2f} degrees"

    kinetic_energy_render = font.render(kinetic_energy_text, True, WHITE)
    potential_energy_render = font.render(potential_energy_text, True, WHITE)
    time_render = font.render(time_text, True, WHITE)
    angle_render = font.render(angle_text, True, WHITE)

    screen.blit(kinetic_energy_render, (70, 70))
    screen.blit(potential_energy_render, (70, 100))
    screen.blit(time_render, (70, 130))
    screen.blit(angle_render, (70, 160))

    rect_x = SCREEN_WIDTH // 2 - RECTANGLE_WIDTH // 2
    rect_y = SCREEN_HEIGHT // 4 - RECTANGLE_HEIGHT // 5
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, RECTANGLE_WIDTH, RECTANGLE_HEIGHT))

    pendulum_x = int(SCREEN_WIDTH / 2 + L * math.sin(theta))
    pendulum_y = int(SCREEN_HEIGHT / 4 + L * math.cos(theta))

    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 30), (pendulum_x, pendulum_y), 3)
    pygame.draw.circle(screen, WHITE, (pendulum_x, pendulum_y), 35)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()