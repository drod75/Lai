import streamlit as st


st.set_page_config(
    page_title="Lai",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


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


pg = st.navigation(
    [
        st.Page("src/ui/main_page.py", title="Lai", icon="🤖"),
        st.Page(readme, title="ReadMe", icon=":material/book:"),
    ]
)
pg.run()
