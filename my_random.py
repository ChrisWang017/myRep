import random

def ran_f():
    output = []

    # 初始化列表
    a = list(range(1, 40))

    # 打印初始位置
    for i in range(39):
        output.append(f"位置: {i}, {a[i]}")

    # 進行打散
    for i in range(38, 0, -1):
        r = random.randint(0, i)
        a[i], a[r] = a[r], a[i]
        output.append(f"亂數位置: {r}")

    # 打印打散後的位置
    output.append("\n打散後:")
    for i in range(39):
        output.append(f"位置: {i}, {a[i]}")

    # 打印最後生成的數字
    output.append("\n電腦報牌:")
    for i in range(34, 39):
        output.append(str(a[i]))

    return "\n".join(output)

# 執行函數並打印結果
print(ran_f())
