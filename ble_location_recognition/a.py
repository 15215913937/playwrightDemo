from importlib_metadata import Pair


class Parse_Result:
    def __init__(self):
        self.head_row = None  # 头部所在行
        self.neck_row = None  # 颈部所在行
        self.shoulder_row = None  # 肩膀所在行
        self.buns_row = None  # 屁股所在行
        self.spine_column = None  # 脊椎所在列
        self.buns_column = None  # 屁股所在列


class RowFeature_InitTypeDef:
    def __init__(self):
        self.row_array = [[None] * 8 for i in range(21)]  # [21][8]  # 行矩阵21*8
        self.row_sum = [None] * 21  # 行和
        self.row_average = [None] * 21  # 行均值
        self.row_variance = [None] * 21  # 行方差
        self.row_max = [None] * 21  # 行最大值
        self.row_max_column = [None] * 21  # 行最大值所在列


class ColumnFeature_InitTypeDef:
    def __init__(self):
        self.column_array = [[None] * 21 for i in range(8)]  # 列矩阵21*8
        self.column_sum = [None] * 8  # 列和
        self.column_average = [None] * 8  # 列均值
        self.column_variance = [None] * 8  # 列方差
        self.column_max = [None] * 8  # 列最大值
        self.column_max_row = [None] * 8  # 列最大值所在行


class Position_Result:
    def __init__(self):
        self.head = [None] * 2  # 头部所在行
        self.neck = [None]  # 颈部所在行
        self.shoulder = [None]  # 肩膀所在行0
        self.back = [None] * 2  # 背所在行
        self.wrist = [None] * 2  # 腰部所在行
        self.hip = [None] * 3  # 屁股所在行
        self.leg = [None] * 4  # 大腿所在行
        self.shank = [None] * 4  # 小腿所在行


class PartFeature_InitTypeDef:
    def __init__(self):
        self.enthronement_position = None  # 坐床位置
        self.torso_point = None  # 躯干高点位
        self.torso_variance = None  # 躯干方差
        self.shoulder_point = None  # 肩部高点位
        self.shoulder_variance = None  # 肩部方差
        self.left_count = None  # 用于区分左侧卧
        self.right_count = None  # 用于区分右侧卧
        self.last_sleep_position = None  # 上一次睡姿
        self.sleep_position = None  # 睡姿
        self.lastSleepPotsure = None
        self.currentSleepPotsure = None


SURFACE_HIGH_COUNT_THRESHOLD = 25  # 表面压力有压阈值


def Position_Init(parse_rst, Row_Init, Column_Init, position_rst, Part_Init):
    RowFeature_Init(SurfaceFeature_Initure.surface_filter_pressure, Row_Init)  # 准备行数据
    ColumnFeature_Init(SurfaceFeature_Initure.surface_filter_pressure, Column_Init)  # 准备列数据
    SurfaceFeature_Init(SurfaceFeature_Initure)  # 表压数据分析
    supineConvert(parse_rst, position_rst, Row_Init)  # 新部位识别   #获取屁股列
    Get_Spine_Column(parse_rst, Column_Init)

def RowFeature_Init(surface_pressure, Row_Init):
    # 1.初始化行矩阵
    for i in range(21):
        for j in range(8):
            Row_Init.row_array[i][j] = surface_pressure[i * 8 + j]

    for i in range(21):
        Row_Init.row_sum[i] = sum(Row_Init.row_array[i])  # 1.行和
        Row_Init.row_average[i] = Row_Init.row_sum[i] / 8.0  # 2.初始化行均值
        Row_Init.row_variance[i] = getVariance(Row_Init.row_array[i])  # 3.初始化行方差
        Row_Init.row_max_column[i] = findN(Row_Init.row_array[i], 1)  # 5.初始化行最大值所在列
        Row_Init.row_max[i] = Row_Init.row_array[i][Row_Init.row_max_column[i]]  # 4.初始化行最大值


