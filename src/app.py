import streamlit as st

from utils import select_n_groups, select_n_names

st.title("Prize Draw App")

if "groups" not in st.session_state:
    st.session_state.groups = []
if "selected_names" not in st.session_state:
    st.session_state.selected_names = []

# Section Divide Names into Groups
st.header("Divide Names into Groups")
names_input = st.text_area(
    "Enter names separated by commas (e.g., John, Sara, Robert)", key="names1"
)
num_groups = st.number_input("Number of groups", min_value=3, step=1, value=3)
if st.button("Divide into Groups"):
    names = [name.strip() for name in names_input.split(",")]
    st.session_state.groups = select_n_groups(names, num_groups)

if st.session_state.groups:
    for i, group in enumerate(st.session_state.groups):
        st.write(f"Group {i + 1}: {', '.join(group)}")

# Section Name Sorting
st.header("Name Sorting")
names_input2 = st.text_area(
    "Enter names separated by commas (e.g., John, Sara, Robert)", key="names2"
)
num_names = st.number_input("Number of names", min_value=1, step=1, value=2)
if st.button("Name Sorting"):
    names = [name.strip() for name in names_input2.split(",")]
    st.session_state.selected_names = select_n_names(names, num_names)

if st.session_state.selected_names:
    st.write(f"Selected Names: {', '.join(st.session_state.selected_names)}")
