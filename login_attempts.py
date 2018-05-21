import time
class Users():

    def __init__(self,first_name, last_name, *user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        print(" Hello "+ self.first_name + ' '+ self.last_name +"\n")
        print(" " + str(self.user_info) + " ")

    def greet_user(self):
        print(" Hello "+ self.first_name + ' '+ self.last_name +"\n")

    def incr_login_attempts(self,attempt):
        self.login_attempts += attempt
        print("Total attemps: " + str(self.login_attempts)+ " @ ")
        print(str(time.ctime()))

    def reset_login(self):
        self.login_attempts *= 0
        print("login has been reset! " + str(self.login_attempts))


use = Users("kirk","toliver","chicago","engineering")
use.describe_user()
use.incr_login_attempts(1)
use.incr_login_attempts(1)
use.incr_login_attempts(1)
use.incr_login_attempts(1)
print(str(use.login_attempts))
use.reset_login()
print(str("login attempts: " + str(use.login_attempts)))
use.incr_login_attempts(1)
use.incr_login_attempts(1)
print(str("login attempts: " + str(use.login_attempts)))

user = Users("david", "Capilary")
user.describe_user()
user.incr_login_attempts(1)
user.incr_login_attempts(1)
user.incr_login_attempts(1)
user.incr_login_attempts(1)
print(str(user.login_attempts))

#use.greet_user()
