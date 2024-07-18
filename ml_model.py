import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


df = pd.read_csv(r"C:\Users\azaru\Azar documents\Data science - GUVI\capstone project\Project 4 - Industrial copper modelling\sample_model.csv")

st.title(':orange[Industrial Copper Modeling]')

with st.sidebar:

    menu  = option_menu("Main Menu",["Price Prediction","Win/Loss Prediction"])

if menu == "Price Prediction":
    quan_tons = st.number_input("Please enter Quantity tons :" )
    
    country = st.selectbox("plese enter country code :",df['country'].unique())
    
    status = st.number_input("Please enter status as Won = 1 or Loss = 0 :",min_value=0,max_value=1)
    
    application = st.number_input("Please enter applicate number :",max_value=100)
    
    thickness = st.number_input("Please enter the thickness :",max_value=20)
    
    width = st.number_input("Please enter the width :",max_value=2000)
    
    product_ref = st.selectbox("Please enter the Product refrence :",df['product_ref'].unique())
    
    item_type = st.selectbox("Please enter item type :",df['item type'].unique())
    
    if item_type == 'IPL':
        ipl = 1
        others = 0
        pl = 0
        s = 0
        slawr = 0
        w = 0
        wi = 0
    elif item_type == 'Others':
        ipl = 0
        others = 1
        pl = 0
        s = 0
        slawr = 0
        w = 0
        wi = 0
    elif item_type == 'PL':
        ipl = 0
        others = 0
        pl = 1
        s = 0
        slawr = 0
        w = 0 
        wi = 0
    elif item_type == 'S':
        ipl = 0
        others = 0
        pl = 0
        s = 1
        slawr = 0
        w = 0
        wi = 0  
    elif item_type == 'SLAWR':   
        ipl = 0
        others = 0
        pl = 0
        s = 0
        slawr = 1
        w = 0
        wi = 0
    elif item_type == 'W':    
        ipl = 0
        others = 0
        pl = 0
        s = 0
        slawr = 0
        w = 1
        wi = 0 
    elif item_type == 'WI':        
        ipl = 0
        others = 0
        pl = 0
        s = 0
        slawr = 0
        w = 0
        wi = 1 

    my_input = [quan_tons,country,status,application,thickness,width,product_ref,ipl,others,pl,s,slawr,w,wi]

    if st.button("Apply"):
        st.write('Quantity tons = ',quan_tons)
        st.write('Country = ',country)
        st.write('Status = ',status)
        st.write('Application = ',application)
        st.write('Thickness = ',thickness)
        st.write('Width = ',width)
        st.write('Product refrence = ',product_ref)
        st.write('Item Type = ',item_type)
        
    if st.button("Predict"):
        with open('Price_prediction.pkl','rb') as ft:
            model = pickle.load(ft)
        result = model.predict([my_input])
        st.write("Predicted Price :- ",result)
        st.info("Done",icon="🔥")
            
elif menu == "Win/Loss Prediction":
    quan_tons = st.number_input("Please enter Quantity tons :" )
    
    country = st.selectbox("plese enter country code :",df['country'].unique())
    
    application = st.number_input("Please enter applicate number :",max_value=100)
    
    thickness = st.number_input("Please enter the thickness :",max_value=20)
    
    width = st.number_input("Please enter the width :",max_value=2000)
    
    product_ref = st.selectbox("Please enter the Product refrence :",df['product_ref'].unique())

    selling_price = st.number_input("Please enter the Selling Price :")
    
    item_type = st.selectbox("Please enter item type :",df['item type'].unique())
    
    if item_type == 'IPL':
        ipl = 1
        others = 0
        pl = 0
        s = 0
        slawr = 0
        w = 0
        wi = 0
    elif item_type == 'Others':
        ipl = 0
        others = 1
        pl = 0
        s = 0
        slawr = 0
        w = 0
        wi = 0
    elif item_type == 'PL':
        ipl = 0
        others = 0
        pl = 1
        s = 0
        slawr = 0
        w = 0 
        wi = 0
    elif item_type == 'S':
        ipl = 0
        others = 0
        pl = 0
        s = 1
        slawr = 0
        w = 0
        wi = 0  
    elif item_type == 'SLAWR':   
        ipl = 0
        others = 0
        pl = 0
        s = 0
        slawr = 1
        w = 0
        wi = 0
    elif item_type == 'W':    
        ipl = 0
        others = 0
        pl = 0
        s = 0
        slawr = 0
        w = 1
        wi = 0 
    elif item_type == 'WI':        
        ipl = 0
        others = 0
        pl = 0
        s = 0
        slawr = 0
        w = 0
        wi = 1 

    my_input_1 = [quan_tons,country,application,thickness,width,product_ref,selling_price,ipl,others,pl,s,slawr,w,wi]

    if st.button("Apply"):
        st.write('Quantity tons = ',quan_tons)
        st.write('Country = ',country)
        st.write('Application = ',application)
        st.write('Thickness = ',thickness)
        st.write('Width = ',width)
        st.write('Product refrence = ',product_ref)
        st.write('Selling Price = ',selling_price)
        st.write('Item Type = ',item_type)
        
    if st.button("Predict"):
        with open('Win_loss prediction.pkl','rb') as ft:
            model_1 = pickle.load(ft)

        result_1 = model_1.predict([my_input_1])

        if result_1 == 1:
            st.write(result_1)
            st.success('Won', icon="✅")
        else:
            st.write(result_1)
            st.error('Loss', icon="🚨")       


        