from lunar_python import Solar, Lunar
from datetime import datetime

# 定义基础数据
tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 定义关系映射
sanhe = {
    "水局": {"申", "子", "辰"},
    "火局": {"寅", "午", "戌"},
    "金局": {"巳", "酉", "丑"},
    "木局": {"亥", "卯", "未"}
}

liuchong = {
    ("子", "午"), ("丑", "未"), ("寅", "申"),
    ("卯", "酉"), ("辰", "戌"), ("巳", "亥")
}

liuhai = {
    ("子", "未"), ("丑", "午"), ("寅", "巳"),
    ("卯", "辰"), ("申", "亥"), ("酉", "戌")
}

sanxing = {
    ("子", "卯"): "子卯刑",
    ("寅", "巳", "申"): "寅巳申三刑",
    ("丑", "未", "戌"): "丑未戌三刑"
}

zixing = {"辰", "午", "酉", "亥"}

# 定义十神关系映射
shishen_map = {
    # 格式: (干支关系位置): "十神名称"
    (0, 0): "比肩", (0, 1): "劫财", (0, 2): "偏印", (0, 3): "正印",
    (0, 4): "七杀", (0, 5): "正官", (0, 6): "偏财", (0, 7): "正财",
    (0, 8): "食神", (0, 9): "伤官"
}

# 添加长生十二运映射
changsheng_map = {
    "甲": "亥", "乙": "午", "丙": "寅", "丁": "酉",
    "戊": "寅", "己": "酉", "庚": "巳", "辛": "子",
    "壬": "申", "癸": "卯"
}

# 长生十二运顺序
changsheng_order = ["长生", "沐浴", "冠带", "临官", "帝旺", "衰", "病", "死", "墓", "绝", "胎", "养"]

# 添加三会关系定义
sanhui = {
    "会水": {"申", "子", "辰"},
    "会金": {"巳", "酉", "丑"},
    "会火": {"寅", "午", "戌"},
    "会木": {"亥", "卯", "未"}
}

# 添加天干合化关系
ganhe = {
    ("甲", "己"): "化土",
    ("乙", "庚"): "化金",
    ("丙", "辛"): "化水",
    ("丁", "壬"): "化木",
    ("戊", "癸"): "化火"
}

def get_shishen(gan1, gan2):
    """计算十神关系"""
    pos1 = tiangan.index(gan1)
    pos2 = tiangan.index(gan2)
    diff = (pos2 - pos1) % 10
    return shishen_map.get((0, diff))

def check_sanhe(dizhi_list):
    """检查三合"""
    dizhi_set = set(dizhi_list)
    positions = ["年支", "月支", "日支", "时支"]
    for name, combo in sanhe.items():
        if len(combo & dizhi_set) >= 2:
            matched = []
            matched_pos = []
            for i, d in enumerate(dizhi_list):
                if d in combo:
                    matched.append(d)
                    matched_pos.append(positions[i])
            
            if len(matched) == 2:
                print(f"三合提示：{matched_pos[0]}{matched[0]}与{matched_pos[1]}{matched[1]}半合{name}")
            elif len(matched) == 3:
                print(f"三合提示：{matched_pos[0]}{matched[0]}、{matched_pos[1]}{matched[1]}与{matched_pos[2]}{matched[2]}成{name}")
            return True
    return False

def check_chong_hai(dizhi_list, relations, relation_name):
    """检查冲害关系"""
    found = False
    results = []
    positions = ["年支", "月支", "日支", "时支"]
    
    for i, d1 in enumerate(dizhi_list):
        for j, d2 in enumerate(dizhi_list[i+1:], i+1):
            if (d1, d2) in relations or (d2, d1) in relations:
                if relation_name == "六冲":
                    results.append(f"{positions[i]}{d1}冲{positions[j]}{d2}")
                else:
                    results.append(f"{positions[i]}{d1}害{positions[j]}{d2}")
                found = True
    
    if found:
        print(f"{relation_name}提示：{'，'.join(results)}")
    return found

def check_sanxing(dizhi_list):
    """检查三刑"""
    dizhi_set = set(dizhi_list)
    for combo, name in sanxing.items():
        if set(combo).issubset(dizhi_set):
            print(f"三刑提示：{name}")
            return True
    return False

def check_zixing(dizhi_list):
    """检查自刑"""
    found = False
    results = []
    for zi in zixing:
        if dizhi_list.count(zi) >= 2:
            results.append(f"{zi}{zi}")
            found = True
    if found:
        print(f"自刑提示：{'，'.join(results)}")
    return found

def get_changsheng(gan, zhi):
    """获取长生十二运"""
    if gan not in changsheng_map:
        return None
        
    start_zhi = changsheng_map[gan]
    start_idx = dizhi.index(start_zhi)
    current_idx = dizhi.index(zhi)
    
    # 阳干顺数，阴干逆数
    if tiangan.index(gan) % 2 == 0:  # 阳干
        pos = (current_idx - start_idx) % 12
    else:  # 阴干
        pos = (start_idx - current_idx) % 12
        
    return changsheng_order[pos]

