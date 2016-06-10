import  pygame ,random splite3
from pygame.locals import *

form_width = 800
form_height = 600

white     = (255, 255, 255)
black     = (  0,   0,   0)
red       = (155,   0,   0)
light_red = (175,  20,  20)
green     = (  0, 200,   0)
yellow       = (200,200,0)
light_green = ( 0, 255,  0)
light_blue   = ( 20,  20, 175)
light_yellow = (255,255,0)
brown = (182,42,42)
antique_white = (139,131,120)
gainsboro = (220,220,220)
deep_sky_blue = (0,191,255)

tank_width = 40
tank_height = 20
turret_Width = 5
wheel_width = 5

ground_height = 35



def main():
    global  form_display, big_font , small_font , medium_font , clock
    pygame.init()
    form_display = pygame.display.set_mode((form_width, form_height))
    big_font = pygame.font.Font('freesansbold.ttf', 60)
    small_font = pygame.font.Font('freesansbold.ttf', 20)
    medium_font = pygame.font.Font('freesansbold.ttf',40)
    pygame.display.set_caption('tank game')
    form_display.fill(light_blue)
    clock = pygame.time.Clock()
    
    game_intro()
    
def quit_game():
    pygame.quit()
    quit()
    
def create_text(text, font, color):
    surface = font.render(text, True, color)
    return surface, surface.get_rect()

def tank(x,y,turret_pos):
    x = int(x)
    y = int(y)

    possible_Turrets = [(x-27 , y-2),
                        (x-26 , y-5),
                        (x-25 , y-8),
                         (x-23 , y-12),
                         (x-20 , y-14),
                       (x-18 , y-15),
                       (x-16 , y-17),
                       (x-13 , y-19),
                       (x-11 , y-21),
                       ]


                        
    
    pygame.draw.circle(form_display,brown,(x,y),int(tank_height/2))
    
    pygame.draw.rect(form_display , brown, (x - tank_height , y , tank_width , tank_height))
    pygame.draw.line(form_display,brown,(x,y),possible_Turrets[turret_pos] , turret_Width)

                     
    pygame.draw.circle(form_display,brown,(x-15 ,y+20),wheel_width)
    pygame.draw.circle(form_display,brown,(x-10 ,y+20),wheel_width)
    pygame.draw.circle(form_display,brown,(x-5,y+20),wheel_width)
    pygame.draw.circle(form_display,brown,(x, y+20),wheel_width)
    pygame.draw.circle(form_display,brown,(x+5,y+20),wheel_width)
    pygame.draw.circle(form_display,brown,(x+10,y+20),wheel_width)
    pygame.draw.circle(form_display,brown,(x+15,y+20),wheel_width)

    return possible_Turrets[turret_pos]


def enemy_tank(x,y,turret_pos):
    x = int(x)
    y = int(y)

    possible_Turrets = [(x+27 , y-2),
                        (x+26 , y-5),
                        (x+25 , y-8),
                         (x+23 , y-12),
                         (x+20 , y-14),
                       (x+18 , y-15),
                       (x+16 , y-17),
                       (x+13 , y-19),
                       (x+11 , y-21),
                       ]


                        
    
    pygame.draw.circle(form_display,deep_sky_blue,(x,y),int(tank_height/2))
    
    pygame.draw.rect(form_display,deep_sky_blue, (x-tank_height, y, tank_width , tank_height))
    pygame.draw.line(form_display,deep_sky_blue,(x,y),possible_Turrets[turret_pos] , turret_Width)

                     
    pygame.draw.circle(form_display,deep_sky_blue,(x-15 ,y+20),wheel_width)
    pygame.draw.circle(form_display,deep_sky_blue,(x-10 ,y+20),wheel_width)
    pygame.draw.circle(form_display,deep_sky_blue,(x-5,y+20),wheel_width)
    pygame.draw.circle(form_display,deep_sky_blue,(x, y+20),wheel_width)
    pygame.draw.circle(form_display,deep_sky_blue,(x+5,y+20),wheel_width)
    pygame.draw.circle(form_display,deep_sky_blue,(x+10,y+20),wheel_width)
    pygame.draw.circle(form_display,deep_sky_blue,(x+15,y+20),wheel_width)

    return possible_Turrets[turret_pos] 
  
  
