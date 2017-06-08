#!/usr/bin/python3

#
# @author: Jonathan Sawin
#

import sys, traceback
#import optparse
import ztc_choices, ztc_rooms

#main function
def main(argv):

    # if len(sys.argv) <= 1:
    #     print("expected cmd line args: exiting")
    #     return 1
    # if argv[1] == "" :
    #     print("expected cmd line args: exiting")
    #     return 1

    first_room = ztc_rooms.room.room_list[0]
    first_room.load_room()
    
    #asdf_choices.choose(asdf_choices.choice_list[argv[1]])

    

    # parser = optparse.OptionParser()
    # parser.add_option('left', action="move", direction="left")
    # parser.add_option('up', action="move", direction="up")
    # parser.add_option('down', action="move", direction="down")
    # parser.add_option('right', action="move", direction="right")
    # parser.add_option('use', action="use", direction="left")

if __name__ == "__main__":
    main(sys.argv)
