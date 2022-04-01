'''
Do Now 4.01

1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following
Briefly write down what happened. What would happen if you added 100 items to the list single_fruit? 
Write down how you would update multi_fruit.

1. Answers: When hit run, the list multi_fruit will be empty but then every item in single_fruit will be added to multi_fruit. If I added 100 items to single_fruit, I would have to add a lot append commands and it would make the code too long. I could use a for loop to make it shorter. 

2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is " + {num})
        
Continue in your notebook
Respond to the following
Briefly write down what happened. How would this change if you added 100 items to list_of_numbers?

Recieved Error because the print statement is a set not a str.

3. In your console
Rewrite the code from part 1 using knowledge from part 2.
'''
# number 3 
single_fruit = ['apple', 'banana', 'watermelon', 'grape']
multi_fruit = []
for num in single_fruit: 
    print(f"the fruit is {num}")