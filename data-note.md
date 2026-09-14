# Data Note

## 1. Lagos State Road Network

**Source:** OpenStreetMap (OSM), downloaded through Geofabrik

**Source link:** https://www.openstreetmap.org/

**Purpose:** To obtain the road network of Lagos State for the analysis of roads potentially affected by rainfall-related disruption.

**Geometry type:** LineString

**Number of features:** 67,830 features (clipped to the Lagos State boundary and filtered using fclass to major roads).

**Key columns:**

* `name` – road name
* `fclass` – road/transport feature classification
* `osm_id` – OpenStreetMap feature identifier
* 'oneway' – whether traffic is restricted to one direction on that road.

**Observations / missing values:**
A number of road features do not have values in the `name` field. Some minor roads and pathways also have limited attribute information. The completeness of road attributes varies between features. Does not have a surface field

---

## 2. Lagos State Boundary

**Source:** Humanitarian Data Exchange (HDX) – Nigeria Subnational Administrative Boundaries

**Source link:** https://data.humdata.org/dataset/cod-ab-nga

**Purpose:** To define the geographical extent of Lagos State and provide the boundary used to clip and analyse other datasets.

**Geometry type:** Polygon

**Number of features:** 1 (Selected Lagos state from admn1 and saved the selected feature)

**Key columns:**

* `adm1_name` – name of the feature
* `area sqkm` – area of the boundary 
* `center_lat` – latitide of the polygon
* `center_long` – longitude of the polygon
* `adm1_pcode` – administrative place/code identifier

**Observations / missing values:**
The dataset was inspected in QGIS for completeness. Many fields have null values

---

## 3. Rainfall Data

**Source:** Climate Hazards Center – CHIRPS

**Source link:** https://chc.ucsb.edu/data/chirps3

**Purpose:** To provide rainfall information for analysing the potential relationship between rainfall intensity/distribution and road disruption in Lagos State.

**Data type:** Raster

**Geometry:** Raster/grid

**Number of features:** Not applicable because this is a raster dataset. It consists of raster cells/pixels rather than individual vector features.

**Key information:**

* Rainfall measurement represented by raster cell values
* Spatial resolution:  Native CHIRPS v3 resolution is 0.05° (~5 km). The downloaded raster is stored in EPSG:3857 and has a pixel size of approximately 612.93 m × 612.93 m.
* Temporal period: January 2007 to August 2026 
* CRS: EPSG:3857 - WGS 84 / Pseudo-Mercator
* Raster dimensions: 1109 × 444 pixels
* Band count: 1
* NoData value: 0

**Observations / missing values:**
The dataset has a Band count of	1, which is of band 1, it has a NoData value of 0 and Stored raster value range: 4,194–56,843

---

## 4. Waterbodies

**Source:**  OpenStreetMap (OSM), downloaded through Geofabrik

**Source link:** https://www.openstreetmap.org/

**Purpose:** To identify waterbodies that may contribute to or influence rainfall-related flooding and road disruption.

**Geometry type:** Polygon

**Number of features:** 307 (Clipped to the boundary of Lagos )

**Key columns:**

* `fclass` – waterbody type classification
* `name` – waterbody name
* `osm_id` – OpenStreetMap feature identifier

**Observations / missing values:**
some water bodies feature do not have names. No waterbody area field

---

## Data Preparation

The datasets were downloaded from their respective sources and opened in QGIS for inspection. The attribute tables were reviewed to identify feature counts, important fields and missing values. The datasets will be used in subsequent stages of the project to analyse the relationship between rainfall, waterbodies and the Lagos road network.
