
from test_cases import file_path, test_case

def instructions(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def dupe_check(input_str, count=0):
    if count > len(input_str)/2:
        print("working")
        return False
    new_string = input_str[count:]
    old_string = input_str[:count]
    #print(new_string)
    #print(old_string)
    if not old_string == new_string:
        print("fail")
        count +=1
        dupe_check(input_str, count)
    return True
        

print(dupe_check("212121215"))


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
        string_hold = ""
        #if counter == 0 and dupe_check(num_str):
            #print(num)
        #    sku_addition += num



#print(sku_addition)
