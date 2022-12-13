######################################################

# Project: Project 2
# UIN: 660866964
# repl.it URL: https://replit.com/@TylerStrach/VideoGame-1#main.py

# For this project, I received help from the following members of CS111.
# Manav Kohli, netID mkohli4: help with getting the start screen working

######################################################

#imports
import turtle
import random

#basic turtle and screen objects
s = turtle.Screen()
t = turtle.Turtle()

#setting the screen size for edge conditions and placing objects
w = 300
h = 300

#game dictionary with values to run the entire game
game = {"lives": 3, "level": 0, "multiplier": 1, "background_image": "start_screen.gif", "state": "n/a", "t": turtle.Turtle()}

#user dictionary to be able to access seperately
user = {"t": turtle.Turtle(), "x": 0, "y": -135, "radius": 15, "img": "user_spaceship.gif", "direction": 90, "type": "user"}

#coin dictionary to be able to access sperately
coin = {"t": turtle.Turtle(), "x": 0, "y": 135, "radius": 15, "img": "coin.gif", "direction": "n/a", "type": "coin"}

#empty object function to load all objects
objects = []

'''this is a function to load all the dictionaries of each object into a list
in order to be able to loop through them all at one time'''
def load_objects():
  start_h = -100
  objects.append(user)
  objects.append(coin)

  #used even/odd to alternate directions of harm objects
  for i in range(8):
    if i % 2 == 0:
      objects.append({"t": turtle.Turtle(), "x": random.randint(-w / 2, w / 2), "y": start_h, "radius": 15, "img": "spaceship.gif", "direction": "right", "type": "harm"})
    else:
      objects.append({"t": turtle.Turtle(), "x": random.randint(-w / 2, w / 2), "y": start_h, "radius": 15, "img": "spaceship.gif", "direction": "left", "type": "harm"})
    start_h += 30

'''this function is called right away in order to set the screen properties, and to write all the text on the starting screen'''
def startup():
  s.setup(300, 300)
  s.tracer(0)

  game["t"].hideturtle()
  game["background_image"] = "start_screen.gif"
  s.bgpic(game["background_image"])
  game["state"] = "new"

  game["t"].color('red')

  game["t"].penup()
  game["t"].goto(0, 50)
  game["t"].pendown()

  style = ('Comic sans', 12, 'bold')
  game["t"].write('Welcome to SpaceChaser', font=style, align = 'center')

  game["t"].penup()
  game["t"].goto(0, -20)
  game["t"].pendown()

  game["t"].write('Collect the coins.', font=style, align='center')

  game["t"].penup()
  game["t"].goto(0, -40)
  game["t"].pendown()

  game["t"].write('You have 3 lives', font=style, align='center')
  
  game["t"].penup()
  game["t"].goto(0, -75)
  game["t"].pendown()

  style = ('Comic sans', 8, 'bold')
  game["t"].write('Press Space to Start', font=style, align='center')

'''this is the function called when space is pressed and actually starts the game, it waits for space to run, sets the game to play, sets the background, and assigns the images to the turtle objects'''
def start():
  s.clear()
  game['background_image'] = "background.gif"
  s.bgpic(game["background_image"])

  game['state'] = 'play'

  for obj in objects:
    s.addshape(obj["img"])
    obj["t"].shape(obj["img"])
    obj['t'].goto(obj['x'], obj['y'])

  main()

'''this is the scoreboard seen in the bottom right when game is in play
it is called only when the game starts, and when there is a change to lives or level'''
def scoreboard():
  game["t"].clear()

  game["t"].color('yellow')
  style = ('Comic sans', 8, 'normal')

  game["t"].penup()
  game["t"].goto(65, -125)
  game["t"].pendown()

  score = "Lives: ", game['lives'], "Level: ", game['level']

  game["t"].write(score, font=style, align = 'center')


'''sets the new locations for the harm objects every time the loop is ran
this causes them to animate aross the screen either left to right or right to left'''
def update_values():
  for obj in objects:
    if(obj["type"] == "harm"):

      if (obj["direction"] == "right"):
        obj["x"] -= (0.8 * game['multiplier'])
      else:
        obj["x"] += (0.8 * game['multiplier'])


'''checks the distance between the user object and either the coin and harm objects
returns true if they are touching'''
def collision_check(t1, t2):
  if ((t1.distance(t2)) < 20):
    return True
  else:
    return False


'''this checks all of the conditons and does specific actions based on where each object is
for harms, it checks if touching the end of the screen to be moved to the other side AND if it is touching the user object
for the coin, it checks if in contact with the user'''
def handle_conditions():
  for obj in objects:
    
    if (obj['x'] > (w / 2 - 15)):
      obj['x'] = ((w / 2 * -1) + 15)
    elif (obj['x'] < (-w / 2 + 15)):
      obj['x'] = ((w / 2 * 1) -15)
    
    if obj["type"] == "harm":

      if((collision_check(user["t"], obj["t"])) == True):
        user['x'] = 0
        user['y'] = -135
        game['lives'] -= 1
        scoreboard()
    
    if obj['type'] == 'coin':

      if((collision_check(user['t'], coin['t'])) == True):
        user['x'] = 0
        user['y'] = -135
        game['level'] += 1
        coin['x'] = random.randint((-w / 2) + 30, (w / 2) -30)
        game['multiplier'] += 0.8
        scoreboard()


'''this moves all the objects to their new position after the values are 
updated and the conditions are checked'''
def render():
  for obj in objects:
    obj['t'].goto(obj['x'], obj['y'])

'''this function is called when the user presses the up key to move the user one lane up'''
def up():
  user['t'].setheading(180)
  user['y'] += 30

'''this function is called when the user presses the down key to move the user one lane down'''
def down():
  user['t'].setheading(0)
  user['y'] -= 30

'''this function is called when the user presses the right key to move the user 1/2 a lane to the right'''
def right():
  user['t'].setheading(90)
  user['x'] += 15

'''this function is called when the user presses the left key to move the user 1/2 a lane to the left'''
def left():
  user['t'].setheading(270)
  user['x'] -= 15

'''this function is called when game lives variable is 0 and shows the end screen and ends all the code'''
def game_over():
  s.clear()

  game['background_image'] = "start_screen.gif"
  s.bgpic(game["background_image"])

  game["t"].penup()
  game["t"].goto(0, 50)
  game["t"].pendown()

  style = ('Comic sans', 16, 'bold')
  game["t"].write('GAME OVER', font=style, align = 'center')

  game["t"].penup()
  game["t"].goto(0, 0)
  game["t"].pendown()

  style = ('Comic sans', 12, 'bold')
  score = "Final Score: ", game['level']
  game["t"].write(score, font=style, align = 'center')

'''function that contains the animation loop, tells the screen to listen for user movements, and ends the loop'''
def main():

  #keypress handlers
  s.onkey(up, "Up")
  s.onkey(down, "Down")
  s.onkey(right, "Right")
  s.onkey(left, "Left")
  s.listen()

  game['state'] = 'play'
  scoreboard()

  #animation loop
  while (game['state'] != 'end'):

    #clears objects
    if(game['state'] == 'play'):
      for obj in objects:
        obj['t'].clear()

      #calls update and condition functions
      update_values()
      handle_conditions()

      #checks if game should be over
      if game['lives'] < 1:

        #ends loop
        game['state'] = 'end'
      
      #moves the objects to new positions after checking conditions
      render()

      #update screen
      s.update()

  #calls to display game over screen when amination loop ends
  game_over()

#calls functions to set up new game
load_objects()
startup()

#listens for space to start game
s.onkey(start, "space")
s.listen()




  

    



  