def ColumnFeature_Init(surface_pressure, Column_Init):
    # 1.初始化列矩阵
    for i in range(8):
        for j in range(21):
            Column_Init.column_array[i][j] = surface_pressure[i + 8 * j]

    for i in range(8):
        Column_Init.column_sum[i] = sum(Column_Init.column_array[i])  # 2.列和
        Column_Init.column_average[i] = Column_Init.column_sum[i] / 21.0  # 2.列均值
        Column_Init.column_variance[i] = getVariance(Column_Init.column_array[i])  # 3.列方差
        Column_Init.column_max_row[i] = findN(Column_Init.column_array[i], 1)  # 5.列最大值所在行
        Column_Init.column_max[i] = Column_Init.column_array[i][Column_Init.column_max_row[i]]  # 4.初始化列最大值


def SurfaceFeature_Init(Surface_Init):
    # 2.初始化列整体均值阈值
    Surface_Init.surface_average = mean(Surface_Init.surface_pressure)
    Surface_Init.surface_high_count = number_greater_than_threshold(Surface_Init.surface_pressure,
                                                                    SURFACE_HIGH_COUNT_THRESHOLD)

    # 3.初始化6个较大值
    for mm in range(6):
        line = 0
        row = 0
        index = findN(Surface_Init.surface_pressure, mm + 1)
        Find_RowColumn_by_Index(index, line, row)
        Surface_Init.surface_max[mm] = Surface_Init.surface_pressure[index]  # 最大值
        Surface_Init.surface_max_index[mm] = index  # 最大值
        Surface_Init.surface_max_row[mm] = line  # 所在行
        Surface_Init.surface_max_column[mm] = row  # 所在列

    Surface_Init.surface_variance = getVariance(Surface_Init.surface_pressure)


def ordered_array_contains(target_array, value):
    result = 0
    for i in range(len(target_array)):
        if value > target_array[i]:
            break
        if value == target_array[i]:
            result = 1
            break
    return result


def Find_RowColumn_by_Index(index):
    Row = index // 8
    Column = index % 8
    return Row, Column


def number_greater_than_threshold(data_array, count, threshold_value):
    number = 0
    for i in range(count):
        if data_array[i] > threshold_value:
            number += 1
    return number


def mean(data_array, count):
    total = 0
    for i in range(count):
        total += data_array[i]
    return total / count


def getVariance(data_array, count):
    ave = 0  # 平均值
    sum_value = 0  # 和

    # 遍历数组,求和
    sum_value = sum(data_array)
    # 求平均值
    ave = sum_value / count

    # 遍历求数组元素与平均值差值
    for i in range(count):
        sum_value += (data_array[i] - ave) ** 2

    return sum_value / count


def findN(arr, count, n):
    index = [0] * n
    flag = 0

    for i in range(n):
        for j in range(count):
            if arr[index[i]] <= arr[j]:
                for k in range(i + 1):
                    if j == index[k]:
                        flag = 1
                        break
                if not flag:
                    index[i] = j
                else:
                    flag = 0
                    continue

    tmp = index[n - 1]
    return tmp


def Get_Head_Neck_Shulder_Row(parse_result, Row_Init):
    parse_result['shoulder_row'] = 4
    temp_ = Row_Init['row_max'][2]
    for i in range(2, 6):
        if temp_ < Row_Init['row_max'][i]:
            temp_ = Row_Init['row_max'][i]
            parse_result['shoulder_row'] = i
    parse_result['neck_row'] = parse_result['shoulder_row'] - 1
    parse_result['head_row'] = parse_result['shoulder_row'] - 2


def supineConvert(parse_result, position_result, Row_Init):
    partition = Row_Init['row_array']
    bodyLength = 7
    shoulderIndex1 = rollingSelectMainBody(partition, bodyLength)
    fillHeadAndNeck(position_result, shoulderIndex1)
    fillMainBody(position_result, partition, shoulderIndex1, bodyLength)
    kneeInfo = kneeIndex(partition, position_result['hip'][1])
    fillLegAndShank(kneeInfo[0], position_result)


