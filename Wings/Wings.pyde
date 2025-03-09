from time import time
from random import randint # Подключаем модули

diff = 'easy'
PLAY = False

class Object():
   def __init__( self, x, y, shir, vis, list_rgb, list_objects, img=None): # Класс объекта
        # Мы привязываем к объекту его координаты, ширину, высоту, картинку/цвет
       self.x = x
       self.y = y
       self.shir = shir
       self.vis = vis
       self.list_rgb = list_rgb
       
       self.mode_img = False
       
       if img != None:
           self.img = img
           self.mode_img = True
       
       

       list_objects.append(self)

   def draw_object(self):
        # Рисуем квадрат с определнным цветом на этих координатах или картинку
       if not self.mode_img:
           r = self.list_rgb[0]
           g = self.list_rgb[1]
           b = self.list_rgb[2]
           fill( r,g,b )
           rect(self.x,self.y,self.shir,self.vis)
       else:
           image(self.img,self.x,self.y)
       
class Block(): # Класс блока
    def __init__( self, x, y, type='ordinary'):
         # Мы привязываем к объекту его координаты и тип (категорию)
        self.x = x
        self.y = y
        self.type = type

    def draw_object(self):
         # Рисуем на месте координат либо определенн. картинку, либо заливаем определенн. цветоми 
         # (в зависимости от типа блока)
        if self.type == 'ordinary':  # Обычный блок
            r, g, b = 99, 82, 60
            fill( r,g,b )
            rect(self.x,self.y,block, block)
        elif self.type == 'digged': # Выкопанный блок
            r, g, b = 230, 197, 177
            fill( r,g,b )
            rect(self.x,self.y,block, block)
        elif self.type == 'home': # Блок дома
            r, g, b = 230, 193, 133
            fill( r,g,b )
            rect(self.x,self.y,block, block)
        elif self.type == 'stone': # Блок камня
            r, g, b = 71, 70, 70
            fill( r,g,b )
            rect(self.x,self.y,block, block)
        elif self.type == 'red_stone':  # Блок красного камня
            image(red_img, self.x, self.y)
        elif self.type == 'green_stone': # Блок зеленого камня
            image(green_img, self.x, self.y)

