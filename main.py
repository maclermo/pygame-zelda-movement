import os
import pygame

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DIR_RES = os.path.join(BASE_DIR, "assets")

WIDTH = 256
HEIGHT = 224
FPS = 60


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Zelda")

        self.running = True

        self.background_x = -1920
        self.background_y = -3120

        self.color_key = (0, 64, 64)

        self.link_x = int(WIDTH / 2)
        self.link_y = int(HEIGHT / 2)
        self.link_orientation = 0
        self.link_speed = 2
        self.link_down = (1, 4, 16, 21)
        self.link_up = (1, 111, 16, 21)
        self.link_right = (1, 58, 16, 21)
        self.link_left = (457, 58, 16, 21)

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load(os.path.join(DIR_RES, "overworld.png")).convert()

        self.link_image = pygame.image.load(os.path.join(DIR_RES, "link.png")).convert()
        self.link_image.set_colorkey(self.color_key)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            key = pygame.key.get_pressed()

            if key[pygame.K_DOWN]:
                self.link_orientation = 0
                if self.link_y >= HEIGHT - self.link_down[3] - 50:
                    self.background_y -= self.link_speed
                else:
                    self.link_y += self.link_speed

            elif key[pygame.K_UP]:
                self.link_orientation = 1
                if self.link_y <= 0 + 50:
                    self.background_y += self.link_speed
                else:
                    self.link_y -= self.link_speed

            if key[pygame.K_RIGHT]:
                self.link_orientation = 2
                if self.link_x >= WIDTH - self.link_right[2] - 50:
                    self.background_x -= self.link_speed
                else:
                    self.link_x += self.link_speed

            elif key[pygame.K_LEFT]:
                self.link_orientation = 3
                if self.link_x <= 0 + 50:
                    self.background_x += self.link_speed
                else:
                    self.link_x -= self.link_speed

            self.screen.blit(self.background_image, (self.background_x, self.background_y))

            if self.link_orientation == 0:
                self.screen.blit(self.link_image, (self.link_x, self.link_y), self.link_down)
            elif self.link_orientation == 1:
                self.screen.blit(self.link_image, (self.link_x, self.link_y), self.link_up)
            elif self.link_orientation == 2:
                self.screen.blit(self.link_image, (self.link_x, self.link_y), self.link_right)
            elif self.link_orientation == 3:
                self.screen.blit(self.link_image, (self.link_x, self.link_y), self.link_left)

            pygame.display.flip()
            self.clock.tick(FPS)


game = Game()
