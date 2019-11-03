for i in range(6):
    # 总体思路是，先打印一行空行，代表每一行星星前的空格
    # 在不换行，打印星号
    for j in range(6-i):
        print(" ",end="")
    for m in range(i+1):
        print("* ", end="")
        # 打印完一行后换行
    print()
    ''''
    试着更改一些内容
    '''