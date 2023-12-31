class Player:
    def __init__(self, instrument):
        self.instrument = instrument

    def __prepare(self):
        print(self.instrument + "를 연주할 준비 중 입니다.")

    def __ing(self):
        print(self.instrument + "를 연주 중 입니다.")

    def __end(self):
        print(self.instrument + "를 연주했습니다.")

    def __curtain_call(self):
        print("커튼콜을 진행합니다.")

    # Facade patten
    # 객체의 자율성 : 객체가 역할 및 책임을 수행하는 과정을 객체가 자율적으로 결정하도록 코드를 작성
    def play(self):
        self.__prepare()
        self.__ing()
        self.__end()
        self.__curtain_call()
