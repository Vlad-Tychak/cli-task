# -*- coding: utf-8 -*-
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # Масть карти
        self.rank = rank  # Номер/ранг карти

    def __str__(self):
        return f"{self.rank} {self.suit}"


class Deck:
    # Масти карт українською
    suits = ['Черви', 'Бубни', 'Трефи', 'Піки']
    # Ранги карт українською
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    def __init__(self):
        # Створення колоди карт
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()  # Перемішування колоди при створенні

    def shuffle(self):
        """Перемішує карти в колоді."""
        random.shuffle(self.cards)

    def get_card_by_position(self, position):
        """Отримати карту за номером розташування в колоді (починаючи з 1)."""
        if 1 <= position <= len(self.cards):
            return self.cards[position - 1]
        else:
            raise ValueError("Неправильна позиція!")

    def draw_one_card(self):
        """Видає одну карту з колоди."""
        if self.cards:
            return self.cards.pop(0)
        else:
            raise ValueError("Колода порожня!")

    def draw_six_cards(self):
        """Видає шість карт з колоди."""
        if len(self.cards) >= 6:
            return [self.draw_one_card() for _ in range(6)]
        else:
            raise ValueError("У колоді недостатньо карт!")

    def show_all_cards(self):
        """Виводить всі карти в колоді."""
        return [str(card) for card in self.cards]


# Функція для виконання команд
def interactive_mode(deck):
    print("Команди:\n"
          "1. show_all - Вивести всі карти\n"
          "2. get_card - Взяти карту за позицією\n"
          "3. shuffle - Перемішати колоду\n"
          "4. draw_one - Взяти одну карту\n"
          "5. draw_six - Взяти шість карт\n"
          "6. show_remaining - Вивести залишок колоди\n"
          "7. exit - Вийти з програми\n")
    
    while True:
        command = input("Введіть команду: ").strip().lower()
        
        try:
            if command == "show_all":
                print("Всі карти в колоді:")
                print(deck.show_all_cards())
            elif command == "get_card":
                position = int(input("Введіть номер позиції карти: "))
                print(f"Карта на позиції {position}: {deck.get_card_by_position(position)}")
            elif command == "shuffle":
                deck.shuffle()
                print("Колода перемішана!")
            elif command == "draw_one":
                print(f"Взято одну карту: {deck.draw_one_card()}")
            elif command == "draw_six":
                print("Взято шість карт:")
                print([str(card) for card in deck.draw_six_cards()])
            elif command == "show_remaining":
                print("Залишок колоди:")
                print(deck.show_all_cards())
            elif command == "exit":
                print("Вихід з програми.")
                break
            else:
                print("Невідома команда. Спробуйте ще раз.")
        except ValueError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print(f"Щось пішло не так: {e}")


# Демонстрація роботи класу
if __name__ == "__main__":
    deck = Deck()
    interactive_mode(deck)