def Get_Spine_Column(parse_result, Column_Init):
    row_sum = [0 for i in range(6)]
    for i in range(6):
        row_sum[i] = sum(Column_Init['column_array'][i + 1][2:8])
    parse_result['spine_column'] = findN(row_sum, 1) + 1


def getRealMaxPartLines(parts, partLines, Row_Init):
    maxLine = 0
    for i in range(1, len(partLines)):
        if Row_Init['row_max'][maxLine] < Row_Init['row_max'][i]:
            maxLine = i + 1

    parts[0] = maxLine
    downMax = 0
    if ordered_array_contains(partLines, maxLine) == 1:
        downMax = Row_Init['row_max'][maxLine]

    upMax = 0
    if ordered_array_contains(partLines, maxLine - 2) == 1:
        upMax = Row_Init['row_max'][maxLine - 2]

    if downMax > upMax:
        if ordered_array_contains(partLines, maxLine + 1):
            parts[1] = maxLine + 1
    else:
        if ordered_array_contains(partLines, maxLine - 1) == 1:
            parts[1] = maxLine - 1


import ctypes

c_uint16 = ctypes.c_uint16
realloc = ctypes.CDLL(None).realloc


def addElement(array, size, element):
    array = realloc(array, (size + 1) * ctypes.sizeof(c_uint16))
    if array:
        array[size] = element
        size += 1
    return array


def rollingSelectMainBody(avgList, bodyLength):
    pivotIndex = -1
    pivotSum = 0
    for i in range(2, 8):
        curSum = sum(avgList[i:i + bodyLength])
        if curSum > pivotSum:
            pivotSum = curSum
            pivotIndex = i
    return pivotIndex


def fillMainBody(position_result, partition, shoulderIndex1, bodyLength):
    position_result['shoulder'][0] = shoulderIndex1 + 1
    backIndex1 = shoulderIndex1 + 1
    backIndex2 = backIndex1 + 1
    position_result['back'][0] = backIndex1 + 1
    position_result['back'][1] = backIndex2 + 1

    lastHipIndex = shoulderIndex1 + bodyLength - 1
    hipMeanList = [0 for i in range(3)]
    for i in range(3):
        hipMeanList[i] = mean(partition[lastHipIndex - 3 + i])

    if hipMeanList[0] > hipMeanList[1] and hipMeanList[0] > hipMeanList[2]:
        hipIndex3 = lastHipIndex - 1 - (bodyLength - 7)
    else:
        hipIndex3 = lastHipIndex

    hipIndex2 = hipIndex3 - 1
    hipIndex1 = hipIndex2 - 1
    if hipIndex1 - backIndex2 == 1:
        hipIndex1 += 1
        hipIndex2 += 1
        hipIndex3 += 1

    for i in range(backIndex2 + 1, hipIndex1):
        position_result['wrist'][i - backIndex2 - 1] = i + 1

    position_result['hip'][0] = hipIndex1 + 1
    position_result['hip'][1] = hipIndex2 + 1
    position_result['hip'][2] = hipIndex3 + 1


def fillHeadAndNeck(position_result, shoulder1):
    if shoulder1 > 3:
        neck1 = shoulder1 - 1
        position_result['neck'][0] = neck1
        head2 = neck1 - 1
        head1 = head2 - 1
        position_result['head'][0] = head1
        position_result['head'][1] = head2
    elif shoulder1 > 2:
        neck1 = shoulder1 - 1
        position_result['neck'][0] = neck1
        head2 = neck1 - 1
        position_result['head'][0] = head2
        position_result['head'][1] = 0


