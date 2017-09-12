def read_file(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as f:
            content = f.readlines()
            weather_info = {}
    except:
        return read_file(input("找不到天气相关文件，请重新输入路径："))
    else:
        for line in content:
            line = line.strip('\n').split(',')
            weather_info[line[0]] = line[1].strip("''")
        return weather_info

def main():
    path = '../resource/weather_info.txt'
    weather_info = read_file(path)
    histories = ''
    while True:
        order = input("请输入指令或您要查询的城市名>")
        if order in weather_info.keys():
            weather = weather_info[order]
            history = '%s : %s\n' % (order, weather)
            histories += history
            print("%s的天气状况为：%s " % (order,weather))

        elif order == 'help':
                print("""
- 输入城市名，查询该城市的天气；
- 输入help，获取帮助文档；
- 输入history，获取查询历史；
- 输入quit，退出天气查询系统；
                        """)
        elif order == 'history' and len(histories) > 0:
            print(histories)
        elif order == 'history' and histories == '':
                print("暂无记录")
        elif order == 'quit':
            return
        else:
            print("查询不到相关城市")

if __name__ == "__main__":
     main()
