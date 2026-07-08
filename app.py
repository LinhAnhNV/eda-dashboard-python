import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA Dashboard", layout="wide")
dataset_name = st.sidebar.selectbox("Select Dataset", ["Titanic", "Iris"])

@st.cache_data
def load_data(name: str) -> pd.DataFrame:
    return sns.load_dataset(name.lower())

df = load_data(dataset_name)
st.title(f"Tổng quan Dataset {dataset_name}")
st.caption("Bảng điều  khiển EDA tương tác - Streamlit, Matplotlib & Seaborn.")

if dataset_name ==  "Titanic":
    df.dropna(subset=["age", "fare"], inplace=True)
    sex_options = df["sex"].unique().tolist()
    sex_filter = st.sidebar.multiselect("Chọn giới tính", options=sex_options, default=sex_options)
    pclass_options = sorted(df["pclass"].unique().tolist())
    pclass_filter = st.sidebar.multiselect("Chọn hạng vé", options=pclass_options, default=pclass_options)
    age_min, age_max = int(df["age"].min()), int(df["age"].max())
    age_range = st.sidebar.slider("Chọn khoảng tuổi", min_value=age_min, max_value=age_max, value=(age_min, age_max))
    df = df[
        df["sex"].isin(sex_filter) &
        df["pclass"].isin(pclass_filter) &
        df["age"].between(age_range[0], age_range[1])
    ]
else:
    species_options = df["species"].unique().tolist()
    species_filter = st.sidebar.multiselect("Chọn loài", options=species_options, default=species_options)
    df = df[df["species"].isin(species_filter)]

st.sidebar.markdown(f"**Số dòng sau khi lọc:**  {len(df)}")
st.header("1. Tổng quan Dataset")
col1, col2 = st.columns([1, 2])
with col1:
    st.write(df.shape)
    st.write(df.isnull().sum())
with col2:
    st.write(df.describe(include="all").T)

st.dataframe(df.head(10))
st.header("2. Trực quan hóa dữ liệu")
if dataset_name == "Titanic":
    st.subheader("2.1. Tỉ lệ sống sót theo giới tính")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x="survived", hue="sex", data=df, ax=ax)
    st.pyplot(fig)
    
    st.subheader("2.2. Phân phối tuổi hành khách")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df["age"], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("2.3. Phân phối hạng vé")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x="pclass", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("2.4. Giá vé theo hạng vé")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x="pclass", y="fare", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("2.5. Tỉ lệ sống sót trung bình theo giới tính")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="sex", y="survived", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("2.6. Tương quan giữa các biến số")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.subheader("2.1. Phân phối chiều dài cánh hoa")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df, x="petal_length", hue="species", bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("2.2. Sepal length vs Sepal width")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df, x="sepal_length", y="sepal_width", hue="species", bins=20, kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("2.3. Boxplot các đặc trưng theo loài")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x="species", y="petal_length", data=df, ax=ax)
    st.pyplot(fig)

    st.subheader("2.4. Tương quan giữa các biến số")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)