from facade.Player import Player


class SpringConcert:
    def start_concert(self):
        p = Player("바이올린")
        # p.prepare()
        # p.ing()
        # p.end()
        # p.curtain_call()
        p.play()

        print("봄... 이었습니다.")
