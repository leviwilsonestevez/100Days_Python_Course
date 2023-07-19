class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.size = kwargs.get("size")


car = Car(make="Nissan", model="GTR")
car2 = Car(make="Honda")
car3 = Car(make="Honda", model="Prius", color="White", size="big")
print(car, car2, car3)


# Interesting exercise
def add(a, *args, **kw) -> None:
    print(a, args, kw)


print(add(4, 7, 3, 0, x=10, y=64))
# it will print 4 (7, 3, 0) {'x': 10, 'y': 64}
