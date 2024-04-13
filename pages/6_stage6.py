import streamlit as st
st.header("STAGE 6")
st.write(" 1. Conduct a thorough search to ensure your idea is not already patented.")
title = st.text_input('Project title', '')
st.button("submit")
st.button("Completed task 1")

st.write(" 2. Consult with a legal expert to determine the intellectual property rights associated with your idea.")
st.button("Completed task 2")

st.write(" 3. File for copyright protection for any original content, such as branding materials or software code.")
st.button("Completed task 3")

st.write(" 4. Consider applying for a patent if your idea is innovative and meets the criteria for patent ability. ")
st.button("Completed task 4")

st.write(" 5. Prepare the necessary documentation and drawings for the patent application. ")
option = st.selectbox(
    ' ?',
    ('yess', 'NO'))
st.write('You selected:', option)
if option=='YES':
    st.button("Completed task 5")

st.write(" 6. Work with a patent attorney to draft and file the patent application. ")
option = st.selectbox(
    ' ?',
    ('Yup', 'NO'))
st.write('You selected:', option)
if option=='YES':
    st.button("Completed task 6")

st.write(" 7. Respond to any office actions or objections from patent examiners.")
option = st.selectbox(
    ' ?',
    ('YEah', 'NOt'))
st.write('You selected:', option)
if option=='YES':
    st.button("Completed task 7")

st.write(" 8. Monitor the progress of the patent application and address any issues that arise. ")
st.button("Completed task 8")

st.write(" 9. Explore international patent protection if you plan to expand globally.")
option = st.selectbox(
    ' ?',
    ('Y', 'N'))
st.write('You selected:', option)
if option=='YES':
    st.button("Completed task 9")

st.write(" 10. Once granted, enforce your patent rights against any infringement. ")
option = st.selectbox(
    ' ?',
    ('YEss', 'NOo'))
st.write('You selected:', option)
if option=='YES':
    st.button("Completed task 10")
if st.button("Continue with task 7"):
    st.switch_page("pages/7_stage7.py")



    