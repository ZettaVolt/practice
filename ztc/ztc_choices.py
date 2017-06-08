#!/usr/bin/python3

import subprocess, sys, time
import ztc_rooms

choice_list = {}
choice_list['left'] = "goLeft"
choice_list['up'] = "goUp"
choice_list['down'] = "goDown"
choice_list['right'] = "goRight"
choice_list['use'] = "tryUse"
choice_list['help'] = 'help'

def move(direction, room_id):
    print("Moving " + direction)
    time.sleep(1)
    ztc_rooms.room.room_list[room_id].move_room(direction)

def use(room_id):
    print("performing use in room " + str(room_id))
    print("no effect")
    time.sleep(1)
    ztc_rooms.room.room_list[room_id].load_room()

def help_text(room_id):
    ztc_rooms.room.room_list[room_id].load_room()

def callMethod(method, room_id, *arguments):

    if method == "move":
        move(arguments[0], room_id)
    if method == "use":
        use(room_id)
    if method == "help":
        help_text(room_id)

def choose(choice, room_id):
    function = ""
    choice = choice.lower()
    if choice == "left":
        function = "move"
        direction = "left"
    if choice == "up":
        function = "move"
        direction = "up"
    if choice == "right":
        function = "move"
        direction = "right"
    if choice == "down":
        function = "move"
        direction = "down"
    if choice == "use":
        function = "use"
    if choice == "help":
        function = "help"
    
    if choice not in choice_list:
        tryagain = raw_input("invalid, try again")
        choose(tryagain, room_id)

    if function == "move":
        callMethod(function, room_id, direction)
    elif function == "use" or function == "help":
        callMethod(function, room_id)
