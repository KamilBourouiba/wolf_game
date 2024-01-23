import random

def make_the_pool(players):
    count_occurrences_wolf = players.count("Wolf")
    count_occurrences_villager = players.count("Villager")
    return count_occurrences_wolf, count_occurrences_villager

def vote(players):
    return [random.randint(1, 10) for _ in range(len(players))]  # Random votes for each player

def kill_someone(players):
    target_players = [i for i, role in enumerate(players) if role == "Villager"]
    if target_players:
        target_index = random.choice(target_players)
        players.pop(target_index)
    return players

def vote_someone(players):
    remaining_villagers = [role for role in players if role == "Villager"]
    if not remaining_villagers:
        return players

    votes = vote(players)
    max_vote = max(votes)
    voted_players = [i for i, vote in enumerate(votes) if vote == max_vote]

    if len(voted_players) == 1:
        players.pop(voted_players[0])

    return players

def play_game(wolf, villager):
    round_count = 1
    players = ["Wolf"] * wolf + ["Villager"] * villager

    while True:
        wolf_count, villager_count = make_the_pool(players)
        players = kill_someone(players)
        players = vote_someone(players)

        if wolf_count == 0:
            return "Villagers"
        elif villager_count == 0:
            return "Wolves"

        round_count += 1

def simulate_game(iterations, wolf, villager):
    villagers_win_count = 0
    wolves_win_count = 0

    print("\nSimulation Progress:")
    
    for iteration_number in range(iterations):
        result = play_game(wolf, villager)
        if result == "Villagers":
            villagers_win_count += 1
        else:
            wolves_win_count += 1

        progress = int((iteration_number + 1) / iterations * 100)
        print("\r[" + "=" * progress + " " * (100 - progress) + "] " + str(progress) + "%", end='', flush=True)

    print("\n\nSimulation Results:")
    print("Villagers win", villagers_win_count, "times")
    print("Wolves win", wolves_win_count, "times")

if __name__ == "__main__":
    iterations = int(input("How many iterations do you want to simulate? "))
    wolf = int(input("How many wolves do you want? "))
    villager = int(input("How many villagers do you want? "))

    simulate_game(iterations, wolf, villager)
