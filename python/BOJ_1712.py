x,y,z = map(int, input().split())

print (-1 if y>=z else x//(z-y)+1)
