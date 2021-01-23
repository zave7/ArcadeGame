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

# 이벤트 루프가 실행되고 있어야 프로그램이 계속 실행중인 상태에 있게된다.
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 이벤트를 감지하는 로직
        if event.type == pygame.QUIT: # 종료 이벤트 감지
            running = False

    # screen.fill((0,0,255)) # 색으로 배경 채우기
    screen.blit(background, (0,0)) # 배경 그리기

    pygame.display.update() # 게임 화면을 다시 그리기 (반드시 계속 호출 필요)

# pygame 종료
pygame.quit()