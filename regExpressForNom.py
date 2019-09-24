han = open('text2Read.py')
for line in han:
    line = line.rstrip()
    wds = line.split()
    count = 0
    if wds.endswith("ing"):
        count++
        continue
    elif wds.endswith("or"):
        count++
        continue
    elif wds.endswith("ee"):
        count++
        continue
    elif wds.endswith("ion"):
        count++
        continue
    print("The current count is ",count)
