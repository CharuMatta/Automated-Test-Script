# Finding most occuring character

import sys

def get_max_occuring_char(input):
    # Set frequency as empty dictionary
    frequency_dict={}
    for i in input:  
        if i in frequency_dict: #checking if occurence already exit or not
            frequency_dict[i] +=1 #if yes than increase counter by 1
        else:
            frequency_dict[i] =1 #else counter=1
    # import pdb;pdb.set_trace()
    most_occurence =max(frequency_dict, key=frequency_dict.get) #using max method to get maximum frequency in dictnary
    return most_occurence

if __name__ == "__main__":
    # Get string from user
    input_str = input("\nPlease enter the text only in: ") #user input
    if any(char.isdigit() for char in input_str):
        print("Please do not include digits in your name.")
        sys.exit(1)
    most_occurence = get_max_occuring_char(input_str)
    # Displaying result
    print(f"\nMost occuring character is: {most_occurence}\n")
            