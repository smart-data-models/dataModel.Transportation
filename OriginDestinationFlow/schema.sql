/* (Beta) Export of data model OriginDestinationFlow of the subject dataModel.Transportation 
for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE flowType_type AS ENUM ('tourism', 'commuting', 'business', 'migration', 'mixed');
CREATE TYPE OriginDestinationFlow_type AS ENUM ('OriginDestinationFlow');

CREATE TABLE OriginDestinationFlow (
    address JSON,
    aggregationDateType TEXT,
    alternateName TEXT,
    areaServed TEXT,
    countryCode TEXT,
    dataProvider TEXT,
    dateCreated TIMESTAMP,
    dateModified TIMESTAMP,
    dateObserved TIMESTAMP,
    description TEXT,
    destinationLocation JSON,
    destinationLocationCode TEXT,
    destinationLocationName TEXT,
    flowCount NUMERIC,
    flowType flowType_type,
    hour NUMERIC,
    id TEXT PRIMARY KEY,
    location JSON,
    name TEXT,
    nationality TEXT,
    nationalityName TEXT,
    originLocation JSON,
    originLocationCode TEXT,
    originLocationName TEXT,
    owner JSON,
    seeAlso JSON,
    source TEXT,
    type OriginDestinationFlow_type
);