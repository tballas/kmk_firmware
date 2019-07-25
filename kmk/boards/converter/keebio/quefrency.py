import board

from kmk.consts import DiodeOrientation
from kmk.mcus.circuitpython_usbhid import KeyboardConfig as _KeyboardConfig
from kmk.pins import Pin as P


class KeyboardConfig(_KeyboardConfig):
    # Will need additional work and testing
    col_pins = (P.A1, P.A2, P.A3, P.A4, P.A5, P.SCK, P.MOSI, P.D12)
    row_pins = (P.A0, P.D13, P.D11, P.D10, P.D9, P.D7)
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.TX
    uart_pin = board.SCL
    split_type = 'UART'
    split_flip = False
    split_offsets = [8, 8, 8, 8, 8, 8]