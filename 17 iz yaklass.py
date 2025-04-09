f = open('17.txt')
nums = [int(i) for i in f]
troiki = []
c = 0
answer_l = []
for i in range(len(nums) - 2):
    troiki.append([nums[i], nums[i+1], nums[i+2]])

for j in troiki:
    if max(j) % 17 == min(j):
        c += 1
        answer_l.append(sum(j))
print(c, max(answer_l))