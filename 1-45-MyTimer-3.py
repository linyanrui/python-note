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
    
    # star calculate
    def start(self):
        if not self.begin:
            self.begin = t.localtime()
            self.prompt = 'tip: please stop calculating first'
            print('star calculate')
        else:
            print('tip: please stop calculating first')

    # stop calculate
    def stop(self):
        if not self.begin:
            print('tip: please zhenglei start calculating first')
        else:
            self.end = t.localtime()
            self._calc()
            print('stop calculating')
            self.begin = 0

    # calculate the running time
    def _calc(self):
        self.lasted = []
        self.prompt = 'the total running time is '
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index])+self.unit[index])
