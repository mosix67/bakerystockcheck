import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import yfinance as yf

st.set_page_config(
    page_title="Ko cakes Portfolio",
    page_icon=":cake:",
    layout="wide",
)

# ------ LOAD ANIMATION FROM LOTTIES --------


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url = "https://assets5.lottiefiles.com/private_files/lf30_lXFF5L.json"
lottie_json = load_lottieurl(lottie_url)


# ------ HEADER SECTION --------
with st.container():
    st.title("Welcome to Ko Cakes Portfolio")
    st.subheader(
        "We are is the Professional’s Gateway to the World’s Bakery Markets")
    st.write("""
    If you’re passionate about investing in world renowned bakries, 
    you’re in the right place. From experienced associates to industry-leading education and technology, 
    we provide the knowledge you need to become an even smarter investor.
    """)
    st.write(
        "[Check out our Yahoo Finance Page for more information](https://finance.yahoo.com/lookup?s=BAKE)")

# ------ WHAT WE DO -----------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Do")
        with st.expander("LOW TRADING COST"):
            st.write("""
            We offer the lowest commissions and access to stocks, options, futures, currencies, bonds and 
            funds from a single unified platform. 
            """)
        with st.expander("LOWEST FIANNCING COST:"):
            st.write(
                """
                Because of our specialized focus, We offer the lowest margin loan rates of any broker, 
                according to the Yahoo finance 2022 online broker review.
                """)
        with st.expander("EARN EXTRA INCOME:"):
            st.write(
                """
            Earn extra income on the fully-paid shares of stock held in your account. 
            Each day shares are on loan you are paid interest while retaining the ability to trade your loaned stock without restrictions.
            """)

    with right_column:
        st_lottie(lottie_json, height=300, key='coding')

with st.container():
    st.write("""
    # Bakery Stock Monitor

    Stay up-to-date with your preferred bakery's **closing price** and **Volume**

    """)

    tickerOption = st.selectbox(
        'Which Bakery would you like to check its stock?',
        ('BKR', 'TBAKF', 'CAKE', 'LOTB.BR', 'SZ8.MU'))

    if tickerOption == 'BKR':
        st.write('You selected: Bakers Hughes Company')
    elif tickerOption == 'TBAKF':
        st.write('You selected: Ted Baker')
    elif tickerOption == 'CAKE':
        st.write('You selected: The Cheesecake Factory')
    elif tickerOption == 'LOTB.BR':
        st.write('You selected: Lotus Baker')
    elif tickerOption == 'SZ8.MU':
        st.write('You selected: Sumitomo Bakerlite')

    tickerSymbol = tickerOption
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(
        period='1d', start='2010-1-1', end='2020-1-25')
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
