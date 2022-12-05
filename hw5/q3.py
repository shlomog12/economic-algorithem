import numpy as np


def division_with_fewer_items_in_common(player1, player2, division1, division2):
    n = len(division1)
    check_if__index_of_incompletes_func = lambda i: (division1[i] < 1 and division1[i] > 0)
    index_of_incompletes = list(filter(check_if__index_of_incompletes_func, range(n)))
    
    # sort by "Orderly division"
    index_of_incompletes = sorted(index_of_incompletes, key=lambda i: player1[i]/player2[i]) 
    
    player2_loss = 0
    # Gives all items to Player1 and calculates how much Player2 lost
    for i in index_of_incompletes:
        division1[i] = 1
        player2_loss += division2[i] * player2[i]

    # This gives player 2 exactly how much he lost
    for i in index_of_incompletes:
        if player2[i] <= player2_loss:
                division1[i] = 0
                player2_loss -= player2[i]
        else:
            division1[i] = 1-player2_loss/player2[i]
            break
    return division1, [1-x for x in division1]






player2 = [10,20,30,40]
player1 = [40,30,20,10]
division2 = [0.7, 0.4, 0, 1]
division1 = [1-x for x in division2]
sum1 = np.array(division1).dot(player1)
sum2 = np.array(division2).dot(player2)
print(f'before: sum1 = {sum1} sum2 = {sum2}')


division1,division2 = division_with_fewer_items_in_common(player1,player2,division1,division2)
sum1 = np.array(division1).dot(player1)
sum2 = np.array(division2).dot(player2)
print(f'after: sum1 = {sum1} sum2 = {sum2}')

print(division1,division2)

player1 = [90,70,80]
player2 = [2,4,4]
division1 = [0, 1, 1]
division2 = [1-x for x in division1]

sum1 = np.array(division1).dot(player1)
sum2 = np.array(division2).dot(player2)
print(f'before: sum1 = {sum1} sum2 = {sum2}')


division1,division2 = division_with_fewer_items_in_common(player1,player2,division1,division2)
sum1 = np.array(division1).dot(player1)
sum2 = np.array(division2).dot(player2)
print(f'after: sum1 = {sum1} sum2 = {sum2}')


print(division1,division2)