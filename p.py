import base64
import streamlit as st
import numpy as np
import pickle


@st.cache_data 
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# img = get_img_as_base64("image1.jfif")

# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("data:image/png;base64,{img}");
# background-size: 100%;
# background-repeat: no-repeat;
# width: 100%;
# font-size: 50px;

# }}


# .st-emotion-cache-5jqujg e1y5xkzn3{{
# border-style: outset;
# }}


# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)


model = pickle.load(open('./Model/dtree_Model1','rb'))


def run():
    st.title("Home Loan Prediction using Machine Learning")
    col1, col2, col3 = st.columns(3)

    # Account Number
    with col1:
        account_no = st.text_input('Account Number')

    ## Full Name
    with col2:
        fn = st.text_input('Full Name')

    ## For gender
    with col3:
        gen_display = ('Female','Male')
        gen_options = list(range(len(gen_display)))
        gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    with col1:
        mar_display = ('No','Yes')
        mar_options = list(range(len(mar_display)))
        mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    # Number of Dependents
    with col2:
        dep = st.number_input("Number of Dependents",value=0)

    ## For edu
    with col3:
        edu_display = ('Not Graduate','Graduate')
        edu_options = list(range(len(edu_display)))
        edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    with col1:
        emp_display = ('Job','Business')
        emp_options = list(range(len(emp_display)))
        emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## For Credit Score
    with col2:
        cred = st.number_input('Credit Score',value=0)

    ## Applicant Annual Income
    with col3:
        An_income = st.number_input("Applicant's Annual Income($)",value=0)

    ## Applicant Movable Assets 
    with col1:
        Mov_ac = st.number_input("Applicant's Movable Assets($)",value=0)

    ## Applicant Immovable Assets
    with col2: 
        Imov_ac = st.number_input("Applicant's Immovable Assets($)",value=0)

    ## Loan Amount 
    with col3:
        an_lon = st.number_input('loan Amount',value=0)

    ## Loan Term 
    loan_tm = st.number_input("Loan Term",value=0)

    if st.button('Predict Price',type="primary"):
    # query
   
        query = np.array([dep, edu, emp, An_income, an_lon, loan_tm, cred, Mov_ac, Imov_ac])

        query = query.reshape(1,9)
        st.title("The predicted price of this configuration is " + str(int(np.exp(model.predict(query)[0]))))
        ans = int(np.exp(model.predict(query)[0]))

        if ans == 1:
             st.success(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations!! you will get the loan from Bank'
            )
        elif ans == 2:
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
            

run()

