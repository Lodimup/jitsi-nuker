ffmpeg -stream_loop -1 -re -i ~/Fake-Stream/test.mp4 -vcodec rawvideo -threads 0 -f v4l2 /dev/video0

