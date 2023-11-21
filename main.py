import pandas as pd
import random
from time import sleep

import itertools
# 名簿を読み込む
df = pd.read_csv("名簿.csv", header = 0, encoding = "shift-jis")
# print(df)
# print(len(df))
# print(len(df.columns))

# 席数を読み込む
seatN = list(pd.read_csv("席数.csv", header = None, encoding = "shift-jis").loc[0])
# print(seatN)
# そのうえで空のリストを作る
seatSet = []
numSet = []
for i in range(len(seatN)):
    seatSet.append([])
    numSet.append(i)
# print(seatSet)
# print(numSet)

# 属性（部署等）の種類をリストにする
alllist = list(df["属性1"])+list(df["属性2"])+list(df["属性3"])+list(df["属性4"])+list(df["属性5"])

xlist = list(set(alllist))
# print(xlist)

x2list = [item for item in xlist if not(pd.isnull(item)) == True]
# print(x2list)

# 属性の数のリスト
NoZokusei = []
for x in x2list:
    NoZokusei.append(alllist.count(x))
# print(NoZokusei)

# 属性の数と席数の差のリスト
SaZokusei = [n - 8 for n in NoZokusei]
# print(SaZokusei)

# ランダムな人から始まるように
r1 = random.randint(0,len(df)-1)
# print(r1)

while True:
    # やり直し関数
    dcount = 0
    # 出来た回数
    ccount = 0
    seatSet = []
    numSet = []
    for i in range(len(seatN)):
        seatSet.append([])
        numSet.append(i)
    wseatSet = seatSet
    wnumSet = numSet

    # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    # print(wseatSet)
    for i in range(len(df)):
        # ランダムな人から始まるように
        r2 = r1 + i
        if r2 >= len(df):
            r2 = r2-len(df)
        kari_numSet = wnumSet
        NOW = df.iloc[r2].to_list()
        # print(NOW)
        # 自分の属性確認
        NOWZokusei = list(set([item for item in NOW[2:] if not(pd.isnull(item)) == True]))
        # print(NOWZokusei)
        while True:
            # ランダムに席を決める
            r3 = random.choice(kari_numSet)
            # print(r3)
            # print(seatSet[r3])
            

            # シートに座っている人の属性を確認
            seatlistZokusei = []
            for i in wseatSet[r3]:
                seatlist1 = df.iloc[i].to_list()
                # print(seatlist1[2:])
                seatlistZokusei.extend(seatlist1[2:])
            
            seatlistZokusei = list(set([item for item in seatlistZokusei if not(pd.isnull(item)) == True]))
            # print(seatlistZokusei)
            # 属性確認ここまで

            #属性かぶりを確認
            DoubleZokusei = list(set(NOWZokusei) & set(seatlistZokusei))
            # print(DoubleZokusei)
            if DoubleZokusei == []:
                # print("被りなしだよ")
                break
            # sleep(5)
            # print(kari_numSet)
            dcount += 1
            if dcount >10:
                break
            
            
        if dcount >10:
            break
        dcount = 0
        # 席を配置
        wseatSet[r3].append(r2)
        # 席が埋まってないか確認
        if len(seatSet[r3]) >= seatN[r3]:
            # print(r3)
            wnumSet.remove(r3)

        # print(wseatSet)
        ccount += 1
        # print(ccount)
        
    # sleep(0.3)
    if ccount == len(df):
        break

print(wseatSet)
# wseatSet = list(itertools.chain.from_iterable(wseatSet))
