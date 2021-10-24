# use ctrl-f and the find ',0'and replace with ','
# remove last ',' in last row

path = [
3164,3485,
3164,3474,
3164,3463,
3159,3452,
3148,3444,
3137,3439,
3128,3432,
3118,3424,
3108,3420,
3098,3417,
3094,3407,
3091,3396,
3084,3386,
3081,3376,
3075,3365,
3072,3354,
3072,3343,
3072,3332,
3072,3321,
3072,3310,
3073,3299,
3075,3288,
3076,3277,
3078,3267,
3080,3256,
3088,3249,
3093,3242
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
