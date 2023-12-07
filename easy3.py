# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []

    triangle = [[1]]
    
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

numRows = int(input())
result = generate_pascals_triangle(numRows)
print(result)