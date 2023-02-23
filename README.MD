# Dependencies

This project is implemented on Python.

To run the codes, please install the `numpy` and `Jupyter Notebook`.

# Usage

You can run the project via terminal and jupyter notebook.

Run program via terminal, for instance run the blank input:

```
.\main.py --input_file sudoku-inputs/input.blank.txt
```

If you equipped with Jupter Noteboook, please go to `main.ipynb` to run the program.

  
# Overview 

For any given input, I read from the file and store them in a numpy array. In the initialize step, I randomly fill the number for each row in the array (via numpy.random.randint), and make sure there is no repeat items in each row. Next, I randomly generated 3 integers. The first integer represents a row, and the last two integer represents two colums that ready to swap. Of course, here I'll check if the two swap elements are they appear in the original input, if so, regenerate new cols. Then, I swap the two elements in the selected row, and calculate the fitness values. If the fitness is less or less equal than, then we use current state as our new game board state. Lastly, the program stops when the fitness value is 0 (that means best solution), or if the number of steps greater than a overhead I setted up initially. 

# Transformation 
Function I initialize the game board and make sure each row have no repeat element. My transformation is randomly select 2 element in a random row, and swap them. 

# Fitness Function 
the fitness function equals how many repeat items in each colum as well as in each small square. # Stopping Criteria When the fitness value is 0, or the number of step greater than a overhead I setted up. 
# Parameter Recommendation 

1. If fitness less than and equal, both of them go to next state. 
2. the coin flip prabability best in 0.01. 
3. sumary: in my experiment, the more randomness, the better results you will get!