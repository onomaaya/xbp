#インポート文
import random as r
import tkinter,tkinter.messagebox

#tkinterの初期化
root = tkinter.Tk()
root.withdraw()

#メッセージボックスの表示
tkinter.messagebox.showinfo(title="あなたの今日の運勢を勝手に占っちゃいます。",
message = "下のボタンを押してください。")

#運勢の一覧（リスト）
unseis = ["大吉","中吉","小吉","吉","凶","大凶"]

#運勢の一覧からランダムで選択
unsei = r.choice(unseis)

#運勢の内容で表示する文章を変える
if unsei == "大吉" or unsei == "中吉":
   detail = "おめでとうございます。運命の人と出会うかも！？"
elif unsei == "小吉" or unsei == "吉":
   detail = "ごくごく普通の一日です。転ばないように気を付けてください。"
else:
   detail = "今日は家にいてください。絶対に、、。"

#結果の表示
tkinter.messagebox.showinfo(title="今日の運勢は、、！",
message="あなたの今日の運勢は{0}です。\n{1}".format(unsei,detail))

tkinter.messagebox.showinfo(title="結果がやだったらもう一回やてみてね♡",
message="以上、今日の運勢でした！皆さん今日も頑張って生きましょう！")
#自動的に閉じる