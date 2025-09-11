# Task 2: Demonstrate List Slicing 
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list


Original_list=[1,2,3,4,5,6,7,8,9,10]
First_five=Original_list[:5]
Reversed_Five=First_five[::-1]
print("Original List:",Original_list)
print("Extracted first five elements:",First_five)
print("Reversed extracted elements:",Reversed_Five)
