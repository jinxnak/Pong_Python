import pygame

class Pong ():
    pygame.init()
    def __init__(self):
        self.running = True
        self.WIDTH, self.HIGH = 1880, 980
        self.screen = pygame.display.set_mode ((self.WIDTH, self.HIGH))
        self.BKG_W = (255, 255, 255)
        self.image_game = pygame.image.load ("pong.jpg")
        self.image_t = pygame.transform.scale (self.image_game, (self.WIDTH, self.HIGH))
        self.x1, self.y1, self.x2, self.y2 = 50, 400, 1800, 500
        self.ball_x, self.ball_y = 87, 420
        self.P1_UP, self.P1_DOWN, self.P2_UP, self.P2_DOWN = False, False, False, False

    def check_event (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.P2_UP = True
                if event.key == pygame.K_DOWN:
                    self.P2_DOWN = True
                if event.key ==	pygame.K_z:
                    print("z")
                    self.P1_UP = True
                if event.key == pygame.K_s:
                    print ("s")
                    self.P1_DOWN = True
    
    def resset_key(self):
        self.P1_UP, self.P1_DOWN, self.P2_UP, self.P2_DOWN = False, False, False, False
    
    def main (self):
        pygame.display.set_caption ("PONG PYTHON");
        self.screen.fill(self.BKG_W)
        self.screen.blit (self.image_t, (0, 0))
        while self.running:
            self.check_event ()
            self.resset_key()
            pygame.draw.rect(self.screen, (255, 255, 255), [self.x1, self.y1, 20, 200], 0)
            pygame.draw.rect(self.screen, (255, 255, 255), [self.x2, self.y2, 20, 200], 0)
            pygame.draw.circle (self.screen, (255, 0, 0), [self.ball_x, self.ball_y,], 17, 0)
            pygame.display.flip ()

