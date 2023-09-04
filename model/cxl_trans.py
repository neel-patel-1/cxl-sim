
directions = ["H2D", "D2H"]
types = ["Request", "Response"]
prots = ["cache", "mem"]

class Trans():
    def __init__(self, latency, direction, type, prot):
        self.latency = latency

        if direction not in directions:
            raise Exception("Unknown Transaction Direction: %s", direction)
        self.direction = direction

        if prot not in prots:
            raise Exception("Unkown protocol: %s", prot)
        self.prot = prot

        if type not in types:
            raise Exception("Unkown type: %s", type)
        self.type = type

    def getLatency(self):
        return self.latency

class H2DRequest(Trans):
    def __init__(self):
        super().__init__(10, "H2D", "Request", "cache")
        