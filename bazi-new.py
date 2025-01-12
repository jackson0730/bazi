from lunar_python import Solar, Lunar
from datetime import datetime
# import pandas as pd

# 定义基础数据
tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 定义关系映射
sanhe = {
    ("申", "子", "辰"): "水局",
    ("巳", "酉", "丑"): "金局",
    ("寅", "午", "戌"): "火局",
    ("亥", "卯", "未"): "木局"
}

liuchong = {
    "子": "午", "午": "子",
    "丑": "未", "未": "丑",
    "寅": "申", "申": "寅",
    "卯": "酉", "酉": "卯",
    "辰": "戌", "戌": "辰",
    "巳": "亥", "亥": "巳"
}

liuhai = {
    # 添加六害关系
}

sanxing = {
    ("子", "卯"): "子卯刑",
    ("寅", "巳", "申"): "寅巳申三刑",
    ("丑", "未", "戌"): "丑未戌三刑"
}

zixing = {"辰", "午", "酉", "亥"}

# 定义十神关系映射
shishen_map = {('甲', '甲'): '比肩', ('甲', '乙'): '劫财', ('甲', '丙'): '食神', ('甲', '丁'): '伤官', ('甲', '戊'): '偏财', ('甲', '己'): '正财', ('甲', '庚'): '七杀', ('甲', '辛'): '正官', ('甲', '壬'): '偏印', ('甲', '癸'): '正印', ('乙', '甲'): '劫财', ('乙', '乙'): '比肩', ('乙', '丙'): '伤官', ('乙', '丁'): '食神', ('乙', '戊'): '正财', ('乙', '己'): '偏财', ('乙', '庚'): '正官', ('乙', '辛'): '七杀', ('乙', '壬'): '正印', ('乙', '癸'): '偏印', ('丙', '甲'): '偏印', ('丙', '乙'): '正印', ('丙', '丙'): '比肩', ('丙', '丁'): '劫财', ('丙', '戊'): '食神', ('丙', '己'): '伤官', ('丙', '庚'): '偏财', ('丙', '辛'): '正财', ('丙', '壬'): '七杀', ('丙', '癸'): '正官', ('丁', '甲'): '正印', ('丁', '乙'): '偏印', ('丁', '丙'): '劫财', ('丁', '丁'): '比肩', ('丁', '戊'): '伤官', ('丁', '己'): '食神', ('丁', '庚'): '正财', ('丁', '辛'): '偏财', ('丁', '壬'): '正官', ('丁', '癸'): '七杀', ('戊', '甲'): '七杀', ('戊', '乙'): '正官', ('戊', '丙'): '偏印', ('戊', '丁'): '正印', ('戊', '戊'): '比肩', ('戊', '己'): '劫财', ('戊', '庚'): '食神', ('戊', '辛'): '伤官', ('戊', '壬'): '偏财', ('戊', '癸'): '正财', ('己', '甲'): '正官', ('己', '乙'): '七杀', ('己', '丙'): '正印', ('己', '丁'): '偏印', ('己', '戊'): '劫财', ('己', '己'): '比肩', ('己', '庚'): '伤官', ('己', '辛'): '食神', ('己', '壬'): '正财', ('己', '癸'): '偏财', ('庚', '甲'): '偏财', ('庚', '乙'): '正财', ('庚', '丙'): '七杀', ('庚', '丁'): '正官', ('庚', '戊'): '偏印', ('庚', '己'): '正印', ('庚', '庚'): '比肩', ('庚', '辛'): '劫财', ('庚', '壬'): '食神', ('庚', '癸'): '伤官', ('辛', '甲'): '正财', ('辛', '乙'): '偏财', ('辛', '丙'): '正官', ('辛', '丁'): '七杀', ('辛', '戊'): '正印', ('辛', '己'): '偏印', ('辛', '庚'): '劫财', ('辛', '辛'): '比肩', ('辛', '壬'): '伤官', ('辛', '癸'): '食神', ('壬', '甲'): '食神', ('壬', '乙'): '伤官', ('壬', '丙'): '偏财', ('壬', '丁'): '正财', ('壬', '戊'): '七杀', ('壬', '己'): '正官', ('壬', '庚'): '偏印', ('壬', '辛'): '正印', ('壬', '壬'): '比肩', ('壬', '癸'): '劫财', ('癸', '甲'): '伤官', ('癸', '乙'): '食神', ('癸', '丙'): '正财', ('癸', '丁'): '偏财', ('癸', '戊'): '正官', ('癸', '己'): '七杀', ('癸', '庚'): '正印', ('癸', '辛'): '偏印', ('癸', '壬'): '劫财', ('癸', '癸'): '比肩'}

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

