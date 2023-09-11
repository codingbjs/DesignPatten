from proxy.libraray.Developer import Developer
from proxy.libraray.ProxyDeveloper import ProxyDeveloper


class Woman(Developer):
    def __new__(cls):
        return ProxyDeveloper(super().__new__(cls))

    def develop(self):
        print("파이썬으로 개발한다.")
