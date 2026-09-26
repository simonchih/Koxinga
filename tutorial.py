"""Self-contained, deterministic interactive lessons; never mutate a live game."""
import pygame
from functools import lru_cache
import presentation as ui


@lru_cache(maxsize=6)
def action_die(value):
    """Use the same six-sided day/night dice artwork as the live board."""
    side = {1:2, 2:1, 3:1, 4:1, 5:1, 6:2}[value]
    source=pygame.image.load(ui.asset(f'Image/die-{value}+{side}.gif')).convert()
    return pygame.transform.smoothscale(source,(130,151))

# Each page has an actual task. Its local scenario is reset when revisited.
LESSONS = [
    ('認識你的艦隊', '點選藍色的艦隊 1。', [
        '你操作艦隊 1，其餘五隊由電腦操作。船邊框的顏色和編號可辨識玩家，發光圈代表目前行動的艦隊。',
        '正式棋盤外圍是航路；糧袋和金幣旁的數字代表停靠費用，寶箱代表可探索的寶藏。中央左側是骰子與手牌，右側是各隊剩餘牌數。',
        '每隊有五個船艙，開局分別帶有 3 份糧食和 3 枚金幣。教學使用固定範例，不會消耗正式遊戲的資源。']),
    ('領航者擲骰', '按「擲骰」，觀察日骰和夜骰。', [
        '每輪的領航者擲兩顆六面骰，所有艦隊共用這兩個點數。領航者每輪輪替，不一定由你先擲骰。',
        '左邊是日骰，右邊是夜骰，點數介於 1～6。骰點決定卡牌行動的移動距離或補給數量；海戰使用的是另一顆戰鬥骰。',
        '教學固定擲出日骰 2、夜骰 5，方便比較接下來的操作；正式對局是隨機結果。']),
    ('交換日夜順序', '把日骰換成 5。', [
        '領航者在確認出牌前，可以按「交換骰子」交換兩顆骰子的日夜順序。其他玩家只能依照決定好的點數選牌。',
        '例如打算白天航行、晚上補砲，日骰 5／夜骰 2 代表前進 5 格，再獲得 2 份火砲。交換後影響的是所有艦隊。',
        '可多次交換，直到你確定日夜配置，再選牌並確認。']),
    ('選牌，再確認', '選「航行／火砲」牌，然後確認出牌。', [
        '你通常有三張手牌可選，每張分成左右兩半：左半在日間執行，右半在夜間執行。請同時考慮兩種行動。',
        '點牌只是選取；還要按「確認出牌」才算提交。在確認前可改選。其他艦隊也會選好自己的牌。',
        '本例請選船／火砲：白天前進、晚上補砲。每輪使用一張牌，之後補一張；牌庫用完時，程式會回收已使用的牌。']),
    ('日間與夜間行動', '先執行日間航行，再執行夜間補給。', [
        '大家選好牌後，從領航者開始依序執行日間行動；所有艦隊完成後，才以同樣順序執行夜間行動。',
        '日骰 5 配上船圖案＝前進 5 格；夜骰 2 配上火砲＝補給 2 份火砲。糧袋、金幣圖案也是依該時段骰點獲得資源。',
        '標示－1、－2 的船要先扣除骰點。結果為 0 時不移動；若骰點 1 配－2，實際會後退 1 格。']),
    ('五個船艙怎麼使用', '按「補給 4 份糧食」，查看新船艙。', [
        '每個船艙放一批單一種類的資源：糧食、金幣或火砲。糧食與金幣用於支付停靠費，火砲用於加強海戰。',
        '每次補給會優先放進第一個空船艙，不會直接合併到原本同類資源的船艙。',
        '本例原有糧食 3、金幣 3。補給 4 份糧食後，第三艙會新增一批糧食 4，總糧食成為 7。']),
    ('滿載時的自動替換', '補給金幣，觀察哪一艙被替換。', [
        '如果五艙全滿，程式會按照數量由少到多，找出與本次補給不同種類的船艙，丟棄那一艙並放入新資源。',
        '本例五艙依序是糧食 1、金幣 3、火砲 2、糧食 4、火砲 5。補給金幣 6 時，最少的糧食 1 會被整艙替換。',
        '如果五個船艙全都是要補給的同一種類，這次補給無法加入。正式對局會自動處理，包括人類玩家。']),
    ('停靠費與資源不足', '支付 3 份糧食，再試一次不足的支付。', [
        '移動結束後，停在糧袋格要付糧食，停在金幣格要付金幣；付的是格上數字，不是移動骰點。經過的格子不收費。',
        '程式優先使用數量較少的同類船艙。本例糧食 5，支付 3 後剩 2。',
        '下一站若要糧食 4，你的 2 份會被扣光，接著後退一格並處理新的落點；可能繼續後退，直到停靠成功。']),
    ('航路分岔', '點選其中一條航路箭頭。', [
        '船走到分岔點時會暫停，棋盤顯示兩個箭頭。點選外圈或內圈後，船會繼續走完剩餘步數。',
        '內圈路程較短，外圈可能經過更多寶藏；要同時考慮最後的停靠費、目前資源和其他船的位置。',
        '這裡是簡化路線練習，兩條路都可以選。正式棋盤的費用和寶藏是隨機配置，請以實際格子為準。']),
    ('探索寶藏', '點寶箱，翻開這次的發現。', [
        '停到尚未被拿走的寶箱格可抽取寶藏，探索後該格的寶箱就會消失。',
        '寶藏共十種：7 份糧食、7 枚金幣，以及 2～9 分的寶藏。糧食與金幣立即進入補給流程；分數寶藏保留到結算。',
        '本次示範抽到 7 分寶藏。它和「獲得 7 枚金幣」不同：寶藏分數獨立加分，也可能在海戰中被奪走。']),
    ('海戰：火砲加戰骰', '投入兩份火砲，再按開砲。', [
        '船隻完成移動、與其他船在同一格時會觸發海戰；起點臺灣海峽不會開戰。多人同格時會依序處理對手。',
        '戰鬥骰有 0～10 與火焰，共十二種結果。一般戰力＝戰骰數字＋投入的火砲數量。火砲一旦投入就會消耗。',
        '正式遊戲每按一次「投入火砲」消耗 1 份，也可點自己的火砲船艙逐份投入，再按「開砲」。本例敵方戰力 7，投入 2 份、擲出 6，即以 8 獲勝。']),
    ('火焰與平手', '點戰骰，查看火焰結果。', [
        '擲出火焰代表立即獲勝，不能用更多火砲超過火焰。若攻擊者先擲出火焰，後續防守者不用再擲骰。',
        '一般數字戰力相同時為平手，不交換戰利品。如果對方已沒有資源與分數寶藏，也沒有物品可以掠奪。',
        '教學固定示範火焰；正式遊戲的結果是隨機的。不要把普通日夜骰的 6 點，當成海戰必勝的結果。']),
    ('選擇戰利品', '從對手的金幣船艙或寶藏中選一個。', [
        '戰鬥獲勝可拿取敗方的一個船艙資源，或一張分數寶藏。不是一次拿走對手全部物品。',
        '點對方船艙可取該艙資源；點寶藏會隨機取走對方一張分數寶藏，也可用「自動掠奪」。取得的船艙資源仍受五艙容量限制。',
        '本例可選一艙金幣 4，或一張 7 分寶藏。金幣可以付費並在最後加分，寶藏則直接提供結算分數。']),
    ('怎樣計算勝負', '選出這支艦隊的最終得分。', [
        '有人完成航程後，程式在本輪行動結束時計分。總分＝剩餘金幣＋位置分數＋寶藏分數。糧食和火砲不計分。',
        '完成航程的位置分數是 15；接近終點的計分區依位置給 1～10 分；其他位置是－5。最快到終點不保證總分最高。',
        '本例剩餘金幣 8、完成航程 15 分、寶藏 7 分。請點選總分；最高分者獲勝，同分可能有多位贏家。']),
    ('準備正式啟航', '你已完成所有練習。', [
        '每輪先看日夜骰，再檢查手牌兩半、船艙和預計落點。保留糧食與金幣，才能避免付不出停靠費而後退。',
        '船艙快滿時注意自動丟棄規則；追求寶藏與航程時，也別忘了評估海戰風險。',
        '按「開始遊戲」進入全新的正式對局，或返回開始選單。遊戲中按 F1 可暫停並查看簡要說明。'])]


