cd ~ && \
sudo apt-get update && \
sudo apt-get install v4l2loopback-utils ffmpeg fonts-liberation git python3-pip vim -y && \
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
sudo dpkg -i google-chrome-stable_current_amd64.deb && \
sudo modprobe v4l2loopback card_label="FakeCam" exclusive_caps=1
