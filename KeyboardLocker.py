__author__ = 'madsens'


class KeyboardLocker:

    def __init__(self, serio=0):
        self._on = False
        self.serio = serio

    def on(self):
        return self._on

    def write_value(self,path, value):
        with open(path, "a") as f:
            f.write(value)

    def toggle(self):
        if self.on():
            self.turn_off()
        else:
            self.turn_on()

    def description(self):
        path = '/sys/devices/platform/i8042/serio%d/description' % (self.serio,)
        with open(path, "r") as f:
            description = f.read()
        return description

    def turn_on(self):
        try:
            self.write_value('/sys/devices/platform/i8042/serio%d/bind_mode' % (self.serio,),'auto')
        except IOError, e:
            self._on = False
            raise
        else:
            self._on = True
        return self.on()

    def turn_off(self):
        try:
            self.write_value('/sys/devices/platform/i8042/serio%d/bind_mode' % (self.serio,),'manual')
            self.write_value('/sys/devices/platform/i8042/serio%d/drvctl' % (self.serio,),'psmouse')
        except IOError, e:
            self._on = True
            raise
        else:
            self._on = False
        return self.on()
