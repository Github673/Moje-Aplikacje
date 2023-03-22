import os

def list_files(path):
    # Wyświetlenie listy plików i folderów w danym folderze
    files = os.listdir(path)
    for file in files:
        print(file)

def main():
    # Początkowa ścieżka, od której zaczynamy eksplorację
    current_path = "."
    
    while True:
        # Wyświetlenie bieżącej ścieżki i listy plików/folderów
        print("Current path:", current_path)
        list_files(current_path)
        
        # Pobranie wyboru użytkownika
        user_input = input("Enter folder name or '..' to go up:")
        
        # Przejście do folderu o nazwie podanej przez użytkownika
        if os.path.isdir(os.path.join(current_path, user_input)):
            current_path = os.path.join(current_path, user_input)
        
        # Przejście do folderu nadrzędnego
        elif user_input == "..":
            current_path = os.path.dirname(current_path)
        
        # Zakończenie programu, jeśli użytkownik wpisze 'exit'
        elif user_input == "exit":
            break
        
        # W przypadku nieprawidłowego wpisu przez użytkownika, wyświetlenie komunikatu o błędzie
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
