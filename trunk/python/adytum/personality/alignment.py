import protocols
from peak.binding.components import Component
from interfaces import IAlignment

class Alignment(Component):
    MORALS = ['good', 'neutral', 'evil']
    ETHICS = ['chaotic', 'neutral', 'lawful']

    def __init__(self, moral_type=None, ethical_type=None):
        pass

    def setMorality(self):
        pass
    def getMorality(self):
        pass
    def setEthics(self):
        pass
    def getEthics(self):
        pass
    def getOCEANMap(self):
        pass
