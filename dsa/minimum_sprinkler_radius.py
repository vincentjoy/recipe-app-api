# Question - Minimum sprinkler radius to cover all plants

# Every plant can be watered, as long as the plant is within the sprinkler's radius range. Given the positions of plants and sprinkler on a horizontal line, return the minimum radius standard of sprinkler so that those
# sprinkler could cover all plants.

def min_radius(plant_positions, sprinkler_positions):
    """
    Calculate the minimum radius needed for sprinklers to cover all plants.

    Args:
        plant_positions: List of integer positions of plants on a line
        sprinkler_positions: List of integer positions of sprinklers on a line

    Returns:
        The minimum radius required to cover all plants
    """
    # Edge cases
    if not plant_positions or not sprinkler_positions:
        return 0

    # Sort sprinklers for binary search approach
    sprinkler_positions.sort()
    max_min_radius = 0

    for plant in plant_positions:
        # Find the closest sprinkler distance using binary search
        closest_distance = find_closest_sprinkler(plant, sprinkler_positions)
        max_min_radius = max(max_min_radius, closest_distance)

    return max_min_radius

def find_closest_sprinkler(plant, sprinklers):
    """
    Find the distance to the closest sprinkler for a given plant using binary search.

    Args:
        plant: Integer position of a plant
        sprinklers: Sorted list of sprinkler positions

    Returns:
        The distance to the closest sprinkler
    """
    # Edge cases - if plant is outside all sprinklers
    if plant <= sprinklers[0]:
        return sprinklers[0] - plant
    elif plant >= sprinklers[-1]:
        return plant - sprinklers[-1]

    # Binary search
    left, right = 0, len(sprinklers) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if sprinklers[mid] == plant:
            return 0  # Exact match
        elif sprinklers[mid] < plant:
            left = mid + 1
        else:
            right = mid - 1

    # At this point, right < left and sprinklers[right] < plant < sprinklers[left]
    left_distance = plant - sprinklers[right]
    right_distance = sprinklers[left] - plant

    return min(left_distance, right_distance)

# Example usage
plants = [1, 5, 9, 12]
sprinklers = [2, 11]
result = min_radius(plants, sprinklers)
print(f"Minimum radius needed: {result}")  # Output: 3.0