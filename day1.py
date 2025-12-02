
file_path = "/home/ipohl/workspace/github.com/Divetrainer/Advent_of_Code/day1_input"
test_case = "/home/ipohl/workspace/github.com/Divetrainer/Advent_of_Code/day1_test"

def instructions(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

dial_inputs = instructions(file_path).split()
dial_start = 50
dial_position = dial_start
dial_movement = 0
zero_counts = 0
any_zero_count = 0
for input in dial_inputs:
    if input[0] == "L":
        # print(f"Left {input[1:]}")
        dial_movement = int(input[1:])
        for i in range(1, dial_movement+1):
            dial_position -= 1
            if dial_position == 0:
                any_zero_count += 1
            if dial_position == -1:
                dial_position = 99
                



    elif input[0] == "R":
        #print(f"Right {input[1:]}")
        dial_movement = int(input[1:])
        for i in range(1, dial_movement+1):
            dial_position += 1
            if dial_position == 100:
                dial_position = 0
                any_zero_count += 1
    
    if dial_position == 0:
        zero_counts += 1

print(zero_counts)
print(any_zero_count)