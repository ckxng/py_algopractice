import math


def clock_angle(time_string, unit='degrees'):
    """
    for an input time such as "05:15", find the measure of the acute angle that is formed
    by the hour and minute hands on a standard 12-hour analog clock
    :param time_string: a time such as '05:15'
    :param unit: either 'degrees' or 'radians'
    :return: the measure of the angle rounded to four decimal points
    """
    (hour_string, minute_string) = time_string.split(':')
    (hour_segments, minute_segments) = (int(hour_string), int(minute_string) / 5.0)

    segment_value = None
    if unit == 'degrees':
        segment_value = 30
    elif unit == 'radians':
        segment_value = math.pi * 2 / 12

    return round(abs((hour_segments + (minute_segments / 12)) - minute_segments) * segment_value, 4)


def trapped_rain_water(arr):
    """
    For an array of positive numeric values, each element of the array represents
    the height of terrain capable of blocking water.
    :param arr: an array describing terrain height
    :return: the volume of water trapped within the terrain described by arr
    """
    larr = len(arr)
    volume = 0
    watermap = [0] * larr

    # initial pass, determine how much water can fill in from the left
    peak = 0
    for i in range(larr):
        # new or same peak, we are not adding water
        if peak <= arr[i]:
            peak = arr[i]
            continue

        # tentatively presume that the distance between the last peak and this height
        # is filled with water
        watermap[i] = peak - arr[i]

    # second pass, eliminate impossible amounts of water by finding right edges
    peak = 0
    for i in range(larr):
        # reverse the index
        i = larr - 1 - i

        # we found a new peak moving in reverse, this cell cannot add water
        if peak <= arr[i]:
            watermap[i] = 0
            peak = arr[i]
            continue

        # discover the cell's water level to the lesser of it's current water level (determined
        # by moving forward) or the current measured water level (determined by moving
        # in reverse) and add it to volume
        volume += min(watermap[i], peak - arr[i])

    return volume


def ideal_buy_and_sell_days(arr):
    """
    given an array representing stock prices on a daily basis,
    determine the best days to buy and sell
    :param arr: an array representing a series of stock prices
    :return: a tuple containing the index of an ideal buy day, and the index of an ideal selling day
    """
    # the first element is always the lowest price at the start
    trailing_low_index = 0
    best_buy_index = 0
    best_profit = 0
    best_sell_index = None

    for i in range(len(arr)):
        # found a new low price, obviously not a buying day
        if arr[i] < arr[trailing_low_index]:
            trailing_low_index = i
            continue

        # never sell at a loss
        if arr[i] < arr[trailing_low_index]:
            continue

        # new best trading days found
        test_profit = arr[i] - arr[trailing_low_index]
        if test_profit > best_profit:
            best_buy_index = trailing_low_index
            best_sell_index = i
            best_profit = test_profit

    return [best_buy_index, best_sell_index]


def possible_game_scores(score):
    """
    given a game with three possible scores per round (1, 2, and 3), return
    a list of lists containing every possible scenario for a user's scores
    that could add up to the provided score
    :param score: the target score
    :return: a list of list of all possible game scenarios adding up to score
    """
    score_collection = []

    # done recursing
    if score == 0:
        return []

    for move in range(1, 4):  # 1..3
        # don't consider this option if we cannot make this move because it would exceed
        # the target score
        if move > score:
            continue

        # if this is the last possible move, append it and move on
        if not score - move:
            score_collection.append([move])
            continue

        # find the possible remaining moves
        found_scores = possible_game_scores(score - move)

        # add this game scenario to our collection of scores
        for game in found_scores:
            score_collection.append([move] + game)

    return score_collection


def find_duplicates(arr):
    """
    find the duplicates in a list
    :param arr: list to search
    :return: list containing unique duplicate elements
    """
    cache = {}
    dupe = {}

    for e in arr:
        try:
            cache[e]  # raise an error if not found
            dupe[e] = 1  # mark as a duplicate since we've previously seen one
        except KeyError as err:
            # the element has not been seen yet and is not a duplicate
            cache[e] = 1

    return list(dupe.keys())


def count_matching_pairs(arr, k):
    """
    given a unique sorted list, count the pairs of elements which sum to equal k.
    an element cannot pair with itself, and each pair counts as only one match.
    :param arr: a unique sorted list
    :param k: the target sum value
    :return: the number of elements which sum to equal k
    """
    forward_index = 0
    reverse_index = len(arr) - 1
    count = 0

    # if the array is empty or contains only one value, no matches are possible
    if reverse_index < 1:
        return 0

    while forward_index < reverse_index:
        test_sum = arr[forward_index] + arr[reverse_index]

        # we found a match, advance both the forward and reverse indexes
        if test_sum == k:
            count += 1
            forward_index += 1
            reverse_index -= 1

        # test sum is too low, we need bigger numbers.  advance forward_index
        elif test_sum < k:
            forward_index += 1

        # test sum is too high, we need smaller numbers.  advance reverse_index
        elif test_sum > k:
            reverse_index -= 1

    return count
