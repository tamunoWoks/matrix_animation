## Matrix Digital Rain Animation
This Python script simulates the iconic **Matrix "digital rain" effect**, where streams of binary digits (`0` and `1`) fall down the screen in random columns. It uses simple console output with randomization to generate an endlessly scrolling animation.

### Features:
- **Matrix-style falling code effect** using `0`s and `1`s  
- Adjustable screen **width** (`WIDTH` variable)  
- Streams appear at **random intervals** and last for random lengths  
- Smooth animation controlled with `time.sleep()`  
- Graceful exit with **Ctrl+C**  


### Code Review:
This program creates a scrolling animation by printing rows of text inside an infinite loop that is stopped when the user presses ctrl-C. The main data structure in this program is the columns list, which holds 70 integers, one for each column of output. When an integer in columns is 0, it prints an empty space for that column. When it’s greater than 0, it randomly prints a 0 or 1 and then decrements the integer. Once the integer is reduced to 0, that column prints an empty space again. The program randomly sets the integers in columns to integers between 4 and 14 to produce streams of random binary 0s and 1s.  

Let’s take a look at each part of the program:
1. We import the `random` module for its `choice()` and `random()` functions, the `sys` module for its `exit()` function, and the `time` module for its `sleep()` function. We also set a variable named `WIDTH` to `70` so that the program produces output for 70 columns of characters.
&nbsp;&nbsp;&nbsp;&nbsp;The `WIDTH` variable is a constant thats why it is written in uppercase. Using constants allows you to write more readable code, such as `columns = [0] * WIDTH` instead of `columns = [0] * 70`.
```python
import random, sys, time
WIDTH = 70  # The number of columns
```
2. The bulk of the program occurs inside a try block, which catches if the user presses `ctrl-C` to raise a `KeyboardInterrupt` exception.
&nbsp;&nbsp;&nbsp;&nbsp;The `columns` variable contains a list of 0 integers. The number of integers in this list is equal to the WIDTH. Each of these integers controls whether a column of the output window prints a stream of binary numbers or not 
```python
try:
    columns = [0] * WIDTH
```
3.  We want this program to run forever, so we place it all inside an infinite `while True:` loop. Inside this loop is a `for` loop that iterates over each column of a single row. The loop variable `i` represents the indexes of columns; it begins at `0` and goes up to but does not include WIDTH. The value in columns[0] represents what should be printed in the leftmost column, columns[1] does so for the second column from the left, and so on.
&nbsp;&nbsp;&nbsp;&nbsp;For each column, there is a two percent chance that the integer at columns[i] is set to a number between `4` and `14`. We calculate this chance by comparing `random.random()` (a function that returns a random float between 
0.0 and 1.0) to 0.02. If you want the streams to be denser or sparser, you can increase or decrease this number, respectively. We set the counter integers for each column to a random number between 4 and 14.
```python
while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                columns[i] = random.randint(4, 14)
```
4. Also inside the `for` loop, the program determines if it should print a random `0` or `1` binary number or an empty space. If columns[i] is 0, it prints an empty space. Otherwise, it passes the list [0, 1] to the `random.choice()` function, which returns a random value from that list to print. The code also decrements the counter at columns[i] so that it gets closer to 0 and no longer prints binary numbers.
```python
         # Print a character in this column:
            if columns[i] == 0:
                # Change this ' '' to '.' to see the empty spaces:
                print(' ', end='') 
            else:
                # Print a 0 or 1:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1  # Decrement the counter for this column.
```
5. After the `else` block ends, the `for` loop block also ends. The `print(`) call after the `for` loop prints a newline, as the previous `print()` calls for each column pass the `end=''` keyword argument to prevent a newline from being printed after each column. For each row printed, the program introduces a tenth-of-a-second pause by calling `time.sleep(0.1)`.
&nbsp;&nbsp;&nbsp;&nbsp;The final part of the program is an except block that exits the program if the user pressed `ctrl-C` to raise a `KeyboardInterrupt` exception.

### Notes:
- The program runs infinitely until stopped manually.
- Best viewed in a dark terminal background for full "Matrix" effect.
- Adjust width and speed to fit your terminal size and performance.

