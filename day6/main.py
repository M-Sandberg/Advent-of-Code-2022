
def part_one(msg):
    for idx in range(0, len(msg), 1):
        if len(set(msg[idx:idx+4])) == len(msg[idx:idx+4]):
            return idx + 4

def part_two(msg):
    for idx in range(0, len(msg), 1):
        if len(set(msg[idx:idx+14])) == len(msg[idx:idx+14]):
            return idx + 14

with open('./list.txt', 'r') as day6_data:
    msg = day6_data.readlines()[0]
    print(part_one(msg))
    print(part_two(msg))

