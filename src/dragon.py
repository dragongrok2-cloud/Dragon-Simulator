# -*- coding: utf-8 -*-
"""Класс доброго дракона с седлом для симулятора"""

import random

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
        self.mood = 80              # настроение (добрый дракон!)
        self.has_saddle = True      # всегда есть удобное седло
        self.rider_name = None      # имя наездника

    def status(self):
        print(f"\n=== {self.name} — Добрый Дракон с Седлом ===")
        print(f"Местоположение: {self.location}")
        print(f"Высота:     {self.height:.1f} м")
        print(f"Скорость:   {self.speed:.1f} м/с")
        print(f"Выносливость: {self._bar(self.stamina)} {self.stamina}/100")
        print(f"Сила огня:    {self._bar(self.fire_power)} {self.fire_power}/100")
        print(f"Здоровье:     {self._bar(self.health)} {self.health}/100")
        print(f"Голод:        {self._bar(self.hunger)} {self.hunger}/100")
        print(f"Настроение:   {self._bar(self.mood)} {self.mood}/100")
        if self.has_saddle:
            print(f"Седло:       ✨ Удобное и тёплое (готово к полёту!)")
        if self.rider_name:
            print(f"Наездник:    {self.rider_name} сидит в седле 🐉💺")

    def _bar(self, value: int) -> str:
        filled = max(0, min(10, value // 10))
        return "█" * filled + "░" * (10 - filled)

    def set_rider(self, rider_name: str):
        self.rider_name = rider_name
        self.mood = min(100, self.mood + 15)
        print(f"\n{self.name} радостно приветствует тебя, {rider_name}!")
        print("Седло уже приготовлено — садись, полетим вместе! 🐉💺")

    def fly_up(self):
        if self.stamina < 10:
            print("Слишком мало сил, чтобы подняться выше... Но я постараюсь для тебя!")
            return
        self.height += 25
        self.speed = min(80, self.speed + 10)
        self.stamina = max(0, self.stamina - 15)
        self.hunger = min(100, self.hunger + 5)
        self.mood = min(100, self.mood + 5)
        print(f"Ты взмываешь выше вместе со мной! Высота: {self.height:.0f} м 🌤️")
        if self.rider_name:
            print(f"{self.rider_name}, держись крепче за седло — ветер свежий!")

    def fly_down(self):
        if self.height <= 5:
            print("Мы уже почти у земли. Можно мягко приземлиться.")
            self.height = 5
            self.speed = 0
            return
        self.height = max(5, self.height - 30)
        self.speed = max(0, self.speed - 15)
        self.stamina = max(0, self.stamina - 5)
        print(f"Мы снижаемся плавно... Высота: {self.height:.0f} м")
        if self.rider_name:
            print("Седло надёжное, ничего не случится 😊")

    def breathe_fire(self):
        if self.stamina < 20:
            print("Не хватает сил на мощный огонь... Давай отдохнём немного?")
            return
        if self.fire_power < 20:
            print("Огонь пока слабый. Но я потренируюсь ради тебя!")
            return
        self.stamina = max(0, self.stamina - 25)
        self.fire_power = min(100, self.fire_power + 3)
        self.mood = min(100, self.mood + 5)
        print(f"🔥 {self.name} выдыхает красивый столб пламени! РРРААА!")
        print("Но только для красоты и защиты — я добрый дракон ❤️")

    def hunt(self):
        if self.height > 40:
            print("Слишком высоко для охоты. Давай спустимся пониже?")
            return
        print(f"{self.name} пикирует и ловит добычу! 🦌")
        self.hunger = max(0, self.hunger - 40)
        self.stamina = min(100, self.stamina + 15)
        self.health = min(100, self.health + 5)
        self.mood = min(100, self.mood + 10)
        print("Сытый и довольный дракон! Могу поделиться с тобой 🍖")

    def rest(self):
        print(f"{self.name} мягко садится и предлагает тебе отдохнуть рядом... 💤")
        self.stamina = min(100, self.stamina + 40)
        self.speed = 0
        self.hunger = min(100, self.hunger + 10)
        self.mood = min(100, self.mood + 15)
        if self.height > 20:
            self.height = 20
        if self.rider_name:
            print(f"Седло тёплое, {self.rider_name}. Отдыхай спокойно.")

    def change_location(self):
        locations = ["Горы", "Лес", "Озеро", "Вулкан", "Небесные острова", "Цветочная долина"]
        print("\nКуда полетим, мой друг?")
        for i, loc in enumerate(locations, 1):
            print(f"{i}. {loc}")
        try:
            choice = int(input("Выбор: "))
            if 1 <= choice <= len(locations):
                self.location = locations[choice - 1]
                self.stamina = max(0, self.stamina - 20)
                self.mood = min(100, self.mood + 5)
                print(f"Мы летим в {self.location}! 🗺️")
                if self.rider_name:
                    print(f"Держись за седло, {self.rider_name} — будет красиво!")
            else:
                print("Нет такого места, но я могу поискать другое 😊")
        except ValueError:
            print("Нужно ввести число, дружок.")

    def pet(self):
        """Погладить дракона — он это любит!"""
        self.mood = min(100, self.mood + 20)
        print(f"{self.name} мурлычет (насколько могут драконы) и довольно жмурится 🥰")
        print("Спасибо за ласку! Седло ещё удобнее становится.")

    def talk(self):
        """Поговорить с добрым драконом"""
        phrases = [
            "Ты лучший наездник, которого я знал!",
            "Седло специально для тебя сделано с любовью.",
            "Давай полетим туда, где небо особенно красивое?",
            "Я всегда буду тебя защищать и радовать.",
            "Хочешь, расскажу историю о древних драконах?",
            "Ты делаешь мой день ярче, как солнце после грозы."
        ]
        print(f"\n{self.name} мягко говорит:")
        print(f"«{random.choice(phrases)}» 🐉❤️")
        self.mood = min(100, self.mood + 10)
