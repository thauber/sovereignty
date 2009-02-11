from random import Random

class Effect(object):
    def __init__(self, probability, var, change, reverse_change=None):
        self.probability = probability
        self.var = var
        self.change = change
    
    def apply_change(self, nation):
        stat = getattr(nation, var, None)
        if stat is not None:
            if Random().random() > self.probability:
                setattr(nation, var, stat+change)
            elif reverse_change is not None:
                setattr(nation, var, stat+reverse_change)
        return nation

STATUSES = ('Very Poor', 'Poor', 'Average', 'Good', 'Very Good')
class Stat(object):
    def __init__(self, int, name, statuses = STATUSES):
        self._value = int
        self.name = name
        if len(statuses) == 5:
            self.statuses = statuses
        else:
            self.statuses = STATUSES
    
    def get_status(self):
        if self.value > 90:
            return self.statuses[4]
        elif self.value > 70:
            return self.statuses[3]
        elif self.value > 30:
            return self.statuses[2]
        elif self.value > 10:
            return self.statuses[1]
        else:
            return self.statuses[0]
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if value > 100:
            self._value = 100
        elif value < 0:
            self._value = 0
        else:
            self._value = value
    value = property(get_value, set_value)
    
    def __add__(self, value):
        self.value += value
    def __sub__(self, value):
        self.value -= value
    def __int__(self):
        return self.value
    def __unicode__(self):
        return self.value
        