import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file):
    ext = file.name.split(".")[-1].lower()
    if ext == "csv":
        return pd.read_csv(file)
    elif ext in ["xls", "xlsx"]:
        return pd.read_excel(file)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return None

def show_statistics(df):
    st.write("### Basic Statistics")
    st.write(df.describe().T)

def show_graphs(df):
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if not numeric_cols:
        st.warning("No numerical columns found for visualization.")
        return
    
    st.write("### Data Visualizations")
    
    # Let the user select a column for analysis
    column = st.selectbox("Select a column for analysis", numeric_cols)
    
    # Compute and display detailed statistics for the selected column
    st.write(f"### Detailed Statistics for Column: {column}")
    max_val = df[column].max()
    min_val = df[column].min()
    mean_val = df[column].mean()
    median_val = df[column].median()
    mode_series = df[column].mode()
    mode_val = mode_series[0] if not mode_series.empty else 'N/A'
    
    st.write(f"**Maximum Value:** {max_val}")
    st.write(f"**Minimum Value:** {min_val}")
    st.write(f"**Average (Mean):** {mean_val:.2f}")
    st.write(f"**Median:** {median_val}")
    st.write(f"**Mode:** {mode_val}")
    
    # Histogram
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    sns.histplot(df[column], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Box Plot
    st.subheader("Box Plot")
    fig, ax = plt.subplots()
    sns.boxplot(y=df[column], ax=ax)
    st.pyplot(fig)
    
    # Trend Line
    st.subheader("Trend Line")
    fig, ax = plt.subplots()
    df[column].plot(kind='line', ax=ax)
    st.pyplot(fig)

def main():
    st.title("Data Analysis Dashboard")
    st.write("Upload a CSV or Excel file to analyze the data.")
    
    file = st.file_uploader("Upload File", type=["csv", "xls", "xlsx"])
    
    if file is not None:
        df = load_data(file)
        if df is not None:
            st.write("### Preview of Data")
            st.write(df.head())
            show_statistics(df)
            show_graphs(df)

if __name__ == "__main__":
    main()
