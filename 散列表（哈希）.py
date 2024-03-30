voted = {}
voted["mike"] = True
def voted_check(name):
    if voted.get(name):
        print("you can not vote")
    else:
        voted[name] = True
        print("you can vote")
    return name
print(voted_check("tom"))
print(voted_check("tom"))
print(voted_check("mike"))
#解决冲突的方法
#开放定址法：再散列函数法，公共溢出法，链地址法
#线性探测，二次探测，随机探测