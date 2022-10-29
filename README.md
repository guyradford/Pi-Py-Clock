# Pi Py Clock

## Connecting up Display to RPi1

https://raspi.tv/2013/8-x-8-led-array-driven-by-max7219-on-the-raspberry-pi-via-python

## Python 3

Installing pip:

```commandline
sudo apt update
sudo apt install python3-pip
```


## Copying the files

`pip3 install luma.led-matrix==1.6.1`

`sudo apt-get install libopenjp2-7`
`sudo apt install libtiff5`

## Setting up the Service

https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267

Copy `service/clock.service` to `/etc/systemd/system/clock.service`

```commandline
sudo systemctl daemon-reload
sudo systemctl enable clock.service
sudo systemctl start clock.service
```