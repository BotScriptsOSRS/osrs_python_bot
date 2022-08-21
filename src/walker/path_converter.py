# use ctrl-f and the find ','and replace with ','
# remove last ',' in last row

path = [
3164,3482,
3164,3471,
3166,3460,
3173,3449,
3175,3438,
3175,3438,
3184,3429,
3195,3429,
3196,3428,
3196,3428,
3194,3439,
3192,3448,
3192,3448,
3181,3455,
3170,3464,
3170,3464,
3164,3467,
3164,3467,
3166,3478,
3167,3481
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
