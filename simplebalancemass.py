### SIMPLE STEADY STATE BATCH MASS BALANCE CALCULATOR

import numpy as np

def get_ins_outs():
    while True:
        try:
            input_inlets_num = int(input("Give the amount of inlets:\n"))
        except ValueError as invalid_input:
            print(invalid_input)
            print("Invalid value given, must be a number\n")
        else:
            while True:
                try:
                    input_outlets_num = int(input("Give the amount of outlets:\n"))
                except ValueError as invalid_input:
                    print(invalid_input)
                    print("Invalid value given, must be a number\n")
                else:
                    print(f"Number of inlets: {input_inlets_num}\nNumber of outlets: {input_outlets_num}")
                    return input_inlets_num, input_outlets_num

inlets_num, outlets_num = get_ins_outs()

print(inlets_num)



