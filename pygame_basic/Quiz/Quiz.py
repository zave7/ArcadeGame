# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30 으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로, 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png

import pygame
import random as rd
################################## 기본 초기화 (반드시 해야 하는 것들)##################################

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 설정

# 화면 타이틀 설정
pygame.display.set_caption("똥피하기 게임") # 게임 이름

# FPS 설정
clock = pygame.time.Clock()

######################################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 화면
background = pygame.image.load("C:\\dev\\workspace\\python-ArcadeGame\\pygame_basic\\Quiz\\background.png")

# 랜덤 좌표 값 구하는 함수
def getEnemyXPosition():
    return rd.randint(0, screen_width - enemy_width)

# 캐릭터
character = pygame.image.load("C:\\dev\\workspace\\python-ArcadeGame\\pygame_basic\\Quiz\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 똥
enemy = pygame.image.load("C:\\dev\\workspace\\python-ArcadeGame\\pygame_basic\\Quiz\\enemy.jpg")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = getEnemyXPosition()
enemy_y_pos = -enemy_height

# 캐릭터 좌표
c_to_x = 0
c_to_y = 0

# 똥 좌표
e_to_x = 0
e_to_y = 0

# 캐릭터 속도
character_speed = 0.6

# 똥 속도
enemy_speed = 0.5

running = True
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                c_to_x = -1
            if event.key == pygame.K_RIGHT:
                c_to_x = 1
            if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
                print("동시에눌림")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                c_to_x = 0

    character_x_pos += character_speed * dt * c_to_x
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > ( screen_width - character_width ):
        character_x_pos = screen_width - character_width

    # 똥의 y 좌표 조정
    # e_to_y += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_x_pos = getEnemyXPosition()
        enemy_y_pos = -enemy_height
    enemy_y_pos += enemy_speed * dt

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    # 3. 게임 캐릭터 위치 정의
    

    # 4. 충돌 처리
    if character_rect.colliderect(enemy_rect):
        print("게임 종료")
        running = False

    # 5. 화면에 그리기

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

pygame.quit()