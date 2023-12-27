input = open("input.txt", "r")

nums = []

for line in input:
    p1 = 0
    p2 = len(line)-1
    leftFound = ""
    rightFound = ""
    while leftFound is "" or rightFound is "":
        if not leftFound:
            if line[p1].isnumeric():
                leftFound = line[p1]
            else:
                for i, word in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[p1:].startswith(word):
                        leftFound = str(i + 1)
                        break
                if not leftFound:
                    p1 += 1

        if not rightFound: 
            if line[p2].isnumeric():
                rightFound = line[p2]
            else:
                for i, word in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                    if line[p2:].startswith(word):
                        rightFound = str(i + 1)
                        break
                if not rightFound:
                    p2 -= 1

    nums.append(int(leftFound+rightFound))

print(sum(nums))
        