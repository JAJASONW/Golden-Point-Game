import numpy as np

if __name__ == '__main__':
    N, G, GOLDEN = 0, 0, 0.618
    print("请输入参与游戏的人数：", end='')
    N = int(input())
    print("请玩家依次输入一个0~100的有理数")
    
    nums, grades = [], [0 for i in range(N)]
    for i in range(N):
        print("玩家" + str(i+1) + "：", end='')
        nums.append(float(input()))
    
    G = sum(nums) / N * GOLDEN
    bias = np.abs(np.array(nums) - G)
    grades[bias.argmin()] = N
    grades[bias.argmax()] = -2
    
    print("本轮各位玩家的得分如下：")
    for i in range(N):
        print("玩家" + str(i+1) + "：", end='')
        print("【" + str(grades[i]) + "】分")
