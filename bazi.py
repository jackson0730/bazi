# 定义天干和地支
tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 输入年月日时的天干和地支
y_t, y_d, m_t, m_d, d_t, d_d, h_t, h_d = input("请输入年月日时的天干和地支：\n").split()


# 判断地支中是否同时出现申子辰，寅午戌，巳酉丑，亥卯未
flag1 = "申" in [y_d, m_d, d_d, h_d] and "子" in [y_d, m_d, d_d, h_d] and "辰" in [y_d, m_d, d_d, h_d]
if flag1:
    print("申子辰三合水局")

flag2 = "寅" in [y_d, m_d, d_d, h_d] and "午" in [y_d, m_d, d_d, h_d] and "戌" in [y_d, m_d, d_d, h_d]
if flag2:
    print("寅午戌三合火局")

flag3 = "巳" in [y_d, m_d, d_d, h_d] and "酉" in [y_d, m_d, d_d, h_d] and "丑" in [y_d, m_d, d_d, h_d]
if flag3:
    print("巳酉丑三合金局")

flag4 = "亥" in [y_d, m_d, d_d, h_d] and "卯" in [y_d, m_d, d_d, h_d] and "未" in [y_d, m_d, d_d, h_d]
if flag4:
    print("亥卯未三合木局")

if not (flag1 or flag2 or flag3 or flag4):
    print("地支中没有出现“三合”即“申子辰三合水局；寅午戌三合火局；巳酉丑三合金局；亥卯未三合木局”")

# 判断地支中是否同时出现子午相冲、丑未相冲、寅申相冲、卯酉相冲、辰戌相冲、巳亥相冲。
flag5 = "子" in [y_d, m_d, d_d, h_d] and "午" in [y_d, m_d, d_d, h_d]
if flag5:
    print("子午相冲")
flag6 = "丑" in [y_d, m_d, d_d, h_d] and "未" in [y_d, m_d, d_d, h_d]
if flag6:
    print("丑未相冲")
flag7 = "寅" in [y_d, m_d, d_d, h_d] and "申" in [y_d, m_d, d_d, h_d]
if flag7:
    print("寅申相冲")
flag8 = "卯" in [y_d, m_d, d_d, h_d] and "酉" in [y_d, m_d, d_d, h_d]
if flag8:
    print("卯酉相冲")
flag9 = "辰" in [y_d, m_d, d_d, h_d] and "戌" in [y_d, m_d, d_d, h_d]
if flag9:
    print("辰戌相冲")
flag10 = "巳" in [y_d, m_d, d_d, h_d] and "亥" in [y_d, m_d, d_d, h_d]
if flag10:
    print("巳亥相冲")
if not (flag5 or flag6 or flag7 or flag8 or flag9 or flag10):
    print("地支中没有出现“六冲”即“子午相冲；丑未相冲；寅申相冲；卯酉相冲；辰戌相冲；巳亥相冲”")

# 判断地支中是否同时出现子未相害，丑午相害，寅巳相害，卯辰相害，申亥相害，酉戌相害。
flag11 = "子" in [y_d, m_d, d_d, h_d] and "未" in [y_d, m_d, d_d, h_d]
if flag11:
    print("子未相害")
flag12 = "丑" in [y_d, m_d, d_d, h_d] and "午" in [y_d, m_d, d_d, h_d]
if flag12:
    print("丑午相害")
flag13 = "寅" in [y_d, m_d, d_d, h_d] and "巳" in [y_d, m_d, d_d, h_d]
if flag13:
    print("寅巳相害")
flag14 = "卯" in [y_d, m_d, d_d, h_d] and "辰" in [y_d, m_d, d_d, h_d]
if flag14:
    print("卯辰相害")
flag15 = "申" in [y_d, m_d, d_d, h_d] and "亥" in [y_d, m_d, d_d, h_d]
if flag15:
    print("申亥相害")
flag16 = "酉" in [y_d, m_d, d_d, h_d] and "戌" in [y_d, m_d, d_d, h_d]
if flag16:
    print("酉戌相害")
