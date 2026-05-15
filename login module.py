saved_username = "admin"
saved_password = "1234"
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "" or password == "":
        print("Username and password cannot be empty.")
    elif username == saved_username and password == saved_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
def logout():
    print("Logged out successfully.")
is_logged_in = login()
if is_logged_in:
    choice = input("Do you want to logout? (yes/no): ")
    if choice.lower() == "yes":
        logout()
    else:
        print("You are still logged in.")