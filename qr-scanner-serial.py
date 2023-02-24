from threading import Thread
import serial

COM_PORT = "COM6"
BAUDRATE = 1200

class BarCodeHolder:
    def __init__(self, initial_value = "") -> None:
        self._value = initial_value
        self._callbacks = []
        
    @property
    def value(self) -> None:
        return self._value

    @value.setter
    def value(self, new_value) -> None:
        old_value = self._value
        self._value = new_value
        self._notify_observers(old_value, new_value)
        
    def _notify_observers(self, old_value, new_value) -> None:
        for callback in self._callbacks:
            callback(old_value, new_value)
    
    def register_callback(self, callback) -> None:
        self._callbacks.append(callback)
        
BAR_CODE = BarCodeHolder()

try:
    ser = serial.Serial(COM_PORT, BAUDRATE)
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 1
except:
    raise OSError("Could not open serial port")

def change_val():
    while True:
        try:
            byte = ser.readline()
            BAR_CODE.value = byte.decode('UTF-8')
        except:
            pass
        
bar_reading_thread = Thread(target=change_val)
bar_reading_thread.start()