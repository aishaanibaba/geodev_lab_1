# Data Preparation and Quality Checks

## 1. Coordinate Reference System

The working coordinate reference system selected for the project is **WGS 84 / UTM Zone 31N (EPSG:32631)**.

This CRS was selected because Lagos State lies within UTM Zone 31N and the projected coordinate system uses metres. This makes it suitable for distance, road-length, area, buffering and other spatial analyses required for the project.

## 2. Data Reprojection and Clipping

The following vector datasets were reprojected to EPSG:32631:

* Lagos State boundary
* Road network
* Drainage
* Waterbodies

The road, drainage and waterbody datasets were clipped to the Lagos State study boundary.

The rainfall data is raster data and is being prepared separately using the same working CRS and Lagos State study extent.

## 3. Quality Checks

### Check 1 — CRS consistency

**Result:** All layers were reprojected to WGS 84 / UTM Zone 31N (EPSG:32631)

**Action:** All layers required reprojection to the working CRS

### Check 2 — Geometry validity

**Result:** All datasets geometry were valid

**Action:** No invalid or error geometry were found through all vector datasets using check validity under vector geometry tool

### Check 3 — Duplicate features

**Result:**  No obvious duplicate features were identified after clipping.

**Action:** Applied the delete duplicate geometry tool on each vector layer 

### Check 4 — Missing/null attributes

**Result:** Some road, waterbodies, drainage features contain missing values in the `name` field.

**Action:** These features were retained because a missing feature name does not prevent the geometry from being used in the rainfall-disruption analysis.

### Check 5 — Study-area/extent check

Study-area check: Processed vector layers were clipped to the Lagos State boundary and visually checked to confirm that features outside the study area were removed.

## 4. Problems Identified

The main data-quality issue identified was missing feature-name information in some OpenStreetMap features. These features were retained because the feature geometry remains useful for spatial analysis.

## 5. Analysis-Ready Data

The processed vector datasets have been saved in gpkg

The GeoPackage contains the prepared vector layers used for subsequent analysis.

Rainfall raster data is stored separately in the project's processed rainfall-data directory.


