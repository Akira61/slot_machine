import random

MAX_LINES = 3 # max lines to bet on
MAX_BET = 100 # max amount of bet for each line
MIN_BET = 1 # min amount of bet for each line

# slot machine settings
ROWS = 3 
COLS = 3

symbols = {
    # symbol: the amount of symbol on each column
    " 🍉 ": 2,
    " 🍋 ": 4,
    " 🍇 ": 6,
    " 🍓 ": 8,
    " 7️⃣ ": 1
}

symbols_value = {
    " 🍉 ": 5,
    " 🍋 ": 3,
    " 🍇 ": 7,
    " 🍓 ": 2,
    " 7️⃣ ": 10
}

def check_winnings(columns, lines, bet, symbols_value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbols_value[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def run_slot(rows, cols, symbols):
    all_symbols = []
    for (symbol, amount) in symbols.items():
        for _ in range(amount):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = [] # store column's symbols here
        # make copy of all symbols so we can't exceed the amount of symbols specified for each symbol
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)  
        
        columns.append(column)
        
    return columns 

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("\nWhat is your deposit💰: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 00️⃣.")
        else:
            print("Please enter a number🔢.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"\nWhat is the number of lines to bet on (1-{MAX_LINES})🔢: ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("The amount of lines to bet on are between 1 to 3🔢.")
        else:
            print("Please enter a number🔢.")
    return lines

def get_bet():
    while True:
        amount = input("\nHow mutch would you like to bet on each line🪙: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between (${MIN_BET}-${MAX_BET})💵.")
        else:
            print("Please enter a number🔢.")
    return amount

def game(balance):
    lines = get_number_of_lines()
    # make sure bet is on range of balance
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your bet is out of range of your balance💸.\n Total bet is ${total_bet}💵. \n Your current balance is ${balance}💰")
        else:
            break
    print(
        f"""
            🧾
            Your Bet Is ${bet}🪙.
            On {lines} Lines🔢.
            Total Bet is ${total_bet}💵.
            Deposit is ${balance}💰.
            🧾
        """.title()
    )
    
    slots = run_slot(ROWS, COLS, symbols)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print(f"you won ${winnings}🤑".upper())
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def play():
    print("\n🎰 Welcome to slot game 🎰\n".title())
    balance = deposit()
    while True:
        if balance == 0:
            break
        print(f"current balance is ${balance}💰".title())
        spin = input("Press enter to play (q to quit)🕹️: ")
        if spin.lower() == 'q' :
            break
        balance += game(balance)
    
    print(f"You Left With ${balance}💰")

play()