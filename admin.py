class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self, username, password):
        return self.username == username and self.password == password

    def admin_dashboard(self):
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")

            if self.login(username, password):
                print("Login Successful!")
                break
            else:
                print("Invalid credentials. Please try again.")