# 添加地支十神映射
dizhi_shishen = {'子': {'甲': '正印', '乙': '偏印', '丙': '正官', '丁': '七杀', '戊': '正财', '己': '偏财', '庚': '伤官', '辛': '食神', '壬': '劫财', '癸': '比肩'}, '丑': {'甲': '正财', '乙': '偏财', '丙': '伤官', '丁': '食神', '戊': '劫财', '己': '比肩', '庚': '正印', '辛': '偏印', '壬': '正官', '癸': '七杀'}, '寅': {'甲': '比肩', '乙': '劫财', '丙': '偏印', '丁': '正印', '戊': '七杀', '己': '正官', '庚': '偏财', '辛': '正财', '壬': '食神', '癸': '伤官'}, '卯': {'甲': '劫财', '乙': '比肩', '丙': '正印', '丁': '偏印', '戊': '正官', '己': '七杀', '庚': '正财', '辛': '偏财', '壬': '伤官', '癸': '食神'}, '辰': {'甲': '偏财', '乙': '正财', '丙': '食神', '丁': '伤官', '戊': '比肩', '己': '劫财', '庚': '偏印', '辛': '正印', '壬': '七杀', '癸': '正官'}, '巳': {'甲': '食神', '乙': '伤官', '丙': '比肩', '丁': '劫财', '戊': '偏印', '己': '正印', '庚': '七杀', '辛': '正官', '壬': '偏财', '癸': '正财'}, '午': {'甲': '伤官', '乙': '食神', '丙': '劫财', '丁': '比肩', '戊': '正印', '己': '偏印', '庚': '正官', '辛': '七杀', '壬': '正财', '癸': '偏财'}, '未': {'甲': '正财', '乙': '偏财', '丙': '伤官', '丁': '食神', '戊': '劫财', '己': '比肩', '庚': '正印', '辛': '偏印', '壬': '正官', '癸': '七杀'}, '申': {'甲': '七杀', '乙': '正官', '丙': '偏财', '丁': '正财', '戊': '食神', '己': '伤官', '庚': '比肩', '辛': '劫财', '壬': '偏印', '癸': '正印'}, '酉': {'甲': '正官', '乙': '七杀', '丙': '正财', '丁': '偏财', '戊': '伤官', '己': '食神', '庚': '劫财', '辛': '比肩', '壬': '正印', '癸': '偏印'}, '戌': {'甲': '偏财', '乙': '正财', '丙': '食神', '丁': '伤官', '戊': '比肩', '己': '劫财', '庚': '偏印', '辛': '正印', '壬': '七杀', '癸': '正官'}, '亥': {'甲': '偏印', '乙': '正印', '丙': '七杀', '丁': '正官', '戊': '偏财', '己': '正财', '庚': '食神', '辛': '伤官', '壬': '比肩', '癸': '劫财'}}

# 定义四刑组
sixing = [
    ("子", "午", "卯", "酉"),
    ("寅", "申", "巳", "亥"),
    ("辰", "戌", "丑", "未")
]

def get_shishen(gan1, gan2):
    """获取十神关系"""
    result = shishen_map.get((gan1, gan2))
    #print(f"DEBUG - 查找十神关系: 日干{gan1}看{gan2}, 结果: {result}")
    return result

def check_sanhe(dizhi_list):
    """检查三合"""
    positions = ["年支", "月支", "日支", "时支"]
    for he_zhi, ju in sanhe.items():
        matched_positions = []
        for i, zhi in enumerate(dizhi_list):
            if zhi in he_zhi:
                matched_positions.append(i)
        if len(matched_positions) >= 3:
            pos_names = [positions[i] for i in matched_positions[:3]]
            print(f"三合提示：{pos_names[0]}、{pos_names[1]}、{pos_names[2]}形成{he_zhi[0]}{he_zhi[1]}{he_zhi[2]}三合{ju}")
            return True
    return False

