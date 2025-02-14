# Formula 1 Data Analysis Dashboard

This project is an interactive dashboard built using Streamlit to visualize and analyze Formula 1 data. The dashboard provides insights into various aspects of Formula 1 races, including constructors' performance in qualifying, top drivers and constructors, fastest and slowest circuits, average pit stop times, and lap times visualization.

## Features

- **Constructors in Qualifying**: Visualize the number of front row qualifications and pole positions by team.
- **Top Drivers and Constructors**: Display the top 25 drivers with the most wins and the top 20 constructors with the most wins.
- **Fastest and Slowest Circuits**: Identify the fastest and slowest circuits based on average lap times.
- **Average Pit Stop Time**: Analyze the average pit stop time over the years.
- **Lap Times Visualization**: Explore lap times and driver positions by lap for a specific race.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/F1_Analysis.git
    cd F1_Analysis
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Data

The data used in this project is sourced from various CSV files located in the [data](http://_vscodecontentref_/0) directory. The following datasets are used:

- [drivers.csv](http://_vscodecontentref_/1): Information about drivers.
- [constructors.csv](http://_vscodecontentref_/2): Information about constructors.
- [races.csv](http://_vscodecontentref_/3): Information about races.
- [qualifying.csv](http://_vscodecontentref_/4): Qualifying results.
- [lap_times.csv](http://_vscodecontentref_/5): Lap times for each race.
- [pit_stops.csv](http://_vscodecontentref_/6): Pit stop data.
- [circuits.csv](http://_vscodecontentref_/7): Information about circuits.
- `results.csv`: Race results.

## Usage

1. Launch the Streamlit app by running the command mentioned in the installation section.
2. Use the sidebar to navigate between different sections of the dashboard.
3. Explore the visualizations and insights provided in each section.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/8) file for more details.

## Acknowledgements

- The data used in this project is sourced from [Ergast API](http://ergast.com/mrd/).
- This project uses [Streamlit](https://streamlit.io/) for building the interactive dashboard.
- Visualizations are created using [Plotly](https://plotly.com/).

## Contact

For any questions or feedback, please contact Aneesh Angane at [your-email@example.com].

