from data import Username, Password
from user import User
import functionslog as function

user = User()
user.fname = input("Enter your first name >> ")
user.lname = input("Enter your last name >> ")
user.username = input("Enter your last username >> ")
function.actions(user.fname, user.lname, "username")
user.password = input("Enter your password >> ")
function.actions(user.fname, user.lne, "")

if(user.username == Username and user.password == Password):
   print("User has been authenticated")
else:
    print("Wrong credentials")