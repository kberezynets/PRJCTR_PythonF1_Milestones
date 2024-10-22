# “Pascal's Triangle”

# Alice loves triangles and math.
# She wants to create a poster on the wall
# with Pascal's triangle. Let's help her!

# Create a file triangle.py,
# where define a function def get_triangle(rows: int) -> List[List[int]],
# which will return the triangle as a list of lists
# with the specified number of rows:

# get_triangle(5) ==
# [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
# ]

def get_triangle(rows: int):
    List = []
    for i in range(rows):
        row = [1]
        for j in range(i):
            if j == 0:
                row.insert(j, 1)
            else:
                row.insert(j, List[i-1][j-1]+List[i-1][j])
        List += row,
    return List


# print(get_triangle(4))

# In the same file, write logic to get the number of rows
# from command line arguments and print the resulting triangle to the console:

# python triangle.py 5
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

def shape_triangle(List: list):
    print('python triangle.py ', len(List))
    for i in range(len(List)):
        print(' ' * (len(List)-i) + ' '.join(str(j) for j in List[i]))


shape_triangle(get_triangle(5))
