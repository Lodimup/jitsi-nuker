# jitsi-nuker
Spawns multiple chrome instances to <del>nuke</del> load test jitsi
# Usage
Requires python 3.10 

download /scripts to your server
```
sudo bash install.sh  # install dependencies, and add kernel moduel
sudo clone.sh  # clone repositories to your home dir
```
rename .env.sample to .env, then edit configs in ~/jitsi-nuker
```
cd ~/jitsi-nuker
mv .env.sample .env
vim .env
```
create fake webcam stream
```
cd ~/jitsi-nuker/scripts
bash stream.sh
```
<del>nuke</del> load test jitsi
```
cd ~/jitsi-nuker/scripts
bash join.sh
```

# note
does not require fake-stream anymore.  
edit stream.sh, and change ~/Fake-Stream/test.mp4 to any mp4
## srcs
https://www.linuxfordevices.com/tutorials/linux/fake-webcam-streams
