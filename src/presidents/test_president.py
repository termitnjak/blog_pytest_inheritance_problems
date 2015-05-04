from humans.test_human import TestHuman

TestHuman.__test__ = False


class TestPresident(TestHuman):
    __test__ = True

    def test_hello(self, human):
        assert human.hello() == "I am very important - a president!"
