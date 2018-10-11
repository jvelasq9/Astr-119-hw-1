#Joy
#the numpy library
import numpy as np

#defining the function main()
def main():
    i = 0 #An interger 0 for i
    x = 119.0 #float x
    
    for i in range (120): #Loop i from 0 to 119
        if((i%2)==0): #if i is even 
            x +=3.0 #(x+3)
            
        else:   #if i is odd the it will do else
            x -=5.0   #(x-5)
            
    s = "%3.2e" % x    #make a string containing x with sci. notation w/2 decimal places
    print(s)   #printing s
    
#Rest of the program continues

if __name__ == "__main__":   #if the main() function exists, run it
    main()