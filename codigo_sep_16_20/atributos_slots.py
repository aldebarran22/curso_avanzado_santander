
class S():

    __slots__ = ['val']

    def __init__(self, v):
        self.val = v


x = S(42)
print(x.val)
#print(x.__dict__)

x.new = "not possible"