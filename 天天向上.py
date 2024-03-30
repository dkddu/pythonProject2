def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup *= 0.99
        else:
            dayup *= df
    return dayup

dayfactor = 0.01
index = dayup(dayfactor)
while index < 37.78:
    dayfactor += 0.001
    index = dayup(dayfactor)
print(f"工作日的努力参数是: {round(dayfactor, 3)}")

def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup

dayfactor = 0.01
index = dayUp(dayfactor)
while index < 37.78:
    dayfactor += 0.001
    index = dayUp(dayfactor)
print("工作日的努力参数是: {:.3f}".format(dayfactor))