import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
drivers = pd.read_csv("data/drivers.csv")
constructors = pd.read_csv("data/constructors.csv")
races = pd.read_csv("data/races.csv").drop("url", axis=1)
qualifying = pd.read_csv("data/qualifying.csv")
lap_times = pd.read_csv("data/lap_times.csv")
pit_stops = pd.read_csv("data/pit_stops.csv")
race_results = pd.read_csv("data/results.csv")
circuits = pd.read_csv("data/circuits.csv")


# Define function to get colorscale
def colorscale():
    named_colorscales = px.colors.named_colorscales()
    return st.selectbox("Select Colorscale", named_colorscales)


# Set up Streamlit app
st.title("F1 Data Analysis Dashboard")

# Get the selected colorscale
selected_colorscale = colorscale()

# Constructors in Qualifying
st.header("Constructors in Qualifying")
merged_df = qualifying.merge(constructors, on="constructorId", how="left")

# Selection for front row or pole positions
option = st.selectbox("Select Position Type", ["Front Row", "Pole Positions"])

if option == "Front Row":
    result = (
        merged_df[(merged_df["position"] == 1) | (merged_df["position"] == 2)]["name"]
        .value_counts()
        .sort_index()
    )
    fig = px.bar(
        result,
        x=result.index,
        y=result.values,
        labels={"x": "Team", "y": "Number of Front Row Qualifications"},
        title="Number of Front Row Qualifications by Team",
        color=result.values,
        color_continuous_scale=selected_colorscale,
    )
else:
    result = merged_df[merged_df["position"] == 1]["name"].value_counts().sort_index()
    fig = px.bar(
        result,
        x=result.index,
        y=result.values,
        labels={"x": "Team", "y": "Number of Pole Positions"},
        title="Number of Pole Positions by Team",
        color=result.values,
        color_continuous_scale=selected_colorscale,
    )

fig.update_layout(
    xaxis_tickangle=-45,
    height=600,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    title_font=dict(size=24),
    xaxis_title_font=dict(size=18),
    yaxis_title_font=dict(size=18),
)
st.plotly_chart(fig)

# Most races won
st.header("Most Races Won by Driver and Constructor")

# Selection for driver or constructor
option = st.selectbox("Select Category", ["Drivers", "Constructors"])

if option == "Drivers":
    merged_result_driver = race_results.merge(drivers, on="driverId", how="left")
    df = merged_result_driver[merged_result_driver["positionText"] == "1"][
        ["forename", "surname"]
    ]
    df["fullname"] = df["forename"] + " " + df["surname"]
    df_val = df["fullname"].value_counts().head(25)
    fig = px.bar(
        df_val,
        x=df_val.index,
        y=df_val.values,
        labels={"x": "Drivers", "y": "Number of Wins"},
        title="Top 25 Drivers with Most Wins",
        color=df_val.values,
        color_continuous_scale=selected_colorscale,
    )
else:
    merged_result_contructor = race_results.merge(
        constructors, on="constructorId", how="left"
    )
    df = merged_result_contructor[merged_result_contructor["positionText"] == "1"]
    df_val = df["name"].value_counts().head(20)
    fig = px.bar(
        df_val,
        x=df_val.index,
        y=df_val.values,
        labels={"x": "Constructors", "y": "Number of Wins"},
        title="Top 20 Constructors with Most Wins",
        color=df_val.values,
        color_continuous_scale=selected_colorscale,
    )

fig.update_layout(
    xaxis_tickangle=-45,
    height=600,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    title_font=dict(size=24),
    xaxis_title_font=dict(size=18),
    yaxis_title_font=dict(size=18),
)
st.plotly_chart(fig)

# Fastest Laps on each circuit
st.header("Fastest Laps on Each Circuit")

merged_results = race_results.merge(
    races.merge(circuits, how="left", on="circuitId"), how="left", on="raceId"
)

# Selection for country or circuit
option = st.selectbox("Select View", ["Country", "Circuit"])

if option == "Country":
    result = merged_results["country"].value_counts().sort_values(ascending=False)
    fig = px.bar(
        result,
        x=result.index,
        y=result.values,
        labels={"x": "Country", "y": "Number of Races"},
        title="Number of Races Held in Each Country",
        color=result.values,
        color_continuous_scale=selected_colorscale,
    )
else:
    result = (
        merged_results["name_y"].value_counts().sort_values(ascending=False).head(25)
    )
    fig = px.bar(
        result,
        x=result.index,
        y=result.values,
        labels={"x": "Circuit", "y": "Number of Races"},
        title="Number of Races Held at Each Circuit (Top 25)",
        color=result.values,
        color_continuous_scale=selected_colorscale,
    )

fig.update_layout(
    xaxis_tickangle=-45,
    height=600,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    title_font=dict(size=24),
    xaxis_title_font=dict(size=18),
    yaxis_title_font=dict(size=18),
)
st.plotly_chart(fig)
