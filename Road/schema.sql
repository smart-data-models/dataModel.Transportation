/* (Beta) Export of data model Road of the subject dataModel.Transportation for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE Road_roadClass_type AS ENUM ('motorway', 'primary', 'residential', 'secondary', 'service', 'tertiary', 'trunk', 'unclassified');
CREATE TYPE Road_type AS ENUM ('Road');
CREATE TABLE Road (
  "address" JSON,
  "alternateName" TEXT,
  "annotations" JSON,
  "areaServed" TEXT,
  "color" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "image" TEXT,
  "length" NUMERIC,
  "location" JSON,
  "name" TEXT,
  "owner" JSON,
  "refRoadSegment" JSON,
  "responsible" TEXT,
  "roadClass" Road_roadClass_type,
  "seeAlso" JSON,
  "source" TEXT,
  "type" Road_type
);