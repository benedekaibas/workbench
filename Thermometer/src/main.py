#!/usr/bin/python

"""
Temperature conversion program used to demonstrate:

* interactive programs
* data types
* basic computation

This program serves as part of the Allegheny College CMPSC 100: Computational
Expression course.
"""

def main():
    
    #print program name
    print("Farenheiht to celsius converter", end = "\n\n")

    #Request user input
    temp_f = int(input("Enter the temperature (without units): "))
    #Perform a calculation
    #to_int = int(temp_f)
    
    temp_c = (temp_f - 32) / 1.8
    #temp_c *= 5/9
    #Report result
    print(temp_c)

if __name__ == "__main__":
    main()
    