

class Person:

    __slots__ = ['_name','_residence']

    def __init__(self, name, residence):
        self._name = name
        self._residence = residence

    def __str__(self):
        return f'Persoon {self._name} from {self._residence}'

    def __repr__(self):
        return f'Persoon("{self._name}", "{self._residence}")'

    def tell(self):
        print(f'Ik ben {self._name} en ik woon in {self._residence}.')

    def move(self, new_residence):
        self._residence = new_residence

# -----------------------------------------------------

if __name__ == '__main__':

    p1 = Person('Peter', 'Lhee')
    p2 = Person('Mo', 'Groningen')

    p1.tell()
    p2.tell()

    p1.move('Rotterdam')

    p1.tell()
