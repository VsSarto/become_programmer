
class Words:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    def introduce_self(self):
        print(f'{self.x} , {self.y}')


w1 = Words("Hello" ,"World!")

w1.introduce_self()