if not (flag11 or flag12 or flag13 or flag14 or flag15 or flag16):
    print("地支中没有出现“六害”即”子未相害；丑午相害；寅巳相害；卯辰相害；申亥相害；酉戌相害”")

# 判断地支中是否同时出现子卯刑；寅巳申相刑；丑未戌相刑。
flag17 = "子" in [y_d, m_d, d_d, h_d] and "卯" in [y_d, m_d, d_d, h_d]
if flag17:
    print("子卯相刑")
flag18 = "寅" in [y_d, m_d, d_d, h_d] and "巳" in [y_d, m_d, d_d, h_d] and "申" in [y_d, m_d, d_d, h_d]
if flag18:
    print("寅巳申三刑")
flag19 = "丑" in [y_d, m_d, d_d, h_d] and "未" in [y_d, m_d, d_d, h_d] and "戌" in [y_d, m_d, d_d, h_d]
if flag19:
    print("丑未戌三刑")
if not (flag17 or flag18 or flag19):
    print("地支中没有出现”三刑”即”子卯刑；寅巳申相刑；丑未戌相刑”")

# 判断地支中是否同时出现辰辰自刑；午午自刑；酉酉自刑；亥亥自刑。
# 定义四种自刑的地支组合
zixing1 = ['辰辰']
zixing2 = ['午午']
zixing3 = ['酉酉']
zixing4 = ['亥亥']

if y_d + m_d in zixing1 or y_d + d_d in zixing1 or y_d + h_d in zixing1 or m_d + d_d in zixing1 or m_d + h_d in zixing1 or d_d + h_d in zixing1:
    print("辰辰自刑")
elif y_d + m_d in zixing2 or y_d + d_d in zixing2 or y_d + h_d in zixing2 or m_d + d_d in zixing2 or m_d + h_d in zixing2 or d_d + h_d in zixing2:
    print("午午自刑")
elif y_d + m_d in zixing3 or y_d + d_d in zixing3 or y_d + h_d in zixing3 or m_d + d_d in zixing3 or m_d + h_d in zixing3 or d_d + h_d in zixing3:
    print("酉酉自刑")
elif y_d + m_d in zixing4 or y_d + d_d in zixing4 or y_d + h_d in zixing4 or m_d + d_d in zixing4 or m_d + h_d in zixing4 or d_d + h_d in zixing4:
    print("亥亥自刑")
else:
    print("地支中没有出现自刑即“辰辰自刑；午午自刑；酉酉自刑；亥亥自刑”")

# 输出八字天干地支的十神
# 定义十神组合
tiangan1 = ['甲']
tiangan2 = ['乙']
tiangan3 = ['丙']
tiangan4 = ['丁']
tiangan5 = ['戊']
tiangan6 = ['己']
tiangan7 = ['庚']
tiangan8 = ['辛']
tiangan9 = ['壬']
tiangan10 = ['癸']

