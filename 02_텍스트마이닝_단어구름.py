from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

keyword = input("키워드 입력 >> ")
encoded = par.quote(keyword) # 한글 -> 특수한 문자

page_num = 1
output_total = ""
while True:
    url = "https://news.joins.com/Search/JoongangNews?page={}&Keyword={}&SortType=New&SearchCategoryType=JoongangNews".format(page_num, encoded)
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h2.headline.mg > a")
    if len(title) == 0: # 끝 페이지까지 크롤링 완료했으면?
        break
    for i in title:
        print("제목 :", i.text)
        print("링크 :", i.attrs["href"])
        print()
        code_news = req.urlopen(i.attrs["href"])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        result = content.text.strip().replace("     ", " ").replace("   ", "")
        print(result)
        output_total += result

    if page_num == 1:
        break
    page_num += 1

# 형태소 분석
print("형태소를 분석 중입니다..")
from konlpy.tag import Okt

okt = Okt()
nouns_list = okt.nouns(output_total)
print(nouns_list)

# 불용어 제거
print("불용어를 제거 합니다..")
nouns_list_without_stopwords = []
for i in nouns_list:
    if len(i) != 1:
        nouns_list_without_stopwords.append(i)

# 단어 출현 빈도수 카운트
print("단어 출현 빈도수를 카운트합니다.")
from collections import Counter
count_result = Counter(nouns_list_without_stopwords)
print(count_result)

# 단어구름 만들기
print("단어구름을 만듭니다.")
from wordcloud import WordCloud
wc = WordCloud(font_path="./NanumMyeongjoBold.ttf",
               background_color="white").generate_from_frequencies(count_result)

# 단어구름 띄우기
import matplotlib.pyplot as plt
plt.figure() # 창 만들기
plt.imshow(wc, interpolation="bilinear") # 창에 이미지 넣기
plt.axis("off") # 축 없애기
plt.show()