"""This is a tea party planner"""

__author__: str = "730736480"


def main_planner(guests: int) -> None:
    """This is the function for the main planner"""
    print("A Cozy Tea party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """This calculates the amount of tea bags"""
    return people * 2


def treats(people: int) -> int:
    """This function calculates the amount of treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This calculates the cost"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
