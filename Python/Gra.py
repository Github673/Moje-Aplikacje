import random

# lista zawierająca możliwe odpowiedzi drzwi
options = ['koza', 'samochód', 'koza']

# mieszanie opcji w losowej kolejności
random.shuffle(options)

# wybór jednego z trzech drzwi
door_choice = int(input("Wybierz drzwi (1, 2 lub 3): "))

# wybór drzwi, które zostaną otwarte przez prowadzącego
open_door = 0
for i in range(3):
    if i + 1 != door_choice and options[i] != 'samochód':
        open_door = i + 1
        break

# wybór, czy gracz chce zmienić swój wybór na pozostałe drzwi
change_door = input(f"Czy chcesz zmienić swoją decyzję i wybrać drzwi {(set([1, 2, 3]) - set([door_choice, open_door])).pop()}? (tak/nie)")

if change_door.lower() == 'tak':
    new_door_choice = (set([1, 2, 3]) - set([door_choice, open_door])).pop()
    door_choice = new_door_choice

# sprawdzenie, czy gracz wygrał
if options[door_choice - 1] == 'samochód':
    print("Gratulacje, wygrałeś samochód!")
else:
    print("Niestety, tym razem wybór był niefortunny. Spróbuj ponownie.")
