import random
hands=['guu','choki','paa']

def start_message():
    print('janken - ')

def get_my_hand():
    print('my hand =')
    return input("0:'guu',1:'choki',2:'paa'")

def get_your_hand():
    return random.randint(0, 2)
    
    
def get_hand_name(hand_number):
    return hands[hand_number]


