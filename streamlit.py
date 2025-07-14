import streamlit as st
#https://docs.streamlit.io.
st.title("Hey there,Welcome to my world")
st.subheader("Choose Your strength in coding")
st.text("Show us,what you got")
st.write("Choose Your fav coding")
code=st.selectbox("Your fav code:",["C++","Python","Java","C#","Javascript","C"])
choice=st.selectbox("Show us Your level",["Beginner","Intermediate","Advanced","Expert"])
st.write(f"Your fav code is {code} and You are a {choice} coder")
st.success("Welcome to the journey")
