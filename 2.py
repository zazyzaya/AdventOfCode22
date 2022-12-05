ROCK = 'A'
PAPER = 'B'
SCISSOR = 'C'

P2_MAP = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSOR
}

# Beaten by 
BEATS = {
    ROCK: PAPER,
    PAPER: SCISSOR,
    SCISSOR: ROCK
}

BONUS = {
    ROCK: 1,
    PAPER: 2,
    SCISSOR: 3
}

WIN_BONUS = 6
TIE_BONUS = 3
LOSS_BONUS = 0 

def score(p1,p2):
    if p1==p2: 
        return TIE_BONUS+BONUS[p2]

    if BEATS[p1] == p2:
        return WIN_BONUS+BONUS[p2]
    else:
        return LOSS_BONUS+BONUS[p2]


with open('data.txt', 'r') as f:
    data = f.read()
    

###### PART 1 #####
def simulate(games):
    tot_score = 0
    for game in games.split('\n'):
        p1,p2 = game.split(' ')
        p2 = P2_MAP[p2]
        tot_score += score(p1,p2)

    return tot_score

print(simulate(data))


##### PART 2 ######
LOSE = 'X'
TIE = 'Y'
WIN = 'Z'
loses_to = {v:k for k,v in BEATS.items()}
def new_p2_map(p1,p2):
    if p2 == TIE:
        return p1 
    elif p2 == WIN: 
        return BEATS[p1]
    else: 
        return loses_to[p1]

def simulate2(games):
    tot_score = 0
    for game in games.split('\n'):
        p1,p2 = game.split(' ')
        p2 = new_p2_map(p1,p2)
        tot_score += score(p1,p2)

    return tot_score

print(simulate2(data))