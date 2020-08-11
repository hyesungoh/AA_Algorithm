n = int(input())
for i in range(n, -1, -1):
    if i >= 2:
        w1 = str(i) + ' bottles'
        w2 = str(i-1) + ' bottles' if i-1 > 1 else '1 bottle'
    elif i == 1:
        w1 = '1 bottle'
        w2 = 'no more bottles'
    else:
        w1 = 'no more bottles'
        w2 = str(n) + ' bottles' if n > 1 else '1 bottle'

print(w1 + ' of beer on the wall, ' + w1 + ' of beer.' if w1 != 'no more bottles' else
      'No more bottles of beer on the wall, no more bottles of beer.')
print('Take one down and pass it around, ' + w2 + ' of beer on the wall.' if w1 != 'no more bottles' else
      'Go to the store and buy some more, ' + w2 + ' of beer on the wall.')
print('')

# def n(x):
#     if x == 0:
#         return 'no more bottles'
#     return '1 bottle' if x == 1 else str(x)+' bottles'
#
# j = int(input())
# for i in range(j, 0, -1):
#     print(n(i) + ' of beer on the wall, ' + n(i) + ' of beer.')
#     print('Take one down and pass it around, ' + n(i-1) + ' of beer on the wall.')
#     print('')
# print("No more bottles of beer on the wall, no more bottles of beer.")
# print("Go to the store and buy some more, " + n(j) + " on the wall.")
