class A():
    def __init__(self):
        self.pub = 'pub'
        self._prot = 'prot'
        self.__priv = 'priv'

class B(A):
    def dowork(self):
        print('Public', self.pub)
        print('Prot ', self._prot)
        print('Priv ', self._A__priv)

b = B()
print('The items is ', b.dowork())

class MixinA():
    def printter(self):
        super().printer()
        pass

class (MIxina, Mixinb, c):
    self.printer()


def add(x,y):
    return x / y


@pytest
@pytest.mark.parameterize(
    (2,4, 6, True),
    (5,6,11, True),
    (2, 0, _, False)
)
def test_add(a,b,c,d):
    assert add(a,b) == c
    
