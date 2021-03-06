import types
import Flyweight as F


class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self, flyweight_factory):
        print(self.name)
        # print(self)
        return F.printing("flyweight execution example strat", flyweight_factory)


def replace1(self, flyweight_factory):
    print('Replacement Strategy 1')
    # print(self)
    return F.printing("flyweight Replacement 1", flyweight_factory)


def replace2(self, flyweight_factory):
    print('Replacement Strategy 2')
    # print(self)
    return F.printing("flyweight Replacement 2", flyweight_factory)


def test():
    fl = F.FlyweightFactory()
    strat0 = StrategyExample()

    strat1 = StrategyExample(replace1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(replace2)
    strat2.name = 'Strategy Example 2'

    strat0.execute(fl)
    strat1.execute(fl)
    strat2.execute(fl)


if __name__ == '__main__':
    test()
