import streamlit as st
import plotly_express as px
import pandas as pd
from PIL import Image

#configuration
st.set_option('deprecation.showfileUploaderEncoding',False)
html_temp=""" <div style="background-color:#722F37;padding:2px"> """
img1 = Image.open('data-visualization-illustration.jpg')
img1 = img1.resize((500,245))
st.image(img1,use_column_width=False)
#title of app
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Data Visualization App</p>'
st.markdown(new_title, unsafe_allow_html=True)
#st.title("Data Visualization App")
st.markdown(html_temp, unsafe_allow_html=True)

#Add sidebar
st.sidebar.subheader("Visualization settings")

#setup file upload
uploaded_file=st.sidebar.file_uploader(label="Upload your CSV or Excel file:-",type=['csv','xlsx'])

global read_file
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")
    try:
        read_file=pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        read_file = pd.read_excel(uploaded_file)

global numeric_columns
global string_columns
try:

    st.write("Your Data:",read_file)
    numeric_columns=list(read_file.select_dtypes(['float','int64']).columns)
    string_columns = list(read_file.select_dtypes(['object', 'string']).columns)
except Exception as e:
    print(e)
    st.write("Please upload file ")

#add select widget  to the side bar
chart_select=st.sidebar.selectbox(label="Selet The Chart Type",
                                  options=['Scatterplots','Lineplots','Histogram','Boxplot'])

if chart_select =='Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_value=st.sidebar.selectbox('X-axis',options=numeric_columns)
        y_value= st.sidebar.selectbox('Y-axis',options=numeric_columns)
        plot=px.scatter(data_frame=read_file,x=x_value,y=y_value)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif chart_select =='Lineplots':
    st.sidebar.subheader("Lineplot Settings")
    try:
        x_value=st.sidebar.selectbox('X-axis',options=numeric_columns)
        y_value= st.sidebar.selectbox('Y-axis',options=numeric_columns)
        plot=px.line(data_frame=read_file,x=x_value,y=y_value,line_group=None)
        st.write(plot)
    except Exception as e:
        print(e)

elif chart_select =='Histogram':
    st.sidebar.subheader("Histogram Settings")
    try:
        x_value=st.sidebar.selectbox('X-axis',options=numeric_columns)
        y_value= st.sidebar.selectbox('Y-axis',options=numeric_columns)
        barplot=px.bar(data_frame=read_file,x=x_value,y=y_value)
        st.write(barplot)
    except Exception as e:
        print(e)
elif chart_select =='Boxplot':
    st.sidebar.subheader("Boxplot Settings")
    try:
        x_value=st.sidebar.selectbox('X-axis',options=numeric_columns)
        y_value= st.sidebar.selectbox('Y-axis',options=numeric_columns)
        baxplot=px.box(data_frame=read_file,x=x_value,y=y_value,height=500)
        st.write(baxplot)
    except Exception as e:
        print(e)
