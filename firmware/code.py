import board
import busio
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
i2c = busio.I2C(board.SCL, board.SDA)

macros = Macros()
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

keyboard.modules.append(encoder_handler)
keyboard.modules.append(macros)

keyboard.col_pins = (board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
  [
    KC.Macro(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL)), KC.Macro(Press(KC.LALT), Press(KC.LSHIFT), Tap(KC.F), Release(KC.LSHIFT), Release(KC.LALT)), KC.Macro(Press(KC.LALT), Tap(KC.Tab), Release(KC.LALT)), 
    KC.Macro(Press(KC.LGUI), Tap(KC.PSCREEN), Release(KC.LGUI)), KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)), KC.Macro(Press(KC.LCTRL), Tap(KC.X), Release(KC.LCTRL)), 
    KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)), KC.Macro(Press(KC.LGUI), Press(KC.LSHIFT), Tap(KC.S), Release(KC.LSHIFT), Release(KC.LGUI)), KC.MUTE,
    KC.MPRV, KC.MPLY, KC.MNXT
  ]
]

display.fill(0)
display.show()
display.text('Rumbleeee!', 0, 0, 1)
display.show()

if __name__ == '__main__':
    keyboard.go()