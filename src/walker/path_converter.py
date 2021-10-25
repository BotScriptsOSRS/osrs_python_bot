# use ctrl-f and the find ',0'and replace with ','
# remove last ',' in last row

path = [

]

coords = []
while path:
    coords.append([path[0],path[1]])
    path.pop(0)
    path.pop(0)
print('Path:')
print(coords)
print('\n')
print('Reversed path:')
coords.reverse()
print(coords)
