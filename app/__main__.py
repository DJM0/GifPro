#!/usr/bin/python

# @FarPixel & @DavidMaitland
# https://github.com/davidmaitland/GifPro

import os
import time
import pytumblr
import urllib
import uuid
from subprocess import call

frequency = 10 # Loop interval
frames = 20 # Fames to take
delay = 0.2 # Delay between frames
gifDelay = 20 # Used for timing GIF generation

# Tumblr config
tumblrName = config.tumblrName
consumerKey = config.consumerKey
consumerSecret = config.consumerSecret
oauthToken = config.oauthToken
oauthSecret = config.oauthSecret
tags = config.tags

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
