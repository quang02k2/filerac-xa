import pygame

pygame.init()  # khởi tạo tất cả các mô-đun pygame đã nhập  gọi nó ở vị trí đầu tiên
screen = pygame.display.set_mode((800, 400))  # Khởi tạo mô-đun hiển thị (rộng, cao)
pygame.display.set_caption("Cuoc chien covid")
clock = pygame.time.Clock()

bautroi_surface = pygame.image.load("game/graphics/300.png") #  load ảnh bầu trời
matdat_surface = pygame.image.load("game/graphics/100.png") # loạt ảnh mặt đất

#add player
player_walk = pygame.image.load("game/graphics/Player/rsz_1doctor_walk_e1.png")  #load ảnh player

while True:
    # Tạo nút thoát khi bấm nút x trên cửa sổ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bautroi_surface,(0,0)) # đặt ảnh bầu trời
    screen.blit(matdat_surface,(0,300)) # đặt ảnh mặt đất
    screen.blit(player_walk,(20,170)) # đặt ảnh player
    pygame.display.update()
    clock.tick(60)
