import streamlit as st
import pandas as pd
import nbformat
from nbconvert import PythonExporter
import io

st.set_page_config(page_title="Job Assignment Chatbot", layout="wide")

# Title
st.title("📊 Job Assignment & Chatbot App")

# Upload Excel File
st.header("1️⃣ Uploaded Excel Data")
excel_path = "C:\Users\ECS\OneDrive\Documents\jonassig\chatbot_excel_file.xlsx"
df = pd.read_excel(excel_path)
st.dataframe(df, use_container_width=True)

# Optional: Simple chatbot-like response (example logic)
st.subheader("🤖 Simple Chatbot Response Example")
question = st.text_input("Ask a question related to the job assignments")

if question:
    # Simple matching logic from Excel data
    matched_row = df[df.apply(lambda row: question.lower() in str(row).lower(), axis=1)]
    if not matched_row.empty:
        st.success("Response based on your question:")
        st.dataframe(matched_row)
    else:
        st.warning("No relevant answer found. Please try a different question.")

# Run Jupyter Notebook code
st.header("2️⃣ Executing Notebook Logic")

notebook_path = "C:\Users\ECS\OneDrive\Documents\jonassig\jobassignment.ipynb"

def convert_notebook_to_code(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    exporter = PythonExporter()
    source_code, _ = exporter.from_notebook_node(notebook)
    return source_code

# Convert .ipynb to Python and execute it
notebook_code = convert_notebook_to_code(notebook_path)

with st.expander("📘 View Converted Notebook Code"):
    st.code(notebook_code, language='python')

# Execute notebook code safely
with st.expander("▶️ Execute Notebook"):
    exec_output = io.StringIO()
    try:
        exec(notebook_code, {'__name__': '__main__'})
        st.success("Notebook executed successfully.")
    except Exception as e:
        st.error(f"Error executing notebook: {e}")
