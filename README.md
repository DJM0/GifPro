# GifPro

Project for Hackference 2.0.14 Hackerton.

Live demo: [hackference.tumblr.com](http://hackference.tumblr.com/)

[@FarPixel](https://twitter.com/FarPixel)
[@DavidMaitland](https://twitter.com/DavidMaitland)

## About

Creates a 20 frame GIF every 5 minutes using the GoPro's undocumented "live preview" feature, then uploads it to Tumblr / Twitter using 3/4G or WiFi.

This works even when the camera isn't recording and uses the WiFi bridge the GoPro creates for the official GoPro app.

Currently uses a standalone RaspberryPi to process the stream / upload to various social media sites.

Useful for logging road trips, hackathons or anything you don't want to waste space recording on the camera itself.

### How it works

The GoPro is running a Cherokee server which exposes some very interesting files:

**Insert image here**

## Install

gifsicle
ffmpeg

`sudo pip install pytumblr requests`
