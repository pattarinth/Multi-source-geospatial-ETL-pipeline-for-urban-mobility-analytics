# City Mobility Spatial ETL Pipeline

A spatial data engineering project that builds an ETL pipeline to ingest, transform, and store urban mobility data using Python and PostGIS.

## Project Overview

This project demonstrates a geospatial data pipeline that:

- Extracts open spatial datasets (roads and bike stations)
- Transforms them using GeoPandas
- Loads them into a PostGIS-enabled PostgreSQL database
- Performs spatial analysis using SQL

The goal is to simulate a real-world spatial data engineering workflow for urban mobility analysis.

---

## Tech Stack

- Python
- GeoPandas
- PostgreSQL
- PostGIS
- SQLAlchemy
- Conda environment

---

## Project Structure

```
spatial-city-mobility-et
│
├── data
│   ├── raw
│   └── processed
│
├── scripts
│   ├── etl_roads.py
│   ├── etl_bike_stations.py
│   └── run_pipeline.py
│
├── notebooks
├── sql
├── environment.yml
└── README.md
```

---

## Data Sources

- OpenStreetMap road network (via Geofabrik)
- Bike sharing station data (Berlin open data)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd spatial-city-mobility-et
```

### 2. Create conda environment

```bash
conda env create -f environment.yml
conda activate spatial-etl
```

### 3. Set up PostgreSQL + PostGIS

Create a database named:

```
city_mobility
```

Enable PostGIS:

```sql
CREATE EXTENSION postgis;
```

---

## Run the ETL Pipeline

```bash
python scripts/run_pipeline.py
```

This will:

1. Load road data into PostGIS
2. Load bike station data into PostGIS

---

## Example Spatial Query

Count bike stations near roads:

```sql
SELECT
    COUNT(*) AS stations_near_roads
FROM bike_stations b
JOIN roads r
ON ST_DWithin(b.geometry, r.geometry, 0.0005);
```

---

## Key Skills Demonstrated

- Spatial ETL pipeline design
- Geospatial data transformation
- PostGIS database integration
- Spatial SQL queries
- Python data engineering workflows

---

## Future Improvements

- Add automated scheduling (cron or Airflow)
- Include additional mobility datasets
- Build API or dashboard for visualization
## Data Source
Download Berlin OSM data from:
https://download.geofabrik.de/europe/germany/berlin.html

Extract the shapefiles into:
data/raw/
