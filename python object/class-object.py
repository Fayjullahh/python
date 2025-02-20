class Atm:
    def __init__(self):
        self.pin = ''
        self.balence = 0
        self.menu()
    def menu(self):
        user_input = input("""Press the button for operation:
                           1. Press 1 to create pin
                           2. Press 2 to deposite
                           3. press 3 to withdraw
                           4. press 4 to check balence
                           5. press 5 to exit
                           """)
        if user_input == '1':
            print("Created password")