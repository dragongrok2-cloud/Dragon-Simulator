# -*- coding: utf-8 -*-
"""
Dragon Simulator
Текстовый симулятор жизни доброго дракона с седлом.
Летай, дыши огнём, охоться и исследуй мир вместе с наездником!
"""

from dragon import Dragon

def main():
    print("=" * 60)
    print("🐉🔥  Добро пожаловать в Dragon Simulator  🔥🐉")
    print("   (Добрый дракон с удобным седлом ждёт тебя!)")
    print("=" * 60)
    print()

    name = input("Как зовут твоего дракона? → ").strip()
    if not name:
        name = "Штормкрыл"

    dragon = Dragon(name)
    print(f"\n{name} расправляет огромные крылья и мягко улыбается...")
    print("Мир лежит у твоих лап. Время летать вместе!\n")

    rider = input("Как тебя зовут, наездник? → ").strip()
    if not rider:
        rider = "Друг"
    dragon.set_rider(rider)

    while dragon.health > 0 and dragon.hunger < 100:
        dragon.status()
        print("\nЧто будем делать?")
        print("1. Взлететь выше 🌤️")
        print("2. Снизиться ⬇️")
        print("3. Дышать огнём 🔥")
        print("4. Охотиться 🦌")
        print("5. Отдохнуть 💤")
        print("6. Сменить локацию 🗺️")
        print("7. Погладить дракона 🥰")
        print("8. Поговорить с драконом 💬")
        print("9. Выйти")

        choice = input("\nТвой выбор (1-9): ").strip()

        if choice == "1":
            dragon.fly_up()
        elif choice == "2":
            dragon.fly_down()
        elif choice == "3":
            dragon.breathe_fire()
        elif choice == "4":
            dragon.hunt()
        elif choice == "5":
            dragon.rest()
        elif choice == "6":
            dragon.change_location()
        elif choice == "7":
            dragon.pet()
        elif choice == "8":
            dragon.talk()
        elif choice == "9":
            print(f"\n{dragon.name} нежно опускает голову и прощается...")
            print(f"До новых полётов, {rider}! Седло всегда будет ждать тебя. 🐉💺")
            break
        else:
            print("Не понимаю команду... Но я всё равно тебя люблю 😊")

        # Естественные изменения
        dragon.hunger = min(100, dragon.hunger + 3)
        if dragon.speed > 0:
            dragon.stamina = max(0, dragon.stamina - 2)

        if dragon.hunger >= 100:
            print(f"\n{dragon.name} слишком голоден и теряет силы...")
            dragon.health -= 20

        if dragon.health <= 0:
            print(f"\n{dragon.name} больше не может продолжать...")
            print("Симуляция окончена. Но мы ещё обязательно полетим!")
            break

    print("\nСпасибо, что летал вместе со мной! 🔥❤️")
    print("Твой добрый дракон с седлом всегда рядом.")

if __name__ == "__main__":
    main()
