"""erm this is the tea party exercise"""

__author__: str = "730747262"


def main_planner(guests: int) -> None:
    """this function gathers all the data and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Total Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """this will show how many tea bags we need"""
    return people * 2


def treats(people: int) -> int:
    """this will show how many treats we need based off of the numbe of tea bags"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """this will show the cost of the tea party"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
