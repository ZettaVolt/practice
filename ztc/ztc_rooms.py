#!/usr/bin/python3

import sys, os, subprocess
import asdf_choices

class room:
# a room contains a display (terminal), prompt for an action, and a list of valid actions that 
# the room knows how to handle

    room_list = {}
    current_room = ''
    current_room_counter = 0

    room_id = ''
    display = ''
    prompt = ''
    action_list = ()
    adjacent_rooms = ()

    def __init__(self, room_id, display, prompt, action_list, adjacent_rooms):
        if room_id in room.room_list:
            raise Exception("failed to create room of id " + str(room_id) +": room already exists")
        self.room_id = room_id
        self.display = display
        self.prompt = prompt
        self.action_list = action_list
        self.adjacent_rooms = adjacent_rooms
        room.room_list[room_id] = self
        room.current_room_counter += 1

    def load_room(self):
        current_room = self.room_id
        prompt_text = self.prompt  
        while 1:
            display_screen(self.display)
            action = input(prompt_text)
            cmd = action.split(" ")
            if cmd[0] not in self.action_list:
                prompt_text = "can't do that, try again: "
                continue
            asdf_choices.choose(action, self.room_id)
            break

    def move_room(self, direction):
        if direction == "left":
            next_room = self.adjacent_rooms[0]
        elif direction == "right":
            next_room = self.adjacent_rooms[1]
        elif direction == "up":
            next_room = self.adjacent_rooms[2]
        elif direction == "down":
            next_room = self.adjacent_rooms[3]
        if next_room == -1:
            raise Exception("faileid to load next room, invalid room id")
        room.room_list[next_room].load_room()

def display_screen(display):
    subprocess.call('clear', shell=True)
    print(display)

basecmds = ('use', 'help')

display = "This is screen one"
prompt = "not much to see here... "
action_list = basecmds + ('up',)
#adajacent_rooms will be (left room #, right #, up, down), where invalid rooms are -1
adjacent_rooms = (-1, -1, 1, -1)
room(room.current_room_counter, display, prompt, action_list, adjacent_rooms)

display = "This is screen two"
prompt = "some more movement options available... "
action_list = basecmds + ('up', 'down', 'right', 'left')
#adajacent_rooms will be (left room #, right #, up, down), where invalid rooms are -1
adjacent_rooms = (2, 3, 4, 0)
room(room.current_room_counter, display, prompt, action_list, adjacent_rooms)

display = "This is screen three"
prompt = "you went left... "
action_list = basecmds + ('right',)
#adajacent_rooms will be (left room #, right #, up, down), where invalid rooms are -1
adjacent_rooms = (-1, 1, -1, -1)
room(room.current_room_counter, display, prompt, action_list, adjacent_rooms)

display = "This is screen four"
prompt = "you went right... "
action_list = basecmds + ('left',)
#adajacent_rooms will be (left room #, right #, up, down), where invalid rooms are -1
adjacent_rooms = (1, -1, -1, -1)
room(room.current_room_counter, display, prompt, action_list, adjacent_rooms)

display = "This is screen five"
prompt = "you went up... "
action_list = basecmds + ('down',)
#adajacent_rooms will be (left room #, right #, up, down), where invalid rooms are -1
adjacent_rooms = (-1, -1, -1, 1)
room(room.current_room_counter, display, prompt, action_list, adjacent_rooms)