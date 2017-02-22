# webmc

Video converter - Make webms easily

Dependencies:
ffmpeg


# Instalation

```
pip install webmc
```

## Usage

Just run `webmc` for the GUI

### CLI arguments
* webm.py FILENAME
* -ns -> No audio
* [START FROM]-[DURATION] -> Trims the video duration, use 00:00:00 format or seconds
* [WIDTH]x[HEIGHT] -> Blank keeps aspect ratio - Examples: 640x480 , 640x , x480

examples: 
* `webmc myvideo.mp4`
* `webmc myvideo.mp4 00:03:34-15`
* `webmc myvideo.mp4 -ns x720`
* `webmc myvideo.mp4 00:04:20-00:02:00 200x200`
