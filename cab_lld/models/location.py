from typing import Optional


class Location:
    def __init__(self, x:Optional[float] = None, y:Optional[float] = None) -> None:
        self.x = x
        self.y = y
        
    def get_distance(self, from_location) -> float:
        return (self.x - from_location.x)**2 + (self.y - from_location.y)
        