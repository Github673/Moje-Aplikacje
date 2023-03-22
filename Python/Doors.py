import random

# Utwórz klasę drzwi
class Door:
    def __init__(self, number, is_prize, is_locked, hint):
        self.number = number
        self.is_prize = is_prize
        self.is_locked = is_locked
        self.hint = hint

    # Funkcja zwracająca podpowiedź
    def get_hint(self):
        return self.hint

    # Funkcja zwracająca informację, czy drzwi są zamknięte
    def is_locked(self):
        return self.is_locked

    # Funkcja odblokowująca drzwi
    def unlock(self):
        self.is_locked = False

    # Funkcja zwracająca informację, czy drzwi są nagrodą
    def is_prize(self):
        return self.is_prize

# Utwórz klasę poziomu
class Level:
    def __init__(self, doors):
        self.doors = doors

    # Funkcja sprawdzająca, czy gracz wygrał
    def has_won(self):
        for door in self.doors:
            if door.is_prize and door.is_locked:
                return False
        return True

# Utwórz funkcję tworzącą poziom
def create_level():
    doors = []
    prize_door = random.randint(0, 9)
    for i in range(10):
        hint = "Drzwi " + str(i) + " to "
        if i == prize_door:
            doors.append(Door(i, True, True, hint + "nagroda"))
        else:
            doors.append(Door(i, False, True, hint + "zwykłe"))
    return Level(doors)

# Utwórz główną funkcję gry
def play_game():
    level = create_level()
    while not level.has_won():
        print("Wybierz drzwi:")
        for door in level.doors:
            if door.is_locked:
                print(door.number)
        door_choice = int(input())
        level.doors[door_choice].unlock()
        print(level.doors[door_choice].get_hint())
    print("Gratulacje! Wygrałeś!")

# Rozpocznij grę
play_game()
