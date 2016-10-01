"""
Macalester, COMP 221, HWA, Prof. Shilad Sen

Duc Le - Collaborator: Trung Nguyen, Tuyet-Anh Tran

This is a skeleton of a program to analyze ISC earthquake data. Your job is to
complete two functions. The description below and comments in the script should
guide your work.

Each earthquake has three pieces of data associated with it: a latitude, a longitude,
and a strength. A quake is represented as a Python dictionary, with the following
format:

    {'lat': -10.0, 'strength': 7.58, 'long': 165.0}

Your job is to write a function that takes a list of quakes, a query point, and a
radius. It should calculate and return two numbers: the number of quakes within
radius distance of the query point, and the average strength of these matching quakes.

As a reminder, the Euclidean distance between two points (x0, y0) and (x1, y1)
can be calculated as:

    sqrt( (x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1) )

More details on the parameter and return types are specified in the comment below.

Your program is evaluated (for accuracy and speed) against a set of test questions
with known answers. I have supplied three different test files with 5, 100, and 1000
questions, respectively.

If you run the program right now it would run against the 5-question file and you
would see something like the following:

    for question question-0 expected n=0, mean=0.000, received n=-1, mean=0.000
    for question question-1 expected n=0, mean=0.000, received n=-1, mean=0.000
    for question question-2 expected n=117, mean=5.916, received n=-1, mean=0.000
    for question question-3 expected n=110, mean=5.918, received n=-1, mean=0.000
    for question question-4 expected n=0, mean=0.000, received n=-1, mean=0.000
    analyzed 5 queries in 0.000 seconds (36220.242 queries / second)

To do your work, complete the following steps. Create a large block comment below
(like this one) to answer the questions.

1. Start by creating a brute force working implementation of the analyze_quakes
function. Benchmark this against all three files. List your results, and state
the complexity of a single call to analyze_quakes. Make sure you include all
necessary parameters representing the problem. Justify your answer. For a frame
of reference, my working brute-force version achieved the following results:

    analyzed 5 queries in 0.030 seconds (167.819 queries / second)
    analyzed 100 queries in 0.630 seconds (158.706 queries / second)
    analyzed 1000 queries in 6.043 seconds (165.477 queries / second)

2. Create an optimized version of analyze_quakes. You will probably need to
create some global data structures in the init_earthquake_analyzer function
to speed up your queries. Once again benchmark your program and analyze the time
complexity of a single call to analyze_quakes.

If you are uncertain about this problem, post your questions to Piazza!

"""

"""Answer to questions:
    Question 1:
    The time complexity of a single call analyze_quakes is O(n), with n is the number of quakes in the list of quakes.
    In this case, the Big-O, Big-Omega and Big-Theta all have the same value.
    My working brute-force version achieved the following results:

    analyzed 5 queries in 0.022 seconds (227.294 queries / second)
    analyzed 100 queries in 0.421 seconds (237.810 queries / second)
    analyzed 1000 queries in 3.917 seconds (255.311 queries / second)

    Question 2:
    Based on the original quakes list, I have sorted the quakes list in term of latitude, and then create a global variable
    list named lstLat to keep track only the latitude in sorted order. After that, I created a helper function to take all
    the latitude values of all quakes in the sorted quakes list and add them to lstLat.
    When come to the analyze_quake function, first I used a built-in module in Python named bisect to find the index of the
    leftmost and rightmost value of latitudes that are in the range from center_lat-radius and center_lat+radius. Because the
    index of latitude in lstLat will also be the index of the relevant quake in quakes list (we already sorted quakes), I can take
    a sub list of quakes that are candidates for being in the given radius from the query. And now, I only need to check the distance
    from my query to a much less number of quakes to confirm which one is in suitable range.

    With this approach, my bisect will need O(log n) (actually Big-theta, not Big-O) to complete the search for the indices. After that
    it needs to loop through a sub list with m element, but this number (m) is way more smaller than n, and the function (log n)+m will
    have the Big-Theta is log n. Therefore, in general, our new approach will have the time complexity is O(log n).

"""

import random
import time
import bisect

# Define the global variable list to hold the latitudes sorted, use for optimized code
lstLat = []

def main():
    quakes = read_quakes()
    # Sort quakes in order of latitude. Use for optimized code, comment this step to use brute force
    quakes = init_earthquake_analyzer(quakes)

    benchmark(quakes, 'random_questions.5.txt')

    # Once you get the above benchmark working
    # uncomment the following to perform a more robust benchmark.
    benchmark(quakes, 'random_questions.100.txt')
    benchmark(quakes, 'random_questions.1000.txt')

def init_earthquake_analyzer(quakes):
    """
    Perform any data structure intialization needed for your algorithm.
    Note that the brute force algorithm will not need to do ANYTHING here.
    More sophisticated algorithms will need to initialize global variables
    associated with data structures needed by their algorithm

    :param quakes: List of quakes as returned by read_quakes
    """
    # Sort the quakes list by latitude
    sortlist = sorted(quakes, key=lambda k: (k["lat"]))
    # With the sorted quakes list, fill in the latitude list with the right order
    init_sortListLat(sortlist)

    return sortlist

def init_sortListLat(sortlist):
    """
    This function will fill in the latitude list in sorted order, the same order with sorted quakes list.
    This is used for optimized code, ignore it when use brute force.
    :param sortlist: the sorted quakes list
    :return: none
    """
    global lstLat

    for quake in sortlist:
        lstLat.append((quake["lat"]))

