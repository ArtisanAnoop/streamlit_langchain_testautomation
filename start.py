import streamlit as st
import demo_userstory, demo_api, demo_html

# Set page config
st.set_page_config(page_title="My Multi-App", page_icon=":fire:")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Define the app selection tabs
tabs = ["Build Test Scenarios", "Create API Test scripts", "Generate XPath"]
app = st.query_params.get("app")
if app:
    app = app[0]
    if app not in tabs:
        app = tabs[0]
else:
    app = tabs[0]

app = st.sidebar.radio(
    "Go to", tabs, index=tabs.index(app)
)

# Run the selected app
if app == "Build Test Scenarios":
    demo_userstory.main()
elif app == "Create API Test scripts":
    demo_api.main()
elif app == "Generate XPath":
    demo_html.main()