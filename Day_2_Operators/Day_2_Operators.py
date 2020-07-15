def perc(mealCost, percent):
    return mealCost * (percent/100)

if __name__ == "__main__":
    mealCost = float(input())
    tipPercent = int(input())
    taxPercent = int(input())

    totalCost = mealCost + perc(mealCost, tipPercent) + perc(mealCost, taxPercent)

    print(round(totalCost))    