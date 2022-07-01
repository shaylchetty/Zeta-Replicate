
import turtle
import random
import time
import sys

# Set up the screen
wn = turtle.Screen()
wn.title("Zeta Mac")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center",
          font=("Courier", 24, "normal"))

seconds = 60

# pen.goto(0, 200)
# pen.write("Score: 0  High Score: 0", align="center",
#           font=("Courier", 24, "normal"))

start_time = time.time()  # sets the start time to the current time
score = 0  # counts the number of correct answers
high_score = 0  # records the highest score in a series of games


while True:

    current_time = time.time()  # time at the nth iteration of the loop
    # the difference between the time now and the time at the start
    elapsed_time = current_time - start_time

    # mins, secs = divmod(t, 60)
    # timer = '{:02d}:{:02d}'.format(mins, secs)
    # # print(timer, end="\r")
    # pen.goto(0, 200)
    # pen.write("Time: {}".format(int(x - (current_time - start_time))),
    #           align="center", font=("Courier", 24, "normal"))

    a = random.randint(2, 100)  # Three random integers
    b = random.randint(2, 100)
    d = random.randint(2, 12)
    # choose randomly between addition, subtraction, multiplication, and division
    asmd = random.choice([1, 2, 3, 4])
    if (asmd == 1):
        solve = a + b
        question = "%d + %d = " % (a, b)
    elif (asmd == 2):
        if (a > b):
            solve = a - b
            question = "%d - %d = " % (a, b)
        else:
            solve = b - a
            question = "%d - %d = " % (b, a)
    elif (asmd == 3):
        solve = a * d
        question = "%d * %d = " % (a, d)
    else:
        solve = a
        c = a * d
        question = "%d / %d = " % (c, d)

    answer = False
    # while the answer is incorrect, clear the answer and allow user to try again
    while (solve != int(answer)):
        pen.goto(0, 100)
        pen.write("{}".format(question),
                  align="center", font=("Courier", 24, "normal"))
        answer = input(question)
        pen.goto(80, 100)
        pen.write("{}".format(answer),
                  align="center", font=("Courier", 24, "normal"))
        # clears the incorrect answer allowing the user to guess again
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    # time.sleep(5)
    # enter button instead of answer causes code to crash
    score += 1  # increment score by 1
    pen.clear()
    pen.goto(0, 260)
    pen.write("Score: {}  High Score: {}".format(score, high_score),
              align="center", font=("Courier", 24, "normal"))

    if elapsed_time > seconds:  # if the time has run up the loop ends
        print("Time\'s up! Your score was %d." % (score))
        if score > high_score:
            high_score = score
        start_time += 10
        score = 0

    pen.goto(0, 260)
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score),
              align="center", font=("Courier", 24, "normal"))

    # if wn.onkeypress("Up"):
    #     break
