import re
import numpy as np


def isSatisfiedNum(x) -> bool:
    value = re.compile(r'[0-9]+(\.)?[0-9]*')
    isnumber =  value.match(x)
    
    if isnumber:
        x = float(x)
        return 0 <= x <= 100
    else:
        return False


if __name__ == '__main__':

    M, N, G, GOLDEN = 0, 0, 0, 0.618
    print("请输入参与游戏的人数：", end='')
    N = int(input())
    print("请输入游戏的轮数：", end='')
    M = int(input())
    grades = np.zeros((M, N))
    for x in range(M):

        print("--------------------------------------------------")
        print("第%3d轮:" % (x+1))
        print("请玩家依次输入一个0~100的有理数")

        i, inputs = 1, []
        while (i <= N):
            print("玩家%3d：" % i, end='')
            number = input()

            if not isSatisfiedNum(number):
                print("请重新输入0~100的有理数！")
            else:
                number = float(number)
                i += 1
                inputs.append(number)

        G = sum(inputs) / N * GOLDEN
        bias = np.zeros(N)
        bias = np.abs(np.array(inputs) - G)

        grades[x][bias == np.max(bias)] = -2
        grades[x][bias == np.min(bias)] = N

        print("本轮各位玩家的得分如下：")
        for i in range(N):
            print("玩家%3d：" % (i+1), end='')
            print("【%3d】分" % grades[x][i])


    all_grades = np.sum(grades, axis=0)
    print("--------------------------------------------------")
    print("各位玩家的最终得分如下：")
    for i in range(N):
            print("玩家%3d：" % (i+1), end='')
            print("【%3d】分" % all_grades[i])

