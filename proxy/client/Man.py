from proxy.libraray.Developer import Developer
from proxy.libraray.ProxyDeveloper import ProxyDeveloper


class Man(Developer):
    def __new__(cls):
        return ProxyDeveloper(super().__new__(cls))

    def develop(self):
        print("JS로 개발한다.")
