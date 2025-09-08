import random, sys, time

WIDTH = 70 # Number of columns (screen width)

try:
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Loop over each column:
        for i in range(WIDTH):
            if random.random() < 0.02:
                # Restart a stream counter on this column.
                # The stream length is between 4 and 14 characters long.
                columns[i] = random.randint(4, 14)
            # Print a character in this column:
            if columns[i] == 0:
                # No active stream, print space
                print(' ', end='') 
            else:
                # Active stream, print a random 0 or 1
                print(random.choice([0, 1]), end='')
                columns[i] -= 1  # Decrease stream length of column
        print()  # Print a newline at the end of the row of columns.
        time.sleep(0.1)  # Delay for smooth transition
except KeyboardInterrupt:
    sys.exit() 
