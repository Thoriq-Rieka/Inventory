

class normal_item:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.count: int = 1

    def set_count(self, count: int) -> None:
        self.count: int = count

class consumable_item:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight
        self.count: int = 1

    def set_count(self, count: int) -> None:
        self.count = count

class gun_item:
    def __init__(self, name: str, weight: float, fire_rate: float, mag_size: int, damage: float) -> None:
        self.name = name
        self.weight = weight
        self.fire_rate = fire_rate
        self.mag_size = mag_size
        self.damage = damage
        self.count = 1