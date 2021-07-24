import yfinance as yf
import datetime
import streamlit as st
import plotly.graph_objects as go

st.write("# 주식 데이터 시각화")

# ticker = "TSLA"
ticker = st.text_input("티커 입력 >> ")
data = yf.Ticker(ticker)
today = datetime.datetime.today().strftime("%Y-%m-%d")
df = data.history(period="1d", start="2015-1-1", end=today)

st.dataframe(df)

st.write("# 차트 - 종가")
st.line_chart(df["Close"])

st.write("# 차트 - 거래량")
st.bar_chart(df["Volume"])

st.write("# 차트 - 캔들차트")
data_candle = go.Candlestick(x=df.index,
               open=df["Open"], close=df["Close"],
               low=df["Low"], high=df["High"])
fig = go.Figure(data=[data_candle])
st.plotly_chart(fig)