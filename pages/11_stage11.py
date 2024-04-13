import streamlit as st
st.header("STAGE 11")
st.write(" 1. Develop a detailed implementation plan outlining the steps and resources required to launch your startup.")
title = st.text_input('Project title', '')
st.button("submit")
st.button("Completed task 1")

st.write(" 2. Allocate roles and responsibilities to team members for executing the implementation plan.")
st.button("Completed task 2")

st.write(" 3. Secure the necessary infrastructure, equipment, and technology to support your operations.")
st.button("Completed task 3")

st.write(" 4. Establish partnerships with suppliers, vendors, and service providers. ")
st.button("Completed task 4")

st.write(" 5. Conduct a soft launch or pilot test to validate your product or service in a controlled environment. ")
st.button("Completed task 5")

st.write(" 6. Monitor key performance indicators (KPIs) to track the progress of your implementation efforts. ")
st.button("Completed task 6")

st.write(" 7. Address any operational challenges or issues that arise during the implementation phase.")
st.button("Completed task 7")

st.write(" 8. Train employees on new processes, systems, and procedures. ")
st.button("Completed task 8")

st.write(" 9. Implement feedback mechanisms to gather input from customers and stakeholders. ")
st.button("Completed task 9")

st.write(" 10. Continuously iterate and improve your implementation approach based on lessons learned. ")
st.button("Completed task 10")
if st.button("Continue with task 12"):
    st.switch_page("pages/12_stage12.py")



    