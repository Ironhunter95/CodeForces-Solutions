nums = input()
nums = nums.split()
mainnum = int(nums[0])
sub = int(nums[1])
for i in range(sub):
    if mainnum % 10 != 0:
        mainnum = mainnum-1
    elif mainnum % 10 == 0:
        mainnum = mainnum/10
print(int(mainnum))