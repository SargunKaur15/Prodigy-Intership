import re

# password strength check conditions:
#min 8 characters,digit,uppercase,lowercase,special character

def check_password_strength(password):
    if len(password) < 8: #length of password
     return "😩 Weak :password must be at of atleast 8 chars"
    
    if not any(char.isdigit() for char in password): #check for digit
     return "😩 Weak :password must contain at least one digit"

    if not any(char.isupper() for char in password): #check for uppercase
     return "😩 Weak :password must contain at least one uppercase letter"

    if not any(char.islower() for char in password): #check for lowercase
     return "😩 Weak :password must contain at least one lowercase letter"

    if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password): #check for special character
     return "😩 Weak :password must contain at least one special character"

    return "😎 Hurrah! :password is strong"

def password_checker():
  print("🤗 Welcome to the Password Strength Checker!🥳")

  while True:
    password = input("💻  Please enter your password(or type 'exit' to quit): ")
    if password.lower() == "exit":
        print("Exiting the Password Strength Checker. Goodbye!👋")
        break
    result = check_password_strength(password)
    print(result)


#Run the password checker tool
if __name__ == "__main__":
    password_checker()
