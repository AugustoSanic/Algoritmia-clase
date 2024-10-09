import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

def brute_force_closest_pair(points):
    min_dist = float('inf')
    closest_pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    return closest_pair, min_dist

def closest_cross_pair(points_sorted_by_y, midpoint, min_dist):
    # Crear la franja de puntos que cruzan el midpoint
    strip = [point for point in points_sorted_by_y if abs(point.x - midpoint.x) < min_dist]
    
    min_cross_dist = min_dist
    closest_cross_pair = (None, None)

   
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            dist = distance(strip[i], strip[j])
            if dist < min_cross_dist:
                min_cross_dist = dist
                closest_cross_pair = (strip[i], strip[j])

    return closest_cross_pair, min_cross_dist

def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
    num_points = len(points_sorted_by_x)
    
  
    if num_points <= 3:
        return brute_force_closest_pair(points_sorted_by_x)

    mid = num_points // 2
    midpoint = points_sorted_by_x[mid]

    left_half_x = points_sorted_by_x[:mid]
    right_half_x = points_sorted_by_x[mid:]

    # Dividir los puntos ordenados por y basándose en el midpoint
    left_half_y = [point for point in points_sorted_by_y if point.x <= midpoint.x]
    right_half_y = [point for point in points_sorted_by_y if point.x > midpoint.x]

    left_closest, left_min_dist = closest_pair_recursive(left_half_x, left_half_y)
    right_closest, right_min_dist = closest_pair_recursive(right_half_x, right_half_y)

    
    min_dist = min(left_min_dist, right_min_dist)
    closest_pair = left_closest if left_min_dist <= right_min_dist else right_closest

    closest_cross_pair_result, cross_dist = closest_cross_pair(points_sorted_by_y, midpoint, min_dist)

 
    if cross_dist < min_dist:
        return closest_cross_pair_result, cross_dist
    else:
        return closest_pair, min_dist

def closest_pair_of_points(points):
    if len(points) < 2:
        raise ValueError("Se requieren al menos dos puntos para encontrar un par más cercano.")
    
    points_sorted_by_x = sorted(points, key=lambda point: point.x)
    points_sorted_by_y = sorted(points, key=lambda point: point.y)
    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)
