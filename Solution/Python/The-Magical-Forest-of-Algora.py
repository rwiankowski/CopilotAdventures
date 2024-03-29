from enum import Enum

class DanceMove(Enum):
    TWIRL = "twirl"
    LEAP = "leap"
    SPIN = "spin"

class Character:
    def __init__(self, name):
        self.name = name

    def dance(self, moves):
        if len(moves) != 5:
            raise ValueError("Exactly 5 moves must be provided")
        for move in moves:
            if not isinstance(move, DanceMove):
                raise ValueError("All moves must be instances of DanceMove Enum")
        return [f"{self.name} is doing a {move.value}!" for move in moves]

def main():
    first_character_moves = []
    second_character_moves = []

    first_character_name = input("Enter the name of the first character: ")
    first_character = Character(first_character_name)

    second_character_name = input("Enter the name of the second character: ")
    second_character = Character(second_character_name)

    def get_dance_moves(character):
        moves = []
        for i in range(5):
            while True:
                move = input(f"Enter the dance move {i+1} for {character.name}: ")
                try:
                    move_enum = DanceMove(move.lower())
                    moves.append(move_enum)
                    break
                except ValueError:
                    print("Invalid move. Please enter a valid move from the DanceMove enum.")
        return moves

    first_character_moves = get_dance_moves(first_character)
    second_character_moves = get_dance_moves(second_character)

    for move1, move2 in zip(first_character_moves, second_character_moves):
        if move1 == DanceMove.TWIRL and move2 == DanceMove.TWIRL:
            print("Fireflies light up the forest.")
        elif move1 == DanceMove.LEAP and move2 == DanceMove.SPIN:
            print("Gentle rain starts falling.")
        elif move1 == DanceMove.SPIN and move2 == DanceMove.LEAP:
            print("A rainbow appears in the sky.")
        else:
            print("No special effect.")

  

    
print('Welcome to the Magical Forest of Algora!')
main()