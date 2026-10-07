/* (Beta) Export of data model ItemFlowObserved of the subject dataModel.Transportation for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ItemFlowObserved_itemType_type AS ENUM ('people', 'ship', 'vehicle', 'yacht');
CREATE TYPE ItemFlowObserved_laneDirection_type AS ENUM ('forward', 'backward', 'inbound', 'outbound', 'right', 'left');
CREATE TYPE ItemFlowObserved_type AS ENUM ('ItemFlowObserved');
CREATE TABLE ItemFlowObserved (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "averageGapDistance" NUMERIC,
  "averageHeadwayTime" NUMERIC,
  "averageLength" NUMERIC,
  "averageSpeed" NUMERIC,
  "congested" BOOLEAN,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "dateObserved" TIMESTAMP,
  "dateObservedFrom" TIMESTAMP,
  "dateObservedTo" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "intensity" NUMERIC,
  "itemSubType" TEXT,
  "itemType" ItemFlowObserved_itemType_type,
  "laneDirection" ItemFlowObserved_laneDirection_type,
  "laneId" NUMERIC,
  "location" JSON,
  "maxSpeed" NUMERIC,
  "minSpeed" NUMERIC,
  "name" TEXT,
  "occupancy" NUMERIC,
  "owner" JSON,
  "refDevice" JSON,
  "refRoadSegment" JSON,
  "reverseLane" BOOLEAN,
  "seeAlso" JSON,
  "source" TEXT,
  "type" ItemFlowObserved_type
);