def check_sanhui(dizhi_list):
    """检查三会"""
    dizhi_set = set(dizhi_list)
    positions = ["年支", "月支", "日支", "时支"]
    for name, combo in sanhui.items():
        if len(combo & dizhi_set) >= 2:
            matched = []
            matched_pos = []
            for i, d in enumerate(dizhi_list):
                if d in combo:
                    matched.append(d)
                    matched_pos.append(positions[i])
            
            if len(matched) == 2:
                print(f"三会提示：{matched_pos[0]}{matched[0]}与{matched_pos[1]}{matched[1]}半{name}")
            elif len(matched) == 3:
                print(f"三会提示：{matched_pos[0]}{matched[0]}、{matched_pos[1]}{matched[1]}与{matched_pos[2]}{matched[2]}{name}")
            return True
    return False

def check_ganhe(tiangan_list):
    """检查天干合化"""
    found = False
    results = []
    positions = ["年干", "月干", "日干", "时干"]
    
    for i, gan1 in enumerate(tiangan_list):
        for j, gan2 in enumerate(tiangan_list[i+1:], i+1):
            for (g1, g2), he in ganhe.items():
                if (gan1 == g1 and gan2 == g2) or (gan1 == g2 and gan2 == g1):
                    results.append(f"{positions[i]}{gan1}与{positions[j]}{gan2}{he}")
                    found = True
    
    if found:
        print(f"天干合化：{'，'.join(results)}")
    return found

def main():
    # 获取用户输入的阳历年月日时
    print("请输入阳历年月日时(格式:年 月 日 时),如 1990 1 1 12:")
    try:
        year, month, day, hour = map(int, input().split())
        
        # 验证输入
        if not (1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31 and 0 <= hour <= 23):
            print("输入日期有误,请检查!")
            return
            
        # 转换成八字
        solar = Solar.fromYmdHms(year, month, day, hour, 0, 0)
        lunar = solar.getLunar()
        
        # 获取八字
        bazi = lunar.getEightChar()
        y_t, y_d = bazi.getYear()[:1], bazi.getYear()[1:]  # 年柱
        m_t, m_d = bazi.getMonth()[:1], bazi.getMonth()[1:]  # 月柱
        d_t, d_d = bazi.getDay()[:1], bazi.getDay()[1:]  # 日柱
        h_t, h_d = bazi.getTime()[:1], bazi.getTime()[1:]  # 时柱
        
        print(f"\n您的八字是: {y_t}{y_d} {m_t}{m_d} {d_t}{d_d} {h_t}{h_d}")
        
        # 输出长生十二运
        print("\n长生十二运：")
        print(f"年干：{y_t}之{y_d}为{get_changsheng(y_t, y_d)}")
        print(f"月干：{m_t}之{m_d}为{get_changsheng(m_t, m_d)}")
        print(f"日干：{d_t}之{d_d}为{get_changsheng(d_t, d_d)}")
        print(f"时干：{h_t}之{h_d}为{get_changsheng(h_t, h_d)}\n")
        
        # 输出日干对地支的长生十二运关系
        print("日干长生十二运：")
        print(f"日干{d_t}对年支{y_d}为{get_changsheng(d_t, y_d)}")
        print(f"日干{d_t}对月支{m_d}为{get_changsheng(d_t, m_d)}")
        print(f"日干{d_t}对日支{d_d}为{get_changsheng(d_t, d_d)}")
        print(f"日干{d_t}对时支{h_d}为{get_changsheng(d_t, h_d)}\n")
        
        # 以下是原有的八字分析功能
        tiangan_list = [y_t, m_t, d_t, h_t]
        dizhi_list = [y_d, m_d, d_d, h_d]

        # 检查三合
        if not check_sanhe(dizhi_list):
            print("三合提示：无")

        # 检查三会
        if not check_sanhui(dizhi_list):
            print("三会提示：无")

        # 检查天干合化
        if not check_ganhe(tiangan_list):
            print("天干合化：无")

        # 检查六冲
        if not check_chong_hai(dizhi_list, liuchong, "六冲"):
            print("六冲提示：无")

        # 检查六害
        if not check_chong_hai(dizhi_list, liuhai, "六害"):
            print("六害提示：无")

        # 检查三刑
        if not check_sanxing(dizhi_list):
            print("三刑提示：无")

        # 检查自刑
        if not check_zixing(dizhi_list):
            print("自刑提示：无")

        # 计算十神
        print(f"\n十神关系：")
        print(f"年干：{get_shishen(y_t, d_t)}")
        print(f"月干：{get_shishen(m_t, d_t)}")
        print(f"时干：{get_shishen(h_t, d_t)}\n")
        
    except ValueError:
        print("输入格式错误!请按照格式要求输入.")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()