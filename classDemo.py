class Myclass:

    l=10
    h=20

    def __init__(self):
        print("init")

    def dis(self,l,h):
        print(l,h)

    def __call__(self, *args, **kwargs):
        for j in args:
            print(j)
        for i,k in kwargs.items():
            print(i,k)
obj=Myclass()
obj.dis(10,20)
obj.__call__((1,2,3,4),name=10,age=20,id=30,uid=40)







