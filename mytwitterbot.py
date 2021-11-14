# mytwitterbot.py
# IAE 101, Fall 2020
# Project 04 - Building a Twitterbot
# Name:David Lin       
# netid:davidlin      
# Student ID:113828351 
import os
import sys
import time
import simple_twit
import random

def main():
    api = simple_twit.create_api()
    simple_twit.version()
    random_lines = random.choice(open("Quotes.txt").readlines())
    print(random_lines)
    path = "C:\\Users\\david\\Downloads\\Images"
    files = os.listdir(path)
    x = random.choice(files)
    res = simple_twit.send_media_tweet(api, "To everyone needing a motivational quote today..." + random_lines, x)
    print(type(res))
    
    
# end def main()

if __name__ == "__main__":
       main()
