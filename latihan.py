import streamlit as st
import pandas

 

col1, col2 = st.columns(2)

with col1 :
    st.image("images/profile.png", width=450)
with col2 :
    st.title("Farrel Athallah")
    content = """
  
        Hi there! My name is Farrel Athallah, and I'm bridging the worlds of strategy and design with my analytical 
        approach and a love for creative problem-solving. I have successfully created outstanding brand identities and 
        delivered impactful creative work for enterprises.
   

    """
    st.write(content)

    content2 = """
   I designed a web app that focuses on fulfilling user needs and achieving business targets. Both will make your product beyond meaningful.

   """
    st.info(content2)
    

col3,col4,col5 = st.columns(3)

df = pandas.read_csv('data.csv', sep=";")

bagi = [df[i::3] for i in range (3)]
col3, col4, col5 = st.columns(3)

for index, row in bagi[0].iterrows():
    with col3:
        st.image("images/" + row["image"], width=150)
        st.header(row["title"])
        st.write(row["description"])
        st.write("[Portfolio](https://www.behance.net/farrelathallah)")
for index, row in bagi[1].iterrows():
    with col4 :
        st.image("images/" + row["image"], width=150)
        st.header(row["title"])
        st.write(row["description"])
        st.write("[Portfolio](https://www.behance.net/farrelathallah)")
for index, row in bagi[2].iterrows():
    with col5:
        st.image("images/" + row["image"], width=150)
        st.header(row["title"])
        st.write(row["description"])
        st.write("[Portfolio](https://www.behance.net/farrelathallah)")





col6 = st.columns(1)[0]
with col6 :
     st.header('Why Choose Me?')
     content3 = """
I combine analytical thinking with visual creativity to deliver solutions that are not only beautiful but also aligned with business goals and
You can count on me to deliver on time, communicate clearly, and collaborate effectively from concept to completion.
"""
     st.write(content3)



st.header('Software')
col7, col8, col9, col10 = st.columns(4)
with col7:
    
    st.image('images/6.png', width=200)
with col8:
    st.image('images/7.png', width=200)
with col9:
    st.image('images/9.png', width=200)
with col10:
    st.image('images/10.png', width=200)

    

    
