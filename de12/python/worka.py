 print("私には15歳になる息子がいる。なにやらそろそろ反抗期が始まりそうだ・・・"
        "〜息子帰宅〜"
        "息子「ただいま〜」")
        
        selecta=int(input("1.「おかえり〜ケーキあるよ」2.「おかえり、テストどうだったの？」"))
        
        if selecta==1:
            print("息子「今おなかすいてないからあとで食べるわ」")
            selectab=int(input("1.「わかった後で一緒に食べよう！」2.「早く食べな」"))
        
            if selectab==1:
                print("息子「わかった〜」")
                print("〜1時間後〜")
                selectaba=int(input("1.「そろそろ食べよう？」2.「まだ〜？」"))
        
                if selectaba==1:
                    print("息子「うん！いいよ！」")
                    print("母（息子と一緒にケーキを食べることができた。いい子に育ってくれてよかった・・！）")
        
                elif selectaba==2:
                    print("息子「ちょっと待ってて・・・」")
                    print("母（結局息子と一緒にケーキを食べることができた。まだ反抗期ではないかな・・？）")
        
        
            elif selectab==2:
                print("息子「わかったって・・・」")
                selectabb=int(input("1.「食べるとき言ってね」2.「何その言い方」"))
        
                if selectabb==1:
                    print("息子「うん・・・」")
                    print("母（結局食べてくれたみたい。反抗気ではないか・・・）")
        
                elif selectabb==2:
                    print("息子「・・・」")
                    print("母（まだケーキに手をつけていないみたい。反抗期・・？）")
                    
        
        elif selecta==2:
            print("息子「まあまあ・・・」")
            selectbb=int(input("1.「次は頑張りなさいね」2.「ちゃんと勉強してるの？」"))
        
            if selectbb==1:
                print("息子「あぁ・・・」")
                selectbba=int(input("1.「応援してるよ」2.「しっかりしなさいよ？」"))
        
                if selectbba==1:
                    print("息子「うん・・・」")
                    print("母（ちょっと嫌な顔されたけど、まだ反抗期ではないかな・・？）")
        
                elif selectbba==2:
                    print("息子「わかったってば・・・」")
                    print("母（部屋に戻ってしまった息子。プチ反抗期？）")
        
            elif selectbb==2:
                print("息子「うるせぇなぁ・・・」")
                selectbbb=int(input("1.「言いすぎちゃった、ごめんね」2.「何その言い方」"))
        
                if selectbbb==1:
                    print("息子「・・・」")
                    print("母（部屋に戻ってしまった息子。結構反抗期かも・・・）")
        
                elif selectbbb==2:
                    print("息子「うっせぇ！黙れよ！！」ﾊﾞﾝ")
                    print("母（部屋に戻ってしまった息子。引きこもって3日も出てこない、反抗期になってしまった。）")
