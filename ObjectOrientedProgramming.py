
from turtle import Turtle, Screen             # turtle is the module; Turtle and Screen are classes
from prettytable import PrettyTable

timmy = Turtle()                              # timmy is an object created from class Turtle
print(timmy)
timmy.shape("turtle")                         # shape is a method(function otherwise) of object timmy
timmy.color("coral")                          # color is a method(function otherwise) of object timmy
timmy.forward(100)

my_screen = Screen()                          # my_screen is an object created from class Screen
print(my_screen.canvheight)                   # canvheight is an attribute(variable otherwise) of object my_screen
my_screen.exitonclick()                       # exitonclick is a method(function otherwise) of object my_screen

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmader"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)


class User:
    
    def __init__(self, userid, name):
        self.user_id = userid
        self.user_name = name
        self.followers = 0
        self.following = 0

    def follow(self, any_user):
        self.following += 1
        any_user.followers += 1


user1 = User('001', 'john')
user2 = User('002', 'jack')

user1.follow(user2)

print(user1.followers, user1.following)
print(user2.followers, user2.following)
