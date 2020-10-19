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
    N, G, GOLDEN = 0, 0, 0.618
    print("请输入参与游戏的人数：", end='')
    N = int(input())
    print("请玩家依次输入一个0~100的有理数")
    
    i, inputs, grades = 1, [], np.zeros(N)
    while (i <= N):
        print("玩家%3d：" % i, end='')
        number = input()
        
        if not isSatisfiedNum(number):
            print("请输入0~100的有理数！")
        else:
            number = float(number)
            i += 1
            inputs.append(number)
    
    G = sum(inputs) / N * GOLDEN
    bias = np.abs(np.array(inputs) - G)
    
    grades[bias == np.max(bias)] = -2
    grades[bias == np.min(bias)] = N
    
    print("本轮各位玩家的得分如下：")
    for i in range(N):
        print("玩家%3d：" % (i+1), end='')
        print("【%3d】分" % grades[i])
