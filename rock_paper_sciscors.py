import random
choices=["rock","paper","scissors"]
player_score=0
ai_score=0
draws=0
player_history=[]
def get_player_move():
    while True:
        move=input("Choose rock, paper, scissors, or quit: ").lower().strip()
        if move in choices:
            return move
        elif move=="quit":
            return "quit"
        else:
            print("Invalid choice.")
def get_ai_move():
    if len(player_history)<3:
        return random.choice(choices)
    last_move=player_history[-1]
    if random.random()<0.6:
        if last_move=="rock":
            return "paper"
        elif last_move=="paper":
            return "scissors"
        else:
            return "rock"
    return random.choice(choices)
def determine_winner(player,ai):
    if player==ai:
        return "draw"
    if (player=="rock" and ai=="scissors") or (player=="paper" and ai=="rock") or (player=="scissors" and ai=="paper"):
        return "player"
    return "ai"
def display_scores():
    print("-------------------------")
    print(f"Your score: {player_score}")
    print(f"AI score: {ai_score}")
    print(f"Draws: {draws}")
    print("-------------------------")
def main():
    global player_score,ai_score,draws
    print("ROCK PAPER SCISSORS AI GAME")
    print("Beat the AI!")
    print("Type 'quit' to exit.")
    while True:
        player_move=get_player_move()
        if player_move=="quit":
            break
        ai_move=get_ai_move()
        print(f"You chose: {player_move}")
        print(f"AI chose: {ai_move}")
        winner=determine_winner(player_move,ai_move)
        if winner=="player":
            print("You win!")
            player_score+=1
        elif winner=="ai":
            print("AI wins!")
            ai_score+=1
        else:
            print("It's a draw!")
            draws+=1
        player_history.append(player_move)
        display_scores()
    print("GAME OVER")
    print(f"Your score: {player_score}")
    print(f"AI score: {ai_score}")
    print(f"Draws: {draws}")
if __name__=="__main__":
    main()