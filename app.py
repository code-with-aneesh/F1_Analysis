import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load the data
drivers = pd.read_csv(r"data\drivers.csv")
constructors = pd.read_csv(r"data\constructors.csv")
races = pd.read_csv(r"data\races.csv")
qualifying = pd.read_csv(r"data\qualifying.csv")
lap_times = pd.read_csv(r"data\lap_times.csv")
pit_stops = pd.read_csv(r"data\pit_stops.csv")
circuits = pd.read_csv(r"data\circuits.csv")
race_results = pd.read_csv(r"data\results.csv")

# Streamlit Dashboard Layout
st.title("Formula 1 Data Dashboard")
st.sidebar.header("Navigation")
selected_option = st.sidebar.selectbox(
    "Choose a section",
    [
        "Constructors in Qualifying",
        "Top Drivers and Constructors",
        "Fastest and Slowest Circuits",
        "Average Pit Stop Time",
        "Lap Times Visualization",
    ],
)

# Constructors in Qualifying
if selected_option == "Constructors in Qualifying":
    st.header("Constructors in Qualifying")

    merged_df = qualifying.merge(constructors, on="constructorId", how="left")
    result_front_row = (
        merged_df[(merged_df["position"] == 1) | (merged_df["position"] == 2)]["name"]
        .value_counts()
        .sort_index()
    )

    fig1 = go.Figure()
    fig1.add_trace(
        go.Bar(
            x=result_front_row.index,
            y=result_front_row.values,
            marker_color="skyblue",
        )
    )
    fig1.update_layout(
        title="Number of Front Row Qualifications by Team",
        xaxis_title="Team",
        yaxis_title="Number of Front Row Qualifications",
        xaxis_tickangle=-45,
    )
    st.plotly_chart(fig1)

    result_pole = (
        merged_df[(merged_df["position"] == 1)]["name"].value_counts().sort_index()
    )

    fig2 = go.Figure()
    fig2.add_trace(
        go.Bar(
            x=result_pole.index,
            y=result_pole.values,
            marker_color="salmon",
        )
    )
    fig2.update_layout(
        title="Number of Pole Positions by Team",
        xaxis_title="Team",
        yaxis_title="Number of Pole Positions",
        xaxis_tickangle=-45,
    )
    st.plotly_chart(fig2)

# Top Drivers and Constructors
if selected_option == "Top Drivers and Constructors":
    st.header("Top Drivers and Constructors")

    merged_result_driver = race_results.merge(drivers, on="driverId", how="left")
    df = merged_result_driver[merged_result_driver["positionText"] == "1"][
        ["forename", "surname"]
    ]
    df["fullname"] = df["forename"] + " " + df["surname"]
    df_val = df["fullname"].value_counts().head(25)

    fig3 = go.Figure()
    fig3.add_trace(
        go.Bar(
            x=df_val.index,
            y=df_val.values,
            marker_color="LightGreen",
        )
    )
    fig3.update_layout(
        title="Top 25 Drivers with Most Wins",
        xaxis_title="Drivers",
        yaxis_title="Number of Wins",
        xaxis_tickangle=-45,
    )
    st.plotly_chart(fig3)

    merged_result_contructor = race_results.merge(
        constructors, on="constructorId", how="left"
    )
    df = merged_result_contructor[merged_result_contructor["positionText"] == "1"]
    df_val = df["name"].value_counts().head(20)

    fig4 = go.Figure()
    fig4.add_trace(
        go.Bar(
            x=df_val.index,
            y=df_val.values,
            marker_color="tomato",
        )
    )
    fig4.update_layout(
        title="Top 20 Constructors with Most Wins",
        xaxis_title="Constructors",
        yaxis_title="Number of Wins",
        xaxis_tickangle=-45,
    )
    st.plotly_chart(fig4)

