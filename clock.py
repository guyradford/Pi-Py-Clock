#!/usr/bin/env python
import time
from datetime import datetime
from pathlib import Path

from PIL import ImageFont
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, TINY_FONT, LCD_FONT


def main():
    font = proportional(LCD_FONT)

    # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=False)
    device.contrast(1)

    toggle = False  # Toggle the second indicator every second
    while True:
        toggle = not toggle

        # Do the following twice a second (so the seconds' indicator blips).
        # I'd optimize if I had to - but what's the point?
        # Even my Raspberry PI2 can do this at 4% of a single one of the 4 cores!
        hours = datetime.now().strftime('%H')
        minutes = datetime.now().strftime('%M')
        with canvas(device) as draw:
            width = 0
            for letter in hours:
                width = width + len(font[ord(letter)])

            text(draw, (15 - width, 1), hours, fill="white", font=font)
            text(draw, (15, 1), ":" if toggle else " ", fill="white", font=proportional(TINY_FONT))
            text(draw, (17, 1), minutes, fill="white", font=font)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
