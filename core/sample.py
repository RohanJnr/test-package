class Sample:
    def __init__(self, num: int) -> None:
        self.num = num

    def __add__(self, other: "Sample") -> int:
        return self.num + other.num
