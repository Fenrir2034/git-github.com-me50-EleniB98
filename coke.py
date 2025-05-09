def calculate_change(coins_inserted):
    """
    Calculate the change owed based on the coins inserted.
    """
    total_amount = sum(coins_inserted)
    change_owed = max(0, total_amount - 50)
    return change_owed

def main():
    accepted_coins = [25, 10, 5]
    coins_inserted = []

    while True:
        # Prompt user to insert a coin
        coin = input("Insert Coin: ")

        try:
            # Convert input to integer and check if it's an accepted coin denomination
            coin_value = int(coin)
            if coin_value in accepted_coins:
                coins_inserted.append(coin_value)
                amount_due = 50 - sum(coins_inserted)
                if amount_due > 0:
                    print(f"Amount Due: {amount_due}")
                elif amount_due == 0:
                    print("Change Owed: 0")
                    break  # Terminate the loop when exactly 50 cents is reached
                else:
                    print(f"Change Owed: {abs(amount_due)}")
                    break
            else:
                if sum(coins_inserted) >= 50:
                    print(f"Amount Due: 50\nChange Owed: {calculate_change(coins_inserted)}")
                    break
                else:
                    print("Invalid coin denomination. Please insert a valid coin. Amount Due: 50")
        except ValueError:
            print("Invalid input. Please insert a valid coin.")

if __name__ == "__main__":
    main()

