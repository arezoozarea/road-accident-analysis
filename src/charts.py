# Charts Page
#
# This data is used to illustrate the statistical data in the first page of the website.

total_Accident_by_province = df.groupby("ProvinceName").road_id.count().sort_values(ascending=False)
keys = total_Accident_by_province.keys()
values = total_Accident_by_province.values

most_Collision_Shape_Title = df.groupby("CollisionShapeTitle").CollisionShapeTitle.count()

total_accident_by_road_chart = df.groupby(["road_search_name"]).road_id.count().sort_values(ascending=False).head(10)


total_accident_by_vehicle_name = df.groupby("VehicleTypeNames").VehicleTypeNames.count().sort_values(
    ascending=False).head(10)
total_accident_statistics = total_accident_by_road_chart.agg({"mean", "median", "std"})
total_InjuredNumber_statistics = df.InjuredNumber.agg({"mean", "median", "std"})
total_KilledNumber_statistics = df.KilledNumber.agg({"mean", "median", "std"})