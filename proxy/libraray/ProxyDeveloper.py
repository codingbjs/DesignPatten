from proxy.libraray.Developer import Developer


class ProxyDeveloper(Developer):
    def __init__(self, dev):
        self.dev = dev

    def develop(self):
        print("출근 카드를 찍는다.")

        try:
            self.dev.develop()
        except:
            print("쉬는 날이 었다")
        finally:
            print("집에 간다")
