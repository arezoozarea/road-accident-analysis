# Dashboard Page
#
# This data is used to illustrate the statistical data in the first page of the website.
import json

import pandas as pd

# The data is used in this project after being cleaned and recreated from the original file. Final accident points
# are collected data from Dec 2021 to Aug 2022, which is included the geographic and statistics data. This data is
# allowed to show as a geographical geometry or illustrated as a list of data. As a result, the final file also
# provided the capability to create an analytic tool.
df = pd.read_csv("../data/final_accident_points.csv")

# The total number of accidents is calculated through the count of a column "OBJECTID" of the read CSV file.
total_Accident = df.OBJECTID.count()

# The total number of kills is calculated through the sum up of the "KilledNumber" column of the read CSV file,
# this column is also included as an integer number in the field.
total_killed_number = df.KilledNumber.sum()

# The total number of Injures is calculated through the sum up of the "KilledNumber" column of the read CSV file,
# this column is also included as an integer number in the field.
total_injured_number = df.InjuredNumber.sum()

# The final result is data of JSON type which is ready to develop in the client-side.
# This data is used as specific card views in charts page or default page of the website.
# The location of those is after the header
# of the website.
data = json.dumps({
    "total_Accident": int(total_Accident),
    "total_killed_number": int(total_killed_number),
    'total_injured_number': int(total_injured_number)
})

# This page is provided a place to show charts data as pie chart and bar chart.

# Data are grouped by province which related to accident count. The result is shown as a bar chart from `Alrboz`
# province (the highest number of accidents) and `Azarbijan Garbi` province (the lowest number of accidents)`.
total_Accident_by_province = df.groupby("ProvinceName").road_id.count().sort_values(ascending=False)

most_Collision_Shape_Title = df.groupby("CollisionShapeTitle").CollisionShapeTitle.count()

total_accident_by_road = df.groupby(["road_search_name"]).road_id.count().sort_values(ascending=False).head(10)

total_accident_by_vehicle_name = df.groupby("VehicleTypeNames").VehicleTypeNames.count().sort_values(
    ascending=False).head(10)
total_accident_statistics = total_accident_by_road.agg({"mean", "median", "std"})
total_InjuredNumber_statistics = df.InjuredNumber.agg({"mean", "median", "std"})
total_KilledNumber_statistics = df.KilledNumber.agg({"mean", "median", "std"})
