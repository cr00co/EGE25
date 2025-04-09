string_w_nums = open('6__2pp78.txt').readline()

c = 0
mx = -float('inf')

for i in range(0, len(string_w_nums)-2, 3):
    x = string_w_nums[i:i+3]
    if x == 'YZX' or x == 'ZXY':
        c += 1
        mx = max(c*3, mx)
    else:
        c = 0
print(mx)


