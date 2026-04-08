from dataclasses import dataclass
import random

ENEMY_TEMPLATES = {
    "goblin":   {"hp": 30,  "atk": 8,  "xp": 25,  "gold": 10},
    "orc":      {"hp": 60,  "atk": 15, "xp": 60,  "gold": 25},
    "dragon":   {"hp": 200, "atk": 40, "xp": 300, "gold": 150},
    "skeleton": {"hp": 25,  "atk": 10, "xp": 30,  "gold": 8},
}

@dataclass
class Enemy:
    name: str
    hp: int
    attack: int
    xp_reward: int
    gold_reward: int

    @classmethod
    def from_template(cls, enemy_type: str) -> "Enemy":
        t = ENEMY_TEMPLATES[enemy_type]
        # Biraz rastgelelik ekle
        return cls(
            name=enemy_type.capitalize(),
            hp=t["hp"] + random.randint(-5, 5),
            attack=t["atk"] + random.randint(-2, 2),
            xp_reward=t["xp"],
            gold_reward=t["gold"],
        )

    @property
    def is_alive(self) -> bool:
        return self.hp > 0