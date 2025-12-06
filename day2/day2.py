import textwrap
from test_cases import file_path, test_case

def instructions(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


puzzle_input = instructions(test_case).split(",")
sku_addition = 0


for input in puzzle_input:
    hi_lo_options = input.split("-")
    low_range = int(hi_lo_options[0]) 
    high_range = int(hi_lo_options[1])

    for num in range(low_range, high_range+1):
        num_str = str(num)
        counter = 0
        broken_str = textwrap.wrap(num_str)
        if set(broken_str):
            sku_addition += num
        
        if not len(num_str) % 2:
            split_by = len(num_str)/2
            first_half = num_str[:int(split_by)]
            second_half = num_str[int(split_by):]
            broken_str = textwrap.wrap(num_str)
            if int(first_half) == int(second_half) and not set(broken_str):
                sku_addition += num
                counter = 1
        
        if counter != 1:
            for i in range(len(num_str)):
                broken_str = textwrap.wrap(num_str, i+1)
                if set(int(broken_str)):
                    print(broken_str)
                    sku_addition += num
            




print(sku_addition)
