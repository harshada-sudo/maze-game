import turtle
import math 
import random

#create window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze game")
wn.setup(700,700)
wn.tracer(0) #turns off screen updates

#score
score = 0
high_score = 0

#create pencil
pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape("square")
pencil.color('white')
pencil.penup()
pencil.hideturtle()
pencil.goto(0,295)
pencil.write('Score : 0  High Score :0 ',align='center', font=('times new roman',20,'normal'))

#create pen
class Pen(turtle.Turtle): #everything that a turtule can perform pen can also perform
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#create player
class Player(turtle.Turtle): #Player is child of turtule module's Turtule class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        #calculate move
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x,move_to_y) not in walls :
            self.goto(move_to_x,move_to_y)

    def is_collision(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False
#create treasure class
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#create enemy
class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.direction = random.choice(['up','down','left','right'])

    def move(self):
        if self.direction == 'up':
            dx = 0
            dy = 24
        elif self.direction == 'down':
            dx = 0
            dy = -24
        elif self.direction == 'right':
            dx = 24
            dy = 0
        elif self.direction == 'left':
            dx = -24
            dy = 0
        else:
            dx = 0
            dy = 0

        #if player is close then go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction == 'left'
            elif player.xcor() > self.xcor():
                self.direction == 'right'
            elif player.ycor() > self.ycor():
                self.direction == 'up'
            elif player.ycor() < self.ycor():
                self.direction == 'down'


        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(['up','down','right','left'])

        turtle.ontimer(self.move,t=random.randint(100,300))

    def is_close(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False


    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#create level list
levels = [""] #empty level at levels[0]

level_1=[
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXXE         XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX       EXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXT  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXXE                    X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXXE                   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#create empty list
treasures = []

#create enemies list
enemies = []
#add above maze to maze list
levels.append(level_1)

#co-ordinates of walls' blocks
walls = []

#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            if character == 'X':
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character == 'P':
                player.goto(screen_x,screen_y)
            if character == 'T':
                treasures.append(Treasure(screen_x,screen_y))
            if character == 'E':
                enemies.append(Enemy(screen_x,screen_y))


#create instance of Pen class
pen = Pen()
player = Player()  #player is instance of Player class


#call setup_maze function
setup_maze(levels[1])
print(walls)

#keyboard binding
turtle.listen()
turtle.onkeypress(player.go_left,"Left")
turtle.onkeypress(player.go_right,"Right")
turtle.onkeypress(player.go_up,"Up")
turtle.onkeypress(player.go_down,"Down")

#start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move,t=250)

#main game loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            #increse score
            player.gold += treasure.gold  #add treasure gold to player gold
            score = player.gold

            if score > high_score:
                high_score = score
            
            pencil.clear()
            pencil.write('Score : {}  High Score : {}'.format(score,high_score),align= 'center',font=('times new roman',20,'normal'))

            print(f"player gold {player.gold}") 
            treasure.destroy() #destroy treasure
            treasures.remove(treasure)

    for enemy in enemies:
        if player.is_collision(enemy):
            print('player dies !!')
    #update screen
    wn.update()