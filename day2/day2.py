
from test_cases import file_path, test_case

def instructions(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

puzzle_input = instructions(test_case).split(",")
sku_addition = 0

for input in puzzle_input:
    hi_lo_options = input.split("-")
    low_option = int(hi_lo_options[0])
    high_option = int(hi_lo_options[1])
    for i in range(low_option, high_option+1):
        print(i)
        