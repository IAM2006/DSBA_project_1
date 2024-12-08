import streamlit as st
import json
import requests
import pickle

URL = "http://127.0.0.1:8000/{}"

st.markdown("<h1 style='text-align: center; color: Black;'>Analysis of housing market in the New York City</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>General information about the dataset</h3>", unsafe_allow_html=True)
st.image("graphs/PriceDist.png")
st.image("graphs/BedsDist.png")
st.image("graphs/BathsDist.png")
st.image("graphs/PriceDist.png")
st.image("graphs/SQFTdist.png")
st.image("graphs/PairwiseCor.png")
st.image("graphs/HousesDist.png")
st.image("graphs/ManhattanDist.png")
st.image("graphs/BrooklynDist.png")
st.image("graphs/QueensDist.png")
st.image("graphs/StatenIslandDist.png")
st.image("graphs/BronxDist.png")
st.markdown("<h6 style='text-align: center; color: Black;'>Overall, there are too much neighborhoods to represent each, that is why in the following analysis, they will be united into boroughs, in which they tend to have relativly close median prices.</h6>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>Corelations overview</h3>", unsafe_allow_html=True)
st.image("graphs/SQFT_to_price.png", caption="It is clear that generaly with increasing area footage, price go up as well in every borough.")
st.image("graphs/Baths_to_price.png", caption="It is clear that generaly with increasing number of beds, price go up as well in every borough.")
st.image("graphs/Beds_to_price.png", caption="It is clear that generaly with increasing number of baths, price go up as well in every borough.")
st.image("graphs/Bd_bt_to_price.png", caption="We can see that in the NYC on average additional bathroom increases price more then additional bedroom.")
st.image("graphs/SQFT_to_price_all.png", caption="In general in the NYC property with bigger area footage tend to cost more")
st.image("graphs/Median_price.png", caption="This map shows us which neighborhoods are more expensive to buy an apartment in. It is also seen that the most expesive boroughs are Manhattan and Brooklyn, while the cheapest one is Bronx.")
st.image("graphs/SQFT_to_bd_bt.png", caption="It shows that in general the more space you have the more rooms you have.")
st.image("graphs/Per_sqft.png", caption="It shows that prices per SQFT tend to be the highest on Manhattan and the lowest in Bronx.")
st.markdown("<h6 style='text-align: center; color: Black;'>Conclusion: in general the more you have beds/baths/squere foot in your appartment, the higher the price is, also apartments in neghborhoods whith higher median price tend to cost more.</h6>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black;'>The following model takes into account all data presented above to predict a price of an appartment in the NYC. You can try it out.</h3>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: Black;'>Hypothesis: price of house in the NYC dpend on several key factors: number of beds/baths, squere footage, and neighborhood. The more beds/baths/squre foot the apertment has the higher the price is. Also the higher median price of the apartments in the neighborhood the higher the price is.</h6>", unsafe_allow_html=True)

neighborhood_id = dict()
with open('neighborhood.pkl', 'rb') as f:
    neighborhood_id = pickle.load(f)

with st.form("my_form"):
    beds = st.slider(
        "Number of beds",
        step=1,
        max_value=15,
        min_value=1,
    )

    baths = st.slider(
        "Number of baths",
        step=1,
        max_value=10,
        min_value=1,
    )

    sqft = st.number_input("Area in squere foot", min_value=1, max_value=15000)

    neighborhood = st.selectbox(
        "choose your neighborhood",
        options=list(neighborhood_id.keys())[1:]
    )

    submitted = st.form_submit_button("Submit")

if submitted:
    request_data = json.dumps({
        'beds': beds,
        'baths': baths,
        'sqft': sqft,
        'nb': neighborhood_id[neighborhood],
    })

    response = requests.post(URL.format('price'), request_data)
    dt = json.loads(response.content)

    ans = (float(dict(dt)['result']))

    st.write("Expected price:  ", f'{ans:.2f}' + '$')