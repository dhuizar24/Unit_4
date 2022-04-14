'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''
# THIS IS CODE FOR THE FIRST PROBLEM
# def print_7_stars(): 
#     my_string = ''
#     for i in range(0, 7):
#         my_string += ' *'
#     print(my_string)
# for i in range(7):
#     print_7_stars()


# THIS IS CODE FOR THE SECOND PROBLEM
# def stars_and_stripes():
#     this_string = ''
#     other_string = ''
#     for i in range (0,7):
#         this_string += ' *'
#         other_string += ' -'
#     print(this_string)
#     print(other_string)
# for i in range(3):
#     stars_and_stripes()



# THIS IS CODE FOR THE THIRD PROBLEM
# def increasing_triangle():
#     this_string = ''
#     for i in range (0,7):
#         this_string += f'{i + 1}'
#         print(this_string)
# increasing_triangle()


#THIS IS CODE FOR THE FOURTH PROBLEM
# def vertical_stars_and_stripes():
#     for i in range(7):
#         print('- * - * - * -')
# vertical_stars_and_stripes()


#THIS IS CODE FOR THE FIFTH PROBLEM
# def border_stars_vertical_stars_and_stripes():
#     print('* * * * * * *')
#     for i in range(7):
#         print('* - - - - - *')
#     print('* * * * * * *')
# border_stars_vertical_stars_and_stripes()


# CODE FOR FINAL PROBLEM

def balanced_triangle():
    this_string  = ""
    for i in range(7):
        this_string  += f' {i+1}'
        print(this_string )

    
    for i in reversed(range(7)):
        new_string = ""
        for j in range(i):
            new_string += f' {j+1}'
        print(new_string)

balanced_triangle()

