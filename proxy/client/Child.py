from proxy.libraray.Developer import Developer
from proxy.libraray.ProxyDeveloper import ProxyDeveloper


class Child(Developer):
    def __new__(cls):
        return ProxyDeveloper(super().__new__(cls))

    def develop(self):
        print("스크래치로 개발한다.")
