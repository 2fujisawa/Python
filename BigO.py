#Big O Notation
'''
Describes the upper bound of an algorithm in terms of time(measures time an algorithm takes to complete) or space complexity(amount of memeory used), understanding how an algorithm  sclaes with input size
        -Big-O notation is used to describe the worst-case scenario for an algorithm

        Big-O Time Complexities:
        1. O(1) | Constant Time - Ex. Accessing an element in an array by index
        2. O(log n) | Logarithmic Time - Ex. Binary search
        3. O(n) | Linear Time - Ex. Traversing an array/list
        4. O(n log n) | Linearithmic Time - Ex. Merge Sort, Quick sort
        5. O(n^2) | Quadratic Time - Ex. Bubble sort, Selection sort
        6. O(2^n) | Exponential Time - Ex. Recursive Fibonacci
        7. O(n!) | Factorial Time - Ex. Permutations of n items

        
        How to Analyze Time Complexity:
        1. Identify Dominant Operation - Identify the operation that takes the most time
        2. Remove Constants - Ignore constants and coefficients Ex. O(2n) = O(n)
        3. Drop Non-Dominant Terms - Drop terms that don't contribute to the overall time complexity Ex. O(n^2 + n) = O(n^2)


'''

#Big O Notation Examples
def constant_time(array):
    return array[0] #O(1) - Constant Time as only returns the first element in the array

def logarithmic_time(array, target_value): # we will be doing a binary search
        Lowest = 0
        Highest = len(array) - 1

        #Each iteration of this loop havles the search space
        while Lowest <= Highest: #O(log n) - LOGARITHMIC TIME HALF THE ARRAY EACH TIME
             middle_value = (Lowest + Highest) // 2   #Adding highest and lowest value and dividing it by 2 top get the middle number
             if array[middle_value] == target_value: #if the middle value is the target value return the middle value
                  return middle_value
             elif array[middle_value] < target_value: #else if the middle value is less than the target value start adding one from the middle of the array
                  Lowest = middle_value + 1
             else: #else the middle value is greater than the target value so subtract one from the middle of the array
                  Highest = middle_value - 1
        return None
             


def linear_time(array):
    for element in array: #O(n) - Linear Time as it traverses the entire array
        print(element) 


def main():
#Constant Time
    array = [1,2,3,4,5,6]
    print(constant_time(array), "\n")

#Logarithmic Time
    target_value = 3
    print("The index for the target value is", logarithmic_time(array, target_value))

#Linear Time
    linear_time(array) # if you use the print statement in the function you will see the elements printed out with a none value at the end as its not returning anything 


if __name__ == "__main__":
    main()
    

