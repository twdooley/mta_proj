"""
use plot_income_data(income)
to get the map
"""

import folium
import pandas as pd

income = pd.read_csv("Median Incomes.csv", header=4)

long_lat = pd.read_csv(
    "http://web.mta.info/developers/data/nyct/subway/Stations.csv"
)
income = income[income["Household Type"] == "All Households"]
income = income[income["TimeFrame"] == 2018]

locations = income["Location"].to_string()

coordinates = [
    (40.7128, -74.0060),
    (40.7831, -73.9712),
    (40.7031, -74.0160),
    (40.7336, -74.0027),
    (40.7150, -73.9843),
    (40.7465, -74.0014),
    (40.7549, -73.9840),
    (40.7479, -73.9757),
    (40.7870, -73.9754),
    (40.7736, -73.9566),
    (40.8171, -73.9560),
    (40.8089, -73.9482),
    (40.7957, -73.9389),
    (40.8417, -73.9394),
    (40.8448, -73.8648),
    (40.8091, -73.9229),
    (40.8094, -73.8803),
    (40.8311, -73.9059),
    (40.8369, -73.9271),
    (40.8575, -73.9097),
    (40.8454, -73.8910),
    (40.8701, -73.8857),
    (40.8996, -73.9088),
    (40.8303, -73.8507),
    (40.8184, -73.8213),
    (40.8553, -73.8640),
    (40.8788, -73.8528),
    (40.6782, -73.9442),
    (40.7081, -73.9571),
    (40.6921, -73.9742),
    (40.6872, -73.9418),
    (40.6958, -73.9171),
    (40.6591, -73.8759),
    (40.6711, -73.9814),
    (40.6527, -74.0093),
    (40.6755, -73.9417),
    (40.6670, -73.9424),
    (40.6264, -74.0299),
    (40.6139, -73.9922),
    (40.6350, -73.9921),
    (40.5755, -73.9707),
    (40.6415, -73.9594),
    (40.5954, -73.9458),
    (40.6552, -73.9125),
    (40.6482, -73.9300),
    (40.6402, -73.9061),
    (40.7282, -73.7949),
    (40.7644, -73.9235),
    (40.7433, -73.9196),
    (40.7557, -73.8831),
    (40.7380, -73.8801),
    (40.7044, -73.9018),
    (40.7256, -73.8625),
    (40.7675, -73.8331),
    (40.7335, -73.7801),
    (40.6901, -73.8566),
    (40.6571, -73.8430),
    (40.7586, -73.7654),
    (40.7027, -73.7890),
    (40.7157, -73.7419),
    (40.5927, -73.7978),
    (40.5795, -74.1502),
    (40.6427, -74.0799),
    (40.5904, -74.0668),
    (40.5083, -74.2355),
]

income["lat_long"] = coordinates

income["lat"] = income["lat_long"].apply(lambda x: x[0])
income["long"] = income["lat_long"].apply(lambda x: x[1])
income.drop(columns="lat_long")


def plot_income_data(income_data):
    # generate a new map
    folium_map = folium.Map(
        location=[40.738, -73.98],
        zoom_start=13,
        tiles="CartoDB dark_matter",
        width="50%",
    )

    # for each row in the data, add a cicle marker
    for index, row in income_data.iterrows():

        # generate the popup message that is shown on click.
        popup_text = "{}<b/> Median Household Income: {}"
        popup_text = popup_text.format(row["Location"], row["Data"])

        # radius of circles
        radius = row["Data"] / 5000

        # color
        color = "#007849"

        # add marker to the map
        folium.CircleMarker(
            location=(row["lat"], row["long"]),
            radius=radius,
            color=color,
            popup=popup_text,
            fill=True,
        ).add_to(folium_map)
    return folium_map
