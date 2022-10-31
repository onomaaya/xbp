from abc import ABC
import array
from re import A

from regex import B
from sympy import O


print("こんにちは")
print("これから血液型と生まれた月日で占いを始めます。")

print("誕生日占い")
blood=input("あなたの血液型は？")
month=input("あなたの生まれた月は？")
day=input("あなたの生まれた日は？")

blood=("意外と","思った通り","驚くほど","なぜか")
month=("5年後の自分は","明日の自分は","100歳の自分は","1か月後の自分は",)
day=("セクシーになる","お金持ちになる","健康になる","モテている")
for a,b,c in zip (blood,month,day):
    print("blood=[],month=[],day=[]".format(a,b,c))
