
def part_one_and_two(msg, unique_req):
    for idx in range(0, len(msg), 1):
        if len(set(msg[idx:idx+unique_req])) == len(msg[idx:idx+unique_req]):
            return idx + unique_req

with open('./list.txt', 'r') as day6_data:
    msg = day6_data.readlines()[0]
    print(part_one_and_two(msg, 4))
    print(part_one_and_two(msg, 14))

