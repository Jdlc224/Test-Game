import sys
import time

#NAme : Reggae Raphael


node = None

class Room:
    def __init__(self,name, north, east, south, west, up, down, description):
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.description = description
    
    def move(self,direction):
        global node
        node = globals()[getattr(self,direction)]


Bedroom = Room('Bedroom',None, None,None,'Hallway',None,None,'You awake to the smoke of a fire. The fire is quickly spreading over the house, you must get out.To the west is the hallway.')
Hallway = Room('Hallway','Bathroom','Window',None,'Stairway',None,None,'You are in the hallway.To the north is you bathroom,west is a stairway, and to the east is a window.')
Window = Room('Window',None,None,None,'Hallway',None,'Outside_D','Your standing in front of a opened window and when you look out you notice it\'s not that far of a drop.')
Outside_D = Room('Outside_D',None,None,None,None,None,None,'You Died')
Bathroom = Room('Bathroom',None,None,'Hallway',None,None,None,'You are standing in your bathroom.')
Stairway = Room('Stairway',None,'Hallway',None,None,None,'Front_Room','You\'re standing at the stairs. You could see the front door, you are so close to getting out.')#? New Map Part
Front_Room = Room('Front_Room',None,None,None,None,None,None,'')
Cemetary = Room('Cemetary','Cathedral',None,None,None,None,None,'As you get close to the light you see it\'s coming from a small cathedral and see the speck of light through the boarded up window. To the north is the door')
Cathedral = Room('Cathedral','Inside',None,'Coffin',None,None,None,'As you get close to the light you see it\'s coming from a small cathedral and see the speck of light through the boarded up window. To the north is the door')
Coffin = Room('Coffin',None,None,None,None,None,None,'')
Inside = Room('Inside','Alter',None,None,'Side_Room',None,None,'You walk inside. You notice the candles lit by the window. You see some more light coming from a room to your left, but you also here a faint sound coming from a room ahead of you.')
Alter = Room('Alter',None,'Basement_Door',None,None,None,None,'You are standing at alter. There\'s a door to the east of you.')
Basement = Room('Basement',None,None,'Alter',None,None,None,'You go down to the basement. It\'s empty.')
Side_Room = Room('Side_Room',None,'Stairs',None,'Closet_Door',None,None,'You walk into the room and see two doors west and east of you.')
Closet_Door = Room('Closet_Door',None,None,'Stairs',None,None,None,'You try opening the door multiple times but it won\'t budge.')
Stairs = Room('Stairs',None,'Inside',None,None,None,'Storage_Room','Behind the door are stairs that lead down to another room.')
Storage_Room = Room('Storage_Room','Table',None,'Side_Room',None,None,None,'You go down the stairs into a storage room. It\'s dimly lit by some candles. You see something on a table on the other side of the room in front of you.')
Table = Room('Table',None,'Light','Storage_Room',None,None,None,'You approach the table. There\'s candles surrounding the edges of the table and notice there is a picture in the middle. Before you can look at it you hear something to the left of you and see a light start flickering.')
Light = Room('Light',None,None,None,None,None,None,'')

node = Bedroom
        

while True:
    print node
    print 'Room:' + node.name
    print
    print 'Description:' + node.description
    
    movement = ['north','east','south','west','up','down']
    command = raw_input('>').strip().lower()
    if command in ['q', 'exit', 'quit']:
        print 'You beat yourself to death'
        sys.exit(0)
    if command in movement:
        try:
            node.move(command)
        except:
            print 'You can\'t go that way.'
    if node == Front_Room:
            print 'You go down the stairs as fast as you can.\
    As you\'re going towards the door your hit on the back of your head.\
    You fall to the floor and start losing conscious.\
    Before you lose conscious you see a blurry figure standing above you.'
            node = Cemetary
    
    
    if node == Outside_D:
        print node.name
        print 
        print 'You jumped and were impaled by a old rusty fence pole.'
        print node.description
        sys.exit(0)
    
    
    if node == Cemetary:
            print node.name
            print '-------------------------------------------------------'
            print 
            print 'You awake in a coffin in a cemetary, when you get up you notice a shovel in a pile of dirt. It\'s a foggy night and you can mostly just see trees.'
            print 
            print '-------------------------------------------------------'
    
            
    if node == Coffin:
            print node.name
            print
            print 'You tried to retrace your steps and as your walking you trip on a root and hit your head on a gravestone'
            print 'You died.'
            sys.exit(0)
            

    if node == Light:
            time.sleep(5)
            print node.name
            print '-------------------------------------------------------'
            print 
            print 'You start walking towards the light. The light flickers and you see a man in black standing and staring at you with something in his hand. The light flickers again and he\'s gone. You look around to see where he could have gone and don\'t see anything.'
            print 
            print 'To Be Continued....'
            print 
            print '-------------------------------------------------------'
            sys.exit(0)




