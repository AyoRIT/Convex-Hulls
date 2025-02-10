# Convex-Hulls

There are three files in this folder. Each program file is written in python. Each program file generates a convex hull in counter clockwise order (colinear points are ignored with only the first and last points selected in a sequence of colinear points)

1. graham_scan.py
2. brute_force.py
3. points.txt

You can run either program with the command
python <program_name> <file_path>
    e.g python graham_scan ./points.txt

You can copy the points into the points.txt file if you want to run the program with the ./points.txt file path or you can include a file path to your own points. There are no required libaries outside inbuilt python libaries

Output for each program is going to be created after the program is run with the name <program_name>_output.txt 
The first line in the output is the number of points in the hull. Every other line represent the points that make up the hull when ordered in counterclockwise order.


