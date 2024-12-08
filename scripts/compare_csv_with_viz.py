import streamlit as st
import pandas as pd
import plotly.express as px

# App Title
st.title("CSV Data Comparison with Visualization")

# File Uploads
st.header("Upload Three CSV Files")
file1 = st.file_uploader("Upload the first CSV file", type=["csv"])
file2 = st.file_uploader("Upload the second CSV file", type=["csv"])
file3 = st.file_uploader("Upload the third CSV file", type=["csv"])

if file1 and file2 and file3:
    # Read the CSV files into dataframes
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = pd.read_csv(file3)

    st.subheader("Preview of Uploaded Files")
    st.write("First File")
    st.dataframe(df1.head())
    st.write("Second File")
    st.dataframe(df2.head())
    st.write("Third File")
    st.dataframe(df3.head())

    # Comparison
    st.header("Data Comparison")

    # Unique Rows
    diff1 = pd.concat([df1, df2, df3]).drop_duplicates(keep=False)
    st.write("Rows in File 1 but not in File 2 and File 3")
    st.dataframe(diff1)

    # Common Rows
    common = pd.merge(df1, df2, how="inner")
    common = pd.merge(common, df3, how="inner")
    st.write("Common Rows Across All Files")
    st.dataframe(common)

    # Visualization: Row Counts
    st.subheader("Visualization: Row Counts")
    row_counts = pd.DataFrame({
        "File": ["File 1", "File 2", "File 3"],
        "Rows": [len(df1), len(df2), len(df3)]
    })

    fig = px.bar(row_counts, x="File", y="Rows", title="Number of Rows in Each File", text="Rows")
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    st.plotly_chart(fig)

    # Visualization: Common vs Unique
    st.subheader("Visualization: Common vs Unique Rows")
    comparison_counts = pd.DataFrame({
        "Category": ["Unique to File 1", "Common Across All"],
        "Count": [len(diff1), len(common)]
    })

    pie_chart = px.pie(comparison_counts, names="Category", values="Count", title="Comparison of Rows")
    st.plotly_chart(pie_chart)

    # Optional Scatter Plot for Numeric Data
    st.subheader("Scatter Plot Comparison")
    numeric_columns = df1.select_dtypes(include=['number']).columns
    if not numeric_columns.empty:
        x_axis = st.selectbox("Select X-axis for scatter plot", numeric_columns)
        y_axis = st.selectbox("Select Y-axis for scatter plot", numeric_columns)
        scatter_fig = px.scatter(df1, x=x_axis, y=y_axis, title="Scatter Plot of File 1")
        st.plotly_chart(scatter_fig)
    else:
        st.write("No numeric columns found for scatter plot.")

else:
    st.write("Please upload three CSV files to proceed.")
