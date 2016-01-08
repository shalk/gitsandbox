class func():
    def __init__(self,state):
        self.state = state

    def __call__(self,label):
        print(label,self.state)
        self.state += 1
F=func(1)
G=func(10)
G('AA')
G('BB')
F('aa')
F('bb')



