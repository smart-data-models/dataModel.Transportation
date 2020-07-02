[![Status badge](https://img.shields.io/badge/status-draft-red.svg)](RELEASE_NOTES)
[![Build badge](https://img.shields.io/travis/smart-data-models/dataModel.Transportation.svg "Travis build status")](https://travis-ci.org/smart-data-models/dataModel.Transportation/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
# Transportation Harmonized Data Models

These data models describe the main entities involved with smart applications
that deal with transportation issues. This set of entities is primarily
associated with the Automotive and Smart City vertical segments and related IoT
applications.

When feasible, references to existing schema.org entity types and attributes are
included.

These models have been devised to be as generic as possible, thus allowing to
deal with different scenarios:

-   Traffic flow monitoring
-   Private Vehicles.
-   Public Vehicles (Buses, Trains, etc.).
-   Municipal Vehicles (pick up lorries, cleaning units, ...)
-   Special Vehicles (ambulances, fire brigades, ...)

The main entities identified are:

-   [`TrafficFlowObserved`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/TrafficFlowObserved/swagger.yaml). It represents an
    observation about flow of traffic.
-   [`CrowdFlowObserved`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/CrowdFlowObserved/swagger.yaml). It represents an
    observation related to the movement of people at a certain place and time.
-   [`BikeHireDockingStation`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/BikeHireDockingStation/swagger.yaml). It
    represents an a bike hire docking station where subscribed users can hire
    and return a bike.
-   [`EVChargingStation`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/EVChargingStation/swagger.yaml). It represents a
    public charging station supplying energy to electrical vehicles.
-   [`Road`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/Road/swagger.yaml). It contains a harmonised geographic and
    contextual description of a Road.
-   [`RoadSegment`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/RoadSegment/swagger.yaml). It contains a harmonised
    geographic and contextual description of a road segment.
-   [`Vehicle`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/Vehicle/swagger.yaml). It represents a vehicle with all
    its individual characteristics.
-   [`VehicleModel`](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/VehicleModel/swagger.yaml). It represents a model
    of vehicle, capturing its static properties such as dimensions, materials or
    features.
