import turtle 
import pandas

screen = turtle.Screen()

screen.title("US game")
# image = r"C:\Users\Asus\Pictures\Camera Roll\1cbd7de40fd1c08f99c0.gif"
# screen.addshape(image)
data = pandas.read_csv(r".\day25\us-states-game-start\50_states.csv")
print(data)
screen.exitonclick()