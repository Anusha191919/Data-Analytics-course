import streamlit as st
import plotly.express as px

st.title ("My Web App")

#want to take numbers from user

numbers=st.text_input("Enter multiple numbers separated by space")
num_list= list(map(int, numbers.split()))

#line graph
st.line_chart(num_list, use_container_width=True)
#bar graph
st.bar_chart(num_list, use_container_width=True)

x=st.text_input("Enter area separated by space for x axis")
y=st.text_input("Enter area separated by space for y axis")
x_list = list(map(int,x.split()))
y_list = list(map(int,y.split()))
if len(x_list) != len(y_list):
    st.error("length of x and y must be equal")
else:
    st.plotly_chart(px.scatter(x=x_list, y=y_list, title="Scatter Plot"))

#histogram
c1, c2=st.columns(2)
c1.plotly_chart(px.histogram(x=x_list, title="histogram x"),use_container_width=True)
c2.plotly_chart(px.histogram(y=y_list, title="histogram y"),use_container_width=True)
#for area chart same as line chart, just write area instead of line