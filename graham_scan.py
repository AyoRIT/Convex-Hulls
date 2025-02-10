# Required libraries
import time
import sys

def get_points(file_path):
    # ignore duplicate points
    points = set()
    with open(file_path, 'r') as file:
        # Discard the number of points
        file.readline()
        
        # Process each subsequent line
        for line in file:
            x, y = line.split()  # Split the line 
            points.add((int(x), int(y)))  # Add the tuple (x, y) to the list and convert to integers
    
    return list(points)

def graham_scan(points):
    # Step 1: Sort points by x, and by y as a tiebreaker
    points = sorted(points, key=lambda p: (p[0], p[1]))

    # Step 2: Build the lower hull using cross product 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Step 3: Build the upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Step 4: Combine lower and upper hulls
    # Remove the last point of each half because it's repeated
    return lower[:-1] + upper[:-1]

def cross_product(p1, p2, p3):
    # Calculate the cross product of vectors p1p2 and p1p3
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def main():
    if len(sys.argv) != 2:
        print("Please add a file path for the points. Usage: python graham_scan.py <file_path>")
        return
    
    file_path = sys.argv[1]
    points = get_points(file_path)
    
    
    # Start time
    start_time = time.time()
    hull = graham_scan(points)
    print("Convex Hull:", hull)
    
    # End time
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.4f} seconds")

    # Open a file to write the points
    with open('graham_scan_output.txt', 'w') as file:
        # Write the number of points as the first line
        file.write(f"{len(hull)}\n")
        # Loop through the points
        for point in hull:
            # Format and write each point to the file
            file.write(f"{point[0]} {point[1]}\n")

if __name__ == "__main__":
    main()
