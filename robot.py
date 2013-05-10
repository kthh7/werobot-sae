import os
import sys
import werobot

robot = werobot.WeRoBot(token='whu')


@robot.handler
def echo(message):
    return 'ni mei'
