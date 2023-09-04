
directions = ["H2D", "D2H"]
types = ["Request", "Respones"]

class Trans():
    def __init__(self, latency, direction, type):
        self.latency = latency

        if direction not in directions:
            raise Exception("Unknown Transaction Direction: %s", direction)
        self.direction = direction

    def getLatency(self):
        return self.latency
