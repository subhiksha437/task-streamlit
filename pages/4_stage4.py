import streamlit as st
st.header("STAGE 4")
st.write(" 1. Map out the user journey to understand how customers will interact with your product or service.")
title = st.text_input('!!!', '')
st.button("submit")
st.button("Completed task 1")

st.write(" 2. Identify key touch points and pain points in the workflow.")
title = st.text_input('!!', '')
st.button("Completed task 2")

st.write(" 3. Design wire frames or mock ups to visualize the user experience.")
st.button("Completed task 3")

st.write(" 4. Define the features and functionalities of the product or service. ")
title = st.text_input('!', '')
st.button("Completed task 4")

st.write(" 5. Create a flowchart or diagram illustrating the workflow process. ")
st.button("Completed task 5")

st.write(" 6. Consider potential integration with other tools or platforms. ")
title = st.text_input('What are your considerations ?', '')
st.button("Completed task 6")

st.write(" 7. Collaborate with designers and developers to refine the workflow design.")
option = st.selectbox(
    ' ?',
    ('YES', 'NO'))
st.write('You selected:', option)
if option=='YES':
    st.button("Completed task 7")

st.write(" 8. Test the workflow design with real users to gather feedback. ")
title = st.text_input('!!!!', '')
st.button("Completed task 8")

st.write(" 9. Iterate on the design based on user testing results.")
title = st.text_input('!!!!!', '')
st.button("Completed task 9")

st.write(" 10. Document the finalized product/service workflow for future reference.")
title = st.text_input('!!!!!!', '')
st.button("Completed task 10")
if st.button("Continue with task 5"):
    st.switch_page("pages/5_stage5.py")



    
    