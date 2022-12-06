import re

def part_one( steps_arr, stack_arr ):

    for step in steps_arr:
        _move, _from, _to = step
        while _move:
            crate = stack_arr[_from - 1].pop()
            stack_arr[_to - 1].append(crate)
            _move -= 1

    return stack_arr

def part_two( steps_arr, stack_arr ):

    for step in steps_arr:

        _move, _from, _to = step

        if _move < 2:
            stack_arr[_to - 1].append(stack_arr[_from - 1].pop())

        else:
            stack_arr[_to - 1].extend( [ stack_arr[_from - 1].pop() for idx in range( _move ) ][::] )

    return stack_arr
    
steps = []

with open('./list.txt', 'r') as day_5_list:
    for line in day_5_list:
        m, f, t = [int( val ) for val in re.sub('move |from |to ', '', line.strip()).split(" ")]
        steps.append((m, f, t))

stacks = [
    ['T','Q','V','C','D','S','N'],
    ['V','F','M'],
    ['M','H','N','P','D','W','Q','F'],
    ['F','T','R','Q','D'],
    ['B','V','H','Q','N','M','F','R'],
    ['Q','W','P','N','G','F','C'],
    ['T','C','L','R','F','W'],
    ['S','N','Z','T'],
    ['N','H','Q','R','J','D','S','M']
]

print( "".join([el[len(el) -1 ] for el in part_one( steps, [ stack[::-1] for stack in stacks ] )]))
print( "".join([el[len(el) -1 ] for el in part_two( steps, [ stack[::-1] for stack in stacks ] )]))