def fillMainBody(position_result, partition, shoulderIndex1, bodyLength):
    position_result['shoulder'][0] = shoulderIndex1 + 1
    backIndex1 = shoulderIndex1 + 1
    backIndex2 = backIndex1 + 1
    position_result['back'][0] = backIndex1 + 1
    position_result['back'][1] = backIndex2 + 1

    lastHipIndex = shoulderIndex1 + bodyLength - 1
    hipMeanList = [0 for i in range(3)]
    for i in range(3):
        hipMeanList[i] = mean(partition[lastHipIndex - 3 + i])

    if hipMeanList[0] > hipMeanList[1] and hipMeanList[0] > hipMeanList[2]:
        hipIndex3 = lastHipIndex - 1 - (bodyLength - 7)
    else:
        hipIndex3 = lastHipIndex

    hipIndex2 = hipIndex3 - 1
    hipIndex1 = hipIndex2 - 1
    if hipIndex1 - backIndex2 == 1:
        hipIndex1 += 1
        hipIndex2 += 1
        hipIndex3 += 1

    for i in range(backIndex2 + 1, hipIndex1):
        position_result['wrist'][i - backIndex2 - 1] = i + 1

    position_result['hip'][0] = hipIndex1 + 1
    position_result['hip'][1] = hipIndex2 + 1
    position_result['hip'][2] = hipIndex3 + 1


def fillLegAndShank(kneeIndex, position_rst):
    lastHip = position_rst.hip[2]

    position_rst.leg[0] = lastHip + 1
    position_rst.leg[1] = lastHip + 2
    position_rst.leg[2] = lastHip + 3

    shank1 = position_rst.leg[2] + 1
    shank2 = shank1 + 1
    position_rst.shank[0] = shank1
    position_rst.shank[1] = shank2
    if shank2 < 21:
        shank3 = shank2 + 1
        position_rst.shank[2] = shank3
    else:
        position_rst.shank[2] = 0


def kneeIndex(avgList, hipIndex2):
    kneeIndex = -1
    minPivot = 10000
    for i in range(13, 18):
        v = avgList[i]
        if v < minPivot:
            kneeIndex = i
            minPivot = v

    kneeHipDiff = kneeIndex - hipIndex2
    if kneeHipDiff < 2:
        kneeHipDiff = 2
        kneeIndex = hipIndex2 + kneeHipDiff

    result = Pair()
    result.first = kneeIndex
    result.second = kneeHipDiff
    return result


def supineConvert(parse_result, position_result, Row_Init):
    # 1、构造21-8的二维数组
    indexLength8 = rollingSelectMainBody(Row_Init['row_average'], 8)
    indexLength7 = rollingSelectMainBody(Row_Init['row_average'], 7)
    if indexLength8 == indexLength7:
        bodyLength = 7
        outer = Row_Init['row_average'][indexLength8 + 7]
        inner = Row_Init['row_average'][indexLength8 + 6]
        if outer * 2.0 > inner:
            bodyLength = 8
    elif indexLength7 - indexLength8 == 1:
        bodyLength = 8
        outer = Row_Init['row_average'][indexLength8]
        inner = Row_Init['row_average'][indexLength7]
        if outer * 2.0 < inner:
            bodyLength = 7
    else:
        bodyLength = 8

    if bodyLength == 7:
        shoulderIndex1 = indexLength7
    else:
        shoulderIndex1 = indexLength8

    fillMainBody(position_result, Row_Init['row_array'], shoulderIndex1, bodyLength)
    fillHeadAndNeck(position_result, shoulderIndex1 + 1)
    hip2 = position_result['hip'][1]
    kneeInfo = kneeIndex(Row_Init['row_average'], hip2 - 1)
    fillLegAndShank(kneeInfo[0], position_result)
    parse_result['buns_row'] = position_result['hip'][0]
    parse_result['head_row'] = position_result['head'][0]
    parse_result['neck_row'] = position_result['neck'][0]
    parse_result['shoulder_row'] = position_result['shoulder'][0]
    parse_result['buns_column'] = Row_Init['row_max_column'][parse_result['buns_row']]


def Get_Spine_Column(parse_result, Column_Init):
    row_sum = [0 for i in range(6)]
    for i in range(6):
        row_sum[i] = sum(Column_Init['column_array'][i + 1][2:8])
    parse_result['spine_column'] = findN(row_sum, 6, 1) + 1


print(Get_Spine_Column())
