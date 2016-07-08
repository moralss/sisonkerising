import  pygame ,random ,sys , os, pygbutton
sys.path.insert(0,os.path.abspath(".."))
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


form_display = pygame.display.set_mode((form_width, form_height))
big_font = pygame.font.Font('freesansbold.ttf', 60)
small_font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf',40)
pygame.display.set_caption('tank game')
form_display.fill(light_blue)
clock = pygame.time.Clock()

    

    

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

        colorChoices = [red,light_yellow,yellow,light_red]
        
        magnitude = 1
        while magnitude < size:
            # print ("magnitude %s size %s" % (magnitude, size))
            exploding_bit_x = x + random.randrange(-1*magnitude , magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude , magnitude)

            pygame.draw.circle(form_display,colorChoices[random.randrange(0,4)],(exploding_bit_x,exploding_bit_y),1)
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False
        
def fireShell(xy, tank_x_axis , tank_y_axis , turret_pos , gun_power , fire_location , barrier_width , random_Height,enemy_tank_x,enemy_tank_y):
    damage = 0

    fire = True
    
    startingShell = list(xy)
    
    
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                
                
        pygame.draw.circle(form_display,red,(startingShell[0],startingShell[1]),5)

            
        startingShell[0] -= (12 - turret_pos)*2
        
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2)-(turret_pos+turret_pos/(12-turret_pos)))
        
        if startingShell[1] > form_height-ground_height:
            
            hit_x = int((startingShell[0] * form_height-ground_height) / startingShell[1])
            hit_y = int(form_height - ground_height)      
            
            if enemy_tank_x + 40 > hit_x > enemy_tank_x -40:
                print("hit target")
                damage = 25
                
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
    return(damage) 


def enemy_fireShell(xy, tank_x_axis , tank_y_axis , turret_pos , gun_power , fire_location , barrier_width , random_Height,player_tank_x,player_tank_y):
    damage = 0
    fire = True
    
    startingShell = list(xy)
    
    
    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                
                
        print(( startingShell[0],startingShell[1]))
        pygame.draw.circle(form_display,red,(startingShell[0],startingShell[1]),5)

      
        startingShell[0] += (12 - turret_pos)*2
   
        total_gun_power = random.randrange(int(gun_power*0.90),int(gun_power*1.10))
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(total_gun_power/50))**2)-(turret_pos+turret_pos/(12-turret_pos)))
        
        if startingShell[1] > form_height-ground_height:
            
            hit_x = int((startingShell[0] * form_height-ground_height) / startingShell[1])
            hit_y = int(form_height - ground_height)
            if player_tank_x + 15 > hit_x > player_tank_x - 15:
                print("hit target")
                damage = 25
                
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
        
    return(damage)

        
def power(level):
    text = small_font.render("power: " + str(level)+ "%",True,black)
    form_display.blit(text,[form_width/2,0])



    
def health_bars(player_health,enemy_health):
    
    if player_health >75:
        player_health_color = green
        
    elif player_health >50:
        player_health_color = yellow
        
    else:
        player_health_color = red

    if enemy_health > 75:
        enemy_tank_color = green
        
    elif enemy_health >50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red
        
    pygame.draw.rect(form_display,green,(680,25,player_health,25))
    pygame.draw.rect(form_display,green,(20,25,enemy_health,25))


    
    
    
    
