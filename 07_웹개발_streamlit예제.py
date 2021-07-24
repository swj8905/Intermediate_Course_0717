import streamlit as st

st.text("일반 텍스트입니다.")
st.text("여기에 내가 쓰고 싶은 문장을")
st.text("쓰면 됩니다.")

st.write("----------------")
st.write("이런 것도 됩니다.")
st.write("# 이런 것도 됩니다.")
st.write("## 이런 것도 됩니다.")
st.write("### 이런 것도 됩니다.")
st.write("#### 이런 것도 됩니다.")
st.write("##### 이런 것도 됩니다.")
st.write("###### 이런 것도 됩니다.")
st.write("> 이런 것도 됩니다.")
st.write(">> 이런 것도 됩니다.")
st.write(">>> 이런 것도 됩니다.")

st.write("https://www.naver.com")

foo = {"짜장면":5000, "짬뽕":6000, "탕수육":10000}
st.write(foo)

st.code("print('hello world')")


"그냥 이렇게도 됩니다."

"""
# 매직 커맨드

매직 커맨드는 굳이 write()함수를 쓰지 않아도

이렇게 직관적으로 코드를 짤 수가 있습니다.

---------------

|        |   수학     |   평가   |
|--------|:----------:|:--------:|
| 철수   |   90       |참잘했어요.|
| 영희   |   50       |분발하세요.|

https://www.naver.com

```python
print("Hello World")
```

"""