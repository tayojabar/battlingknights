from dataclasses import (dataclass, field)

@dataclass
class Cell:
    x: int
    y: int
    knight: dict = None
    items: list = field(default_factory=list)

    def __repr__(self):
        """ Similar to the Java toString() method"""
        return '[{}, {}]'.format(self.x, self.y)

    def to_json(self):
        return [self.x, self.y]