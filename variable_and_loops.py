#joy
import numpy as np #the numpy library

#defining the function main()
def main():
    i=0
    n=10    # i & n are both integers
    x=119.0      #floating point num are declared with a "."
    
    #using np to declare arrays quickly 
    y = np.zeros(n,dtype=float)    #declares 10 zeros as floats using np)
    
    #using loops to iterate with a variable
    for i in range(n):
        y[i] = 2.0 * float(i) + 1.0    #set y=2i+1
        
    for y_element in y:
        print(y_element)
        
#execute the main function
if __name__ == "__main__":
    main()