
class Cat:
    def __init__(self, colour: str):
        self.colour = colour

    def meow(self, word: str) -> str:
        """Method that makes the cat meow

        Args:
            word (str): word to meow

        Returns (str): meowed word
        """
        return f"meow {word}"

if __name__ == "__main__":
    print("hello world")