def check_chong_hai(dizhi_list, relation_dict, relation_name):
    """检查六冲或六害"""
    positions = ["年支", "月支", "日支", "时支"]
    found = False
    for i, zhi1 in enumerate(dizhi_list):
        for j, zhi2 in enumerate(dizhi_list[i+1:], i+1):
            if relation_dict.get(zhi1) == zhi2:
                print(f"{relation_name}提示：{positions[i]}{zhi1}冲{positions[j]}{zhi2}")
                found = True
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

def get_dizhi_shishen(dizhi, ri_gan):
    """获取地支十神"""
    return dizhi_shishen[dizhi][ri_gan]

def get_next_ganzi(current_gan, current_zhi, forward=True):
    """获取下一个干支"""
    gan_idx = tiangan.index(current_gan)
    zhi_idx = dizhi.index(current_zhi)
    
    if forward:
        gan_idx = (gan_idx + 1) % 10
        zhi_idx = (zhi_idx + 1) % 12
    else:
        gan_idx = (gan_idx - 1) % 10
        zhi_idx = (zhi_idx - 1) % 12
    
    return tiangan[gan_idx], dizhi[zhi_idx]

def get_dayun(year_gan, month_gan, month_zhi, gender, lunar):
    """计算大运"""
    # 判断年干阴阳
    yang_gan = ["甲", "丙", "戊", "庚", "壬"]
    is_yang_year = year_gan in yang_gan
    
    # 判断大运顺逆
    forward = (is_yang_year and gender == '男') or (not is_yang_year and gender == '女')
    
    # 计算大运干支
    dayun_ganzhi = []
    current_gan, current_zhi = month_gan, month_zhi
    
    for i in range(8):
        next_gan, next_zhi = get_next_ganzi(current_gan, current_zhi, forward)
        dayun_ganzhi.append((next_gan, next_zhi))
        current_gan, current_zhi = next_gan, next_zhi
    
    # 获取节令时间
    current_time = lunar.getSolar()
    
    # 获取上一个和下一个节令
    prev_jie = lunar.getPrevJie().getSolar()  # 上一个节令
    next_jie = lunar.getNextJie().getSolar()  # 下一个节令
    
    # 计算时间差（精确到分钟）
    if (is_yang_year and gender == '男') or (not is_yang_year and gender == '女'):
        # 计算到下一节令的时间
        days = next_jie.getJulianDay() - current_time.getJulianDay()
    else:
        # 计算到上一节令的时间
        days = current_time.getJulianDay() - prev_jie.getJulianDay()
    
    # 计算起运年龄
    years = days / 3  # 3天计1岁
    
    # 添加小时和分钟的影响
    hours = current_time.getHour()
    minutes = current_time.getMinute()
    years += (hours * 5 + minutes * (5/60)) / 365.25  # 1小时计5天，1分钟计2小时
    
    start_age = round(years, 1)
    start_year = lunar.getYear() + int(start_age)
    start_month = (lunar.getMonth() + int((years - int(years)) * 12)) % 12
    
    return dayun_ganzhi, start_age, start_year, start_month

# def update_shishen_from_excel(file_path):
#     # 读取天干十神表
#     tg_df = pd.read_excel(file_path, sheet_name='天干十神', index_col=0)
#     for ri_gan in tg_df.index:
#         for other_gan in tg_df.columns:
#             shishen_map[(ri_gan, other_gan)] = tg_df.at[ri_gan, other_gan]
#     print(shishen_map)

#     # 读取地支十神表
#     dz_df = pd.read_excel(file_path, sheet_name='地支十神', index_col=0)
#     for ri_gan in dz_df.index:
#         for zhi in dz_df.columns:
#             dizhi_shishen[zhi][ri_gan] = dz_df.at[ri_gan, zhi]
#     print(dizhi_shishen)

def check_fuyin(dizhi_list):
    """检查地支伏吟"""
    positions = ["年支", "月支", "日支", "时支"]
    # 统计每个地支出现的位置
    zhi_positions = {}
    found = False
    for i, zhi in enumerate(dizhi_list):
        if zhi not in zhi_positions:
            zhi_positions[zhi] = []
        zhi_positions[zhi].append(i)
    
    # 检查重复
    for zhi, pos_list in zhi_positions.items():
        if len(pos_list) >= 2:
            pos_names = [positions[i] for i in pos_list]
            print(f"伏吟提示：{'、'.join(pos_names)}出现{zhi}伏吟({len(pos_list)}重)")
            found = True
    return found

