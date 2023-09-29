import numpy as py
import pandas as pd
import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')


model =joblib.load('pipe_prc_mdl (1).pkl')

df = pd.read_csv('train.csv')



def predict_subscriber(age,job,marital,education,default,balance,housing,loan,contact,month,day,duration,campaign,pdays,previous,poutcome):

    col_names =['age','job', 'marital', 'education', 'default', 'balance','housing', 'loan', 'contact','month', 'day', 'duration','campaign', 'pdays', 'previous','poutcome']

    col_values = [age,job,marital,education,default,balance,housing,loan,contact,month,day,duration,campaign,pdays, previous,poutcome]

    test = pd.DataFrame([col_values])
    test.columns = col_names
    predicted = model.predict(test)
    return predicted
def main():
    st.title("Hackathon")
    
    html_tmp = """
    <div style='background-color:red;'>
    <h2 style='color:white;text-align:center;'>Subscriber Prediction App</h2>
    </div>
    """
    st.markdown(html_tmp, unsafe_allow_html=True)
    age = st.number_input("Age", min_value=1, max_value=100)
    job = st.selectbox('Type of job:',pd.unique(df['job']))
    marital = st.selectbox('Marital Status:',pd.unique(df['marital']))
    education = st.selectbox('Education:',pd.unique(df['education']))
    default = st.selectbox(' Default:',pd.unique(df['default']))
    balance = st.number_input("Balance amount", min_value=0)
    housing  = st.selectbox('Has housing loan:',pd.unique(df['housing']))
    loan = st.selectbox('Has personal loan:',pd.unique(df['loan']))
    contact = st.selectbox('Type of contact:',pd.unique(df['contact']))
    day = st.number_input("Day", min_value=1,max_value=31) 
    month = st.selectbox('Month :',pd.unique(df['month']))
    duration = st.number_input("Day", min_value=0)
    campaign = st.number_input("Campaign", min_value=1,max_value=31)
    pdays = st.number_input("PrevDays", min_value=0 )
    previous= st.number_input("Previous", min_value=0)
    poutcome= st.selectbox('Prev. campaign out come:',pd.unique(df['poutcome']))
#creating a button click to call the predict method
    result =""
    if st.button("Predict"):
           result= predict_subscriber(age,job,marital,education,default,balance,housing,loan,contact,month,day,duration,campaign,pdays,previous,poutcome)
#displaying the results
           if result==1:
            st.success("A potential Customer")
           elif result==0:
            st.success("Not a potential Customer")
if __name__ == "__main__":
    main()