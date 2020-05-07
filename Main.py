# -*- Nathan Ormond -*-
from graphics import *

#------------------- Main Class
class Main:
     
    def __init__(self):
         print("Main Class init")
         
    def run(self):
        print("running prg...")
        
        prime_num = Prime()
        
        primes_end = 1000
        
        primes_list = prime_num.get_primes(primes_end)
        deltas_list = prime_num.get_deltas(primes_list)
        
        # Check values (Comment out if unnecessary)
        print("PRIMES: \n")
        print(*primes_list)
        
        print("\nDELTAS: \n")
        print(*deltas_list)
        
        ui = Graphics()
        ui.paint_window(deltas_list)
    
#------------------- Prime Class
class Prime:
        
    def __init__(self):
         print("Prime Class init")
    
    # returns list of all prime numbers up to end number    
    def get_primes(self, end):  
        
        return_arr = []                
                                               
        for num in range(end):
            if all(num%i!=0 for i in range(2,num)):
                # insert val to end of list (position len(return_arr))
                return_arr.insert(len(return_arr),num) 
                
        return return_arr
    
    # takes an array of numbers 
    # returns an array of the differences between each element (position i) and i+1
    def get_deltas(self, nums): 
        return_arr = []
        i = 0
        while i < len(nums):
            if (i + 1) < len(nums):
                difference = nums[i + 1] - nums[i]
                return_arr.insert(len(return_arr),difference)
            i+=1
        
        return return_arr
    
    # Takes a list and returns a list with duplicate values removed
    def remove_duplicates(self, x):
        return list( dict.fromkeys(x) )
    
#------------------- Graphics Class
class Graphics:
        
    def __init__(self):
         print("Graphics init")
    
     
    def paint_window(self, deltas):
        
        scaling  = 4
        margin   = 5
        
        # create a window
        #win = GraphWin(width = (max(deltas) * scaling ), height = (len(deltas) * scaling)) 
        
        win = GraphWin(width = 500, height = 500)
        
        # set the coordinates of the window; 
        # bottom left is (0, 0) and top right is (maximum val element, length of elements)
        
        win.setCoords(0, 0, margin + max(deltas) * scaling , margin + len(deltas) * scaling) 
       
        colours = ["green", "blue", "red", "yellow", "grey", "orange", "purple", "brown", "pink", "black"]
        
        i = 0
        while i < len(deltas):
            
            colour = colours[i%10]
            
            j = 0
            while j < deltas[i] :
                # Create Square representing each "one" of value of element in list
                init_x = (margin - 1) + j * scaling
                init_y = (margin - 1) + i * scaling
                end_x = (margin - 1) + ((j * scaling) + scaling)
                end_y = (margin - 1) + ((i * scaling) + scaling)
                
                mySquare = Rectangle(Point(init_x, init_y), Point(end_x, end_y)) 
                mySquare.setFill(colour)
                # Draw element to window
                mySquare.draw(win) 
                j+=1
            i+=1
            
        # pause before closing
        win.getMouse() 

#------------------- Script to run programme
    
main = Main()
main.run()
