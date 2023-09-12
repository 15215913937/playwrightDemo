import datetime

# 获取当前日期时间
now = datetime.datetime.now()

# 定义一个空列表,用于保存前7天日期的时间戳
timestamps = []

# 循环7次,每次减一天,并转为时间戳添加到列表中
for i in range(7):
    day = now - datetime.timedelta(days=i)
    timestamp = datetime.datetime.timestamp(day)
    timestamps.append(timestamp)

# 输出结果
print(timestamps)