selecta=int(input("気持ち、1.「悲しい」2.「嬉しい」"))

if selecta==1:
    print("時間")
    selecta=int(input("1.「朝」2.「昼」3.「夜」"))

    if selecta==1:
        print("状況")
        selecta=int(input("1.「屋外」2.「屋内」"))

        if selecta==1:
            print("じゃあ、何処")

        elif selecta==2:
            print("プロローグ")

    elif selecta==2:
        print("状況")
        selecta=int(input("1.「屋内」2.「屋外」"))

        if selecta==1:
            print("Answer")

        elif selecta==2:
            print("星屑ビーナス")

    elif selecta==3:
        print("状況")
        selecta=int(input("1.「屋内」2.「屋外」"))

        if selecta==1:
            print("あなたがいることで")

        elif selecta==2:
            print("題名のない今日")      

elif selecta==2:
    print("時間")
    selecta=int(input("1.「朝」2.「昼」3.「夜」"))

    if selecta==1:
        print("状況")
        selecta=int(input("1.「屋内」2.「屋外」"))

        if selecta==1:
            print("ペテルギウス")

        elif selecta==2:
            print("sugar")

    elif selecta==2:
        print("状況")
        selecta=int(input("1.「屋内」2.「屋外」"))

        if selecta==1:
            print("魔法のコトバ")

        elif selecta==2:
            print("ピンクムーン") 

    elif selecta==3:
        print("状況")
        selecta=int(input("1.「屋内」2.「屋外」"))

        if selecta==1:
            print("ダレヨリ")

        elif selecta==2:
            print("ナツノオワリ")  

