import random


def play():
    user = input(f"whats your choice ? 'r' for rock , 'p' for paper, 's' for sizer : \n ")
    computer = random.choice(['r','p','s'])
    print(computer)
    if user == computer:
        return 'Its a tie'  
    if user_wins(user,computer):
        return 'You won'
    
    return 'computer won'
    



def user_wins(player, opponent):
    if (player == 'r' and opponent == 's' ) or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


print(play())