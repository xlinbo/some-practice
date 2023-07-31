# city_functions.py

def city_country(city, country, population=None):
    if population:
        return city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        return city.title() + ', ' + country.title()
result = city_country("Beijing", "China", 20000000)
print(result)#这里是把函数操作得到的结果用return隐形存在函数牌名里面，可以简单理解为就是函数输出
