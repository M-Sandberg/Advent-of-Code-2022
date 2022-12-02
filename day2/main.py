
def get_pick_translation(pick):

    translations = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors'
    }

    return translations.get(pick)


def calculate_reward(opponent_pick, self_pick):

    rewards = {
        'Rock': {
            'Rock': 4,
            'Paper': 8,
            'Scissors': 3
        },
        'Paper': {
            'Rock': 1,
            'Paper': 5,
            'Scissors': 9
        },
        'Scissors': {
            'Rock': 7,
            'Paper': 2,
            'Scissors': 6
        },
    }

    return rewards.get(opponent_pick, {}).get(self_pick)


def wallhack_prediction(opponent_pick, self_pick_code):

    responses = {
        'Y': {'Rock': 'Rock', 'Paper': 'Paper', 'Scissors': 'Scissors'},
        'X': {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'},
        'Z': {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'},
    }

    return responses.get(self_pick_code, {}).get(opponent_pick)


def part_one():

    total_score = 0

    with open('./input.txt', 'r') as day_one_list:
        for line in day_one_list:
            opponent_pick = get_pick_translation(line.strip().split(" ")[0])
            my_pick = get_pick_translation(line.strip().split(" ")[1])
            total_score += calculate_reward( opponent_pick, my_pick )

    return total_score


def part_two():

    total_score = 0

    with open('./input.txt', 'r') as day_one_list:
        for line in day_one_list:
            opponent_pick = get_pick_translation(line.strip().split(" ")[0])
            my_pick = wallhack_prediction( opponent_pick, line.strip().split(" ")[1] )
            total_score += calculate_reward(opponent_pick, my_pick)

    return total_score


print(part_one())
print(part_two())
