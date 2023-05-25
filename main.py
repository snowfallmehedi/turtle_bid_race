import turtle
import random

screen = turtle.Screen()
screen.screensize(600, 600)
game_is_on = True


def game():
    location = [(-300, -250), (-300, -150), (-300, -50), (-300, 50), (-300, 150), (-300, 250)]
    color = ["red", "green", "blue", "black", "violet", "yellow"]
    turtle_list = []

    user_choice = screen.textinput(title="Turtle Race Loading 正在工作",
                                   prompt="Please bet on turtle color. 选一个颜色 "
                                          "We have red红, green绿, Blue蓝, black黑, violet and yellow黄").lower()
    for _ in range(6):
        new_turtle = turtle.Turtle("turtle")
        new_turtle.color(color[_])
        turtle_list.append(new_turtle)
        new_turtle.penup()
        new_turtle.goto(location[_])
    global game_is_on
    while game_is_on:
        for _ in range(6):
            turtle_list[_].forward(random.randint(0, 10))
            if turtle_list[_].xcor() > 250:
                game_is_on = False
                if user_choice == turtle_list[_].pencolor():
                    if screen.textinput("Result", f"You Won 你赢了!!!! {turtle_list[_].pencolor()} won the race. "
                                                  "Do You wanna Play Again?").lower() == "yes":
                        with open("winning.txt", mode="r+") as file:
                            score = int(file.read())
                            score += 1
                            file.seek(0)
                            file.write(str(score))

                        screen.clear()
                        game_is_on = True
                        game()

                else:
                    print(f"You Lost!!!! {turtle_list[_].pencolor()} won the race")
                    if screen.textinput("Result", f"You Lost!!!! {turtle_list[_].pencolor()} won the race. "
                                                  "Do you wanna play again?").lower() == "yes":
                        with open("failing.txt", mode="r+") as file:
                            score = int(file.read())
                            score += 1
                            file.seek(0)
                            file.write(str(score))

                        screen.clear()
                        game_is_on = True
                        game()


game()

screen.exitonclick()
