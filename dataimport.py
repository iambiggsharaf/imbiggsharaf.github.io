data = []

f = open("data.txt")

lines = f.readlines()

for i in range(0,66843, 3):
    dict = {}
    dict['name'] = lines[i][2:]
    dict['tle1'] = lines[i + 1]
    dict['tle2'] = lines[i + 2]
    data.append(dict)
