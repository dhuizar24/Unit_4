'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])

    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''
my_list = [1,2, 3, 4 ,5 ,6]

def print_numbers(my_list):
        for i in range(1, len(my_list)+1):
            print(my_list)
        # num_list = [1, 2, 3, 4, 5, 6] # this line does nothing
        # print_numbers(num_list)

def swapping():
    line_str = ""
    for line in range (0, 6):
        for char in range(0,6):
            if line % 2 == char % 2:
                    line_str += "*"
            else:
                    line_str += "-"
    print(line_str)


choice = "print numbers" # input("Would you like to choose function print numbers or swap?")

if choice == "print numbers":
    print(my_list)
elif choice == 'swap':
    swapping()
else:
    print("please try again")
