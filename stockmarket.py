import streamlit as st
import pandas as pd
import yfinance as yf
st.title('Stock market app')
st.write('This is my hope yto get hike')

ticker_symbol = st.text_input('Enter the stock symbol of company', 'AAPL')
ticker_data=yf.Ticker(ticker_symbol)

start_date=d = st.date_input("Enter the starting date ", value=pd.to_datetime("2022-5-1"))
end_date=st.date_input("Enter the end date", value=pd.to_datetime("today"))
hist=ticker_data.history(start=start_date, end=end_date)
st.write('I m going to show you Apple stock data')
st.write(hist)
# if dataframe is huge not to use write but dataframe
#st.dataframe(hist)


#st.write('This plot is for the price of the stock')
#st.line_chart(hist.Close)

col1, col2 = st.columns(2)

with col1:
   st.write('This plot is for volume of the stock')
   st.line_chart(hist.Volume)


with col2:
   st.write('This plot is for the price of the stock')
   st.line_chart(hist.Close)