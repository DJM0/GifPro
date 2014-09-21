#!/usr/bin/python

# @FarPixel & @DavidMaitland
# https://github.com/davidmaitland/GifPro

import os
import time
import pytumblr
import urllib
import uuid
from subprocess import call

frequency = 90 # Loop interval
frames = 20 # Fames to take
delay = 0.2 # Delay between frames
gifDelay = 20 # Used for timing GIF generation

# Tumblr config
tumblrName = "hackference"
consumerKey = "00qcEwFwDX1BiFP3zNNBC1aeFI99jSaiHJmWAYdYoWsLQSMBgJ"
consumerSecret = "tKJape76Tqj6bcUThlXSTaE3ljgWbC1HeKukI3BDj9vtnCd8Z5"
oauthToken = "cnI5FFuiFzJIhopm18DyqBVsQR8GuQhjBvwF6IeH4lX81gW9Oe"
oauthSecret = "zkqEb4I7USyAXeMOXMsKbJpF4EKMICvYiE62ulEFTzSXMoUbK6"
tags = ["Hackference", "GoPro", "GIF", "Hacking"]

# Authenticate via OAuth to Tumblr
tumblr = pytumblr.TumblrRestClient(consumerKey, consumerSecret, oauthToken, oauthSecret)

# Files config
data = "data/"
tmp = data + "tmp/"
output = data + "output/"

# GoPro
goProUrl = "http://10.5.5.9:8080/live/amba.m3u8"

def getGif():

  # Remove tmp files
  call("rm -f " + tmp + "*", shell=True)

  # Get MP4 files from GoPro
  print "[+] Talking to GoPro"
  for i in range(frames):
    num = str(i).zfill(3)
    goGoPro(num)
    time.sleep(delay)

  # Convert MP4 files into single GIF images
  print "[+] Converting GoPro files"
  for i in range(frames):
    num = str(i).zfill(3)
    mp4ToGif(num)

  # Make the final GIF
  print "[+] Making GIF"
  filename = makeGif()

  # Post 
  post(filename)

  print "Done: " + filename


def mp4ToGif(num):

  call("ffmpeg -i " + tmp + num + ".m3u8 -ss 00:00:00 -vframes 1  " + tmp + num + ".png", shell=True)
  call("convert " + tmp + num + ".png " + tmp + num + ".gif", shell=True)

def makeGif():

  uid = str(uuid.uuid4())
  filename = output + uid + ".gif"

  call("gifsicle --colors 256 --delay=" + str(gifDelay) + " --loop " + tmp + "*.gif >" + filename, shell=True)

  return filename

def goGoPro(num):

  urllib.urlretrieve(goProUrl, tmp + num + ".mp4")

def post(filename):

  try:
    tumblr.create_photo(tumblrName, state="published", tags=tags, data=filename)
  except:
    pass

  return True

def status(state):

  print state

  return True

if __name__ == "__main__":

  if not os.path.exists(data):
    os.makedirs(data)
    os.makedirs(tmp)
    os.makedirs(output)


  while 1 == 1:

    try:
      getGif()
    except:
      print "[!] Failed for some reason"

    time.sleep(frequency)
