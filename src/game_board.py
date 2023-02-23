import numpy as np
import copy
import math
class sudoku:

    def __init__(self, input_file_path:str=None, ramdom_seed:int = 0) -> None:
        # np.random.seed(ramdom_seed)
        self.init_board = self.read_board(input_file_path)
        self.board = copy.deepcopy(self.init_board)
        self.current_fitness = math.inf
        self.step = 0
    
    def read_board(self,filename:str=None):
        init_board = np.zeros((9,9))

        if not filename:
            return init_board
        with open(filename) as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                line = line.strip(' \n').split(" ")
                row = [int(i) for i in line]
                init_board[idx] = np.array(row)
        return init_board


    def random_init_state(self):
        for row in self.board:
            for i in range(len(row)):
                while row[i]==0:
                    r=np.random.randint(1,10)
                    if r not in row:
                        row[i] = r
        self.current_fitness = self.fitness(self.board)
        
    def show_board(self):
        print(f"[Initial States]:\n {self.init_board}")
        print(f"[Current Game Board]:\n {self.board}")
        print(f"[Current Fitness Value]:\n {self.fitness(self.board)}")
        print(f"[Number of Steps Used]:\n {self.step}")

    def get_random_pair(self, range=(0,9),size=2):
        row = np.random.randint(range[0],range[1])
        cols = []
        while len(cols) < size:
            r=np.random.randint(range[0],range[1])
            if r not in cols and self.init_board[row,r] == 0:
                cols.append(r)
        return row, cols
    
    def hill_Climbing(self,max_step=5000000):
        self.random_init_state()
        self.show_board()
        while self.current_fitness > 0:
            
            random_row, random_cols = self.get_random_pair()
            new_states = copy.deepcopy(self.board)
            
            new_states[random_row,random_cols[0]], new_states[random_row,random_cols[1]] = \
                 self.board[random_row,random_cols[1]],self.board[random_row,random_cols[0]]
            new_fitness = self.fitness(new_states)


            if new_fitness <= self.current_fitness:

                self.step+=1    
                self.board = new_states
                self.current_fitness = new_fitness
                if self.step % 10000 == 0:
                    self.show_board()
                if self.step >= max_step:
                    break
            
    def check_repeat(self, numbers):
        numbers = numbers.reshape(-1)
        hashMap = {}
        for val in numbers:
            hashMap[val] = 1
        n_repeat = len(numbers) - sum(hashMap.values())
        return n_repeat

    def fitness(self,state):
        
        loss = 0
        for i in range(len(state)):
            col = state[:,i]
            loss += self.check_repeat(col)
        
        for x in range(0,3):
            for y in range(0,3):
                sub_square = state[x*3:x*3+3,y*3:y*3+3]
                loss+=self.check_repeat(sub_square)
        return loss

        


