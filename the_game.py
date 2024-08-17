from random import randint
class Rand:
    def __init__(self, decount, answer, capital, stavka):
        self.decount = decount
        self.answer = answer
        self.capital = capital
        self.stavka = stavka

    def Gambling(self, decount, answer, capital, stavka):
        decount = randint(1, 3)
        stavka = 1000
        for i in range(1, 31):
            if capital >= 12000:
                break
        answer = input(int())
        if answer != decount:
            print(f'неправильно! правильный ответ: {decount}')
            capital -= stavka
            print(f'твой счет: {capital}')
            stavka -= stavka
            print(f'твоя ставка уменьшилась: {stavka}')
        elif answer == decount:
            print(f'правильно ответ: {decount}')
            capital += stavka
            print(f'твой счет: {capital}')
            stavka += stavka
            print(f'твоя ставка: {stavka}')

player = Rand
player.Gambling(3, 3, 1000, 1000, 1000)
