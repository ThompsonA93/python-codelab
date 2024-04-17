
class Singleton:
    _self = None

    def __new__(Singleton):
        if Singleton._self is None:
            Singleton._self = super().__new__(Singleton)
        return Singleton._self



s1 = Singleton()
s2 = Singleton()

print("s1 is equal to s2:", s1 == s2)