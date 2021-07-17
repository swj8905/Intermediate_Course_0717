from konlpy.tag import Okt

okt = Okt()
# result = okt.pos("이런 것도 되나욬ㅋㅋㅋㅋㅋㅋ")
result = okt.nouns("나는 파이썬을 공부 중입니다.")
print(result)