def check_sixing(dizhi_list):
    """检查地支四刑"""
    positions = ["年支", "月支", "日支", "时支"]
    found = False
    
    # 对于每个四刑组合
    for xing_group in sixing:
        # 收集当前八字中属于这个刑组的地支及其位置
        matched_positions = []
        for i, zhi in enumerate(dizhi_list):
            if zhi in xing_group:
                matched_positions.append((i, zhi))
        
        # 如果找到2个或以上的刑
        if len(matched_positions) >= 2:
            # 排除纯伏吟的情况
            unique_zhi = len(set(zhi for _, zhi in matched_positions))
            if unique_zhi > 1:  # 不是纯伏吟
                found = True
                pos_desc = []
                for i, zhi in matched_positions:
                    pos_desc.append(f"{positions[i]}{zhi}")
                print(f"四刑提示：{'、'.join(pos_desc)}形成{len(matched_positions)}刑")
    return found

def main():
    while True:  # 添加循环
        # 在程序开始时打印检查信息
        # update_shishen_from_excel('十神关系表.xlsx')
        
        # 获取用户输入的阳历年月日时
        print("请输入阳历年月日时(格式:年 月 日 时),如 1990 1 1 12:")
        try:
            year, month, day, hour = map(int, input().split())
            print("请输入性别(男/女):")
            gender = input().strip()
            
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

            # 检查四刑
            if not check_sixing(dizhi_list):
                print("四刑提示：无")

            # 检查自刑
            if not check_zixing(dizhi_list):
                print("自刑提示：无")

            # 检查伏吟
            if not check_fuyin(dizhi_list):
                print("伏吟提示：无")

           

            # 计算十神（只显示日干对其他天干的关系）
            print(f"\n日干十神：")
            print(f"日干{d_t}看年干{y_t}为{get_shishen(d_t, y_t)}")
            print(f"日干{d_t}看月干{m_t}为{get_shishen(d_t, m_t)}")
            print(f"日干{d_t}看时干{h_t}为{get_shishen(d_t, h_t)}")
            
            # 输出地支十神（日干看地支）
            print("\n日干看地支：")
            print(f"日干{d_t}看年支{y_d}为{get_dizhi_shishen(y_d, d_t)}")
            print(f"日干{d_t}看月支{m_d}为{get_dizhi_shishen(m_d, d_t)}")
            print(f"日干{d_t}看日支{d_d}为{get_dizhi_shishen(d_d, d_t)}")
            print(f"日干{d_t}看时支{h_d}为{get_dizhi_shishen(h_d, d_t)}")
            
            # 计算大运
            dayun_ganzhi, start_age, start_year, start_month = get_dayun(y_t, m_t, m_d, gender, lunar)
            print(f"\n大运（{start_age}岁/{start_year}年{start_month}月起运）:")
            for i, (gan, zhi) in enumerate(dayun_ganzhi, 1):
                age = start_age + (i-1) * 10
                year = start_year + (i-1) * 10
                month = (start_month + (i-1) * 10) % 12
                shishen_gan = get_shishen(d_t, gan)
                shishen_zhi = get_dizhi_shishen(zhi, d_t)
                changsheng = get_changsheng(d_t, zhi)
                print(f"第{i}运({int(age)}-{int(age+10)}岁/{year}-{year+10}年{month}月): {gan}{zhi} - 对日干{d_t}来说，{gan}是{shishen_gan}，{zhi}是{shishen_zhi}，{d_t}在{zhi}是{changsheng}")
            
            # 添加继续判断
            print("\n是否继续排盘？(Y/N)")
            choice = input().strip().upper()
            if choice != 'Y':
                break

        except ValueError:
            print("输入格式错误!请按照格式要求输入.")
        except Exception as e:
            print(f"发生错误: {str(e)}")
            
        # 添加继续判断（发生错误时也询问）
        print("\n是否继续排盘？(Y/N)")
        choice = input().strip().upper()
        if choice != 'Y':
            break

if __name__ == "__main__":
    main()