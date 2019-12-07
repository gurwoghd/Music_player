'''
작성자: 홍혁재
작성일자: 2019년 8월 2일 금요일
프로그램 설명:  음악 플레이어입니다.
                윈도우상에서 잘 작동합니다.
'''

import pygame as pg
import sys
pg.init()
pg.mixer.init()

white = (255,255,255)
black = (0,0,0)
WIDTH = 700
HEIGHT = 600
PlayerHelp = "q: 프로그램 종료 | s: 음소거/음소거 해제"
#IsHelp = False # 현재 도움말 창인가?
IsFull = False # 전체 화면인가?

music_path = "Music/" # 음악 파일을 찾는 경로
img_path = "images/" # 이미지 파일을 찾는 경로
musics = [
    ["birthday-Somi", music_path + "birthday.mp3", img_path + "birthday-전소미.jpeg"],
    ["2002-Anne Marie", music_path + "2002.mp3", img_path + "2002-Anee Marie.jpeg"],
    ["When The Party's over", music_path + "whenthepartyisover.mp3", img_path + "BillieEilish2.jpg"]
] # 음악 파일들 ( 제목, 음악 위치, 음악 이미지 )
Sidx = 0 # 음악을 지정하기 위한 인덱스
#IsPlaying = True # 음악 재생 중인가?

screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(white)
pg.display.set_caption("음악 플레이어")

font = pg.font.Font("freesansbold.ttf", 50) # 폰트
# 화면에 텍스트 쓰기
def ShowText(song):
    text = font.render(song, True, black, white)
    textRect = text.get_rect()
    textRect.center = (WIDTH / 2, HEIGHT - 50)
    screen.blit(text, textRect)

# 화면에 이미지 띄우기
def ShowImage(image):
    myImg = pg.image.load(image)
    myImg = pg.transform.scale(myImg, (WIDTH, 500))
    ImgPos = (0,0) # 이미지 위치
    screen.blit(myImg, ImgPos)

# 음악 재생
def PlayMusic(music):
    pg.mixer.music.load(music) # 음악을 로드
    pg.mixer.music.play(0)

# 음악 종료와 프로그램 종료
def StopMusic():
    print("음악 플레이어를 종료합니다\n")
    pg.mixer.music.stop()
    pg.quit()
    sys.exit()

# 음악 일시정지
def PauseMusic(flag):
    if flag:
        pg.mixer.music.pause()
    else:
        pg.mixer.music.unpause()

PlayMusic(musics[Sidx][1]) # 해당 음악 재생
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: # 종료 버튼을 누르면 종료
            StopMusic()
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT: # 오른쪽 화살표를 누르면 다음 곡
                if len(musics) - 1 > Sidx: Sidx += 1
                else: Sidx = 0 # 마지막 곡의 다음 곡은 처음 곡
                PlayMusic(musics[Sidx][1]) # 해당 음악 재생
                screen.fill(white)
                
            elif event.key == pg.K_LEFT: # 왼쪽 화살표를 누르면 이전 곡
                if 0 < Sidx: Sidx -= 1
                else: Sidx = len(musics) - 1 # 처음 곡의 이전 곡은 마지막 곡
                PlayMusic(musics[Sidx][1]) # 해당 음악 재생
                screen.fill(white)
                
            elif event.key == pg.K_SPACE: # 스페이스바를 누르면 멈춤 또는 재생
                PauseMusic(IsPlaying)
                IsPlaying = not IsPlaying
                
            elif event.key == pg.K_q: # q키를 누르면 프로그램 종료
                StopMusic()
                
            '''
            elif event.key == pg.K_h: # h키를 누르면 도움말을 띄움
                if not IsHelp: # 도움말 창이 아니라면 도움말 창을 염
                    pg.display.set_mode((400,100))
                    pg.display.set_caption("도움말")
                    pg.display.flip()
                else: # 도움말 창이라면 도움말 창을 닫음
                    pass
            '''

    try:
        if pg.mixer.music.get_busy() == False: # 음악이 끝나면 다음 곡 재생
            if len(musics) - 1 > Sidx: Sidx += 1
            else: Sidx = 0
            PlayMusic(musics[Sidx][1])
            screen.fill(white)
        
        ShowText(musics[Sidx][0]) # 해당 음악의 제목을 표시함
        ShowImage(musics[Sidx][2]) # 해당 음악의 이미지를 표시
        
    except KeyboardInterrupt as e:
        StopMusic()
    pg.display.flip()
