
from test_cases import file_path, test_case

def instructions(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def dupe_check(input_str):
    for i in range(len(input_str)):
        if i == len(input_str)-1:
            return False
        elif input_str[i] == input_str[i+1]:
            if dupe_check(input_str[i+1:]):
                return True
        elif:
            if dupe_check(input_str)
        else:
            return False


puzzle_input = instructions(test_case).split(",")
sku_addition = 0


for input in puzzle_input:
    hi_lo_options = input.split("-")
    low_range = int(hi_lo_options[0])
    high_range = int(hi_lo_options[1])

    for num in range(low_range, high_range+1):
        num_str = str(num)
        counter = 0
        if not len(num_str) % 2:
            split_by = len(num_str)/2
            first_half = num_str[:int(split_by)]
            second_half = num_str[int(split_by):]
            if int(first_half) == int(second_half):
                sku_addition += num
                counter = 1

        #if counter == 0 and dupe_check(num_str):
            #print(num)
        #    sku_addition += num

print(dupe_check("12121212"))

print(sku_addition)
