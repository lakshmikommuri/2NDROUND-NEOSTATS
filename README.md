**OVERVIEW OF MY CHATBOT**

This project is a streamlit-based AI assistant that uses natural language queries to glean insights from Excel spreadsheets. The assistant, which was created as a component of NeoStats' AI Engineer Internship challenge, allows users to upload.xlsx files, pose questions in plain English, and get intelligent, schema-agnostic responses in the form of tables, text, or visualizations.

**FEATURES**

Any Excel file containing tabular data that is structured is accepted

Enables users to query the uploaded data in natural language.

Allows users to ask natural language questions about the uploaded data.

Deals with missing or inconsistent data and automatically determines column types.

For further analytical tasks, logic is executed from a Jupyter notebook.

Streamlit was used to create the fully web-based interface.

**Answers**

Text-based observations

Data views that have been filtered

Histograms, bars, lines, and other charts

**PROJECT STRUCTURE**

app.py->streanlit application

chatbot_excel_file.xlsx->Sample Excel file for testing

jobassignment.ipynb->Notebook with data logic to be executed

README.md->Project documentation

**EXECUTION PROCESS**

**Clonning**

git clone https://github.com/your-username/job-assignment-chatbot.git

cd job-assignment-chatbot

**Requirements**

pip install -r requirements.txt

**app.py**

streamlit run app.py


**SAMPLE QUESTIONS TO ASK**

"What is the average income?"

"How many employees are above 40 years old?"

"Compare sales by region"
"Show a histogram of customer ages"



