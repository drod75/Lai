import streamlit as st

# page configuration for users
st.set_page_config(
    page_title="Lai",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# readme page function
def readme():
    def read_markdown_file(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: The file '{file_path}' was not found."
        except Exception as e:
            return f"Error reading file: {e}"

    readme_content = read_markdown_file("README.md")
    st.set_page_config(page_title="README Page", layout="wide")
    st.markdown(readme_content, unsafe_allow_html=True)


# streamlit page navifation bar, set to top
pg = st.navigation(
    [
        st.Page("src/ui/main.py", title="Lai", icon="🤖"),
        st.Page(readme, title="ReadMe", icon=":material/book:"),
    ],
    position="top",
)
pg.run()
