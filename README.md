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

### Notes:
- The program runs infinitely until stopped manually.
- Best viewed in a dark terminal background for full "Matrix" effect.
- Adjust width and speed to fit your terminal size and performance.

