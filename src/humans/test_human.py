class TestHuman:
    def test_baby_hello(self, human):
        assert human.baby_hello() == "Googoo gaga gaga da gaagaa"

    def test_hello(self, human):
        assert human.hello() == "Hello, I am a normal human!"
