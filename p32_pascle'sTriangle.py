"""
QUES: Pascle Triangle
"""

# 1
# 11
# 121
# 1331
# 14641
# 15101051

# Time(n*n)
# Space(n)
def generate(numRows: int):
    res = [[1]]

    for i in range(numRows - 1):
        row1 = [0] + res[-1] + [0]
        nextRow = []
        for j in range(len(res[-1]) + 1):
            nextRow.append(row1[j] + row1[j + 1])
        res.append(nextRow)
    return res


numRows = 5
print(generate(numRows))
