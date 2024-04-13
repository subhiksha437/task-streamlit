import streamlit as st

def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
def authenticated_menu():
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")


def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")

st.header("INSTRUCTIONS FOR ASESSMENT TEST")

nl(1)

# Text Prompt
st.markdown("""
            1. This quiz contains 15 questions and all the questions must be answered.
            2. Based on the answers given, your current stage will be decided.
            3. Analyse each question and answer. ALL THE BEST!!!
            """)

# Create Placeholder to print test score
scorecard_placeholder = st.empty()
if st.button("Start with tasks"):
    st.switch_page("pages/1_stage1.py")