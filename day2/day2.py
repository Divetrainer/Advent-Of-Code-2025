
from test_cases import file_path, test_case

def instructions(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

puzzle_input = instructions(file_path).split(",")
sku_addition = 0

for input in puzzle_input:
    hi_lo_options = input.split("-")
    low_range = int(hi_lo_options[0])
    high_range = int(hi_lo_options[1])
    for num in range(low_range, high_range+1):
        num_str = str(num)
        
        if not len(num_str) % 2:
            split_by = len(num_str)/2
            first_half = num_str[:int(split_by)]
            second_half = num_str[int(split_by):]
            if int(first_half) == int(second_half):
                sku_addition += num

print(sku_addition)