# 确定年干十神
if (y_t in tiangan1 and d_t in tiangan1) or (y_t in tiangan2 and d_t in tiangan2) or (y_t in tiangan3 and d_t in tiangan3) or (y_t in tiangan4 and d_t in tiangan4) or (y_t in tiangan5 and d_t in tiangan5) or (y_t in tiangan6 and d_t in tiangan6) or (y_t in tiangan7 and d_t in tiangan7) or (y_t in tiangan8 and d_t in tiangan8) or (y_t in tiangan9 and d_t in tiangan9) or (y_t in tiangan10 and d_t in tiangan10):
    value1 = "年干比肩"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan2) or (y_t in tiangan2 and d_t in tiangan1) or (y_t in tiangan3 and d_t in tiangan4) or (y_t in tiangan4 and d_t in tiangan3) or (y_t in tiangan5 and d_t in tiangan6) or (y_t in tiangan6 and d_t in tiangan5) or (y_t in tiangan7 and d_t in tiangan8) or (y_t in tiangan8 and d_t in tiangan7) or (y_t in tiangan9 and d_t in tiangan10) or (y_t in tiangan10 and d_t in tiangan9):
    value1 = "年干劫财"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan3) or (y_t in tiangan2 and d_t in tiangan4) or (y_t in tiangan3 and d_t in tiangan5) or (y_t in tiangan4 and d_t in tiangan6) or (y_t in tiangan5 and d_t in tiangan7) or (y_t in tiangan6 and d_t in tiangan8) or (y_t in tiangan7 and d_t in tiangan9) or (y_t in tiangan8 and d_t in tiangan10) or (y_t in tiangan9 and d_t in tiangan1) or (y_t in tiangan10 and d_t in tiangan2):
    value1 = "年干偏印"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan4) or (y_t in tiangan2 and d_t in tiangan3) or (y_t in tiangan3 and d_t in tiangan6) or (y_t in tiangan4 and d_t in tiangan5) or (y_t in tiangan5 and d_t in tiangan8) or (y_t in tiangan6 and d_t in tiangan7) or (y_t in tiangan7 and d_t in tiangan10) or (y_t in tiangan8 and d_t in tiangan9) or (y_t in tiangan9 and d_t in tiangan2) or (y_t in tiangan10 and d_t in tiangan1):
    value1 = "年干正印"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan5) or (y_t in tiangan2 and d_t in tiangan6) or (y_t in tiangan3 and d_t in tiangan7) or (y_t in tiangan4 and d_t in tiangan8) or (y_t in tiangan5 and d_t in tiangan9) or (y_t in tiangan6 and d_t in tiangan10) or (y_t in tiangan7 and d_t in tiangan1) or (y_t in tiangan8 and d_t in tiangan2) or (y_t in tiangan9 and d_t in tiangan3) or (y_t in tiangan10 and d_t in tiangan4):
    value1 = "年干七杀"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan6) or (y_t in tiangan2 and d_t in tiangan5) or (y_t in tiangan3 and d_t in tiangan8) or (y_t in tiangan4 and d_t in tiangan7) or (y_t in tiangan5 and d_t in tiangan10) or (y_t in tiangan6 and d_t in tiangan9) or (y_t in tiangan7 and d_t in tiangan2) or (y_t in tiangan8 and d_t in tiangan1) or (y_t in tiangan9 and d_t in tiangan4) or (y_t in tiangan10 and d_t in tiangan3):
    value1 = "年干正官"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan7) or (y_t in tiangan2 and d_t in tiangan8) or (y_t in tiangan3 and d_t in tiangan9) or (y_t in tiangan4 and d_t in tiangan10) or (y_t in tiangan5 and d_t in tiangan1) or (y_t in tiangan6 and d_t in tiangan2) or (y_t in tiangan7 and d_t in tiangan3) or (y_t in tiangan8 and d_t in tiangan4) or (y_t in tiangan9 and d_t in tiangan5) or (y_t in tiangan10 and d_t in tiangan6):
    value1 = "年干偏财"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan8) or (y_t in tiangan2 and d_t in tiangan7) or (y_t in tiangan3 and d_t in tiangan10) or (y_t in tiangan4 and d_t in tiangan9) or (y_t in tiangan5 and d_t in tiangan2) or (y_t in tiangan6 and d_t in tiangan1) or (y_t in tiangan7 and d_t in tiangan4) or (y_t in tiangan8 and d_t in tiangan3) or (y_t in tiangan9 and d_t in tiangan6) or (y_t in tiangan10 and d_t in tiangan5):
    value1 = "年干正财"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan9) or (y_t in tiangan2 and d_t in tiangan10) or (y_t in tiangan3 and d_t in tiangan1) or (y_t in tiangan4 and d_t in tiangan2) or (y_t in tiangan5 and d_t in tiangan3) or (y_t in tiangan6 and d_t in tiangan4) or (y_t in tiangan7 and d_t in tiangan5) or (y_t in tiangan8 and d_t in tiangan6) or (y_t in tiangan9 and d_t in tiangan7) or (y_t in tiangan10 and d_t in tiangan8):
    value1 = "年干食神"
    print(value1)
