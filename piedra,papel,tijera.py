##piedra,papel,tijera
import random 

def play ():
    user = input(" cual elegis?'r'para rock, 'p'para papel, 't'para tijera\n")
    computer = random.choice (['r','p','t'] )
    
    if user == computer:
         return 'It\'s a tie'

    #r > p, t > p, r > t
    if is_win(user, computer):
        return 'you won!'
    
    return 'you lost!'
    
    
    def is_win(jugador,oponente):
         #return true if player wins
         #r > s, s > p, p> r
        if (jugador == 'r' and oponente == 't') or (jugador == 't' and oponente == 'p') or (jugador == 'p' and oponente == 'r'):
            return True 

print(play())