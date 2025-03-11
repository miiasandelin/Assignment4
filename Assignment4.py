import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic.csv")

st.title("Titanic Data")
st.markdown("Data on passengers who survived or perished on the Titanic.")

st.subheader("Number of Survivors and Casualties")
fig, ax = plt.subplots()
df["Survived"].value_counts().plot(kind="bar", color=["red", "green"], ax=ax)
ax.set_xticklabels(["Perished", "Survived"], rotation=0)
ax.set_ylabel("Number of People")
st.pyplot(fig)

st.subheader("Survival Rate by Gender")
survival_by_gender = df.groupby("Sex")["Survived"].mean() * 100
fig, ax = plt.subplots()
survival_by_gender.plot(kind="bar", color=["blue", "pink"], ax=ax)
ax.set_ylabel("Survival Rate (%)")
st.pyplot(fig)

st.subheader("Filter Passengers by Age")
age_options = sorted(df["Age"].dropna().unique())
selected_age = st.select_slider("Choose age:", options=age_options)
filtered_df = df[df["Age"] == selected_age]
st.write(f"Passengers aged {selected_age}:")
st.dataframe(filtered_df)

st.subheader("Survival Rate by Passenger Class")
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100
fig, ax = plt.subplots()
survival_by_class.plot(kind="bar", color=["gold", "silver", "brown"], ax=ax)
ax.set_xlabel("Passenger Class")
ax.set_ylabel("Survival Rate (%)")
st.pyplot(fig)
