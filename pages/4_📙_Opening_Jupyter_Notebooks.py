import streamlit as st
from load_css import local_css


st.set_page_config(
    page_title='Opening Jupyter Notebooks',
    page_icon='📙'
)

local_css("css/style.css")

st.title("Opening Jupyter Notebooks")


st.markdown(
    """
### Open and work with Jupyter Notebooks

If you haven't unzipped and placed the jupyter notebooks in a specific folder, do this first. You can find instructions in the last step of the previous page.

Below are the steps you need to take to open the Python jupyter notebooks in VS Code. Apart from step 1, **this is also shown in the video**.
""")

st.markdown(
    """
1. Open the VS Code app.
2. Open the PF_notebooks folder, which contains the different jupyter notebook files. Go to Files > Open Folder and the select the folder.
3. Click on the first jupyter notebook to open it.
4. Select the kernel. The kernel is the specific Python environment to use. We set up the py312 environment with Python 3.12 in a previous step and will use this to 
work with the jupyter notebooks.
5. Read through the description about the workshops/scroll down to the first exercise.
6. Type in your solution code in the code cell and run the code with the Cmd+Enter (Mac) or Ctrl+Enter (Win) keyboard shortcut.
""")

st.markdown(
    """
### Next step

Go to the DSL Python workshops section to 
learn about the format of the Python workshops and how to sign up for a session.
"""
)
