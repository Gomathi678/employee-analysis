
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Employee Data Analysis Dashboard")

df = pd.read_csv("data/clean_data.csv")

st.metric("Total Employees", len(df))

st.subheader("Employee Data")
st.dataframe(df.head(10))

numeric_columns = df.select_dtypes(include="number").columns.tolist()
categorical_columns = df.select_dtypes(include="object").columns.tolist()

if numeric_columns:
    selected = st.selectbox("Select numeric column", numeric_columns)

    fig1, ax1 = plt.subplots()
    ax1.hist(df[selected].dropna(), bins=15)
    ax1.set_title("Distribution of " + selected)
    ax1.set_xlabel(selected)
    ax1.set_ylabel("Count")
    st.pyplot(fig1)
    plt.close(fig1)

    if categorical_columns:
        category = st.selectbox("Select category", categorical_columns)

        chart = df.groupby(category)[selected].mean()

        fig2, ax2 = plt.subplots()
        chart.plot(kind="bar", ax=ax2)
        ax2.set_title("Average " + selected + " by " + category)
        ax2.set_xlabel(category)
        ax2.set_ylabel("Average " + selected)
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close(fig2)
else:
    st.warning("No numeric columns found.")
