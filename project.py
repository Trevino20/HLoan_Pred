import streamlit as st
from PIL import Image
import pickle
import base64


@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stApp"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""

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

    if st.button("Submit"):
        features = [[dep, edu, emp, An_income, an_lon, loan_tm, cred, Mov_ac, Imov_ac]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 1:
            st.error(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'According to our Calculations, you will not get the loan from Bank'
            )
        elif ans == 1:
            st.success(
                "Hello: " + fn +" || "
                "Account number: "+account_no +' || '
                'Congratulations!! you will get the loan from Bank'
            )



run()