def wrapped(surface, message, x, y, width, size=23, color=ui.CREAM):
    line=''
    for char in message:
        if ui.font(size).size(line+char)[0]>width:
            ui.put(surface,line,(x,y),size,color);y+=34;line=''
        line+=char
    if line: ui.put(surface,line,(x,y),size,color);y+=34
    return y


class Tutorial:
    def __init__(self):
        self.step=0
        self.reset()

    def reset(self):
        self.done=self.step==len(LESSONS)-1
        self.state={}
        self.feedback='請操作右側練習區，完成後才能前往下一步。'
        self.targets={}

    def perform(self, action):
        s=self.state
        if self.done: return
        feedback=None
        if self.step==0:
            if action=='fleet1': feedback='找到了！藍色艦隊 1 就是你的船。'
            elif action.startswith('fleet'): self.feedback='這是電腦艦隊，請找藍色編號 1。'
        elif self.step==1 and action=='roll':
            s['rolled']=True;feedback='日骰 2、夜骰 5。下一步試著交換它們。'
        elif self.step==2 and action=='swap':
            s['swapped']=True;feedback='現在日骰 5、夜骰 2，白天可以航行更遠。'
        elif self.step==3:
            if action.startswith('card'):
                s['selected']=action
                self.feedback='已選取，請按確認出牌。' if action=='card0' else '這張也是合法手牌；本次請練習船／火砲牌。'
            elif action=='confirm' and s.get('selected')=='card0': feedback='出牌完成！接下來依序執行兩半行動。'
            elif action=='confirm': self.feedback='請先點選「航行／火砲」牌。'
        elif self.step==4:
            if action=='day': s['day']=True;self.feedback='白天前進 5 格；還需要執行夜間行動。'
            elif action=='night' and s.get('day'): s['night']=True;feedback='夜間獲得 2 份火砲，這張牌的兩半都完成了。'
        elif self.step==5 and action=='supply': s['supplied']=True;feedback='新增第三艙糧食 4；原本糧食 3 的船艙保持不變。'
        elif self.step==6 and action=='supply': s['supplied']=True;feedback='糧食 1 已被替換成金幣 6，其餘四艙保留。'
        elif self.step==7 and action=='pay':
            s['paid']=s.get('paid',0)+1
            if s['paid']==1: self.feedback='糧食 5－3＝2。再試一次需付 4 的停靠費。'
            else: feedback='僅有的糧食 2 被扣光，船後退一格，重新處理落點。'
        elif self.step==8 and action in ('outer','inner'):
            s['route']=action;feedback='已選外圈，沿上方航路前進。' if action=='outer' else '已選內圈，沿下方捷徑前進。'
        elif self.step==9 and action=='chest': s['opened']=True;feedback='獲得 7 分寶藏！它不會直接增加金幣。'
        elif self.step==10:
            if action=='cannon':
                s['cannon']=min(2,s.get('cannon',0)+1)
                self.feedback=f'已投入 {s["cannon"]} 份火砲。投入兩份後按開砲。'
            elif action=='fight':
                if s.get('cannon',0)<2: self.feedback='本次練習先投入兩份火砲，再開砲。'
                else: s['rolled']=True;feedback='你的戰力 6＋2＝8，高於敵方 7，獲勝！'
        elif self.step==11 and action=='fire': s['fire']=True;feedback='火焰：立即獲勝，不再比較一般數字戰力。'
        elif self.step==12 and action in ('gold','treasure'):
            s['loot']=action;feedback='獲得一艙金幣 4。' if action=='gold' else '獲得一張 7 分寶藏。'
        elif self.step==13 and action.startswith('score'):
            if action=='score30': feedback='答對了！8＋15＋7＝30 分。'
            else: self.feedback='再算一次：剩餘金幣 8＋完成航程 15＋寶藏 7。'
        if feedback:
            self.done=True;self.feedback=feedback

    def click(self, pos):
        for name,rect in self.targets.items():
            if rect.collidepoint(pos):
                if name=='menu': return 'menu'
                if name=='start': return 'start'
                if name=='back': self.step=max(0,self.step-1);self.reset()
                elif name=='repeat': self.reset()
                elif name=='next' and self.done: self.step+=1;self.reset()
                else: self.perform(name)
                break

    def control(self,surface,name,label,rect,enabled=True):
        rect=pygame.Rect(rect)
        ui.panel(surface,rect,255,ui.GOLD if enabled else (66,88,98))
        if enabled:
            self.targets[name]=rect
            if rect.collidepoint(ui.mouse_pos()): pygame.draw.rect(surface,ui.GOLD,rect,3,border_radius=12)
        rendered=ui.text(label,ui.CREAM if enabled else (107,126,137),21)
        surface.blit(rendered,rendered.get_rect(center=rect.center))

    def picture(self,surface,name,rect):
        surface.blit(ui.sprite(name,(rect[2],rect[3])),rect[:2])

    def dice(self,surface,values):
        for i,value in enumerate(values):
            x=870+i*285
            rolled=isinstance(value,int)
            die=action_die(value if rolled else 1).copy()
            if not rolled: die.set_alpha(140)
            surface.blit(die,(x,295))
            label=ui.text('日間' if i==0 else '夜間',ui.GOLD,23)
            surface.blit(label,label.get_rect(midbottom=(x+65,282)))
            if not rolled: ui.put(surface,'尚未擲骰',(x+20,460),21,ui.MUTED)

    def holds(self,surface,items):
        for i,(name,value) in enumerate(items):
            x=780+i*137
            ui.panel(surface,(x,320,120,155),255)
            ui.put(surface,f'第 {i+1} 艙',(x+20,280),21,ui.MUTED)
            if name:
                self.picture(surface,name,(x+15,333,90,90))
                ui.put(surface,str(value),(x+47,431),25,ui.GOLD)
            else: ui.put(surface,'空艙',(x+35,374),23,ui.MUTED)

    def draw(self,surface,background):
        surface.blit(background,(0,0))
        shade=pygame.Surface(ui.SIZE,pygame.SRCALPHA);shade.fill((2,15,27,215));surface.blit(shade,(0,0))
        self.targets={}
        title,task,paragraphs=LESSONS[self.step]
        ui.put(surface,'國姓爺 · 互動航海學堂',(88,40),25,ui.GOLD)
        ui.put(surface,f'{self.step+1:02d} / {len(LESSONS):02d}    {title}',(88,83),36)
        pygame.draw.rect(surface,(45,66,76),(90,145,1418,5),border_radius=2)
        pygame.draw.rect(surface,ui.GOLD,(90,145,int(1418*(self.step+1)/len(LESSONS)),5),border_radius=2)
        ui.panel(surface,(88,178,625,523),245)
        y=206
        for paragraph in paragraphs: y=wrapped(surface,paragraph,114,y,573)+18
        ui.panel(surface,(735,178,778,523),245)
        ui.put(surface,'操作練習',(767,200),23,ui.GOLD)
        s=self.state;step=self.step
        if step==0:
            for i in range(6):
                x=815+(i%3)*217;y=285+(i//3)*150
                self.picture(surface,'move',(x+28,y,95,95))
                self.control(surface,f'fleet{i+1}',f'艦隊 {i+1}',(x,y+97,153,46))
                self.targets[f'fleet{i+1}']=pygame.Rect(x,y,153,143)
                pygame.draw.rect(surface,ui.COLORS[i],(x+27,y-2,99,99),3,border_radius=8)
        elif step in (1,2):
            values=(5,2) if s.get('swapped') else (2,5)
            self.dice(surface,values if step==2 or s.get('rolled') else ('?','?'))
            self.control(surface,'roll' if step==1 else 'swap','擲骰' if step==1 else '交換骰子',(994,515,250,58),not self.done)
        elif step==3:
            for i,(a,b,label) in enumerate([('move','cannon','航行／火砲'),('food','gold','糧食／金幣'),('move','move','航行／航行')]):
                x=780+i*240
                self.picture(surface,a,(x,300,93,93));self.picture(surface,b,(x+97,300,93,93))
                ui.put(surface,'日間         夜間',(x+8,264),20,ui.MUTED)
                self.control(surface,f'card{i}',label,(x,408,195,52))
                self.targets[f'card{i}']=pygame.Rect(x,296,195,164)
                if s.get('selected')==f'card{i}': pygame.draw.rect(surface,ui.GOLD,(x-4,296,198,168),3,border_radius=8)
            self.control(surface,'confirm','確認出牌',(994,515,250,58),not self.done)
        elif step in (4,8):
            if step==4:
                for i in range(6):
                    x=804+i*113;pygame.draw.circle(surface,ui.GOLD,(x,342),27,2)
                    ui.put(surface,str(i),(x-6,381),20)
                shipx=804+(565 if s.get('day') else 0)
                self.picture(surface,'move',(shipx-26,316,52,52))
                ui.put(surface,'火砲：'+('2' if s.get('night') else '0'),(1038,439),26,ui.GOLD)
                self.control(surface,'day','執行日間：前進 5',(798,519,310,57),not s.get('day'))
                self.control(surface,'night','執行夜間：補砲 2',(1128,519,310,57),bool(s.get('day')) and not self.done)
            else:
                for yy in (330,465):
                    pygame.draw.lines(surface,ui.GOLD,False,[(840,398),(1050,yy),(1370,yy)],3)
                    for xx in (1050,1210,1370):pygame.draw.circle(surface,ui.GOLD,(xx,yy),24,2)
                route=s.get('route');pos=(1345,305 if route=='outer' else 440) if route else (815,373)
                self.picture(surface,'move',(*pos,50,50))
                self.control(surface,'outer','↑ 外圈航路',(900,530,235,55),not self.done)
                self.control(surface,'inner','↓ 內圈捷徑',(1170,530,235,55),not self.done)
        elif step in (5,6):
            if step==5: items=[('food',3),('gold',3),('food',4) if s.get('supplied') else (None,0),(None,0),(None,0)]
            else: items=[('gold',6) if s.get('supplied') else ('food',1),('gold',3),('cannon',2),('food',4),('cannon',5)]
            self.holds(surface,items)
            self.control(surface,'supply','補給 4 份糧食' if step==5 else '補給 6 枚金幣',(957,520,325,57),not self.done)
        elif step==7:
            paid=s.get('paid',0)
            self.picture(surface,'food',(833,288,120,120));ui.put(surface,f'糧食剩餘：{[5,2,0][min(paid,2)]}',(800,432),27)
            self.picture(surface,'move',(1270-(110 if paid==2 else 0),316,70,70))
            ui.put(surface,'← 資源不足時後退',(1102,432),25,ui.GOLD)
            self.control(surface,'pay','支付 3 份糧食' if not paid else '嘗試支付 4 份糧食',(957,520,325,57),not self.done)
        elif step in (9,11):
            name='treasure' if step==9 else ('fire' if s.get('fire') else 'die')
            self.picture(surface,name,(1020,271,210,210))
            if s.get('opened'): ui.put(surface,'獲得 7 分寶藏',(1018,474),27,ui.GOLD)
            self.control(surface,'chest' if step==9 else 'fire','探索寶箱' if step==9 else '擲戰鬥骰',(997,529,250,57),not self.done)
            if not self.done:self.targets['chest' if step==9 else 'fire']=pygame.Rect(997,271,250,315)
        elif step==10:
            self.picture(surface,'cannon',(802,274,147,147));self.picture(surface,'die',(1050,274,147,147))
            ui.put(surface,str(6 if s.get('rolled') else '?'),(1108,321),40,ui.GOLD)
            ui.put(surface,f'已投入：{s.get("cannon",0)}',(805,444),25)
            ui.put(surface,'敵方戰力：7',(1205,330),27)
            if self.done:ui.put(surface,'你的戰力：8',(1205,390),27,ui.GOLD)
            self.control(surface,'cannon','投入 1 份火砲',(822,525,285,55),not self.done and s.get('cannon',0)<2)
            self.control(surface,'fight','開砲',(1132,525,285,55),not self.done)
        elif step==12:
            self.picture(surface,'gold',(853,285,155,155));self.picture(surface,'treasure',(1200,285,155,155))
            self.control(surface,'gold','拿取金幣 4',(810,509,250,57),not self.done)
            self.control(surface,'treasure','拿取 7 分寶藏',(1155,509,250,57),not self.done)
            if not self.done:
                self.targets['gold']=pygame.Rect(810,285,250,281)
                self.targets['treasure']=pygame.Rect(1155,285,250,281)
        elif step==13:
            for i,(name,label) in enumerate([('gold','金幣 8'),('move','位置 15'),('treasure','寶藏 7')]):
                x=820+i*237;self.picture(surface,name,(x,280,130,130));ui.put(surface,label,(x+14,429),26,ui.GOLD)
            for i,n in enumerate((15,23,30)):self.control(surface,f'score{n}',f'{n} 分',(812+i*237,521,185,57),not self.done)
        else:
            self.picture(surface,'win',(1010,267,220,220))
            ui.put(surface,'所有練習已完成',(997,510),28,ui.GOLD)
        wrapped(surface,self.feedback if step!=14 else '可以開始正式對局，或返回選單再次練習。',766,618,715,21,ui.GOLD if self.done else ui.MUTED)
        ui.put(surface,task,(95,717),22,ui.GOLD)
        self.control(surface,'menu','返回開始選單',(90,770,225,53))
        self.control(surface,'back','上一步',(755,770,160,53),self.step>0)
        self.control(surface,'repeat','重練本節',(938,770,200,53),step<14)
        self.control(surface,'start' if step==14 else 'next','開始遊戲' if step==14 else '下一步 →',(1161,770,349,53),self.done)


def run(surface,background):
    lesson=Tutorial();clock=pygame.time.Clock()
    while True:
        lesson.draw(surface,background);ui.present(surface)
        for event in pygame.event.get():
            if event.type==pygame.QUIT: ui.quit_game()
            if event.type==pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE,pygame.K_F1): return 'menu'
                if event.key==pygame.K_LEFT and lesson.step>0: lesson.step-=1;lesson.reset()
                elif event.key in (pygame.K_RIGHT,pygame.K_RETURN) and lesson.done:
                    if lesson.step==len(LESSONS)-1:return 'start'
                    lesson.step+=1;lesson.reset()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                result=lesson.click(ui.mouse_pos())
                if result:return result
        clock.tick(60)
