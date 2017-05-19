import math, random

"""
This simulation is based on the exponential method in binary option. THe method is described below:
    Exponential method in binary option is the method in which player will try to cover their lost and gain profit in 
    in the next trade in the last trade was a lost. The investment amount depends on how much trader want to start with,
    how much money they have for capital, and how much profit they want to earn back.
    For example, the following rates are commonly used for starting point of $2:
        2   6   16  36  80  176 ...
    The rate is calculated by:
        nextRate = sum[previousRates] / (profitRate - ratioProfitWanted)
        Where: 
            nextRate: is the next amount of investment to put in
            sum[previousRates]: sum of all previous rates
            profitRate: the profit rate of the market
            ratioProfitWanted: the expected amount of money to earn for each trade (if win).
"""


def calculateRates(initialAmount, marketProfit, expectedProfit):
    """
    The method to calculate the rates sequences for a given initial amount of $.
    :param initialAmount: the initial amount to begin with
    :return: the list of 10 first rates to use for exponential method with that initial amount
    """
    listRates = []  # The list for use in dynamic programming
    listRates.append(initialAmount)

    for i in range(10):
        listRates.append(math.ceil(sum(listRates[:i+1]) / (marketProfit - expectedProfit)))

    return listRates


def simulation(numTransaction ,capital, initialAmount, marketProfit, expectedProfit):
    """
    This is the function to perform the simulation for the exponential method for binary option
    Each time the function run, it will take in an initial amount and the first investment to begin with
    The function will run until there has been 100 transactions made, or the player running out of money
    It will then show the total amount after the transactions.
    :param numTransaction: 
    :param capital: The capital amount the user has
    :param initialAmount: The initial investment to begin the exponential method
    :param marketProfit: The profit rate of the market
    :param expectedProfit: The expected profit from each transaction
    :return: the amount of money in balance after numTransaction transaction
    """
    minPrice = 0
    maxPrice = 100
    listOfRates = calculateRates(initialAmount, marketProfit, expectedProfit)
    pos = 0

    for i in range(numTransaction):
        if capital <= listOfRates[pos]:
            # print("The capital is: " + str(capital) + " but the rate now is: " + str(listOfRates[pos]))
            break
        else:
            guess = random.randrange(-1,2,2)    # -1 is put, 1 is call
            guessPrice = random.randrange(minPrice, maxPrice)
            finishedPrice = random.randrange(minPrice, maxPrice)
            if guessPrice < finishedPrice:
                # This is the case that call is true
                if guess == -1:
                    capital -= listOfRates[pos]
                    pos += 1
                else:
                    capital += listOfRates[pos]
                    pos = 0
            elif guessPrice > finishedPrice:
                # This is the case that put is true
                if guess == -1:
                    capital += listOfRates[pos]
                    pos = 0
                else:
                    capital -= listOfRates[pos]
                    pos += 1
    return capital


if __name__ == '__main__':
    print(calculateRates(2, 0.89, 0.3))
    countLost = 0
    listAmount = []
    for i in range(100):
        capital = simulation(20, 100, 3, 0.94, 0.3)
        listAmount.append(capital)
        if capital < 1000:
            countLost += 1
    print("The average capital after 100 times is: "+str(sum(listAmount)/100)+" with number of lost time is: "+str(countLost))
