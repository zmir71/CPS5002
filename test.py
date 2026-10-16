b = [' ' for _ in range(9)]
print("Current Board:\n")
for row in range(3):
    print("  |  ".join(b[row*3:(row+1) * 3]))
    if row < 2:
        print("------------")