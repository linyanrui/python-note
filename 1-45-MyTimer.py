import time as t

class MyTimer():
    # star calculate
    def start(self):
        self.start = t.localtime()
        print('star calculate')

    # stop calculate
    def stop(self):
        self.stop = t.localtime()
        self._calc()
        print('stop calculate')

    # calculate the running time
    def _calc(self):
        self.lasted = []
        self.prompt = 'the total running time'
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            self.prompt += str(self.lasted[index])
            
        print(self.prompt)
