"""Naval board-game presentation, viewport and non-blocking visual effects."""
from functools import lru_cache
from pathlib import Path
import math
import os
import random
import sys
import time
import pygame

ROOT = Path(getattr(sys, '_MEIPASS', Path(__file__).resolve().parent))
SIZE = (1599, 860)
GOLD = (222, 181, 99)
CREAM = (250, 234, 199)
MUTED = (156, 193, 202)
NAVY = (8, 29, 43)
COLORS = [(80,185,239),(112,198,154),(236,211,108),(237,121,105),(231,167,99),(186,156,222)]
PAWN_SIZE = 26
FAST = os.environ.get('KOXINGA_FAST') == '1'
_window = None
_viewport = pygame.Rect(0,0,*SIZE)
_particles = []
_last_turn = None
_last_frame = time.monotonic()
_rng = random.Random(1661)  # Visual effects never consume the game's random stream.

def asset(path):
    return str(ROOT / path)

def init_display():
    global _window
    pygame.init()
    info=pygame.display.Info()
    scale=min(1.0, max(640,info.current_w-80)/SIZE[0], max(400,info.current_h-100)/SIZE[1])
    _window=pygame.display.set_mode((int(SIZE[0]*scale),int(SIZE[1]*scale)),pygame.RESIZABLE)
    pygame.display.set_caption('Koxinga 國姓爺 · 航海棋局')
    pygame.display.set_icon(pygame.image.load(asset('Image/ui_compass.png')))
    return pygame.Surface(SIZE).convert()

