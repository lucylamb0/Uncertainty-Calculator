from sympy import symbols, diff, lambdify
from math import *

def re_value(letter):
    if letter == "A":
        A = float(input("Please input a value for A: "))
        return A

    if letter == "B":
        B = float(input("Please input a value for B: "))
        return B

    if letter == "C":
        C = float(input("Please input a value for C: "))
        return C

    if letter == "D":
        D = float(input("Please input a value for D: "))
        return D

    if letter == "E":
        E = float(input("Please input a value for E: "))
        return E

    if letter == "F":
        F = float(input("Please input a value for F: "))
        return F

    if letter == "G":
        G = float(input("Please input a value for G: "))
        return G

def re_value2(letter):

    if letter == "err_A":
        A = float(input("Please input a value for err_A: "))
        return A

    if letter == "err_B":
        B = float(input("Please input a value for err_B: "))
        return B

    if letter == "err_C":
        C = float(input("Please input a value for err_C: "))
        return C

    if letter == "err_D":
        D = float(input("Please input a value for err_D: "))
        return D

    if letter == "err_E":
        E = float(input("Please input a value for err_E: "))
        return E

    if letter == "err_F":
        F = float(input("Please input a value for err_F: "))
        return F

    if letter == "err_G":
        G = float(input("Please input a value for err_G: "))
        return G

print("This program can only support equations with 7 variables")
cont = "y"
while cont == "y":
    signs = input("Please input the number of symbols/variables you wish to use for your equation: ")
    signs = int(signs)
    equ = input("Using signs and math symbols python would use (eg sqrt, pi, e, *, ** etc), please input your equation (using symbols A B C D E F G for variables): ")
    if signs == 1:
        A = symbols('A')
    if signs == 2:
        A, B = symbols('A B')
    if signs == 3:
        A, B, C = symbols('A B C')
    if signs == 4:
        A, B, C, D = symbols('A B C D')
    if signs == 5:
        A, B, C, D, E = symbols('A B C D E')
    if signs == 6:
        A, B, C, D, E, F = symbols('A B C D E F')
    if signs == 7:
        A, B, C, D, E, F, G = symbols('A B C D E F G')
    count = signs

    letter_list = ["A","B","C","D","E","F","G"]
    num_list = len(letter_list)

    for i in range(num_list - signs):
        letter_list.pop(num_list - i - 1)

    diff_A = diff(equ, A)
    res_diff_A = lambdify(letter_list, diff_A)

    if signs >= 2:
        diff_B = diff(equ, B)
        res_diff_B = lambdify(letter_list, diff_B)

    if signs >= 3:
        diff_C = diff(equ, C)
        res_diff_C = lambdify(letter_list, diff_C)

    if signs >= 4:
        diff_D = diff(equ, D)
        res_diff_D = lambdify(letter_list, diff_D)

    if signs >= 5:
        diff_E = diff(equ, E)
        res_diff_E = lambdify(letter_list, diff_E)

    if signs >= 6:
        diff_F = diff(equ, F)
        res_diff_F = lambdify(letter_list, diff_F)

    if signs == 7:
        diff_G = diff(equ, G)
        res_diff_G = lambdify(letter_list, diff_G)

    result_func = lambdify(letter_list, equ)


    A = float(input("Please input a value for A: "))
    err_A = float(input("Please input a value for the uncertainty in A: "))

    if signs >= 2:
        B = float(input("Please input a value for B: "))
        err_B = float(input("Please input a value for the uncertainty in B: "))

    if signs >= 3:
        C = float(input("Please input a value for C: "))
        err_C = float(input("Please input a value for the uncertainty in C: "))

    if signs >= 4:
        D = float(input("Please input a value for D: "))
        err_D = float(input("Please input a value for the uncertainty in D: "))

    if signs >= 5:
        E = float(input("Please input a value for E: "))
        err_E = float(input("Please input a value for the uncertainty in E: "))

    if signs >= 6:
        F = float(input("Please input a value for F: "))
        err_F = float(input("Please input a value for the uncertainty in F: "))

    if signs >= 7:
        G = float(input("Please input a value for G: "))
        err_G = float(input("Please input a value for the uncertainty in G: "))

    re_try = "y"
    while re_try == "y":
        re_input1 = input("Would you like to reinput any values for a letter? (y/n): ")
        if re_input1 == "y":
            which_input = input("Which input would you like to re-input? (A,B,C etc): ")
            globals()[which_input] = re_value(which_input)

        re_input2 = input("Would you like to reinput any error values for a letter? (y/n): ")
        if re_input2 == "y":
            which_input = input("Which input would you like to re-input? (err_A, err_B, err_C etc): ")
            globals()[which_input] = re_value2(which_input)

        if ((re_input1 and re_input2) == "n"):
            re_try = "n"

    if signs == 1:
        result = result_func(A)
        error_final = sqrt((res_diff_A(A)*err_A)**2)
    if signs == 2:
        result = result_func(A, B)
        error_final = sqrt((res_diff_A(A, B)*err_A)**2 + (res_diff_B(A, B)*err_B)**2)
    if signs == 3:
        result = result_func(A, B, C)
        error_final = sqrt((res_diff_A(A, B, C)*err_A)**2 + (res_diff_B(A, B, C)*err_B)**2 + (res_diff_C(A, B, C)*err_C)**2)
    if signs == 4:
        result = result_func(A, B, C, D)
        error_final = sqrt((res_diff_A(A, B, C, D)*err_A)**2 + (res_diff_B(A, B, C, D)*err_B)**2 + (res_diff_C(A, B, C, D)*err_C)**2 + (res_diff_D(A, B, C, D)*err_D)**2)
    if signs == 5:
        result = result_func(A, B, C, D, E)
        error_final = sqrt((res_diff_A(A, B, C, D, E)*err_A)**2 + (res_diff_B(A, B, C, D, E)*err_B)**2 + (res_diff_C(A, B, C, D, E)*err_C)**2 + (res_diff_D(A, B, C, D, E)*err_D)**2 + (res_diff_E(A, B, C, D, E)*err_E)**2)
    if signs == 6:
        result = result_func(A, B, C, D, E, F)
        error_final = sqrt((res_diff_A(A, B, C, D, E, F)*err_A)**2 + (res_diff_B(A, B, C, D, E, F)*err_B)**2 + (res_diff_C(A, B, C, D, E, F)*err_C)**2 + (res_diff_D(A, B, C, D, E, F)*err_D)**2 + (res_diff_E(A, B, C, D, E, F)*err_E)**2 + (res_diff_F(A, B, C, D, E, F)*err_F)**2)
    if signs == 7:
        result = result_func(A, B, C, D, E, F, G)
        error_final = sqrt((res_diff_A(A, B, C, D, E, F, G)*err_A)**2 + (res_diff_B(A, B, C, D, E, F, G)*err_B)**2 + (res_diff_C(A, B, C, D, E, F, G)*err_C)**2 + (res_diff_D(A, B, C, D, E, F, G)*err_D)**2 + (res_diff_E(A, B, C, D, E, F, G)*err_E)**2 + (res_diff_F(A, B, C, D, E, F, G)*err_F)**2 + (res_diff_G(A, B, C, D, E, F, G)*err_G)**2)

    print("The result is: ", result)
    print("The uncertainty in the result is: ", error_final)
    cont = input("Would you like to enter another equation? (y/n): ")

input("Are you done reading the answer? ") #to let user read answer if in console
