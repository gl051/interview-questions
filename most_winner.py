"""
    GIVEN a list of tuple (Player, Won Games)
    THEN return the most winner player

    Input: [(Mark, 5), (Tom, 10), (John, 20)]
    Output: (John, 20)

"""
import heapq


def get_most_winner_player(player_game_report):
    if player_game_report is None or len(player_game_report) == 0:
        return None
    hp = []
    for tp in player_game_report:
        heapq.heappush(hp, tp)
    # get a list as a result, convert it to tuple
    return heapq.nlargest(1, hp, key=__sort_function).pop()


def __sort_function(tuple_player):
    # Given (player, score) returns score
    return tuple_player[1]
