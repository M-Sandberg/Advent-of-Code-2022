
def part_one( backpack_list, priorities ):
        
    sum_priorities  = 0
    
    for backpack in backpack_list:

        first_compartment, second_compartment = (backpack[len(backpack) // 2:], backpack[:len(backpack) // 2])

        already_found = []

        for item in first_compartment:
            if item in second_compartment and item not in already_found:
                sum_priorities += priorities.index(item)
                already_found.append(item)

    return sum_priorities

def part_two( backpack_list, priorities ):

    sum_priorities  = 0
    
    list_len = len(backpack_list)

    for idx in range(2, list_len, 3):
        bp_one, bp_two, bp_three = backpack_list[idx - 2], backpack_list[idx -1], backpack_list[idx]

        for item in bp_one:

            if item in bp_two and item in bp_three:
                sum_priorities += priorities.index(item)
                break

    return sum_priorities

with open('./list.txt', 'r') as day_three_list:
    
    backpack_list = [ line.strip() for line in day_three_list  ]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    priorities = [None, *[letter.lower() for letter in letters], *[letter.upper() for letter in letters] ]

    print(part_one(backpack_list, priorities))
    print(part_two(backpack_list, priorities))