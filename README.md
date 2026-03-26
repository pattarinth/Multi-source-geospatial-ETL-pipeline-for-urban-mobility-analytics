# Multi-source Geospatial ETL Pipeline for Urban Mobility Analytics

![Berlin Mobility Analysis](output/berlin_mitte_mobility_map.png)

## Project Overview

This project builds a **multi-source geospatial ETL pipeline** that integrates bike-sharing stations, bike lane infrastructure, traffic sensors, and public transport data to analyze mobility infrastructure coverage in Berlin.

The workflow demonstrates how spatial data pipelines can support **urban mobility planning and infrastructure analysis**.

---

## Key Features

- Multi-source geospatial data integration
- Automated ETL pipeline using Python
- Spatial analysis with GeoPandas and PostGIS
- Infrastructure coverage analysis using spatial joins
- Professional cartographic visualization

---

## Coverage Metrics

| Metric | Value |
|------|------|
| Total bike stations | X |
| Stations within bike lane buffer | Y |
| Stations without bike lane access | Z |
| Coverage rate | W% |

---

## Data Sources

- OpenStreetMap – road network and bike lanes  
- Nextbike Berlin station dataset  
  https://github.com/MaxHalford/bike-sharing-history/blob/main/data/stations/berlin/nextbike.geojson  
- Berlin traffic sensor dataset  
- GTFS public transport data (VBB)

---

## Spatial Analysis Workflow

1. Extract mobility datasets from multiple sources
2. Transform and standardize spatial data
3. Load datasets into PostGIS
4. Create bike-lane buffer zones
5. Perform spatial joins with bike stations
6. Identify stations without nearby bike lane access
7. Visualize results using a professional map layout

---

## Repository Structure

```
Multi-source-geospatial-ETL-pipeline-for-urban-mobility-analytics
│
├── notebooks/
│ ├── mobility_analysis.ipynb
│ ├── berlin_mitte_portfolio_map.png
│ └── berlin_mitte_mobility_map.pdf
│
├── scripts/
│ ├── etl_roads.py
│ ├── etl_bike_lanes.py
│ └── etl_bike_stations.py
│
├── run_pipeline.py
│
├── data/
│ └── raw/ (datasets not included in repo)
│
└── README.md
```


## Technologies Used

- Python
- GeoPandas
- PostGIS
- Pandas
- Matplotlib
- Contextily

---

## Example Output

The final visualization highlights:

- Bike lane infrastructure
- Bike sharing stations
- Stations without bike lane coverage
- Traffic sensors
- Public transport stops

---

## Author

Pattarin Thunyapar  
MSc Data Analytics