if (y_t in tiangan1 and d_t in tiangan10) or (y_t in tiangan2 and d_t in tiangan9) or (y_t in tiangan3 and d_t in tiangan2) or (y_t in tiangan4 and d_t in tiangan1) or (y_t in tiangan5 and d_t in tiangan4) or (y_t in tiangan6 and d_t in tiangan3) or (y_t in tiangan7 and d_t in tiangan6) or (y_t in tiangan8 and d_t in tiangan5) or (y_t in tiangan9 and d_t in tiangan8) or (y_t in tiangan10 and d_t in tiangan7):
    value1 = "年干伤官"
    print(value1)

# 确定月干十神
if (m_t in tiangan1 and d_t in tiangan1) or (m_t in tiangan2 and d_t in tiangan2) or (m_t in tiangan3 and d_t in tiangan3) or (m_t in tiangan4 and d_t in tiangan4) or (m_t in tiangan5 and d_t in tiangan5) or (m_t in tiangan6 and d_t in tiangan6) or (m_t in tiangan7 and d_t in tiangan7) or (m_t in tiangan8 and d_t in tiangan8) or (m_t in tiangan9 and d_t in tiangan9) or (m_t in tiangan10 and d_t in tiangan10):
    value2 = "月干比肩"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan2) or (m_t in tiangan2 and d_t in tiangan1) or (m_t in tiangan3 and d_t in tiangan4) or (m_t in tiangan4 and d_t in tiangan3) or (m_t in tiangan5 and d_t in tiangan6) or (m_t in tiangan6 and d_t in tiangan5) or (m_t in tiangan7 and d_t in tiangan8) or (m_t in tiangan8 and d_t in tiangan7) or (m_t in tiangan9 and d_t in tiangan10) or (m_t in tiangan10 and d_t in tiangan9):
    value2 = "月干劫财"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan3) or (m_t in tiangan2 and d_t in tiangan4) or (m_t in tiangan3 and d_t in tiangan5) or (m_t in tiangan4 and d_t in tiangan6) or (m_t in tiangan5 and d_t in tiangan7) or (m_t in tiangan6 and d_t in tiangan8) or (m_t in tiangan7 and d_t in tiangan9) or (m_t in tiangan8 and d_t in tiangan10) or (m_t in tiangan9 and d_t in tiangan1) or (m_t in tiangan10 and d_t in tiangan2):
    value2 = "月干偏印"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan4) or (m_t in tiangan2 and d_t in tiangan3) or (m_t in tiangan3 and d_t in tiangan6) or (m_t in tiangan4 and d_t in tiangan5) or (m_t in tiangan5 and d_t in tiangan8) or (m_t in tiangan6 and d_t in tiangan7) or (m_t in tiangan7 and d_t in tiangan10) or (m_t in tiangan8 and d_t in tiangan9) or (m_t in tiangan9 and d_t in tiangan2) or (m_t in tiangan10 and d_t in tiangan1):
    value2 = "月干正印"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan5) or (m_t in tiangan2 and d_t in tiangan6) or (m_t in tiangan3 and d_t in tiangan7) or (m_t in tiangan4 and d_t in tiangan8) or (m_t in tiangan5 and d_t in tiangan9) or (m_t in tiangan6 and d_t in tiangan10) or (m_t in tiangan7 and d_t in tiangan1) or (m_t in tiangan8 and d_t in tiangan2) or (m_t in tiangan9 and d_t in tiangan3) or (m_t in tiangan10 and d_t in tiangan4):
    value2 = "月干七杀"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan6) or (m_t in tiangan2 and d_t in tiangan5) or (m_t in tiangan3 and d_t in tiangan8) or (m_t in tiangan4 and d_t in tiangan7) or (m_t in tiangan5 and d_t in tiangan10) or (m_t in tiangan6 and d_t in tiangan9) or (m_t in tiangan7 and d_t in tiangan2) or (m_t in tiangan8 and d_t in tiangan1) or (m_t in tiangan9 and d_t in tiangan4) or (m_t in tiangan10 and d_t in tiangan3):
    value2 = "月干正官"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan7) or (m_t in tiangan2 and d_t in tiangan8) or (m_t in tiangan3 and d_t in tiangan9) or (m_t in tiangan4 and d_t in tiangan10) or (m_t in tiangan5 and d_t in tiangan1) or (m_t in tiangan6 and d_t in tiangan2) or (m_t in tiangan7 and d_t in tiangan3) or (m_t in tiangan8 and d_t in tiangan4) or (m_t in tiangan9 and d_t in tiangan5) or (m_t in tiangan10 and d_t in tiangan6):
    value2 = "月干偏财"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan8) or (m_t in tiangan2 and d_t in tiangan7) or (m_t in tiangan3 and d_t in tiangan10) or (m_t in tiangan4 and d_t in tiangan9) or (m_t in tiangan5 and d_t in tiangan2) or (m_t in tiangan6 and d_t in tiangan1) or (m_t in tiangan7 and d_t in tiangan4) or (m_t in tiangan8 and d_t in tiangan3) or (m_t in tiangan9 and d_t in tiangan6) or (m_t in tiangan10 and d_t in tiangan5):
    value2 = "月干正财"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan9) or (m_t in tiangan2 and d_t in tiangan10) or (m_t in tiangan3 and d_t in tiangan1) or (m_t in tiangan4 and d_t in tiangan2) or (m_t in tiangan5 and d_t in tiangan3) or (m_t in tiangan6 and d_t in tiangan4) or (m_t in tiangan7 and d_t in tiangan5) or (m_t in tiangan8 and d_t in tiangan6) or (m_t in tiangan9 and d_t in tiangan7) or (m_t in tiangan10 and d_t in tiangan8):
    value2 = "月干食神"
    print(value2)
