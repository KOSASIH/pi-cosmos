# main.py
from .cosmos import Cosmos

def main():
    data = [...]  # load data from file or API
    cosmos = Cosmos(data)

    stars = cosmos.get_stars()
    planets = cosmos.get_planets()

    print("Stars:", stars)
    print("Planets:", planets)

if __name__ == "__main__":
    main()
