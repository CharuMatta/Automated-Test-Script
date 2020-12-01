# Finding most occuring character

def get_max_occuring_char(input):
    # Set frequency as empty dictionary
    frequency_dict={}
    for i in input:  
        if i in frequency_dict:
            frequency_dict[i] +=1
        else:
            frequency_dict[i] =1
    # import pdb;pdb.set_trace()
    most_occurence =max(frequency_dict, key=frequency_dict.get)
    return most_occurence

if __name__ == "__main__":
    # Get string from user
    input_str = input("\nPlease enter the text: ")
    most_occurence = get_max_occuring_char(input_str)
    # Displaying result
    print(f"\nMost occuring character is: {most_occurence}\n")
            