def barrier(barrier_location,random_Height,barrier_width ):
    pygame.draw.rect(form_display,black, [barrier_location,form_height - random_Height,barrier_width,random_Height])


def explosion(x,y,size=50 ):

    explode = True
    
    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               quit_game()
               
        startPoint = x,y

        colorChoices = [red,light_yellow]
        
        magnitude = 1
        while magnitude < size:
            # print ("magnitude %s size %s" % (magnitude, size))
            exploding_bit_x = x + random.randrange(-1*magnitude , magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude , magnitude)

            pygame.draw.circle(form_display,colorChoices[random.randrange(0,2)],(exploding_bit_x,exploding_bit_y),2)
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False
        
def fireShell(xy, tank_x_axis , tank_y_axis , turret_pos , gun_power , fire_location , barrier_width , random_Height):
    fire = True
    
    startingShell = list(xy)
    
    
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                
                
        print(( startingShell[0],startingShell[1]))
        pygame.draw.circle(form_display,red,(startingShell[0],startingShell[1]),5)

            
        startingShell[0] -= (12 - turret_pos)*2
        
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2)-(turret_pos+turret_pos/(12-turret_pos)))
        
        if startingShell[1] > form_height-ground_height:
            
            hit_x = int((startingShell[0] * form_height-ground_height) / startingShell[1])
            hit_y = int(form_height - ground_height)      
            explosion(hit_x , hit_y)
            fire = False

        check_x_1 = startingShell[0] <=  fire_location + barrier_width
        check_x_2 = startingShell[0] >= fire_location
        
        check_y_1 = startingShell[1] <= form_height
        check_y_2 = startingShell[1] >= form_height - random_Height        

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])      
            explosion(hit_x,hit_y)
            fire = False
            
        pygame.display.update()
        clock.tick(60)


def enemy_fireShell(xy, tank_x_axis , tank_y_axis , turret_pos , gun_power , fire_location , barrier_width , random_Height,ptank_x,ptank_y):
    fire = True
    
    startingShell = list(xy)
    
    
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                
                
        print(( startingShell[0],startingShell[1]))
        pygame.draw.circle(form_display,red,(startingShell[0],startingShell[1]),5)

      
        startingShell[0] += (12 - turret_pos)*2
   
        
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2)-(turret_pos+turret_pos/(12-turret_pos)))
        
        if startingShell[1] > form_height-ground_height:
            
            hit_x = int((startingShell[0] * form_height-ground_height) / startingShell[1])
            hit_y = int(form_height - ground_height)      
            explosion(hit_x , hit_y)
            fire = False

        check_x_1 = startingShell[0] <=  fire_location + barrier_width
        check_x_2 = startingShell[0] >= fire_location
        
        check_y_1 = startingShell[1] <= form_height
        check_y_2 = startingShell[1] >= form_height - random_Height        

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])      
            explosion(hit_x,hit_y)
            fire = False
            
        pygame.display.update()
        clock.tick(60)


def power(level):
    text = small_font.render("power: " + str(level)+ "%",True,black)
    form_display.blit(text,[form_width/2,0])
    
