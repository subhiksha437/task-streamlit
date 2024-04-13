import streamlit as st
st.header("STAGE 2")
st.write(" 1. Develop a minimum viable product (MVP) to demonstrate the core functionality.")
title = st.text_input('1. Identify and point out your assumptions', '')
title = st.text_input('2. Identify minimum features needed to start your project', '')
title = st.text_input('3. Build MVP and test your hypothesis', '')
st.link_button("How to develop MVP ?", "https://uizard.io/blog/how-to-create-a-succesful-mvp-a-step-by-step-guide/")
if st.button("submit"):
    st.button("Completed task 1")

st.write(" 2. Test the MVP with a small group of users or beta testers.")
option = st.selectbox(
    'Did you complete testing wih small group?',
    ('YES', 'NO'))
st.write('You selected:', option)
if st.button("YES"):
    st.button("Completed task 2")

st.write(" 3. Gather feedback on the usability and performance of the POC.")
title = st.text_input('', '')
st.link_button("To know more about templates...","https://slideuplift.com/blog/best-websites-for-powerpoint-templates/")
st.button("Completed task 3")

st.write(" 4. Iterate on the POC based on user feedback. ")
title = st.text_input('', '')
st.button("Completed task 4")

st.write(" 5. Measure key metrics to validate the effectiveness of the concept.")
title = st.text_input('', '')
st.button("Completed task 5")

st.write(" 6. Identify any technical or operational challenges.")
title = st.text_input('', '')
st.button("Completed task 6")

st.write(" 7. Refine the POC to address any identified issues.")
st.button("Completed task 7")

st.write(" 8. Document the POC process and outcomes for future reference. ")
st.button("Completed task 8")

st.write(" 9. Assess the scalability of the concept. ")
title = st.text_input('', '')
st.button("Completed task 9")

st.write(" 10. Analyze the cost-effectiveness of scaling the POC. ")
title = st.text_input('', '')
st.button("Completed task 10")
if st.button("Continue with task 3"):
    st.switch_page("pages/3_stage3.py")



    