# Fastest and Slowest Circuits
if selected_option == "Fastest and Slowest Circuits":
    st.header("Fastest and Slowest Circuits")

    merged_results = race_results.merge(
        races.merge(circuits, how="left", on="circuitId"), how="left", on="raceId"
    )
    merged_races_laptimes_circuits = circuits.merge(
        races.merge(lap_times, on="raceId", how="left"), how="left", on="circuitId"
    )

    average_lap_times = (
        merged_races_laptimes_circuits.groupby("circuitId")["milliseconds"]
        .mean()
        .reset_index()
    )
    average_lap_times = average_lap_times.merge(
        circuits[["circuitId", "name"]], on="circuitId"
    )
    average_lap_times = average_lap_times.sort_values(by="milliseconds").dropna()

    fastest_5 = average_lap_times.head(5)
    slowest_5 = average_lap_times.tail(5)
    combined = pd.concat(
        [fastest_5.assign(speed="Fastest"), slowest_5.assign(speed="Slowest")]
    )

    fig5 = px.bar(
        combined,
        x="milliseconds",
        y="name",
        color="speed",
        orientation="h",
        title="Fastest 5 and Slowest 5 Circuits based on Average Lap Time",
        labels={"milliseconds": "Average Lap Time (milliseconds)", "name": "Circuit"},
    )
    st.plotly_chart(fig5)

# Average Pit Stop Time
if selected_option == "Average Pit Stop Time":
    st.header("Average Pit Stop Time Over the Years")

    races.drop("time", axis=1, inplace=True)
    merged_pitstops_races = races.merge(pit_stops, on="raceId", how="left")
    avg_time_per_year = (
        merged_pitstops_races.groupby("year")["milliseconds"].mean().dropna()
    )
    avg_time_per_year_seconds = avg_time_per_year / 1000

    fig6 = go.Figure()
    fig6.add_trace(
        go.Scatter(
            x=avg_time_per_year_seconds.index,
            y=avg_time_per_year_seconds.values,
            mode="lines+markers",
            marker=dict(color="skyblue"),
            line=dict(color="skyblue"),
        )
    )
    fig6.update_layout(
        title="Average Pit Stop Time over the Years",
        xaxis_title="Year",
        yaxis_title="Average Pit Stop Time (Seconds)",
    )
    st.plotly_chart(fig6)

# Lap Times Visualization
if selected_option == "Lap Times Visualization":
    st.header("Lap Times Visualization")

    race_842 = lap_times[lap_times["raceId"] == 842]

    st.subheader("Lap Times by Driver and Lap Number")
    grouped = race_842.groupby(["driverId", "lap"])["milliseconds"].sum().reset_index()

    fig7 = go.Figure()
    for driver_id, data in grouped.groupby("driverId"):
        fig7.add_trace(
            go.Scatter(
                x=data["lap"],
                y=data["milliseconds"],
                mode="lines+markers",
                name=f"Driver {driver_id}",
            )
        )

    for trace in fig7.data:
        driver_id = int(trace.name.split()[1])
        driver_name = drivers[drivers["driverId"] == driver_id]["code"].values[0]
        trace.name = f"{driver_name} ({driver_id})"

    fig7.update_layout(
        title="Lap Times by Driver and Lap Number",
        xaxis_title="Lap Number",
        yaxis_title="Lap Time (milliseconds)",
        legend_title="Driver",
    )

    st.plotly_chart(fig7)

    st.subheader("Driver Positions by Lap")
    grouped = race_842.groupby(["driverId", "lap"])["position"].sum().reset_index()

    fig8 = go.Figure()
    colors = px.colors.qualitative.Alphabet
    for i, (driver_id, data) in enumerate(grouped.groupby("driverId")):
        fig8.add_trace(
            go.Scatter(
                x=data["lap"],
                y=data["position"],
                mode="lines+markers",
                name=f"Driver {driver_id}",
                line=dict(color=colors[i % len(colors)]),
                marker=dict(color=colors[i % len(colors)]),
            )
        )

    for trace in fig8.data:
        driver_id = int(trace.name.split()[1])
        driver_name = drivers[drivers["driverId"] == driver_id]["driverRef"].values[0]
        trace.name = f"{driver_name} ({driver_id})"

    fig8.update_layout(
        title="Driver Positions by Lap",
        xaxis_title="Lap Number",
        yaxis_title="Position",
        legend_title="Driver",
        yaxis_autorange="reversed",
    )

    st.plotly_chart(fig8)
