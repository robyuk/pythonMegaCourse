"""Coding Exercise

Note: This is a very challenging exercise. Do not worry if you can't get it right. Just try to code until you get bored. The sole experience of trying to code helps your learning a ton.

A client wants to buy a coin-flip probability program from you.

The programs should work like this:

1. The user runs the program.
2. The program asks the user to enter "head" or "tail".
3. The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail".
4. The user does the same over and over again.
5. In each cycle, the program should return the current percentage of heads in the program,
   similar to what you see in the screenshot above. Also, you should write each user entry
   (i.e., head or tail) in a text file using a with-context manager, one entry per line.

Solution:"""

def writeresult(result):
    with open("heads_tails.txt", "a") as file:
        file.write(result + "\n")


h=0
t=0

while True:
    result = input("Flip a coin and enter heads or tails here: ")
    match result[0].strip().lower():
        case 'h':
            h += 1
            writeresult("Heads")
        case 't':
            t += 1
            writeresult("Tails")
        case 'q':
            exit(0)
        case _else:
            print("Please enter heads or tails.")
    try:
        percent = h * 100 / (h + t)
    except ZeroDivisionError:
        percent = 0

    print(f"Heads: {percent}%")
