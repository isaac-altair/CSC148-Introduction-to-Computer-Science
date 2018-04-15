class TipJar(object):
    def __init__(self):
        self._amount = 0

    def tip(self, amount):
        self._amount = self._amount + amount

    def get_amount(self):
        return self._amount

if __name__ == "__main__":
    jar = TipJar()
    print(jar.get_amount())
    jar.tip(1.25)
    jar.tip(2)
    print(jar.get_amount())
