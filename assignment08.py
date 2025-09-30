# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ------------------------------
# Title
# ------------------------------
st.title("CORD-19 Data Explorer")
st.write("""
Simple exploration of COVID-19 research papers.
This app allows you to explore publication trends, top journals, word frequencies in titles, and more.
""")

# ------------------------------
# Load Dataset
# ------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("metadata.csv")
        # Drop rows with missing essential info
        df = df.dropna(subset=['title', 'abstract', 'publish_time'])
        # Convert date
        df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
        df['year'] = df['publish_time'].dt.year
        df['abstract_length'] = df['abstract'].apply(lambda x: len(str(x).split()))
        return df
    except FileNotFoundError:
        st.error("File metadata.csv not found. Please check the path.")
        return pd.DataFrame()

df = load_data()

# ------------------------------
# Basic Exploration
# ------------------------------
if not df.empty:
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))

    st.subheader("Data Info")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    st.write(df.dtypes)
    st.write("Missing values per column:")
    st.write(df.isnull().sum())

    # ------------------------------
    # Sidebar Filters
    # ------------------------------
    st.sidebar.header("Filters")
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
    selected_journals = st.sidebar.multiselect(
        "Select Journals (leave empty for all)",
        options=df['journal'].dropna().unique()
    )

    # Filter dataframe based on user input
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    if selected_journals:
        filtered_df = filtered_df[filtered_df['journal'].isin(selected_journals)]

    st.subheader(f"Filtered Data: {filtered_df.shape[0]} Papers")

    # ------------------------------
    # Analysis & Visualizations
    # ------------------------------
    # 1. Publications per year
    st.subheader("Publications per Year")
    papers_per_year = filtered_df['year'].value_counts().sort_index()
    fig1, ax1 = plt.subplots()
    sns.barplot(x=papers_per_year.index, y=papers_per_year.values, palette="Blues_d", ax=ax1)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Number of Papers")
    st.pyplot(fig1)

    # 2. Top Journals
    st.subheader("Top 10 Journals by Number of Papers")
    top_journals = filtered_df['journal'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    sns.barplot(x=top_journals.values, y=top_journals.index, palette="Greens_d", ax=ax2)
    ax2.set_xlabel("Number of Papers")
    ax2.set_ylabel("Journal")
    st.pyplot(fig2)

    # 3. Word Cloud of Paper Titles
    st.subheader("Word Cloud of Paper Titles")
    text = " ".join(title for title in filtered_df['title'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig3, ax3 = plt.subplots(figsize=(10,5))
    ax3.imshow(wordcloud, interpolation='bilinear')
    ax3.axis('off')
    st.pyplot(fig3)

    # 4. Abstract Length Distribution
    st.subheader("Distribution of Abstract Lengths")
    fig4, ax4 = plt.subplots()
    sns.histplot(filtered_df['abstract_length'], bins=50, color='purple', ax=ax4)
    ax4.set_xlabel("Number of Words")
    ax4.set_ylabel("Frequency")
    st.pyplot(fig4)

    # 5. Scatter Plot: Abstract Length vs Year
    st.subheader("Abstract Length vs Year")
    fig5, ax5 = plt.subplots()
    sns.scatterplot(x='year', y='abstract_length', data=filtered_df, alpha=0.5, ax=ax5)
    ax5.set_xlabel("Year")
    ax5.set_ylabel("Abstract Length (words)")
    st.pyplot(fig5)

    # ------------------------------
    # Insights
    # ------------------------------
    st.subheader("Insights")
    st.write("""
    - COVID-19 research publications increased over the years.
    - Certain journals dominate the publications.
    - Abstract lengths vary widely, indicating some papers are very detailed while others are concise.
    - Word cloud shows the most common terms in titles, giving an overview of trending topics.
    """)
else:
    st.warning("No data available to display.")
