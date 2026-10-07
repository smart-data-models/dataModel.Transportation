/* (Beta) Export of data model RoadAccident of the subject dataModel.Transportation for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE RoadAccident_accidentLocation_type AS ENUM ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
CREATE TYPE RoadAccident_roadIntersection_type AS ENUM ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12');
CREATE TYPE RoadAccident_roadPaving_type AS ENUM ('1', '2', '3');
CREATE TYPE RoadAccident_roadSign_type AS ENUM ('1', '2', '3', '4', '5');
CREATE TYPE RoadAccident_roadSurface_type AS ENUM ('1', '2', '3', '4', '5');
CREATE TYPE RoadAccident_roadTrunk_type AS ENUM ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '15');
CREATE TYPE RoadAccident_status_type AS ENUM ('archived', 'onGoing', 'solved');
CREATE TYPE RoadAccident_type AS ENUM ('RoadAccident');
CREATE TYPE RoadAccident_weakestSubject_type AS ENUM ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24');
CREATE TABLE RoadAccident (
  "accidentDate" TIMESTAMP,
  "accidentDescription" JSON,
  "accidentLocation" RoadAccident_accidentLocation_type,
  "accidentStatisticalDate" JSON,
  "accidentType" JSON,
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "id" TEXT PRIMARY KEY,
  "localId" TEXT,
  "location" JSON,
  "name" TEXT,
  "numPassengersDead" NUMERIC,
  "numPassengersInjured" NUMERIC,
  "numPedestrianDead" NUMERIC,
  "numPedestrianInjured" NUMERIC,
  "owner" JSON,
  "pedestriansInvolved" BOOLEAN,
  "roadClass" TEXT,
  "roadIntersection" RoadAccident_roadIntersection_type,
  "roadPaving" RoadAccident_roadPaving_type,
  "roadSign" RoadAccident_roadSign_type,
  "roadSurface" RoadAccident_roadSurface_type,
  "roadTrunk" RoadAccident_roadTrunk_type,
  "seeAlso" JSON,
  "source" TEXT,
  "status" RoadAccident_status_type,
  "totalDeadPeopleWithin24Hours" NUMERIC,
  "totalDeadPeopleWithin30Days" NUMERIC,
  "totalInjured" NUMERIC,
  "type" RoadAccident_type,
  "vehiclesInvolved" JSON,
  "weakestSubject" RoadAccident_weakestSubject_type,
  "weatherConditions" JSON
);