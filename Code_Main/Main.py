#import motor
import catcher
import save_new_color

print('*******************************\n'
      'Welcome to ISAAC, please choose a function to start :\n'
      'Input C: Catch a object\n'
      'Input S: Save a new color of object\n'
      'Input F: Follow movement function\n'
      'Input Q: Quit the program.\n'
      'Wish you have a pleasant journey!\n'
      '******************************\n')
while True:
    choose_function = input('Please input C,S,F or Q: ')

    if choose_function == 'C':
        color = input('Please choose a color:')
        big_case, small_case = catcher.give_position(color)
        print(big_case,small_case)
        # num = num-200
        # print("get information ",num)
        # motor.motor_move(num)
        # print(color)
        # reponse = 'no'

    elif choose_function == 'S':
        print('Please input a color name for your new object.')
        obj_name = input('My new color is: ')
        lower,upper = save_new_color.get_hsv()
        print("Color: " + obj_name + "'s hsv is between :", lower, " and ", upper)

    elif choose_function == 'F':
        print('To be done in the future')


    elif choose_function == 'Q':
        print('Program ended.\n'
              'Thanks for using ISAAC!\n'
              'See you next time :)')
        break

    else:
        print('Wrong, please input S, D or Q: ')