def game_loop():
    

    barrier_width = 50
    fps = 10
    main_Tank_width = form_width * 0.9
    main_tank_height = form_height * 0.9
    tank_move = 0

    current_turrets_pos = 0
    changetur = 0

    enemy_tank_width = form_width * 0.1
    enemy_tank_height = form_height * 0.9
    
    fire_power = 50
    power_change = 0
    
    random_barrier_location = (form_width/2) + random.randint(-0.2 * form_width, 0.2 * form_height)
    random_Height = random.randrange(form_height * 0.1 , form_height * 0.6)

            
    

    while True:
       
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tank_move = -5

                elif event.key == pygame.K_RIGHT:
                    tank_move = 5

                if  event.key == pygame.K_UP:
                    changetur = 1

                elif event.key == pygame.K_DOWN:
                    changetur = -1
                    
                elif event.key == pygame.K_SPACE:
                    fireShell(gun,main_Tank_width,main_tank_height, current_turrets_pos ,fire_power,random_barrier_location,barrier_width,random_Height)
                    enemy_fireShell(enemy_gun , enemy_tank_width , enemy_tank_height , 8 , 50 , random_barrier_location , barrier_width , random_Height,main_Tank_width,main_tank_height)

                elif event.key ==pygame.K_a:
                    power_change = -1
                
                elif event.key == pygame.K_d:
                    power_change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tank_move = 0
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changetur = 0
                if event.key ==pygame.K_a or  event.key ==pygame.K_d:
                    power_change = 0
                                  
            
            main_Tank_width += tank_move
            current_turrets_pos += changetur
            if current_turrets_pos > 8:
                current_turrets_pos = 8
            elif current_turrets_pos < 0:
                current_turrets_pos = 0

            if main_Tank_width - tank_width/2 < random_barrier_location + barrier_width:
                main_Tank_width += 5


            form_display.fill(antique_white)
            
            gun = tank(main_Tank_width , main_tank_height , current_turrets_pos)
            enemy_gun = enemy_tank(enemy_tank_width , enemy_tank_height , 8)
                
            fire_power += power_change

            power(fire_power)
            barrier(random_barrier_location , random_Height , barrier_width)
            form_display.fill(green,rect=[0,form_height-ground_height , form_width , ground_height])
            pygame.display.update()
            clock.tick(fps)
                   
                    
  
    pygame.quit()
    quit()
          

    
    
def screen_text(text , color , font , height_displacement ):
    title_surface, title_object = create_text(text, font,color)
    title_object.center = (int(form_width / 2), int(form_height / height_displacement)) 
    form_display.blit(title_surface, title_object)


    
def button(text , x_axis , y_axis , width_button , height_button , inactive_color , active_color , action = None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    
    
    if x_axis + width_button > mouse[0] > x_axis and y_axis + height_button > mouse[1] > y_axis:
        pygame.draw.rect(form_display, active_color , (x_axis , y_axis , width_button , height_button))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
                
            if action == "QUIT":
                pygame.quit()
                quit()
     
                
            
            
                
                        
          
    else:
        pygame.draw.rect(form_display , inactive_color , (x_axis , y_axis , width_button , height_button))
        title_surface, title_object = create_text(text, small_font,black)
        title_object.center = ((x_axis+(width_button/2)), (y_axis+(height_button/2)))
        form_display.blit(title_surface, title_object)
            

def check_For_Key_events():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               quit_game()
               
        button("PLAY",150,500,100,50,light_green , green , "play")
        button("QUIT",550,500,100,50,light_red , red , "QUIT")
        button("SETTINGS",350,500,100,50,light_yellow , yellow, game_controls)  
        pygame.display.update()
                      
def game_intro():
    screen_text("Still under construction ",white, big_font , 6)
    screen_text("Clash of the titans", white, big_font , 3 ) 
    check_For_Key_events()


def game_controls():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               quit_game()
               
        form_display.fill(white)       
        screen_text("CONTROLS",red, medium_font , 11)
        screen_text("SPACE: TO FIRE ", black, medium_font , 7 )
        screen_text("MOVE: UP AND DOWN TO ARM ", black, medium_font , 5)
        screen_text("MOVE TANK: left and right TO MOVE ", black, medium_font , 3 )
        screen_text("PAUSE: P TO PAUSE ", black, medium_font , 2 )

        button("PLAY",150,500,100,50,light_green , green , "play")
        button("QUIT",550,500,100,50,light_red , red , "QUIT")
        
        pygame.display.update()
    
                                    
if __name__ == '__main__':
    main()

