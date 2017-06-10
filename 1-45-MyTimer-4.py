import time as t

class MyTimer():
    def __init__(self): #avoid the mistake
        self.unit = ['year', 'month', 'day', 'hour', 'minute', 'second']
        self.prompt = 'not start calculating yet'
        self.lasted = []
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    def __add__(self, other):
        prompt = 'the total running time is '
        result = []
        for index in range(6):
            result.append(self.lasted[index]+other.lasted[index])
            if result[index]:
                prompt += (str(result[index])+self.unit[index])
        return prompt
    
    # star calculate
    def start(self):
        self.begin = t.localtime()
        self.prompt = 'tip: please stop calculating first'
        print('star calculate')

    # stop calculate
    def stop(self):
        if not self.begin:
            print('tip: please start calculating first')
        else:
            self.end = t.localtime()
            self._calc()
            print('stop calculating')

    # calculate the running time
    def _calc(self):
        self.lasted = []
        self.prompt = 'the total running time is '
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index])+self.unit[index])
        # initialize for next turn
        self.begin = 0
        self.end = 0
