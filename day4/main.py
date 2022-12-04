
def part_one( assignment_pairs_list ):

    total_fully_overlapping_pairs = 0

    for pair in assignment_pairs_list:
        section1, section2 = pair

        section1_range = range(section1[0], section1[1] + 1)
        section2_range = range(section2[0], section2[1] + 1)

        overlap_case1 = section1[0] in section2_range and section1[1] in section2_range
        overlap_case2 = section2[0] in section1_range and section2[1] in section1_range

        if overlap_case1 or overlap_case2:
            total_fully_overlapping_pairs += 1

    return total_fully_overlapping_pairs

def part_two( assignment_pairs_list ):

    total_overlapping_pairs = 0

    for pair in assignment_pairs_list:
        section1, section2 = pair

        section1_range = range(section1[0], section1[1] + 1)
        section2_range = range(section2[0], section2[1] + 1)

        overlap_case1 = section1[0] in section2_range or section1[1] in section2_range
        overlap_case2 = section2[0] in section1_range or section2[1] in section1_range

        if overlap_case1 or overlap_case2:
            total_overlapping_pairs += 1

    return total_overlapping_pairs

def split_str_value( s ):
    section_1, section_2 = s.split(",")[0], s.split(",")[1]
    section_1_int_1, section_1_int_2 = section_1.split('-')[0], section_1.split('-')[1]
    section_2_int_1, section_2_int_2 = section_2.split('-')[0], section_2.split('-')[1]
    return [(int(section_1_int_1), int(section_1_int_2)), (int(section_2_int_1), int(section_2_int_2))]

with open('./list.txt', 'r') as day_three_list:
    assignment_pairs_list = [ split_str_value(line.strip()) for line in day_three_list  ]
    print(part_one(assignment_pairs_list))
    print(part_two(assignment_pairs_list))