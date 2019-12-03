import os

def cost_of_module(N):
    cost_now = N // 3 - 2
    if cost_now <= 0:
         return 0
    return cost_now + cost_of_module(cost_now)

def main():
    with open("input.txt","r") as fp:
        sum = 0
        for line in fp:
            number = int(line.rstrip().split()[0])
            sum += cost_of_module(number)
        print(sum)


main()
# print(cost_of_module(100756))

