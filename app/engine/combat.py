from app.models.character import Character
from app.models.enemy import Enemy
import random

class Combat:
    def __init__(self, character: Character, enemy_type: str):
        self.character = character
        self.enemy = Enemy.from_template(enemy_type)
        self.log = []

    def run(self) -> dict:
        self.log.append(f"⚔️ {self.character.name} vs {self.enemy.name} başladı!")

        round_num = 1
        while self.character.is_alive and self.enemy.is_alive:
            self._player_turn()
            if self.enemy.is_alive:
                self._enemy_turn()
            round_num += 1

            if round_num > 50:  # sonsuz döngü koruması
                break

        return self._resolve()

    def _player_turn(self):
        dmg = self.character.attack_damage()
        self.enemy.hp -= dmg
        self.log.append(f"🗡️ {self.character.name} → {dmg} hasar verdi. Düşman HP: {max(0, self.enemy.hp)}")

    def _enemy_turn(self):
        dodge_chance = self.character.stats.agility * 0.02  # %2 * çeviklik
        if random.random() < dodge_chance:
            self.log.append(f"💨 {self.character.name} saldırıyı savuşturdu!")
            return
        dmg = self.enemy.attack
        self.character.current_hp -= dmg
        self.log.append(f"💥 {self.enemy.name} → {dmg} hasar verdi. HP: {max(0, self.character.current_hp)}")

    def _resolve(self) -> dict:
        if self.character.is_alive:
            self.character.gain_experience(self.enemy.xp_reward)
            self.character.gold += self.enemy.gold_reward
            self.log.append(f"🏆 Zafer! +{self.enemy.xp_reward} XP, +{self.enemy.gold_reward} altın")
            return {"result": "win", "log": self.log, "character": self._char_state()}
        else:
            self.log.append(f"💀 {self.character.name} yenildi...")
            return {"result": "lose", "log": self.log}

    def _char_state(self) -> dict:
        c = self.character
        return {"name": c.name, "level": c.level, "hp": c.current_hp, "gold": c.gold}