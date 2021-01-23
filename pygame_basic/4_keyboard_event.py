# 파이게임 설치 확인
# import pygame

# 파이게임을 위한 뼈대 생성 py

import pygame
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 설정

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이미지 불러오기
background = pygame.image.load("C:\\dev\\workspace\\python-ArcadeGame\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\dev\\workspace\\python-ArcadeGame\\pygame_basic\\character.png")

# 캐릭터는 항상 움직임
character_size = character.get_rect().size # 이미지 사이즈 가져오기
character_width = character_size[0] # 가로크기
character_height = character_size[1] # 세로크기
character_x_pos = ( screen_width / 2 ) - ( character_width / 2 ) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프가 실행되고 있어야 프로그램이 계속 실행중인 상태에 있게된다.
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 이벤트를 감지하는 로직
        if event.type == pygame.QUIT: # 종료 이벤트 감지
            running = False
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 0.8
            elif event.key == pygame.K_RIGHT:
                to_x += 0.8
            elif event.key == pygame.K_UP:
                to_y -= 0.8
            elif event.key == pygame.K_DOWN:
                to_y += 0.8
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # pass
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # pass
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 캐릭터가 화면 밖으로 나가지 않도록 좌표 조정

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > ( screen_width - character_width ):
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > ( screen_height - character_height ):
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임 화면을 다시 그리기 (반드시 계속 호출 필요)

# pygame 종료
pygame.quit()