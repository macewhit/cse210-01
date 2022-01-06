"""
A Tic-Tac-Toe game
Author: Macy Whitney
"""

def print_board(options):
    print(f"""
        {options[0]} | {options[1]} | {options[2]}
        {options[3]} + {options[4]} + {options[5]}
        {options[6]} | {options[7]} | {options[8]}
        """
    )

def get_input(whose_turn, options):
    """ Gets players' input and prevents them from invalid entries"""
    while True:
        try:
            p = int(input(f"{whose_turn}'s turn: "))
            if p <= 0 or p > 9:
                print("That's not an option. Try again!")
                continue
            if options[p-1] == 'O':
                print("That's already taken. Try again!")
                continue
            if options[p-1] == 'X':
                print("That's already taken. Try again!")
                continue
            return p
        except ValueError:
            continue

def check_end_game(options):
    if options[0] == options[1] == options[2]:
        print(f"{options[0]} wins!")
        return True
    elif options[3] == options[4] == options[5]:
        print(f"{options[3]} wins!")
        return True
    elif options[6] == options[7] == options[8]:
        print(f"{options[6]} wins!")
        return True
    elif options[0] == options[3] == options[6]:
        print(f"{options[0]} wins!")
        return True
    elif options[1] == options[4] == options[7]:
        print(f"{options[1]} wins!")
        return True
    elif options[2] == options[5] == options[8]:
        print(f"{options[2]} wins!")
        return True
    elif options[0] == options[4] == options[8]:
        print(f"{options[0]} wins!")
        return True
    elif options[2] == options[4] == options[6]:
        print(f"{options[2]} wins!")
        return True
    for option in options:
        if isinstance(option, int):
            return False
    print(f"Cat's game!")
    return True

def main():
    print("Let's play Tic Tac Toe!")

    # Create options for users to pick from to place their X or O
    options = [1,2,3,4,5,6,7,8,9]

    print_board(options)

    # updates board with users' placement
    while True:
        p1 = get_input("X", options)
        options[p1-1] = 'X'
        print_board(options)
        if check_end_game(options):
            break


        p2 = get_input("O", options)
        options[p2-1] = 'O'
        print_board(options)
        if check_end_game(options):
            break

if __name__ == "__main__":
    main()
