# GifPro

![GifPro](http://josh.farrant.me/images/gifPro/gifPro.png "GifPro")

![Cool Gif of me walking through Newstreet station](http://38.media.tumblr.com/7dda37134158f24c08b394498fc3ad1d/tumblr_nc8uygxP0i1tmy92xo1_500.gif)

**Gif-ify Your Life!**

Project for Hackference 2.0.14 Hackathon.

By [@FarPixel](https://twitter.com/FarPixel) & [@DavidMaitland](https://twitter.com/DavidMaitland)

## Live demos
[hackference.tumblr.com](http://hackference.tumblr.com/)

[@GifProHack](https://twitter.com/GifProHack)

## About

**GifPro** creates a 20 frame GIF once every 5 minutes using the GoPro's undocumented *live preview* feature, which it then uploads to Tumblr / Twitter using 3G, 4G, or WiFi!

This works both when the camera is and isn't recording by utilizing the WiFi bridge that the GoPro creates to communicate with the official GoPro app.

Currently, it uses a standalone RaspberryPi to process the stream and upload the resulting .gif to various social media sites.

GifPro can be useful for logging road trips, hackathons, or anything that you want to record snippets of, without wasting space recording on the camera itself.

### How it works

The GoPro is running a Cherokee server which exposes some small files, including some short video snippets used for the live preview in the official GoPro app, and a single stream file. It is possible to extract single frames from this stream to get a live view from the camera, even when it is not actively recording. These frames are then stitched together into a short GIF on the Raspberry Pi, and uploaded directly to Tumblr to provide a near-live gif stream.

## Installation

`sudo apt-get install gifsicle imagemagick ffmpeg`

`sudo pip install pytumblr requests`

![David dancing Gif](http://31.media.tumblr.com/16887c2b9d54680fa07cf4e8449e1fca/tumblr_nc9sqzJZVn1tmy92xo1_500.gif)