def collide(list_objects, holes, torgovla, gx, gy, gshir, gvis, speed_x, speed_y, gravity, see_detector=True): 
     # Обработка столкновений крота с объектами (которые даны в списках list_objects, holes, и torgovla)
     # и какие-либо действия (например, отключение гравитации)
    global jump, gamemode, moveBG_y, eda, red_stones, green_stones
    GravityON = True
    SpeedXON = True
    SpeedYON = True
    
    for object in holes: # Обработка списка с норками
        x = object.x
        y = object.y
        shir = object.shir
        vis = object.vis

        # detector = (x, y, shir, vis)
    
        if speed_x > 0: #Направо хочу
            d = [ gx+gshir, gy+gvis//4, speed_x, gvis//2 ]
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                gamemode = 0
                gx = x+block
                gy = y+block*2 +3

        elif speed_x < 0: # Налево хочу
            d = [ gx+speed_x, gy+gvis//4, abs(speed_x), gvis//2 ]
            
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                gamemode = 0
                gx = x+block
                gy = y+block*2 +3

        d = [ gx+gshir//4, gy+gvis, gshir//2, abs(speed_y) ]
        if speed_y > 0: # Вниз хочу
            
            if see_detector:
                draw_obj(d[0], d[1], d[2], d[3],     255, 0, 0)
    
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                SpeedYON = False
                jump = False
                
        # Обработка гравитации
        if (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis) : 
            GravityON = False

    for object in torgovla: # Обработка списка с торговой лавкой

        x = object.x
        y = object.y
        shir = object.shir
        vis = object.vis

        # detector = (x, y, shir, vis)
    
        if speed_x > 0: #Направо хочу
            d = [ gx+gshir, gy+gvis//4, speed_x, gvis//2 ]
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                eda += red_stones * 2
                eda += green_stones * 3
                
                red_stones = 0
                green_stones = 0

        
    
    for object in list_objects: # Обработка списка с другими предметами (землей)
        x = object.x
        y = object.y
        shir = object.shir
        vis = object.vis

        # detector = (x, y, shir, vis)
    
        if speed_x > 0: #Направо хочу
            d = [ gx+gshir, gy+gvis//4, speed_x, gvis//2 ]
            if see_detector:
                draw_obj(d[0], d[1], d[2], d[3],     255, 0, 0)
            
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                SpeedXON = False

        elif speed_x < 0: # Налево хочу
            d = [ gx+speed_x, gy+gvis//4, abs(speed_x), gvis//2 ]
            if see_detector:
                draw_obj(d[0], d[1], d[2], d[3],     255, 0, 0)
            
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                SpeedXON = False
            
                

        d = [ gx+gshir//4, gy+gvis, gshir//2, abs(speed_y) ]
        if speed_y > 0: # Вниз хочу
            
            if see_detector:
                draw_obj(d[0], d[1], d[2], d[3],     255, 0, 0)
    
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                SpeedYON = False
                jump = False
                
        # Обработка гравитации
        if (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis) : 
            GravityON = False
    
                
        elif speed_y < 0: # Вверх хочу
            d = [ gx+gshir//4, gy+speed_y, gshir//2, speed_y ]
            
            if see_detector:
                draw_obj(d[0], d[1], d[2], d[3],     255, 0, 0)
            
            if  (d[0] + d[2] > x) and (d[0] < x + shir)  and  (d[1] + d[3] > y) and (d[1] < y + vis):
                SpeedYON = False
                
     # Ходим куда-либо, если можно
    if GravityON:
        gy += gravity
    if SpeedYON:
        gy += speed_y
    if SpeedXON and gx + speed_x >= 10 and gx + speed_x <= width-gshir:
        gx += speed_x
            
    return gx, gy

def setup():
     # Setup начального меню
    global r2, g2, b2
    global r3, g3, b3
    global r4, g4, b4
    
    global diff
    
    global but1, write_diff, but2, but3, but4, but5, screen, zast
    
    global PLAY, diff
    
     # Картинки:
    
    but1=loadImage("but1.png")
    write_diff=loadImage("write_diff.png")
    but2=loadImage("but2.png")
    but3=loadImage("but3.png")
    but4=loadImage("but4.png")
    but5=loadImage("but5.png")
    screen=loadImage("screen.jpg")
    zast=loadImage("zast.png")
    
    diff = 'easy'
    r2, g2, b2 = 166, 224, 119
    r3, g3, b3 = 227, 232, 223
    r4, g4, b4 = 227, 232, 223
    
    fullScreen()
    frameRate(70)
    
    
def start_game():
        # Setup игры
    
       global gx, gy, block, list_blocks, v, gravity, list_objects, gshir, gvis, decorations, holes
       global moveBG_y, y_pos_blocks, block_timing, hungry_timing, game_timing, torgovla, block_speed
       global red_img, green_img, block_img, digged_img, stone_img, hole_img, shovel_img, red_shis_img, green_shis_img, swed_img
       
       global GAME_OVER, DATA_red_stone, DATA_green_stone, DATA_home, DATA_digged, up, right, down, left, a, jump, gamemode, moveBG_y, MAX_SHOVELS, shovels, red_stones, green_stones, eda, length_hungry, block_speed, place_home, dlina_hungry, front
       global cake1, cake2,cake3,cake4,cake5,cake6, cake7, win, over
       
       noCursor() 
       
       GAME_OVER = 'play'
 
        # Сохраненные блоки (домик кротика)
       DATA_stone = [[960, 470], [810, 620], [840, 620], [930, 620], [780, 650], [870, 650], [900, 650], [750, 680], [780, 680], [930, 680], [990, 680], [750, 710], [780, 740], [810, 740], [840, 740], [870, 740], [900, 740], [930, 740]]
       DATA_red_stone = []
       DATA_green_stone = []
       DATA_home = [[810, 650], [840, 650], [810, 680], [840, 680], [870, 680], [900, 680], [780, 710], [810, 710], [840, 710], [870, 710], [900, 710], [930, 710]]
       DATA_digged = [[960, 410], [930, 440], [960, 440], [930, 470], [930, 500], [960, 500], [960, 530], [960, 560], [960, 590], [960, 620], [960, 650], [960, 680], [960, 710]]
    
        # Некоторые начальные переменные
       up = False
       right = False
       left = False
       down = False
       a = 0
       jump = False
       gamemode = 1
       moveBG_y = True
       
        # Вероятность выпадения __ в зависимости от сложности:
       g1 = 5 # камней
       g2 = 3 # красных камней
       g3 = 2 # зеленых камней
       
       
        # Изменяем кол-во лопаток и вероятность блоков в зависимости от сложности:
       if diff == 'easy':
          MAX_SHOVELS = 210
       elif diff == 'medium':
           MAX_SHOVELS = 180
           g2 = 3
           g3 = 1
       elif diff == 'hard':
           MAX_SHOVELS = 140
           g2 = 2
           g3 = 1
           
       s1 = 100 - g1
       s2 = 100 - g1 - g2
       s3 = 100 - g1 - g2 - g3   
           
           
        # Некоторые начальные переменные
       shovels = MAX_SHOVELS
       red_stones = 0
       green_stones = 0
       eda = 5
       length_hungry = 0
       block_speed = 0.025
       place_home = False
       dlina_hungry = 336
       block = 30
    
       front = 1 # В какую сторону смотрит крот, когда стоит
       
        # Картинки торта
       cake1 = loadImage('cake1.png')
       cake2 = loadImage('cake2.png')
       cake3 = loadImage('cake3.png')
       cake4 = loadImage('cake4.png')
       cake5 = loadImage('cake5.png')
       cake6 = loadImage('cake6.png')
       cake7 = loadImage('cake7.png')
       
       
       
    
        # Картинки блоков разных типов
       red_img=loadImage("red.png")
       green_img=loadImage("green.png")
       block_img=loadImage("block.png")
       digged_img=loadImage("digged.png")
       stone_img=loadImage("stone.jpg")
    
        # Значки элементов справа вверху
       hole_img=loadImage("hole.png")
       shovel_img=loadImage("shovel.png")
       red_shis_img=loadImage("red_shis.png")
       green_shis_img=loadImage("green_shis.png")
       swed_img=loadImage("swed.png")
    
        # Картинки хорошей и плохой концовки
       win=loadImage("win.png")
       over=loadImage("over.png")
    
        # Начальная позиция кротика, его ширина, высота, скорость, гравитация...
       gx = width / 2
       gy = int(height*0.38) + block*10
       y_pos_blocks = 9
    
       gshir = 76 // 2
       gvis = 118 // 2
    
       v = 10
       gravity = 1
    
       kray = 3000
    
        # Создаем пустые списки для разных предметов
    
       list_objects = []
       decorations = []
       holes = []
       torgovla = []
       list_blocks = []

       for y in range(int(height*0.38), height+kray, block):  # Заполняем list_blocks
           yyy = y//80 # Что сейчас за глубина?
           for x in range(0, width, block):

                # С глубиной земли будет все меньше и меньше, поэтому меняем вероятность
               if yyy <= 20:
                   ttt = randint(15, 100)
               elif yyy <= 35:
                   ttt = randint(20, 100)
               elif yyy <= 45:
                   ttt = randint(25, 100)
               else:
                   ttt = randint(30, 100)
                
                # Задаем какой-либо тип этому блоку
               if ttt >= s1:
                   ttt = 'stone'
               elif ttt >= s2 and ttt < s1:
                   ttt = 'red_stone'
               elif ttt >= s3 and ttt < s2:
                   ttt = 'green_stone'
               else:
                   ttt = 'ordinary'
               for i in DATA_stone:
                   if i[0] == x and i[1] == y:
                       ttt = 'stone'    
               for i in DATA_red_stone:
                   if i[0] == x and i[1] == y:
                       ttt = 'red_stone'
               for i in DATA_green_stone:
                   if i[0] == x and i[1] == y:
                       ttt = 'green_stone'
               for i in DATA_home:
                   if i[0] == x and i[1] == y:
                       ttt = 'home'
               for i in DATA_digged:
                   if i[0] == x and i[1] == y:
                       ttt = 'digged'
                # Создаем объект и заносим его в список всех блоков
               b = Block(x, y, ttt)
               list_blocks.append(b)
            
    
        # Создаем некоторые предметы:
       ground = Object(0, 385, width + kray, 75, (139, 69, 19), list_objects, loadImage('ground.png')) # Земля
       torgovec = Object(3370//2, 470//2, 470, 300, (214, 194, 79), torgovla, loadImage('dom2.png')) # Торговец
       window = Object(3370//2, 270//2, 220//2, 170//2, (211, 218, 219), decorations, loadImage('tabl.png')) # Табличка
       trava = Object(0, 0, 3840, 770, (211, 218, 219), decorations, loadImage('trava.png')) # Трава
       
       obl1 = Object(2000//2, 130//2, 670, 160, (211, 218, 219), decorations, loadImage('1obl.png')) # Облако1
       obl2 = Object(2400//2, 80//2, 900, 380, (211, 218, 219), decorations, loadImage('2obl.png')) # Облако2
       obl3 = Object(180//2, 70//2, 900, 380, (211, 218, 219), decorations, loadImage('3obl.png')) # Облако3


        # Таймеры:
       block_timing = time() # чтобы быстро не копал блоки (а то блоки не успевают меняться)
       hungry_timing = time() # шкалы голода
       game_timing = time() # длительности игры

def keyPressed():
     # Обработка нажатия клавиш
    global PLAY
    
    global gx, gy, v, right, up, left, down, jump, block, gamemode, moveBG_y, y_pos_blocks
    global block_timing, hungry_timing, list_blocks, shovels
    global red_stones, green_stones, eda, front, block_speed
    
    if PLAY: # Если мы играем в игру
        if gamemode == 1 and time() - block_timing > block_speed:
             # Если крот под землей:
            
            block_timing = time()
            
            if keyCode == UP or keyCode == 87 or keyCode == 73:
                up = True
                
                stop = False
                for i in list_blocks:
                    if i.y == gy - block and i.x == gx and (i.type == 'stone' or (i.type == 'ordinary' and shovels == 0)):
                        stop = True
                        break
                if not stop:
                
                    if moveBG_y == True: # фон двигается
                    
                    
                        for i in list_blocks:
                            i.y += block
                    
                        for i in decorations:
                            i.y += block
                        
                        for i in holes:
                            i.y += block
                        for i in torgovla:
                            i.y += block
                        
                        
                        for i in list_objects:
                            i.y += block
                            
                    else: 
                        gy -= block
                    y_pos_blocks -= 1
            
            elif (keyCode == DOWN or keyCode == 83 or keyCode == 75) and y_pos_blocks <= 86:
                down = True
                
                stop = False
                for i in list_blocks:
                    if i.y == gy + block and i.x == gx and (i.type == 'stone' or (i.type == 'ordinary' and shovels == 0)):
                        stop = True
                        break
                if not stop:
                    if moveBG_y == True: # фон двигается
        
                        for i in list_blocks:
                            i.y -= block
                    
                        for i in decorations:
                            i.y -= block
                        
                        for i in holes:
                            i.y -= block
                        
                        for i in torgovla:
                            i.y -= block
                        
                        
                        for i in list_objects:
                            i.y -= block
                            
                    else: 
                        gy += block
                    y_pos_blocks += 1
            elif (keyCode == LEFT or keyCode == 65 or keyCode == 74) and gx >= 10:
                
                left = True
                
                stop = False
                for i in list_blocks:
                    if i.x == gx - block and i.y == gy and (i.type == 'stone' or (i.type == 'ordinary' and shovels == 0)):
                        stop = True
                        break
                    
                if not stop:
                    gx -= block
                    
            elif (keyCode == RIGHT or keyCode == 68 or keyCode == 76) and gx <= width - block*2:
                
                right = True
                
                stop = False
                for i in list_blocks:
                    if i.x == gx + block and i.y == gy and (i.type == 'stone' or (i.type == 'ordinary' and shovels == 0)):
                        stop = True
                        break
                if not stop:
                
                    gx += block
    
    
        elif gamemode == 0:
             # Если крот на земле:
            
            if  keyCode == LEFT or keyCode == 65 or keyCode == 74:
                front = 1
                left = True
            if (keyCode == UP or keyCode == 87 or keyCode == 73) and gy > 0 and not(jump):
                up = True
            if keyCode == RIGHT or keyCode == 68 or keyCode == 76:
                front = 2
                right = True
            if (keyCode == DOWN or keyCode == 83 or keyCode == 75):
                down = True

def keyReleased():
     # Обработка нажатия клавиш N2 (чтобы несколько клавиш одновременно работало)
    global gx, gy, v, right, up, left, down, moveBG_y, PLAY
    
    if PLAY:
    
        if gamemode == 0 or gamemode == 1:
            
            
            if keyCode == LEFT or keyCode == 65 or keyCode == 74:
                left = False
            #if (keyCode == 38 or keyCode == 87) and gy > 0:
            #    up = False
            if keyCode == RIGHT or keyCode == 68 or keyCode == 76:
                right = False
            if keyCode == DOWN or keyCode == 83 or keyCode == 75:
                down = False

def mousePressed(): 
     # Обработка нажатия мышки (для начального меню)
    global x1, y1, shir1, dlina1
    global x2, y2, shir2, dlina2
    global x3, y3, shir3, dlina3
    global x4, y4, shir4, dlina4
    global x5, y5, shir5, dlina5
    
    global r2, g2, b2
    global r3, g3, b3
    global r4, g4, b4
    
    global diff, PLAY
    
    
    if not PLAY: # Если мы в меню
        if mouseButton == LEFT:
             # 1 кнопка (НАЧАЛО ИГРЫ)
            if mouseX >= x1 and mouseX <= x1 + shir1 and mouseY >= y1 and mouseY <= y1 + dlina1:
                PLAY = True
                start_game()

             # 2 кнопка (Легко)
            elif mouseX >= x2 and mouseX <= x2 + shir2 and mouseY >= y2 and mouseY <= y2 + dlina2:
                r2, g2, b2 = 166, 224, 119
                r3, g3, b3 = 227, 232, 223
                r4, g4, b4 = 227, 232, 223
                diff = 'easy'
        
             # 3 кнопка (Средне)
            elif mouseX >= x3 and mouseX <= x3 + shir3 and mouseY >= y3 and mouseY <= y3 + dlina3:
                r2, g2, b2 = 227, 232, 223
                r3, g3, b3 = 224, 217, 119
                r4, g4, b4 = 227, 232, 223
                diff = 'medium'
                
             # 4 кнопка (Сложно)            
            elif mouseX >= x4 and mouseX <= x4 + shir4 and mouseY >= y4 and mouseY <= y4 + dlina4:
                r2, g2, b2 = 227, 232, 223
                r3, g3, b3 = 227, 232, 223
                r4, g4, b4 = 224, 119, 119
                diff = 'hard'
                
             # 5 кнопка (Выход из игры)
            elif mouseX >= x5 and mouseX <= x5 + shir5 and mouseY >= y5 and mouseY <= y5 + dlina5:
                exit()
   
def draw():
     # Отрисовка и проверка
    global GAME_OVER, DATA_red_stone, DATA_green_stone, DATA_home, DATA_digged, up, right, down, left, a, jump, gamemode, moveBG_y, MAX_SHOVELS, shovels, red_stones, green_stones, eda, length_hungry, block_speed, place_home, dlina_hungry, front
    global x1, y1, shir1, dlina1
    global x2, y2, shir2, dlina2
    global x3, y3, shir3, dlina3
    global x4, y4, shir4, dlina4
    global x5, y5, shir5, dlina5
    
    global r2, g2, b2
    global r3, g3, b3
    global r4, g4, b4
    
    global diff
    
    global but1, write_diff, but2, but3, but4, but5, screen, zast
    
    
    
    global red_img, green_img, block_img, digged_img, stone_img, hole_img, shovel_img, red_shis_img, green_shis_img, swed_img, win, over

    global gx, gy, block, list_blocks, gamemode, moveBG_y, block_timing, hungry_timing, peremenna


    global v, gravity, list_objects, gshir, gvis, decorations, holes, torgovla
    global right, up, left, down, a, jump, shovels, place_home, dlina_hungry
    global red_stones, green_stones, eda, GAME_OVER, length_hungry, game_timing, front, block_speed
    
    global cake1, cake2,cake3,cake4,cake5,cake6, cake7
    
    
    global PLAY
    
    
    if PLAY: # Если мы играем в игру
        
         # Шкала голода, как она уменьшается и как она увелимчивается, когда приносишь еду
        mm = 180 - int(time() - game_timing)
        if time() - hungry_timing >=1:
            hungry_timing = time()
            
            if diff == 'easy':
                dlina_hungry -= 9
            elif diff == 'medium':
                dlina_hungry -= 15
            else:
                dlina_hungry -= 20
                
            if place_home:
                if eda > 0:
                    promezh = (336 - dlina_hungry) // 40
                    if eda - promezh < 0:
                    
                        dlina_hungry += eda*40
                    else:
                        eda-=promezh
                        dlina_hungry += promezh*40
                    if dlina_hungry > 336:
                        dlina_hungry = 336
        
        
        
        
        if dlina_hungry <=0 : # Если шкала голода закончилась, игра заканчивается плохой концовкой
            GAME_OVER = 'over'
        if mm <= 0: # Если время закончилось, игра заканчивается хорошей концовкой
            GAME_OVER = 'win'
        if GAME_OVER == 'play': # Если мы еще играем в игру
     
             # Делаем норку и выходим на поверхность, если пересекли определенн. черту
            if gy > list_blocks[0].y - block:
                gamemode = 1
            elif gy == list_blocks[0].y - block and gamemode == 1:
                if gx < width-block*10:
                    gy -= block*6
            
                    Object(gx - block*2, list_blocks[0].y - 64, block*4, block*2, (219, 211, 145), holes, hole_img) # Ямка
                    
                    gamemode = 0
                    shovels = MAX_SHOVELS
                else:
                    gx -= block                       
            
             # Рисуем небо
            background(213, 239, 249)
            
            
             # Фон двигается, если крот идет вверх/вниз, крот посередине и мы не дошли до края карты
            if (gy >= height/2 and down) or (gy <= height/2 and up):
                moveBG_y = True
            if y_pos_blocks > 75:
                moveBG_y = False
            if y_pos_blocks <= 9:
                moveBG_y = False
                        
             # Отрисовываем по очереди элементы из списков:
            for i in decorations: # декораций
                i.draw_object()
            
            for i in holes: # норок
                i.draw_object()
            
            for i in torgovla: # лавки торговца
                i.draw_object()
            
            for i in list_objects: # предметов, с которыми будет обрабатываться столкновение (земля)
                i.draw_object()
                
            
            if gamemode == 1: # Если мы под землей
                for b in list_blocks:
                    if gx == b.x and gy == b.y: # Если мы стоим на каком-то блоке, меняем некоторые параметры
                        place_home = False
                        if b.type == 'ordinary':
                            block_speed = 0.050
                            b.type = 'digged'
                            shovels -= 1
                        elif b.type == 'red_stone':
                            block_speed = 0.300
                            b.type = 'digged'
                            shovels -= 2
                            red_stones+=1 
                        elif b.type == 'green_stone':
                            block_speed = 0.300
                            b.type = 'digged'
                            shovels -= 3
                            green_stones+=1 
                        elif b.type == 'home':
                            block_speed = 0.025
                            place_home = True
                        elif b.type == 'digged':
                            block_speed = 0.025
                     # И отрисовывем этот блок
                    b.draw_object()

                 # Отрисовывем крота (черный квадратик)
                fill(0, 0, 0)
                rect(gx, gy, block, block)  

            elif gamemode == 0: # Если мы на земле:
                for i in list_blocks: # Отрисовываем еще все блоки
                    i.draw_object()
                
                 # Скорости и обработка прыжка
                speed_x = 0
                speed_y = 0
                
                if up == True and gy > 0:
                    #speed_y -= v
                    a = -13
                    up = False
                    jump = True
            
                if jump:
                    a += 0.5
                    speed_y += a
                    
                    
                # Клавиши:
                
                if right == True:
                    speed_x += v
        
                if left == True:
                    speed_x -= v

                if down == True:
                    speed_y += v
                    
                
                    
                
                    
                 # Вызываем функцию столкновения и забираем оттуда координаты крота
                gx, gy = collide(list_objects, holes, torgovla, gx, gy, gshir, gvis, speed_x, speed_y, gravity, False) # Проверка столкновений
                
                 # Меняем картинки в зависимости от состояния крота
                if jump == True and speed_x > 0:
                    img = loadImage("jumpr.png")
                elif jump == True and speed_x < 0:
                    img = loadImage("jumpl.png")  
                elif jump == True:
                    img = loadImage("jumpr.png")      
                elif speed_x >0:
                    img = loadImage("right.png")
                elif speed_x == 0:
                    if front == 2:
                        img = loadImage("front.png")
                    elif front == 1:
                        img = loadImage("front2.png")
                else:
                    img = loadImage("left.png")
                 # Отрисовываем изображение крота
                image(img, gx-20, gy)
            
            
             # А теперь всякие показатели:
            
            # Элементы кол-во
            
            fill(227, 224, 141)
            rect(width-470//2, 0, 470//2, 170//2)
            fill(46, 45, 33)
            textSize(55//2)
        
            text(shovels, width-130//2, 140//2)
            text(green_stones, width-215//2, 140//2)
            text(red_stones, width-320//2, 140//2)
            text(eda, width-435//2, 140//2)
            
            # Элементы изображение
            image(shovel_img, width-100//2, 20//2)
            image(green_shis_img, width-220//2, 20//2)
            image(red_shis_img, width-325//2, 20//2)
            image(swed_img, width-410//2, 20//2)
            
            # Обертка для шкалы голода
            fill(54, 41, 36)
            rect(15//2, 25//2, 100//2, 90//2)
            fill(54, 41, 36)
            rect(125//2, 25//2, 700//2, 90//2)
            
            # Сама шкала голода
            fill(212, 184, 174)
            rect(135//2, 35//2, dlina_hungry, 70//2)
            
             # Меняем картинку торта в зависимости от длины шкалы голода и рисуем его
            if dlina_hungry >= 42*7:
                image(cake1, 30//2, 36//2)
            elif dlina_hungry >= 42*6 and dlina_hungry < 42*7:
                image(cake2, 30//2, 36//2)
            elif dlina_hungry >= 42*5 and dlina_hungry < 42*6:
                image(cake3, 30//2, 36//2)
            elif dlina_hungry >= 42*4 and dlina_hungry < 42*5:
                image(cake4, 30//2, 36//2)
            elif dlina_hungry >= 42*3 and dlina_hungry < 42*4:
                image(cake5, 30//2, 36//2)
            elif dlina_hungry >= 42*2 and dlina_hungry < 42*3:
                image(cake6, 30//2, 36//2)
            elif dlina_hungry >= 42*1 and dlina_hungry < 42*2:
                image(cake7, 30//2, 36//2)

             # Прямоугольник таймера и значение таймера КРАСНЫМ КРОВАВЫМ ЦВЕТОМ
            fill(209, 190, 230)
            rect(width//2 - 125//2, 25, 250//2, 80//2)

            end = str(mm%60)
            if len(end) == 1:
                end = '0' + end

            fill(232, 42, 70)
            textSize(55//2)
            text(str(mm//60)+':'+end, width//2 - 30, 90//2 + 10)
            
            
            
        elif GAME_OVER == 'over': # Плохая концовка
            image(over, 0, 0)

        elif GAME_OVER == 'win': # Хорошая концовка
            image(win, 0, 0)

    else:
         # Отрисовка меню
        image(screen, 0, 0) # Размытый фон
        
         # Кнопки и их надписи в image()
        shir1 = 650 // 2
        dlina1 = 160 // 2
        x1 = 800
        y1 = 380 + 15
        fill(220, 227, 166)
        rect(x1, y1,shir1,dlina1, 30)

        image(but1, x1, y1)
        
        
        image(write_diff, x1, y1+dlina1 - 10)
        
        shir2 = 180 // 2
        dlina2 = 150 // 2
        x2 = 800
        y2 = height//2 - dlina2 // 2 + 20
        fill(r2, g2, b2)
        rect(x2, y2,shir2,dlina2, 30)
        
        if diff == 'easy':
            image(but2, x2, y2)
        
        shir3 = 180 // 2
        dlina3 = 150 // 2
        x3 = 915
        y3 = height//2 - dlina3 // 2 + 20
        fill(r3, g3, b3)
        rect(x3, y3,shir3,dlina3, 30)
        
        if diff == 'medium':
            image(but3, x3, y3)
        
        shir4 = 180 // 2
        dlina4 = 150 // 2
        x4 = 1030
        y4 = height//2 - dlina4 // 2 + 20
        fill(r4, g4, b4)
        rect(x4, y4,shir4,dlina4, 30)
        
        if diff == 'hard':
            image(but4, x4, y4)
        
        
        shir5 = 650 // 2
        dlina5 = 160 // 2
        x5 = width//2 - shir5// 2
        y5 = 620
        fill(128, 78, 68)
        rect(x5, y5,shir5,dlina5, 30)
        
        image(but5, x5, y5)
        
         # Название игры
        image(zast, 625, 160)
        
    # Принт (для теста)
    #fill(0)
    #textSize(35)
    #text(str(mouseX), mouseX+50,mouseY+150)
    #text(str(mouseY), mouseX+50,mouseY+180)


        
