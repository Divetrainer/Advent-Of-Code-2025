import textwrap
from test_cases import file_path, test_case

def instructions(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def dupe_check(input_str, count=1):
    if len(input_str) % count:
        return False
    broken_str = textwrap.wrap(input_str, count)
    for str in broken_str:
        print(str)
        if str != broken_str[count]:
            dupe_check(input_str, count+1)
    else:
        return True

    
    
    

if dupe_check("2222222223"):
    print("pass")

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
        #if dupe_check(num_str):
        #    print(f"***{num}***")
        #    sku_addition += num



#print(sku_addition)
