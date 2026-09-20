# Week 3 — Data Preparation and Quality Checks

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


