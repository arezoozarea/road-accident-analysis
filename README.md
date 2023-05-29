# road-accident-analysis

This project focuses on the data of the road accident in Iran.
To show the demo, click on the [demo](https://examples.com).

## 1. Data Cleaning

## 2. Make Data Time Series

## 3. Analysis of Data Time Series

## 4. Dashboard Page

This data is used to illustrate the statistical data in the first page of the website.

### 4.1. Read Data

The data is used in this project after being cleaned and recreated from the original file. Final accident points
are collected data from Dec 2021 to Aug 2022, which is included the geographic and statistics data. This data is
allowed to show as a geographical geometry or illustrated as a list of data. As a result, the final file also
provided the capability to create an analytic tool.

```python
df = pd.read_csv("../data/final_accident_points.csv")
```

### 4.2. The total number of accidents

This number is calculated through the count of a column `OBJECTID` of the read CSV file.

```python
total_killed_number = df.KilledNumber.sum()
```

### 4.3. The total number of kills

This number is calculated through the sum up of the `KilledNumber` column of the read CSV file,
this column is also included as an integer number in the field.

```python
total_injured_number = df.InjuredNumber.sum()
```

### 4.4. Save data as a JSON format

The final result is data of JSON type which is ready to develop in the client-side.
This data is used as specific card views in charts page or default page of the website.
The location of those is after the header
of the website.

```python
data = json.dumps({
    "total_Accident": int(total_Accident),
    "total_killed_number": int(total_killed_number),
    'total_injured_number': int(total_injured_number)
})
```

## 5. Charts Page

### 5.1. Total Accident by Province

This page is provided a place to show charts data as pie chart and bar chart.

```python
total_Accident_by_province = df.groupby("ProvinceName").road_id.count().sort_values(ascending=False)
```

### 5.2. Most Collision Shape Title

```python
most_Collision_Shape_Title = df.groupby("CollisionShapeTitle").CollisionShapeTitle.count()
```

### 5.3. Total Accident by Road

```python
total_accident_by_road = df.groupby(["road_search_name"]).road_id.count().sort_values(ascending=False).head(10)
```

### 5.4. Total Accident by Vehicle Name

Data are grouped by province which related to accident count. The result is shown as a bar chart from `Alrboz`
province (the highest number of accidents) and `Azarbijan Garbi` province (the lowest number of accidents)`.

```python
total_accident_by_vehicle_name = df.groupby("VehicleTypeNames").VehicleTypeNames.count().sort_values(
    ascending=False).head(10)
```

### 5.5. Total Accident Statistics

```python
total_accident_statistics = total_accident_by_road.agg({"mean", "median", "std"})
```

### 5.6 Total Injured Number Statistics

```python
total_InjuredNumber_statistics = df.InjuredNumber.agg({"mean", "median", "std"})
```

### 5.7 Total Killed Number Statistics

```python
total_KilledNumber_statistics = df.KilledNumber.agg({"mean", "median", "std"})
```