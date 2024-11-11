import random

def generate_initial_piles(total_cards=45):
    piles = []
    remaining_cards = total_cards
    while remaining_cards > 0:
        pile = random.randint(1, remaining_cards)
        piles.append(pile)
        remaining_cards -= pile
    return piles

def solitaire_step(piles):
    new_pile = len(piles)
    piles = [pile - 1 for pile in piles if pile > 1]
    piles.append(new_pile)
    return piles

def is_final_configuration(piles):
    return sorted(piles) == list(range(1, 10))

def main():
    piles = generate_initial_piles()
    print(f"Initial configuration: {piles}")
    
    step = 0
    while not is_final_configuration(piles):
        piles = solitaire_step(piles)
        step += 1
        print(f"Step {step}: {piles}")
    
    print(f"Final configuration reached in {step} steps: {piles}")

if __name__ == "__main__":
    main()