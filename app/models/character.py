from dataclasses import dataclass, field
from typing import List
import random

@dataclass
class Stats:
    strength: int = 10
    agility: int = 10
    intelligence: int = 10
    constitution: int = 10

@dataclass
class Character:
    name: str
    char_class: str  # "warrior", "mage", "rogue"
    level: int = 1
    experience: int = 0
    stats: Stats = field(default_factory=Stats)
    inventory: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.max_hp = self.stats.constitution * 10
        self.current_hp = self.max_hp
        self.gold = 50

    @property
    def is_alive(self) -> bool:
        return self.current_hp > 0

    def attack_damage(self) -> int:
        base = self.stats.strength * 2
        crit = random.random() < 0.1  # %10 kritik şans
        return base * 2 if crit else base

    def gain_experience(self, amount: int):
        self.experience += amount
        xp_needed = self.level * 100
        if self.experience >= xp_needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.stats.strength += 2
        self.stats.constitution += 2
        self.max_hp = self.stats.constitution * 10
        self.current_hp = self.max_hp
        print(f"⬆️ {self.name} seviye atladı! Seviye {self.level}")