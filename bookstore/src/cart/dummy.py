class SomeSingleton(object):
    __instance__ = None
    def __new__(cls, *args,**kwargs):
        if SomeSingleton.__instance__ is None:
            SomeSingleton.__instance__ = object.__new__(cls)
        return SomeSingleton.__instance__

    def __init__(self,f=0,y=0):
        self.f = f
        self.y= y

    def some_func(self,arg):
        pass


if __name__== "__main__":
    s = SomeSingleton("343","43443")
    