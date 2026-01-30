/* (Beta) Export of data model ElectricVehicleMobility of the subject dataModel.Transportation 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE region_type AS ENUM ('CONTINENTE', 'AÇORES', 'MADEIRA', 'Outros - GDPR');
CREATE TYPE ElectricVehicleMobility_type AS ENUM ('ElectricVehicleMobility');
CREATE TYPE vehicleType_type AS ENUM ('BEV', 'PHEV', 'HEV', 'FCEV', 'unknown');

CREATE TABLE ElectricVehicleMobility (
    address JSON,
    alternateName TEXT,
    areaServed TEXT,
    averageDistanceKm NUMERIC,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    dateObserved DATE,
    description TEXT,
    deviceBrand TEXT,
    district TEXT,
    id TEXT PRIMARY KEY,
    location JSON,
    locationCode TEXT,
    municipality TEXT,
    n NUMERIC,
    name TEXT,
    owner JSON,
    region region_type,
    seeAlso JSON,
    source TEXT,
    type ElectricVehicleMobility_type,
    vehicleType vehicleType_type
);