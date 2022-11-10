# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
# is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
# (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

# Example scoring

#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
import timeit

def score(dice):
    score = 0
    dice_dict, score_dict = {}, {5: 50, 1: 100}
    for one_dice in dice:
        dice_dict[one_dice] = dice.count(one_dice)
        
    for k, v in dice_dict.items():
        if k == 1:
            if v >= 3:
                score += 1000 + ((dice_dict[k] - 3) * score_dict[k])
            else:
                score += dice_dict[k] * score_dict[k]
        
        if k == 5:
            if v >= 3:
                score += 500 + ((dice_dict[k] - 3) * score_dict[k])
            else:
                score += dice_dict[k] * score_dict[k]
            
        if k == 2 and v >= 3:
            score += 200
        elif k == 3 and v >= 3:
            score += 300
        elif k == 4 and v >= 3:
            score += 400
        elif k == 6 and v >= 3:
            score += 600
    
    return score

#Tests
test_cases = {250: (5,1,3,4,1), 1100: (1,1,1,3,1), 450: (2,4,4,5,4)}
for k, v in test_cases.items():
    if score(v) != k:
        print(f'score({v}) != {k} -> NOT OK!')
    else:
        print(f'score({v}) == {k} -> OK!')
