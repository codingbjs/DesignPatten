from proxy.client.Child import *
from proxy.client.Man import *
from proxy.client.Woman import *

if __name__ == '__main__':
    man = Man()
    man.develop()
    print()

    woman = Woman()
    woman.develop()
    print()

    child = Child()
    child.develop()
    print()
