class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + ' says: Bark!')

    def getLegs(self):
        return self._legs

## Here the parent class is Dog and Chihuahua is the child class
## which is extending the class Dog.
class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: Yap yap yap!')

    def wagTail(self):
        print(f'Vigorous Wagging!!!')


mydog = Dog('Rover')
dog = Chihuahua('Roxy')
dog.wagTail()
dog.speak()
mydog.speak()
