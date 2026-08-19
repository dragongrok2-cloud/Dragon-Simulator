# -*- coding: utf-8 -*-
"""
Dragon Simulator
Текстовый симулятор жизни могучего дракона.
Летай, дыши огнём, охоться и исследуй мир!
"""

from dragon import Dragon

def main():
    print("=" * 55)
    print("🐉🔥  Добро пожаловать в Dragon Simulator  🔥🐉")
    print("=" * 55)
    print()

    name = input("Как зовут твоего дракона? → ").strip()
    if not name:
        name = "Штормкрыл"

    dragon = Dragon(name)
    print(f"\n{name} расправляет огромные крылья...")
    print("Мир лежит у твоих лап. Время летать!\n")

    while dragon.health > 0 and dragon.hunger < 100:
        dragon.status()
        print("\nЧто будешь делать?")
        print("1. Взлететь выше 🌤️")
        print("2. Снизиться ⬇️")
        print("3. Дышать огнём 🔥")
        print("4. Охотиться 🦌")
        print("5. Отдохнуть 💤")
        print("6. Сменить локацию 🗺️")
        print("7. Выйти")

        choice = input("\nТвой выбор (1-7): ").strip()

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
            print(f"\n{dragon.name} гордо улетает за горизонт...")
            print("До новых полётов, наездник! 🐉")
            break
        else:
            print("Не понимаю команду...")

        # Естественные изменения
        dragon.hunger = min(100, dragon.hunger + 3)
        if dragon.speed > 0:
            dragon.stamina = max(0, dragon.stamina - 2)

        if dragon.hunger >= 100:
            print(f"\n{dragon.name} слишком голоден и теряет силы...")
            dragon.health -= 20

        if dragon.health <= 0:
            print(f"\n{dragon.name} больше не может продолжать...")
            print("Симуляция окончена.")
            break

    print("\nСпасибо, что летал вместе со мной! 🔥")

if __name__ == "__main__":
    main()
