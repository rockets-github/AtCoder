K, G, M = map(int,input().split())
grass = 0
mag = 0


for i in range(K):
    if grass == G:
        grass = 0
    elif mag == 0:
        mag = M
    else:
        free_space = G - grass
        if mag > free_space:
            mag = mag - free_space
            grass = grass + free_space
        else:
            grass = grass + mag
            mag = 0

print(grass, mag)