def present(surface, *unused):
    global _viewport
    w,h=_window.get_size()
    scale=min(w/SIZE[0],h/SIZE[1])
    size=(max(1,int(SIZE[0]*scale)),max(1,int(SIZE[1]*scale)))
    _viewport=pygame.Rect((w-size[0])//2,(h-size[1])//2,*size)
    _window.fill((3,12,20))
    _window.blit(pygame.transform.smoothscale(surface,size),_viewport)
    pygame.display.flip()

def mouse_pos():
    x,y=pygame.mouse.get_pos()
    return ((x-_viewport.x)*SIZE[0]/_viewport.w,(y-_viewport.y)*SIZE[1]/_viewport.h)

def quit_game():
    pygame.quit()
    raise SystemExit

def pause(seconds):
    if FAST: return
    until=time.monotonic()+seconds
    while time.monotonic()<until:
        for event in pygame.event.get([pygame.QUIT,pygame.KEYDOWN]):
            if event.type==pygame.QUIT or event.key==pygame.K_ESCAPE: quit_game()
        pygame.event.pump()
        pygame.time.wait(10)

@lru_cache(maxsize=48)
def font(size):
    return pygame.font.Font(asset('wqy-zenhei.ttf'),size)

@lru_cache(maxsize=1024)
def text(message,color=CREAM,size=18):
    return font(size).render(str(message),True,color)

@lru_cache(maxsize=64)
def sprite(name,size):
    return pygame.transform.smoothscale(pygame.image.load(asset('Image/ui_'+name+'.png')).convert(),size)

@lru_cache(maxsize=6)
def ship_token(player):
    token=pygame.Surface((PAWN_SIZE,PAWN_SIZE)).convert()
    token.fill(NAVY)
    token.blit(sprite('move',(PAWN_SIZE-4,PAWN_SIZE-4)),(2,2))
    pygame.draw.rect(token,COLORS[player],token.get_rect(),2,border_radius=4)
    badge=pygame.Rect(1,PAWN_SIZE-12,10,11)
    pygame.draw.rect(token,NAVY,badge,border_radius=2)
    token.blit(text(str(player+1),CREAM,10),(2,PAWN_SIZE-13))
    return token

@lru_cache(maxsize=32)
def panel_layer(size,alpha,border):
    layer=pygame.Surface(size,pygame.SRCALPHA)
    pygame.draw.rect(layer,(*NAVY,alpha),layer.get_rect(),border_radius=12)
    pygame.draw.rect(layer,(*border,220),layer.get_rect(),1,border_radius=12)
    return layer

def panel(surface,rect,alpha=220,border=GOLD):
    rect=pygame.Rect(rect)
    surface.blit(panel_layer(rect.size,alpha,tuple(border)),rect)

def put(surface,message,pos,size=18,color=CREAM):
    surface.blit(text(message,color,size),pos)

def button(surface,loc,label,image):
    rect=image.get_rect(topleft=loc)
    hovered=rect.collidepoint(mouse_pos())
    surface.blit(image,rect)
    if hovered:
        pygame.draw.rect(surface,GOLD,rect,2,border_radius=7)
    labels={'Roll':'擲骰','Swap':'交換骰子','Finish':'確認出牌','Fight':'開砲','Add Cannon':'投入火砲','Accept':'確認','Auto Take':'自動掠奪'}
    rendered=text(labels.get(label,label),GOLD if hovered else CREAM,16)
    surface.blit(rendered,rendered.get_rect(center=rect.center))

def burst(pos,color=GOLD,count=22,label=None):
    now=time.monotonic()
    for _ in range(count):
        angle=_rng.uniform(0,math.tau); speed=_rng.uniform(25,110)
        _particles.append((now,pos,math.cos(angle)*speed,math.sin(angle)*speed,color,None))
    if label: _particles.append((now,pos,0,-40,color,label))
    # Bound the effect budget during fast AI simulation or dense battles.
    del _particles[:-180]

def effects(surface,players,turn):
    global _last_turn,_particles
    now=time.monotonic()
    if turn!=_last_turn:
        p=players[turn]
        burst((p.x+PAWN_SIZE/2,p.y+PAWN_SIZE/2),COLORS[turn],12)
        _last_turn=turn
    p=players[turn]
    r=PAWN_SIZE//2+7+int(3*math.sin(now*4))
    pygame.draw.circle(surface,COLORS[turn],(int(p.x+PAWN_SIZE/2),int(p.y+PAWN_SIZE/2)),r,2)
    if p.mode==1:
        for i in range(3):
            pygame.draw.arc(surface,(128,193,213),(p.x-5-i*3,p.y+PAWN_SIZE-6+i*3,PAWN_SIZE+10+i*6,8),0,math.pi,1)
    _particles=[v for v in _particles if now-v[0]<1.15]
    for born,pos,vx,vy,color,label in _particles:
        age=now-born
        x,y=pos[0]+vx*age,pos[1]+vy*age+ (25*age*age if not label else 0)
        if label:
            tile=text(label,color,22).copy(); tile.set_alpha(int(255*(1-age/1.15)))
            surface.blit(tile,(x,y))
        else: pygame.draw.circle(surface,color,(int(x),int(y)),max(1,int(3*(1-age/1.15))))

def chrome(surface,players,turn,night,fight,end_game):
    # Darken only the sailing track; the island remains visible in the center.
    for rect in [(60,60,1479,160),(60,640,1479,160),(60,220,160,420),(1379,220,160,420)]:
        shade=pygame.Surface((rect[2],rect[3]),pygame.SRCALPHA); shade.fill((3,24,39,160)); surface.blit(shade,rect[:2])
    for rect in [(0,0,1599,58),(0,802,1599,58),(0,58,58,744),(1541,58,58,744)]:
        shade=pygame.Surface((rect[2],rect[3]),pygame.SRCALPHA); shade.fill((3,17,28,235)); surface.blit(shade,rect[:2])
    panel(surface,(220,220,118,420),235)
    panel(surface,(1188,220,188,420),235)
    put(surface,'艦 隊', (1230,224),16,GOLD)
    if fight is not None or end_game:
        panel(surface,(345,220,838,420),246)
    else:
        panel(surface,(362,310,790,270),218)
        surface.blit(sprite('admiral',(150,150)),(380,345))
        put(surface,'KOXINGA',(550,337),46,GOLD)
        put(surface,'國 姓 爺  ·  福 爾 摩 沙 航 路',(553,397),21)
        pygame.draw.line(surface,(114,107,77),(552,436),(1108,436))
        modes={0:'等待艦隊部署',1:'揚帆前進',2:'請點選航路箭頭',3:'請擲骰決定日夜行動',4:'可交換骰子，選牌後按確認',5:'請選擇行動牌，再按確認',6:'執行行動',7:'海戰進行中',8:'分配戰利品',9:'回合結束'}
        put(surface,f'艦隊 {turn+1}  /  '+('夜航' if night else '日航'),(552,451),22,COLORS[turn])
        put(surface,modes.get(players[turn].mode,''),(552,489),21)
        put(surface,'卡牌左側＝日間行動  ·  右側＝夜間行動',(552,536),16,MUTED)
    put(surface,'F1 說明 · Esc 離開',(1210,818),15,MUTED)

def help_overlay(surface):
    shade=pygame.Surface(SIZE,pygame.SRCALPHA);shade.fill((0,10,18,215));surface.blit(shade,(0,0))
    panel(surface,(415,155,770,530),255)
    put(surface,'航 海 指 南',(470,190),32,GOLD)
    lines=['你是艦隊 1，其餘五隊由電腦操作。','1  回合領航者擲兩顆骰子，可交換日夜順序。','2  點選一張手牌，再按「確認出牌」。','3  卡牌左半在日間執行，右半在夜間執行。','4  船＝前進；－1 / －2＝骰點扣除後前進。','5  糧食、金幣、火砲按骰點補給；進港需付資源。','6  分岔處點箭頭選路；遭遇其他船隻就進入海戰。','7  海戰可投入火砲，火焰骰代表立即獲勝。','8  航程結束後，金幣、位置與寶藏加總決定勝負。']
    for i,line in enumerate(lines): put(surface,line,(470,250+i*37),21)
    put(surface,'按 F1 返回棋局',(470,624),18,GOLD)

def start_menu(surface, background):
    clock=pygame.time.Clock()
    selected=0
    options=[('start','開始遊戲'),('tutorial','遊戲教學'),('back','返回封面'),('quit','離開遊戲')]
    while True:
        surface.blit(background,(0,0))
        shade=pygame.Surface(SIZE,pygame.SRCALPHA);shade.fill((2,15,27,205));surface.blit(shade,(0,0))
        panel(surface,(495,155,610,550),250)
        put(surface,'開 始 選 單',(676,192),34,GOLD)
        put(surface,'初次遊玩？從互動教學開始。',(620,252),22,MUTED)
        targets=[]
        for i,(action,label) in enumerate(options):
            rect=pygame.Rect(596,310+i*83,408,62)
            targets.append(rect)
            panel(surface,rect,255)
            if i==selected or rect.collidepoint(mouse_pos()): pygame.draw.rect(surface,GOLD,rect,3,border_radius=12)
            rendered=text(label,CREAM,25)
            surface.blit(rendered,rendered.get_rect(center=rect.center))
        put(surface,'↑ ↓ 選擇 · Enter 確認 · F1 / Esc 返回',(575,663),19,MUTED)
        present(surface)
        for event in pygame.event.get():
            if event.type==pygame.QUIT: quit_game()
            action=None
            if event.type==pygame.KEYDOWN:
                if event.key in (pygame.K_F1,pygame.K_ESCAPE): return 'back'
                if event.key==pygame.K_UP: selected=(selected-1)%len(options)
                elif event.key==pygame.K_DOWN: selected=(selected+1)%len(options)
                elif event.key in (pygame.K_RETURN,pygame.K_SPACE): action=options[selected][0]
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                for i,rect in enumerate(targets):
                    if rect.collidepoint(mouse_pos()): action=options[i][0];break
            if action=='quit': quit_game()
            if action: return action
        clock.tick(60)


def title_screen(surface,background):
    clock=pygame.time.Clock()
    cover=pygame.transform.smoothscale(pygame.image.load(asset('art/cover-reference.png')),(610,610))
    start=pygame.Rect(885,542,330,66)
    learn=pygame.Rect(885,620,330,58)
    mode='title'
    while True:
        if mode=='menu':
            result=start_menu(surface,background)
            if result=='start': return
            mode='tutorial' if result=='tutorial' else 'title'
            continue
        if mode=='tutorial':
            from tutorial import run
            if run(surface,background)=='start': return
            mode='menu'
            continue
        surface.blit(background,(0,0))
        shade=pygame.Surface(SIZE,pygame.SRCALPHA);shade.fill((2,15,27,190));surface.blit(shade,(0,0))
        surface.blit(cover,(125,120))
        put(surface,'KOXINGA',(840,238),66,GOLD)
        put(surface,'國 姓 爺',(847,323),38)
        put(surface,'揚帆福爾摩沙，爭奪海上榮耀。',(846,400),24)
        put(surface,'1 位玩家  ·  5 支電腦艦隊  ·  隨機航路',(846,445),18,MUTED)
        panel(surface,start,255)
        if start.collidepoint(mouse_pos()): pygame.draw.rect(surface,GOLD,start,3,border_radius=12)
        put(surface,'啟 航  /  ENTER',(940,558),25,GOLD)
        panel(surface,learn,255)
        if learn.collidepoint(mouse_pos()): pygame.draw.rect(surface,GOLD,learn,3,border_radius=12)
        put(surface,'遊 戲 教 學',(976,632),23,GOLD)
        put(surface,'F1 開始選單   ·   Esc 離開',(885,710),18,MUTED)
        present(surface)
        for event in pygame.event.get():
            if event.type==pygame.QUIT: quit_game()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE: quit_game()
                if event.key in (pygame.K_RETURN,pygame.K_SPACE): return
                if event.key==pygame.K_F1:
                    mode='menu'
                    break
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and start.collidepoint(mouse_pos()): return
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and learn.collidepoint(mouse_pos()):
                mode='tutorial'
                break
        clock.tick(60)