if (m_t in tiangan1 and d_t in tiangan10) or (m_t in tiangan2 and d_t in tiangan9) or (m_t in tiangan3 and d_t in tiangan2) or (m_t in tiangan4 and d_t in tiangan1) or (m_t in tiangan5 and d_t in tiangan4) or (m_t in tiangan6 and d_t in tiangan3) or (m_t in tiangan7 and d_t in tiangan6) or (m_t in tiangan8 and d_t in tiangan5) or (m_t in tiangan9 and d_t in tiangan8) or (m_t in tiangan10 and d_t in tiangan7):
    value2 = "月干伤官"
    print(value2)

# 确定时干十神
if (h_t in tiangan1 and d_t in tiangan1) or (h_t in tiangan2 and d_t in tiangan2) or (h_t in tiangan3 and d_t in tiangan3) or (h_t in tiangan4 and d_t in tiangan4) or (h_t in tiangan5 and d_t in tiangan5) or (h_t in tiangan6 and d_t in tiangan6) or (h_t in tiangan7 and d_t in tiangan7) or (h_t in tiangan8 and d_t in tiangan8) or (h_t in tiangan9 and d_t in tiangan9) or (h_t in tiangan10 and d_t in tiangan10):
    value3 = "时干比肩"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan2) or (h_t in tiangan2 and d_t in tiangan1) or (h_t in tiangan3 and d_t in tiangan4) or (h_t in tiangan4 and d_t in tiangan3) or (h_t in tiangan5 and d_t in tiangan6) or (h_t in tiangan6 and d_t in tiangan5) or (h_t in tiangan7 and d_t in tiangan8) or (h_t in tiangan8 and d_t in tiangan7) or (h_t in tiangan9 and d_t in tiangan10) or (h_t in tiangan10 and d_t in tiangan9):
    value3 = "时干劫财"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan3) or (h_t in tiangan2 and d_t in tiangan4) or (h_t in tiangan3 and d_t in tiangan5) or (h_t in tiangan4 and d_t in tiangan6) or (h_t in tiangan5 and d_t in tiangan7) or (h_t in tiangan6 and d_t in tiangan8) or (h_t in tiangan7 and d_t in tiangan9) or (h_t in tiangan8 and d_t in tiangan10) or (h_t in tiangan9 and d_t in tiangan1) or (h_t in tiangan10 and d_t in tiangan2):
    value3 = "时干偏印"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan4) or (h_t in tiangan2 and d_t in tiangan3) or (h_t in tiangan3 and d_t in tiangan6) or (h_t in tiangan4 and d_t in tiangan5) or (h_t in tiangan5 and d_t in tiangan8) or (h_t in tiangan6 and d_t in tiangan7) or (h_t in tiangan7 and d_t in tiangan10) or (h_t in tiangan8 and d_t in tiangan9) or (h_t in tiangan9 and d_t in tiangan2) or (h_t in tiangan10 and d_t in tiangan1):
    value3 = "时干正印"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan5) or (h_t in tiangan2 and d_t in tiangan6) or (h_t in tiangan3 and d_t in tiangan7) or (h_t in tiangan4 and d_t in tiangan8) or (h_t in tiangan5 and d_t in tiangan9) or (h_t in tiangan6 and d_t in tiangan10) or (h_t in tiangan7 and d_t in tiangan1) or (h_t in tiangan8 and d_t in tiangan2) or (h_t in tiangan9 and d_t in tiangan3) or (h_t in tiangan10 and d_t in tiangan4):
    value3 = "时干七杀"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan6) or (h_t in tiangan2 and d_t in tiangan5) or (h_t in tiangan3 and d_t in tiangan8) or (h_t in tiangan4 and d_t in tiangan7) or (h_t in tiangan5 and d_t in tiangan10) or (h_t in tiangan6 and d_t in tiangan9) or (h_t in tiangan7 and d_t in tiangan2) or (h_t in tiangan8 and d_t in tiangan1) or (h_t in tiangan9 and d_t in tiangan4) or (h_t in tiangan10 and d_t in tiangan3):
    value3 = "时干正官"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan7) or (h_t in tiangan2 and d_t in tiangan8) or (h_t in tiangan3 and d_t in tiangan9) or (h_t in tiangan4 and d_t in tiangan10) or (h_t in tiangan5 and d_t in tiangan1) or (h_t in tiangan6 and d_t in tiangan2) or (h_t in tiangan7 and d_t in tiangan3) or (h_t in tiangan8 and d_t in tiangan4) or (h_t in tiangan9 and d_t in tiangan5) or (h_t in tiangan10 and d_t in tiangan6):
    value3 = "时干偏财"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan8) or (h_t in tiangan2 and d_t in tiangan7) or (h_t in tiangan3 and d_t in tiangan10) or (h_t in tiangan4 and d_t in tiangan9) or (h_t in tiangan5 and d_t in tiangan2) or (h_t in tiangan6 and d_t in tiangan1) or (h_t in tiangan7 and d_t in tiangan4) or (h_t in tiangan8 and d_t in tiangan3) or (h_t in tiangan9 and d_t in tiangan6) or (h_t in tiangan10 and d_t in tiangan5):
    value3 = "时干正财"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan9) or (h_t in tiangan2 and d_t in tiangan10) or (h_t in tiangan3 and d_t in tiangan1) or (h_t in tiangan4 and d_t in tiangan2) or (h_t in tiangan5 and d_t in tiangan3) or (h_t in tiangan6 and d_t in tiangan4) or (h_t in tiangan7 and d_t in tiangan5) or (h_t in tiangan8 and d_t in tiangan6) or (h_t in tiangan9 and d_t in tiangan7) or (h_t in tiangan10 and d_t in tiangan8):
    value3 = "时干食神"
    print(value3)
if (h_t in tiangan1 and d_t in tiangan10) or (h_t in tiangan2 and d_t in tiangan9) or (h_t in tiangan3 and d_t in tiangan2) or (h_t in tiangan4 and d_t in tiangan1) or (h_t in tiangan5 and d_t in tiangan4) or (h_t in tiangan6 and d_t in tiangan3) or (h_t in tiangan7 and d_t in tiangan6) or (h_t in tiangan8 and d_t in tiangan5) or (h_t in tiangan9 and d_t in tiangan8) or (h_t in tiangan10 and d_t in tiangan7):
    value3 = "时干伤官"
    print(value3)
# 十神之间关系的论断
user_input = input(value1)
print("用户输入：", user_input)