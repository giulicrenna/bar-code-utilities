from threading import Thread

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

def change_val():
    while True:
        try:
            BAR_CODE.value = input()
        except:
            pass
        
bar_reading_thread = Thread(target=change_val)
bar_reading_thread.start()

'''
def example_function(old, new):
    if old != "":
        label = new
        BAR_CODE.value = ""

BAR_CODE.register_callback(example_function)
'''
