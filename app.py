import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Excel Insights Chatbot", layout="wide")
st.title("📊 Excel Insights Chatbot")

uploaded_file = st.sidebar.file_uploader("Upload an Excel file", type=[".xlsx"])

if "df" not in st.session_state:
    st.session_state.df = None

def clean_column_names(columns):
    return [col.strip().lower().replace(" ", "_").replace("-", "_") for col in columns]

def infer_column_types(df):
    return df.dtypes.to_dict()

def query_to_action(query, df):
    if "average" in query:
        numeric_cols = df.select_dtypes(include='number').columns
        return df[numeric_cols].mean()
    elif "bar chart" in query:
        for col in df.columns:
            if df[col].nunique() < len(df) * 0.5:
                plt.figure(figsize=(10,4))
                df[col].value_counts().plot(kind='bar')
                plt.title(f"Bar Chart of {col}")
                st.pyplot(plt)
                return
    return "I'm not sure how to answer that yet."

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        df.columns = clean_column_names(df.columns)
        st.session_state.df = df
        st.success("✅ File uploaded and processed successfully!")

        with st.expander("📄 Preview Data"):
            st.dataframe(df.head())

        query = st.text_input("Ask your question in natural language:")

        if query:
            st.markdown("---")
            st.subheader("💡 Answer:")
            result = query_to_action(query.lower(), df)
            if isinstance(result, pd.Series) or isinstance(result, pd.DataFrame):
                st.write(result)
            elif isinstance(result, str):
                st.write(result)

    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("📤 Please upload a .xlsx file to get started.")
