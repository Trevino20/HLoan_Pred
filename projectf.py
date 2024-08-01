import streamlit as st
import numpy as np
import pickle

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


model = pickle.load(open('./Model/dtree_Model1','rb'))

def run():
    st.title("Home Loan Prediction using Machine Learning")

    # Account Number
    account_no = st.text_input('Account Number')

    ## Full Name
    fn = st.text_input('Full Name')

    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    # Number of Dependents
    dep = st.number_input("Number of Dependents",value=0)

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('Job','Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## For Credit Score
    cred = st.number_input('Credit Score',value=0)

    ## Applicant Annual Income
    An_income = st.number_input("Applicant's Annual Income($)",value=0)

    ## Applicant Movable Assets 
    Mov_ac = st.number_input("Applicant's Movable Assets($)",value=0)

    ## Applicant Immovable Assets 
    Imov_ac = st.number_input("Applicant's Immovable Assets($)",value=0)

    ## Loan Amount 
    an_lon = st.number_input('loan Amount',value=0)

    ## Loan Term 
    loan_tm = st.number_input("Loan Term",value=0)

    if st.button('Predict Price'):
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