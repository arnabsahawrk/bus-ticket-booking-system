class BusSystem:  # use case of singleton, design pattern
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(BusSystem, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'buses'):  # Prevent re-initialization
            self.buses = []
            self.passengers = []