def analyze_quakes(quakes, center_lat, center_long, radius):
    """
    Analyzes matching earthquakes.

    :param quakes: List of quakes as returned by read_quakes
    :param center_lat: A float containing the latitude for the query point.
    :param center_long:A float containing the longitude for the query point.
    :param radius: The radius for the query. All earthquakes within the radius
    of the center point match.

    :return: A two-tuple of (num_matches, mean_match_strength). Where
    num_matches is an int containing the number of earth quakes that fell
    inside the geographic constraints and mean_match_strength is the
    mean strength for matching quakes, or 0.0 if none matched.
    """
    global lstLat
    # The variables to keep track on number of quake and sum of strength of quakes in the given radius from query.
    sumStrength = 0
    num_matches = 0
    # The variable with value of squared radius, use to compare with squared distance to avoid using sqrt in math module.
    radius2 = radius*radius

    # Optimized code
    # Find the index of first element has higher or equal latitude with center_lat-radius
    centerRad1 = bisect.bisect_left(lstLat,center_lat-radius)
    # Find the index of first element has higher or equal latitude with center_lat+radius
    centerRad2 = bisect.bisect_left(lstLat,center_lat+radius)
    # Loop through the sub list of quakes that have latitude from center_lat-radius to center_lat+radius
    for quake in quakes[centerRad1:centerRad2]:
        x1 = quake["lat"]
        y1 = quake["long"]
        # Calculate the squared distance between the center point and the center of the quake.
        distance_square = (x1 - center_lat) * (x1 - center_lat) + (y1 - center_long) * (y1 - center_long)
        if distance_square <= radius2:
            num_matches += 1
            sumStrength += quake["strength"]
    if num_matches == 0:
        return 0, 0
    else:
        mean_match_strength = sumStrength / num_matches;
        return num_matches, mean_match_strength

    # Brute force code

    # for quake in quakes:
    #     # Calculate the distance between the center point and the center of the quake.
    #     x1 = quake["lat"]
    #     y1 = quake["long"]
    #     if x1<=center_lat+radius and y1<=center_long+radius:
    #         if x1<=center_lat+radius:
    #             distance = (x1 - center_lat) * (x1 - center_lat) + (y1 - center_long) * (y1 - center_long)
    #             if distance <= radius2:
    #                 num_matches += 1
    #                 sumStrength += quake["strength"]
    # if num_matches == 0:
    #     return 0, 0
    # else:
    #     mean_match_strength = sumStrength / num_matches;
    #     return num_matches, mean_match_strength



def read_quakes():
    """
    Creates a list of all quake records.
    Each record is a dictionary with time, latitude, longitude, and string.
    For example, the very first record looks like:

    {'lat': -10.0, 'strength': 7.58, 'long': 165.0}

    """
    quakes = []
    with open('isc-gem-cat.csv') as f:
        for line in f:
            if line.startswith('#'):
                continue
            tokens = line.split(',')
            timestamp = tokens[0].strip()
            if timestamp < '1960': continue     # Ignore entries during time period with partial data
            lat = float(tokens[1])
            long = float(tokens[2])
            strength = float(tokens[10])
            quakes.append({
                'lat' : lat,
                'long' : long,
                'strength' : strength
            })
    return quakes


def example(quakes):
    """
    This example shows how to read in the earth quake data
    You may find the examples below a useful skeleton for your
    """
    n = 0
    sumLats = 0.0
    sumLongs = 0.0
    sumStrengths = 0.0

    for quake in quakes:
        n += 1
        sumLats += quake['lat']
        sumLongs += quake['long']
        sumStrengths += quake['strength']

    print('observed %d quakes' % n)
    print('mean strength was %.3f' % (sumStrengths / n))
    print('mean location was (lat=%.3f, long=%.3f)' % (sumLats/ n, sumLongs / n))


def benchmark(quakes, question_path):
    """
    This function runs the benchmarking program for your query analyzer
    :param question_path:
    :return:
    """
    t0 = time.time()
    nLines = 0
    with open(question_path) as f:
        for line in f:
            (id, lat, long, radius, n, mean) = line.split(',')
            lat = float(lat)
            long = float(long)
            radius = float(radius)
            correct_n = int(n)
            correct_mean = float(mean)
            (n, mean) = analyze_quakes(quakes, lat, long, radius)
            if correct_n != n or abs(correct_mean - mean) > 0.0001:
                print('for question %s '
                      'expected n=%d, mean=%.3f, '
                      'received n=%d, mean=%.3f' %
                      (id, correct_n, correct_mean, n, mean))
            nLines += 1
    t1 = time.time()
    dt = t1 - t0
    print('analyzed %d queries in %.3f seconds (%.3f queries / second)' % (nLines, dt, nLines / dt))

def write_questions_file(path, num_questions):
    """
    This function was used by me to create the questions files.
    You do not need to use it.
    :param path:
    :param num_questions:
    :return:
    """
    quakes = read_quakes()
    init_earthquake_analyzer(quakes)
    with open(path, 'w') as f:
        for i in range(num_questions):
            lat = random.uniform(-160.0, +160.0)
            long = random.uniform(70.0, +70.0)
            radius = random.uniform(0, 20)
            (n, mean) = analyze_quakes(quakes, lat, long, radius)
            f.write('question-%d,%f,%f,%f,%d,%f\n' % (i, lat, long, radius, n, mean))

if __name__ == '__main__':
    main()
