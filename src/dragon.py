# -*- coding: utf-8 -*-
"""Класс дракона для симулятора"""

class Dragon:
    def __init__(self, name: str):
        self.name = name
        self.height = 10.0          # метры над землёй
        self.speed = 0.0            # скорость полёта
        self.stamina = 100          # выносливость
        self.fire_power = 50        # сила огня
        self.hunger = 30
        self.health = 100
        self.location = "Горы"

    def status(self):
        print(f"\n=== {self.name} — Могучий Дракон ===")
        print(f"Местоположение: {self.location}")
        print(f"Высота:     {self.height:.1f} м")
        print(f"Скорость:   {self.speed:.1f} м/с")
        print(f"Выносливость: {self._bar(self.stamina)} {self.stamina}/100")
        print(f"Сила огня:    {self._bar(self.fire_power)} {self.fire_power}/100")
        print(f"Здоровье:     {self._bar(self.health)} {self.health}/100")
        print(f"Голод:        {self._bar(self.hunger)} {self.hunger}/100")

    def _bar(self, value: int) -> str:
        filled = max(0, min(10, value // 10))
        return "█" * filled + "░" * (10 - filled)

    def fly_up(self):
        if self.stamina < 10:
            print("Слишком мало сил, чтобы подняться выше!")
            return
        self.height += 25
        self.speed = min(80, self.speed + 10)
        self.stamina = max(0, self.stamina - 15)
        self.hunger = min(100, self.hunger + 5)
        print(f"Ты взмываешь выше! Высота: {self.height:.0f} м 🌤️")

    def fly_down(self):
        if self.height <= 5:
            print("Ты уже почти у земли.")
            self.height = 5
            self.speed = 0
            return
        self.height = max(5, self.height - 30)
        self.speed = max(0, self.speed - 15)
        self.stamina = max(0, self.stamina - 5)
        print(f"Ты снижаешься... Высота: {self.height:.0f} м")

    def breathe_fire(self):
        if self.stamina < 20:
            print("Не хватает сил на мощный огонь...")
            return
        if self.fire_power < 20:
            print("Огонь слишком слабый. Нужно потренироваться!")
            return
        self.stamina = max(0, self.stamina - 25)
        self.fire_power = min(100, self.fire_power + 3)
        print(f"🔥 {self.name} выдыхает мощный столб пламени! РРРААА!")
        print("Всё вокруг осветилось огнём...")

    def hunt(self):
        if self.height > 40:
            print("Слишком высоко для охоты. Спустись пониже.")
            return
        print(f"{self.name} пикирует и ловит добычу! 🦌")
        self.hunger = max(0, self.hunger - 40)
        self.stamina = min(100, self.stamina + 15)
        self.health = min(100, self.health + 5)
        print("Сытый и довольный дракон!")

    def rest(self):
        print(f"{self.name} садится на скалу и отдыхает... 💤")
        self.stamina = min(100, self.stamina + 40)
        self.speed = 0
        self.hunger = min(100, self.hunger + 10)
        if self.height > 20:
            self.height = 20

    def change_location(self):
        locations = ["Горы", "Лес", "Озеро", "Вулкан", "Небесные острова"]
        print("\nКуда полетим?")
        for i, loc in enumerate(locations, 1):
            print(f"{i}. {loc}")
        try:
            choice = int(input("Выбор: "))
            if 1 <= choice <= len(locations):
                self.location = locations[choice - 1]
                self.stamina = max(0, self.stamina - 20)
                print(f"Ты летишь в {self.location}! 🗺️")
            else:
                print("Нет такого места.")
        except ValueError:
            print("Нужно ввести число.")