def game_loop():
    
    player_health = 100
    enemy_health = 100
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
                    damage_enemy = fireShell(gun,main_Tank_width,main_tank_height, current_turrets_pos ,fire_power,random_barrier_location,barrier_width,random_Height,enemy_tank_width,enemy_tank_height)
                    enemy_health -= damage_enemy
                    
                    possible_movement = ['F','r']
                    move_index = random.randrange(0,2)
                    
                    for x in range(random.randrange(0,10)):
                        
                        if form_width * 0.3 > enemy_tank_width > form_width * 0.03:
                            if possible_movement[move_index] == 'F':
                                enemy_tank_width += 5
                                
                            elif possible_movement[move_index] == 'r':
                                enemy_tank_width -= 5
                                    
                            form_display.fill(white)
                            health_bars(player_health, enemy_health)
                            gun = tank(main_Tank_width , main_tank_height , current_turrets_pos)
                            enemy_gun = enemy_tank(enemy_tank_width , enemy_tank_height , 8)
                
                            fire_power += power_change

                            power(fire_power)
                            barrier(random_barrier_location , random_Height , barrier_width)
                            form_display.fill(green,rect=[0,form_height-ground_height , form_width , ground_height])
                            pygame.display.update()

                            clock.tick(fps)
                                    
         
                                                     
                    
                    damage_player = enemy_fireShell(enemy_gun , enemy_tank_width , enemy_tank_height , 8 , 50 , random_barrier_location , barrier_width , random_Height,main_Tank_width,main_tank_height)
                    player_health -= damage_player
                    
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
            health_bars(player_health,enemy_health)
            gun = tank(main_Tank_width , main_tank_height , current_turrets_pos)
            enemy_gun = enemy_tank(enemy_tank_width , enemy_tank_height , 8)
                
            fire_power += power_change

            power(fire_power)
            barrier(random_barrier_location , random_Height , barrier_width)
            form_display.fill(green,rect=[0,form_height-ground_height , form_width , ground_height])
            pygame.display.update()

            if player_health< 1:
                pass
                
            if enemy_health <1:
                game_won("game_won")
            
            
                
            clock.tick(fps)
                   
                    
  
    pygame.quit()
    quit()
          

    
    
def screen_text(text , color , font , height_displacement ):
    title_surface, title_object = create_text(text, font,color)
    title_object.center = (int(form_width / 2), int(form_height / height_displacement)) 
    form_display.blit(title_surface, title_object)



def check_For_Key_events():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               quit_game()
               

  
        pygame.display.update()
        
def game_intro():
    
    fps = 100

    button_play = pygbutton.PygButton((150,500,100,50), 'play')
    button_quit = pygbutton.PygButton((550,500,100,50), 'quit')
    button_settings = pygbutton.PygButton((350,500,100,50), 'settings')
    
    screen_text("Still under construction ",white, big_font , 6)
    screen_text("Clash of the titans", white, big_font , 3 ) 

    while True: # main game loop

        for event in pygame.event.get():
            
            event_play = button_play.handleEvent(event)
            if 'click' in event_play:
                game_loop()

            event_quit = button_quit.handleEvent(event)
            if 'click' in event_quit:
                pygame.quit()
            

            event_settings = button_settings.handleEvent(event)
            if 'click' in event_settings:
                game_settings()
                
                
        button_play.draw(form_display)
        button_quit.draw(form_display)
        button_settings.draw(form_display)

        pygame.display.update()
        clock.tick(fps)

                      
def game_won(game_won):
    
    form_display.fill(yellow)
    
    screen_text("game over",white, big_font , 6)
    screen_text("YOU WON ", white, big_font , 3 )
    
    button_play_again = pygbutton.PygButton((150,500,100,50), 'button_again')
    button_quit = pygbutton.PygButton((550,500,100,50), 'quit')
    button_settings = pygbutton.PygButton((350,500,100,50), 'settings')
    
    while  game_won == "game_won":
        
     
             
           
         for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
       
            
            event_play = button_play_again.handleEvent(event)
            if 'click' in event_play:
                game_loop()

            event_quit = button_quit.handleEvent(event)
            if 'click' in event_quit:
                pygame.quit()
            

            event_settings = button_settings.handleEvent(event)
            if 'click' in event_settings:
                game_settings()

         
         button_quit.draw(form_display)
         button_settings.draw(form_display)
         button_play_again.draw(form_display)
      
         pygame.display.update()
        
                      

def game_settings():

      
    fps = 100

    button_play = pygbutton.PygButton((150,500,100,50), 'play')
    button_quit = pygbutton.PygButton((550,500,100,50), 'quit')
    form_display.fill(white)   
    
    while True:

  

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
            
            play = button_play.handleEvent(event)
            if 'click' in play:
                game_loop()

            quit_game = button_quit.handleEvent(event)
            if 'click' in quit_game:
                pygame.quit()
                quit()

        button_quit.draw(form_display)
        button_play.draw(form_display)
        
        pygame.display.update()

game_intro()


                                    
if __name__ == '__main__':
    main()

