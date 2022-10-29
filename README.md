# Pi Py Clock

I did this project as I needed a new clock and I had an only Raspberry Pi lying around unused and I also wanted to use my new 3D Printer.

The idea was simple, buy an LED matrix, connect it to the RPi, then using python write a very simple clock application that would auto-start on boot.

The LED Matrix uses a MAX7219 Chip driving 4 8x8 LED Matrix boards. This easily connects to the Raspberry Pi via the SPI interface.

Then a quick google search revealed the Python [Luma LED Matrix](https://pypi.org/project/luma.led-matrix/) Library. This library nicely wraps the SPI interface and abstracts the display to an easy to use "Canvas".
It even allows you to set different fonts :)

After playing with the library for a bit I discovered the [silly-clock.py](https://github.com/rm-hull/luma.led_matrix/blob/master/examples/silly_clock.py) example. 
I used this as a base, removed some of the "silly" bits, changed the font. This gave me the perfect clock for my project. 



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