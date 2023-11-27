import pandas as pd
import random
sekigaekaisu = 2
xxx = []
abc = [chr(i) for i in range(65,91)]
# 名簿を読み込む
df = pd.read_csv("名簿.csv", header = 0, encoding = "utf-8")

basedf = df
base2df = df
# print(df)
# print(len(df))
# print(len(df.columns))

for kaisuu1 in range(sekigaekaisu):

    # 席数を読み込む
    seatN = list(pd.read_csv("席数.csv", header = None, encoding = "shift-jis").loc[0])
    # print(seatN)

    # 属性（部署等）の種類をリストにする
    alllist = list(df["属性1"]) + list(df["属性2"]) + list(df["属性3"])+list(df["属性4"])+list(df["属性5"])+list(df["属性6"])

    xlist = list(set(alllist))
    # print(xlist)

    x2list = [item for item in xlist if not(pd.isnull(item)) == True]
    # print("x2listです{}".format(x2list))

    # 属性の数のリスト
    NoZokusei = []
    for x in x2list:
        NoZokusei.append(alllist.count(x))
    # print(NoZokusei)

    # 属性の数と席数の差のリスト
    SaZokusei = [n - 8 for n in NoZokusei]
    # print("属性の数と座席の差のリスト{}".format(SaZokusei))
    for i , x in enumerate(SaZokusei):
        # print("iです{}".format(i))
        # print("xです{}".format(x))
        df2 = df[(df["属性1"] == x2list[i]) | 
                (df["属性2"] == x2list[i]) | 
                (df["属性3"] == x2list[i]) | 
                (df["属性4"] == x2list[i]) | 
                (df["属性5"] == x2list[i]) | 
                (df["属性6"] == x2list[i]) ]
        while x > 0:
            # print("もとの配列です。{}".format(df2))
            # print(list(df2.iloc[4]))
            
            # doubleZokusei.append(x2list[i])
            # print(x)
            rr1 = random.randint(0,len(df2)-1)
            # print(rr1)
            zz = list(df2.iloc[rr1])
            # print(zz[0])
            # print("らんだむの数です。{}".format(rr1))
            # print("ランダムの数の行目のリスト{}".format(zz))
            # "本部長"が何番目にあるか
            checkRow = zz.index(x2list[i])
            checkColumn = zz[0]-1
            # print("CheckRowです。{}".format(checkRow))
            # print("CheckColumnです。{}".format(checkColumn))
            df.iat[checkColumn,checkRow] = x2list[i] + str(abc[i]) 
            # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            # print(df.iat[checkColumn,checkRow])

            df2 = df2.drop(zz[0]-1)
            # print("削除後の配列です。{}".format(df2))
            x -= 1
            
            # print(doubleZokusei)
    # print(df)
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
            ccount += 1
        if ccount == len(df):
            break

    print(wseatSet)
    xxx.append(wseatSet)
    for n,x in enumerate(wseatSet):
        print(x)
        print(abc[n])
        for m,y in enumerate(x):
            basedf.iat[y,-kaisuu1-1] = abc[n] 

for kaisuu1 in range(sekigaekaisu):
        for n,x in enumerate(xxx[kaisuu1]):
            print(x)
            print(abc[n])
            for m,y in enumerate(x):
                basedf.iat[y,-kaisuu1-1] = abc[n] + str(m+1)

print(basedf)
df.to_csv("完成品.csv",index = False)