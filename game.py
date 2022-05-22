    if robin.x_speed > 0:
        robin.image = pygame.transform.scale(walkRight[img_counter//3], (player_width, 120)).convert_alpha()
    elif robin.x_speed < 0:
        robin.image = pygame.transform.scale(walkLeft[img_counter//3], (player_width, 120)).convert_alpha()
    else:
        robin.image = pygame.transform.scale(playerStand[img_counter//6], (player_width, 120)).convert_alpha()
    img_counter += 1
    all_sprites.draw(window)
 
class Enemy(GameSprite): 
    side = "left"
    def update(self):
        if self.rect.x <= 0:
            self.side = "right"
        if self.rect.x >= win_width /2:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
 
# Запуск игры
pygame.display.set_caption("ARCADA") 
window = pygame.display.set_mode([win_width, win_height])
 
background = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height)) 
 
# список всех персонажей игры:
all_sprites = pygame.sprite.Group()
# список препятствий:
barriers = pygame.sprite.Group()
# список врагов:
enemies = pygame.sprite.Group()
# список мин:
bombs = pygame.sprite.Group()
 
# создаем персонажа, добавляем его в список всех спрайтов:
robin = Hero(img_file_hero) 
all_sprites.add(robin)
# создаем стены, добавляем их:
w = Wall(50, 150, 480, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 0, 30, 400) 
barriers.add(w)
all_sprites.add(w)
w = Wall(350, 380, 640, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(-200, 590, 1600, 20)
barriers.add(w)
all_sprites.add(w)
 
