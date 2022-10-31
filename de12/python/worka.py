
print("私には15歳になる息子がいる。なにやらそろそろ反抗期が始まりそうだ・・・"
"〜息子帰宅〜"
"息子「ただいま〜」")

selecta=int(input("1.「おかえり〜ケーキあるよ」2.「おかえり、テストどうだったの？」"))

if selecta==1:
    print("息子「今おなかすいてないからあとで食べるわ」")
    selectab=int(input("1.「わかった、あとでたべよう」2.「早く食べなよ」"))

    if selectab==1:
        print("息子「」")
        selectaba=int(input("1.「」2.「」"))

        if selectaba==1:
            print("息子「」")

        elif selectaba==2:
            print("息子「」")

    elif selectab==2:
        print("息子「」")
        selectabb=int(input("1.「」2.「」"))

        if selectabb==1:
            print("息子「」")

        elif selectabb==2:
            print("息子「」")

elif selecta==2:
    print("息子「まあまあ・・・」")
    selectbb=int(input("1.「次は頑張りなさいね」2.「ちゃんと勉強してるの？」"))

    if selectbb==1:
        print("あぁ・・・")
        selectbba=int(input("1.「」2.「」"))

        if selectbba==1:
            print("息子「」")

        elif selectbba==2:
            print("息子「」")

    elif selectbb==2:
        print("うるせぇなぁ・・・")
        selectbbb=int(input("1.「」2.「」"))

        if selectbbb==1:
            print("息子「」")

        elif selectbbb==2:
            print("息子「」")