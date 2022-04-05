'''
##########
Lab 4.02
##########

Part 1
----------
Write a function pluralize_words that takes in a list of words and updates the values of the list 
to make each one plural. It returns nothing.

Making plurals in English has a number of special cases, but for this lab we'll use a simple rule: 
if the word ends in a y remove the y and add ies; otherwise add an 's'.

We'll exercise the function on a list of words.

Create the function contract for pluralize_words.

Provide a few examples that confirm pluralize_words works as expected:

    Include examples with 'berry'

    What if the list is empty?

Example 1
----------
    # contract goes here
    def pluralize_words(word_list):
        # your code goes here
​
    word_list = ['apple', 'berry', 'melon']
    print(f"Singular words: {word_list}")
    pluralize_words(word_list)
    print(f"No longer singular words: {word_list}")
    # more examples go here

#######################################################
Here is what it should look like when you run your code:
#######################################################
Singular words: ['apple', 'berry', 'melon']
No longer singular words: ['apples', 'berries', 'melons']

Hint
-----
Remember that you can index into the string and get the length of a string. Use that to get the last letter of each word.

Part 2
------
Create a function my_reverse, which will return a reversed string.

Create the function contract for my_reverse.

Provide a few examples to confirm that my_reverse works:

    An empty string

    A string of even length

    A string of odd length greater than 1

    A string of length 1
'''
# This is Part 1:

# def pluralize_words(word_list):
#     for i,word in enumerate(words):
#         word = words[i]
#         if word.endswith('y'):
#             words[i] = word[:-1] + 'ies'
#         else:
#             words[i] = word + 's'
            

# words = ['apple', 'berry', 'melon']
# print(words[-1])
# print(f"Singular words: {words}")
# pluralize_words(words)
# print(f"No longer singular words: {words}")


# Part 2 code
my_list = ['apple', 'berry', 'melon']
def my_reverse(string_to_reverse):
    return string_to_reverse[::-1]


def reverse_strings_in_list(list_to_reverse):
    reversed_list = []

    for item in list_to_reverse:
        reversed_list.append(my_reverse(item))
    
    return reversed_list

print(reverse_strings_in_list(my_list))