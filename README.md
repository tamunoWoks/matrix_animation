## Matrix Digital Rain Animation
This Python script simulates the iconic **Matrix "digital rain" effect**, where streams of binary digits (`0` and `1`) fall down the screen in random columns. It uses simple console output with randomization to generate an endlessly scrolling animation.

### Features:
- **Matrix-style falling code effect** using `0`s and `1`s  
- Adjustable screen **width** (`WIDTH` variable)  
- Streams appear at **random intervals** and last for random lengths  
- Smooth animation controlled with `time.sleep()`  
- Graceful exit with **Ctrl+C**  


### How It Works:
1. **Columns tracking**  
   - Each column has a counter stored in the `columns` list.  
   - A counter of `0` means the column is empty.  
   - A positive counter means that many more `0`/`1`s will appear before the column goes empty again.
2. **Random stream generation**  
   - On each frame, each column has a **2% chance** of starting a new stream.  
   - Stream lengths are randomized between **4 and 14 characters**.
3. **Printing logic**  
   - If a column has no active stream → print a space `" "`.  
   - If a column is active → print a random `0` or `1`, then decrement its counter.
4. **Animation loop**  
   - Each row is printed one line at a time across all columns.  
   - After finishing one row, the script prints a newline and sleeps for `0.1` seconds before drawing the next row.  

### Notes:
- The program runs infinitely until stopped manually.
- Best viewed in a dark terminal background for full "Matrix" effect.
- Adjust width and speed to fit your terminal size and performance.
