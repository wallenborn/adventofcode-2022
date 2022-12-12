import re
import math


class Monkey:

    def __init__(self, item_line):
        m = re.match(".*Starting items: ([\\d,\\s]+)", item_line)
        [item_string] = m.groups()
        self.items = list(map(int, item_string.split(",")))
        self.inspector_function = None
        self.test_function = None
        self.if_true = None
        self.if_false = None
        self.base = None
        self.num_inspections = 0

    def set_inspector_function(self, s):
        m1 = re.match(".*new = old \\* (\\d+)", s)
        m2 = re.match(".*new = old \\+ (\\d+)", s)
        m3 = re.match(".*new = old \\* old", s)
        if m1:
            [i] = m1.groups()
            i = int(i)
            self.inspector_function = lambda x: x * i
        elif m2:
            [i] = m2.groups()
            i = int(i)
            self.inspector_function = lambda x: x + i
        elif m3:
            self.inspector_function = lambda x: x * x
        else:
            print("Can't parse operator function: %s" % (s))

    def inspect(self, n):
        self.num_inspections += 1
        return self.inspector_function(n)

    def set_test_function(self, s):
        m = re.match(".*divisible by (\\d+)", s)
        [i] = m.groups()
        i = int(i)
        self.base = i
        self.test_function = lambda x: x % i == 0

    def test(self, n):
        return self.test_function(n)

    def set_if_true(self, s):
        m = re.match(".*throw to monkey (\\d+)", s)
        [i] = m.groups()
        self.if_true = int(i)

    def set_if_false(self, s):
        m = re.match(".*throw to monkey (\\d+)", s)
        [i] = m.groups()
        self.if_false = int(i)

    @staticmethod
    def relax(n):
        return math.floor(n / 3)

    def modulo(self, n):
        return n % self.base

    def throw_to(self, n):
        if self.test(n):
            return self.if_true
        else:
            return self.if_false