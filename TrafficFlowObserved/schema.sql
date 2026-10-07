/* (Beta) Export of data model TrafficFlowObserved of the subject dataModel.Transportation for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TrafficFlowObserved_laneDirection_type AS ENUM ('forward', 'backward');
CREATE TYPE TrafficFlowObserved_type AS ENUM ('TrafficFlowObserved');
CREATE TYPE TrafficFlowObserved_vehicleType_type AS ENUM ('agriculturalVehicle', 'bicycle', 'bus', 'minibus', 'car', 'caravan', 'tram', 'tanker', 'carWithCaravan', 'carWithTrailer', 'lorry', 'moped', 'motorcycle', 'motorcycleWithSideCar', 'motorscooter', 'trailer', 'van', 'constructionOrMaintenanceVehicle', 'trolley', 'binTrolley', 'sweepingMachine', 'cleaningTrolley');
CREATE TABLE TrafficFlowObserved (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "averageGapDistance" NUMERIC,
  "averageHeadwayTime" NUMERIC,
  "averageVehicleLength" NUMERIC,
  "averageVehicleSpeed" NUMERIC,
  "congested" BOOLEAN,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "dateObserved" TEXT,
  "dateObservedFrom" TIMESTAMP,
  "dateObservedTo" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "intensity" NUMERIC,
  "laneDirection" TrafficFlowObserved_laneDirection_type,
  "laneId" NUMERIC,
  "location" JSON,
  "name" TEXT,
  "occupancy" NUMERIC,
  "owner" JSON,
  "refRoadSegment" TEXT,
  "reversedLane" BOOLEAN,
  "seeAlso" JSON,
  "source" TEXT,
  "type" TrafficFlowObserved_type,
  "vehicleSubType" TEXT,
  "vehicleType" TrafficFlowObserved_vehicleType_type
);