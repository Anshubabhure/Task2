import numpy as np

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def nearest_neighbor_algorithm(city_coordinates):
    num_cities = len(city_coordinates)
    unvisited_cities = set(range(num_cities))
    tour = []
    # Start from a random city
    current_city = np.random.choice(list(unvisited_cities))
    unvisited_cities.remove(current_city)
    tour.append(current_city)
    while unvisited_cities:
        nearest_city = min(unvisited_cities,
                           key=lambda city: calculate_distance(city_coordinates[current_city], city_coordinates[city]))
        unvisited_cities.remove(nearest_city)
        tour.append(nearest_city)
        current_city = nearest_city
    return tour

def calculate_total_distance(tour, city_coordinates):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[(i + 1) % len(tour)]])
    return total_distance

def get_city_coordinates(num_cities):
    city_coordinates = []
    for i in range(num_cities):
        print(f"Enter coordinates for city {i + 1}:")
        try:
            x = float(input("X coordinate: "))
            y = float(input("Y coordinate: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for coordinates.")
            return get_city_coordinates(num_cities)
        city_coordinates.append((x, y))
    return city_coordinates

def main():
    try:
        num_cities = int(input("Enter the number of cities: "))
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of cities.")
        return
    city_coordinates = get_city_coordinates(num_cities)
    tour = nearest_neighbor_algorithm(city_coordinates)
    total_distance = calculate_total_distance(tour, city_coordinates)
    print("Optimal tour:", tour)
    print("Total distance:", total_distance)

if __name__ == "__main__":
    main()
