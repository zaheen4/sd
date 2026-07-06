class USBCCharger:
    def charge(self):
        return "Charging via USB-C"

class USBBPort:
    def connect(self):
        return "Connected to USB-B port"

class Adapter(USBCCharger):
    def __init__(self, port):
        self.port = port

    def charge(self):
        return self.port.connect() + " using USB-C to USB-B adapter"


phone = USBBPort()
charger = Adapter(phone)
print(charger.charge())
