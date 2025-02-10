import time
import sys

def get_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        # Read the first line (number of points), but we don't need it
        file.readline()
        
        # Process each subsequent line
        for line in file:
            x, y = line.split()  # Split the line and convert to integers
            points.append((int(x), int(y)))  # Add the tuple (x, y) to the list
    
    return points


def cross_product(p1, p2, p3):
    # Calculate the cross product of vectors p1p2 and p1p3
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

import math

def polar_angle(p0, p1):
    """Calculate the polar angle (in radians) of p1 relative to p0."""
    return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

def distance(p0, p1):
    """Calculate the Euclidean distance between p0 and p1."""
    return (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2


def brute_force_convex_hull(points):
    n = len(points)
    if n < 3:
        return points  # Convex hull is the set of points if fewer than 3

    hull = set()
    
    # Check every pair of points
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            p1, p2 = points[i], points[j]
            valid = False
            for k in range(n):
                if k != i and k != j:
                    p = points[k]
                    res = cross_product(p1, p2, p)
                    # if point is on right side, ignore this particular segment
                    if res < 0:
                        valid = False
                        break
                    # if point is colinear, check if distance between p1 and p2 > p1 and p3
                    elif res == 0:
                        if distance(p1, p2) <= distance(p1, p):
                            valid = False
                            break
                        valid = True
                    # if point is on left side, continue checks for other points
                    elif res > 0:
                        valid = True
            if valid:
                hull.add(p1)
                hull.add(p2)

    unsorted_hull = list(hull)
    
    # Step 1: Find the leftmost point (if tie, choose the lowest one)
    leftmost_point = min(unsorted_hull, key=lambda p: (p[0], p[1]))
    unsorted_hull.remove(leftmost_point)
    # Step 2: Sort points by polar angle with respect to the leftmost point
    sorted_hull = sorted(unsorted_hull, key=lambda p: (polar_angle(leftmost_point, p), distance(leftmost_point, p)))
    
    return [leftmost_point] + sorted_hull

def main():
    if len(sys.argv) != 2:
        print("Please add a file path for the points. Usage: python brute_force.py <file_path>")
        return
    
    file_path = sys.argv[1]
    points = get_points(file_path)
    
    
    # Start time
    start_time = time.time()
    hull = brute_force_convex_hull(points)
    print("Convex Hull:", hull)
    
    # End time
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.4f} seconds")

    # Open a file to write the points
    with open('brute_force_output.txt', 'w') as file:
        # Write the number of points as the first line
        file.write(f"{len(hull)}\n")
        # Loop through the points
        for point in hull:
            # Format and write each point to the file
            file.write(f"{point[0]} {point[1]}\n")

if __name__ == "__main__":
    main()