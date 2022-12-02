import time

def part_one():

    with open('./list.txt', 'r') as day_one_list:

        highest_calorie_count = 0
        current_calorie_count = 0

        for line in day_one_list:

            current_val = line.strip()

            if bool(current_val):
                current_calorie_count = current_calorie_count + int(current_val)
            else:
                highest_calorie_count = max(current_calorie_count, highest_calorie_count)
                current_calorie_count = 0

    return highest_calorie_count


def part_two():
    
    snack_stack = []

    with open('./list.txt', 'r') as day_one_list:

        current_calorie_count = 0

        for line in day_one_list:

            current_val = line.strip()

            if bool(current_val):
                current_calorie_count = current_calorie_count + int(current_val)
            else:
                snack_stack = sorted([*snack_stack, current_calorie_count], reverse=True)[:3]
                current_calorie_count = 0

    return sum(snack_stack)

print("part_one : ", part_one())
print("part_two : ", part_two())
