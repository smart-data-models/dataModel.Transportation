Entität: TransportStation  
=========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TransportStation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Das Datenmodell ist eine allgemeine Beschreibung von städtischen Stationen (Metro, Bus, Straßenbahn, Heliport, ...) nach dem GFTS-Standard https://developers.google.com/transit/gtfs/reference/#stopstxt, sowie die detaillierte Beschreibung dieser (Zugangsmittel, Bahnsteig, Hilfestellung, ...).**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `contactPoint`: Die Angaben zur Kontaktaufnahme mit dem Artikel.  - `contractingAuthority`: Name des öffentlichen Auftraggebers.  - `contractingCompany`: Name des Vertragsunternehmens, das für den Betrieb der Station verantwortlich ist.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateLastReported`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, an dem das Gerät erfolgreich Daten gemeldet hat. Datum und Uhrzeit in einem ISO8601 UTC-Format.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `dimension`: Globale Dimension. Das Format wird durch eine Untereigenschaft von 3 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  - `id`: Eindeutiger Bezeichner der Entität  - `installationMode`: Standort relativ zur Bodenreferenz. Enum:'aerial, ground, underGround, underSea'  - `inventory`: Allgemeines Datenmapping nur für `locationType` = 0, 1, 3, 4. Das Format wird durch eine Untereigenschaft von 4 Elementen strukturiert.  - `levelId`: Etage, auf der sich der Standort befindet. Numerischer Index, der mit der Etage verbunden ist. Gibt die relative Position dieser Etage im Verhältnis zu den anderen an. Der Index 0 zeigt das Erdgeschoss an. Die Etagen oberhalb des Erdgeschosses werden durch positive Indizes und die unterirdischen Etagen durch negative Indizes angezeigt.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `locationType `: Link zum GTFS-Standard-Repository, das den unterschiedlichen Ort beschreibt [Ortstyp]. 0 Haltestelle oder Bahnsteig (Ort, an dem Benutzer in ein öffentliches Verkehrsmittel ein- oder aussteigen). 1 Station (Bereich oder physische Struktur, die einen oder mehrere Bahnsteige umfasst). 2 Eingang oder Ausgang (Ort, an dem Benutzer eine Station von der Straße aus betreten/verlassen können). 3 Generische Kreuzung (Ort in einer Station, der keinem anderen `location_type`-Wert entspricht). 4 Einstiegsbereich eines bestimmten Ortes auf einem Bahnsteig, an dem Benutzer in ein Fahrzeug ein- / aussteigen können.  - `name`: Der Name dieses Elements.  - `openingHoursSpecification`: Ein strukturierter Wert, der Informationen über die Öffnungszeiten eines Ortes oder einen bestimmten Dienst innerhalb eines Ortes liefert  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `parentStation`: Link zum GTFS-Standard-Repository, der die unterschiedliche Verbindung zwischen Station und Plattform beschreibt [Parent STATION]. Fall '1' location_type = 0 (Haltestelle / Bahnsteig ), das Feld parent_station enthält die ID einer Station. Fall '2' location_type = 1 (Station), dieses Feld muss leer sein. Fall '3' location_type = 2 (Eingang / Ausgang) oder location_type = 3 (generische Kreuzung), das parent_station-Feld enthält die ID einer Station location_type = 1. Fall '4' location_type = 4 (Einstiegsbereich), das parent_station-Feld enthält die ID eines Bahnsteigs.  - `platformCode`: Bahnsteigbezeichner für eine Haltestelle vom Bahnsteig-Typ `location_type` = 0, wenn die Haltestelle in einem Bahnhof liegt.  - `refPointOfInterest`: Ein Verweis auf ein Sonderziel, das mit dieser Beobachtung verbunden ist.  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `stationConnected`: Von dieser Station aus mögliche Verbindungen. Ein strukturierter Wert von 0 bis N Vorkommen, wobei jedes Element eine Zeichenkette im Format `stationType` : [Liste der angeschlossenen Linien, getrennt durch ein Komma] ist. Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'  - `stationType`: Typ der Verkehrsstation. Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'  - `type`: NGSI Entity-Typ. Es muss TransportStation sein  - `webSite`: Link zur offiziellen Website für weitere Informationen...  - `wheelChairAccessible `: Zugang für Person mit eingeschränkter Mobilität möglich. Für Haltestellen ohne Eltern 0 sind keine Informationen über die Zugänglichkeit der Haltestelle verfügbar. 1 einige Fahrzeuge an dieser Haltestelle können einen PMR-Benutzer einsteigen. 2 PRM-Benutzer kann an dieser Haltestelle nicht einsteigen. Für eine Haltestelle, die Teil einer Station ist 0 erbt die Haltestelle das wheelchair_boarding Verhalten der übergeordneten Station, wenn diese ausgefüllt ist. 1 Fahrspuren bieten Rollstuhlzugang zu der Haltestelle / dem Bahnsteig von außerhalb der Station. 2 keine Fahrspur bietet Rollstuhlzugang zur Haltestelle / zum Bahnsteig von außerhalb der Station. Für Stationseingänge / -ausgänge 0 der Stationseingang erbt das wheelchair_boarding-Verhalten der Hauptstation, falls angegeben. 1 der Stationseingang ist rollstuhlgerecht. 2 kein rollstuhlgerechter Weg verbindet den Stationseingang mit den Haltestellen / Bahnsteigen.  - `zoneId`: Preiszone der Station.    
Erforderliche Eigenschaften  
- `dateLastReported`  - `dateObserved`  - `id`  - `location`  - `locationType`  - `stationType`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TransportStation:    
  description: "The data model is a general description of urban stations (Metro, Bus, Tram, Heliport, ...) according to the GFTS standard https://developers.google.com/transit/gtfs/reference/#stopstxt, as well the detailed description of these (means of access, platform, assistance, ...)."    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    contactPoint:    
      description: 'The details to contact with the item.'    
      properties:    
        contactType:    
          type: string    
        email:    
          description: 'Property. Email address of owner.'    
          format: idn-email    
          type: string    
        name:    
          type: string    
        telephone:    
          type: string    
        url:    
          format: uri    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
    contractingAuthority:    
      description: 'Name of the contracting authority.'    
      type: Property    
    contractingCompany:    
      description: 'Name of the contracting company responsible for the exploitation of the station.'    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    dimension:    
      description: 'Global dimension. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meters'    
      properties:    
        depth:    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: Property    
      x-ngsi:    
        units: meters    
    id:    
      anyOf: &transportstation_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    installationMode:    
      description: 'Location  relative to the ground reference. Enum:''aerial, ground, underGround, underSea'''    
      enum:    
        - aerial    
        - ground    
        - underGround    
        - underSea    
      type: Property    
    inventory:    
      description: 'General data mapping only for `locationType` = 0, 1, 3, 4. The format is structured by a sub-property of 4 items.'    
      properties:    
        PlatformType:    
          items:    
            enum:    
              - lateral    
              - central    
            type: string    
          type: array    
        nbOfIOPoint:    
          minimum: 0    
          type: number    
        nbOfLane:    
          minimum: 0    
          type: number    
        nbOfPlatform:    
          minimum: 0    
          type: number    
      type: Property    
    levelId:    
      description: 'Floor on which the location is located. Numerical index associated with the floor. Indicates the relative position of this stage in relation to the others. The index 0 indicates the ground floor. The floors above ground level are indicated by positive indices, and the underground stages by negative indices.'    
      type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    'locationType ':    
      description: 'Link to the GTFS standard repository describing the different location [Location Type]. 0 Stop or platform (place where users get on or off in a public transport vehicle). 1 Station (area or physical structure comprising one or more platforms). 2 Entrance or Exit (place where users can enter / exit a station from the street). 3 Generic intersection (location in a station that doesn''t correspond to any other `location_type` value). 4 Boarding area of a specific location on a platform where users can get on / off in a vehicle.'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            type: string    
          dayOfWeek:    
            enum:    
              - Monday    
              - Tuesday    
              - Wednesday    
              - Thursday    
              - Friday    
              - Saturday    
              - Sunday    
              - PublicHolidays    
            type: string    
          opens:    
            format: time    
            type: string    
          validFrom:    
            format: date-time    
            type: string    
          validThrough:    
            format: date-time    
            type: string    
      minItems: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *transportstation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    parentStation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Link to the GTFS standard repository describing the different link between Station and Platform [Parent STATION]. Case ''1'' location_type = 0 (Stop / platform ), the parent_station field contains the ID of a station. Case ''2'' location_type = 1  (Station), this field must be empty. Case ''3'' location_type = 2 (Input / output) or location_type = 3 (generic intersection), the parent_station field contains the ID of a station location_type = 1. Case ''4'' location_type = 4 (boarding area), the parent_station field contains the ID of a platform.'    
      type: Relationship    
    platformCode:    
      description: 'Platform identifier for a platform type stop `location_type` = 0 when the stop is in a station.'    
      type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to a point of interest associated to this observation.'    
      type: Relationship    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    stationConnected:    
      architect:    
        type: string    
      commissioningDate:    
        format: date-time    
        type: string    
      constructionDate:    
        format: date-time    
        type: string    
      currencyAccepted:    
        items:    
          enum:    
            - EUR    
            - USD    
          type: string    
        type: array    
      description: 'Connections possible from this station. A structured value from 0 to N occurrences where each items is a string in the format `stationType` : [List of Lines connected, separated by a comma]. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'''    
      featuredArtist:    
        items:    
          anyOf:    
            - anyOf: *transportstation_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            - type: string    
        type: array    
      items:    
        properties:    
          'linesConnected ':    
            items:    
              type: string    
            type: array    
          stationType:    
            enum:    
              - aerialLift    
              - bus    
              - cableTram    
              - ferry    
              - funicular    
              - monorail    
              - rail    
              - subway    
              - train    
              - tram    
              - trolleybus    
            type: string    
        type: object    
      paymentAccepted:    
        items:    
          enum:    
            - Cash    
            - CreditCard    
            - CryptoCurrency    
            - other    
          type: string    
        type: array    
      services:    
        properties:    
          defibrillator:    
            type: Boolean    
          emergencyPhone:    
            type: Boolean    
          informationBoardDevice:    
            type: Boolean    
          interactiveDevice:    
            type: Boolean    
          messageDevice:    
            type: Boolean    
          purchaseDevice:    
            type: Boolean    
          restBench:    
            type: Boolean    
          shelters:    
            type: Boolean    
          timetableDevice:    
            type: Boolean    
          voiceDevice:    
            type: Boolean    
          wheelChairAccessible:    
            type: Boolean    
        type: object    
      type: Property    
    stationType:    
      description: 'Type of transport station. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'''    
      items:    
        enum:    
          - aerialLift    
          - bus    
          - cableTram    
          - ferry    
          - funicular    
          - monorail    
          - rail    
          - subway    
          - trolleybus    
          - tram    
        type: string    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be TransportStation'    
      enum:    
        - TransportStation    
      type: Property    
    webSite:    
      description: 'Link to the official website for more information..'    
      type: Property    
    'wheelChairAccessible ':    
      description: 'Access possible for Person with Reduced Mobility. For stops without parents 0 no information is available regarding the accessibility of the stop. 1 some vehicles at this stop can board a PMR user. 2 PRM user cannot board  at this stop. For a stop that is part of a station 0 the stop inherits the wheelchair_boarding behavior of the parent station, if it is filled in. 1 lanes provide wheelchair access to the stop / platform  from outside the station. 2 no lane provides wheelchair access to the stop / platform from outside the station. For station inputs / outputs 0 the station entry inherits the wheelchair_boarding behavior of the main station, if specified. 1 the station entrance is wheelchair accessible. 2 no wheelchair accessible route connects the station entrance to the stops / platforms.'    
      enum:    
        - 0    
        - 1    
        - 2    
      type: Property    
    zoneId:    
      description: 'Pricing zone of the station.'    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - dateLastReported    
    - stationType    
    - locationType    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### TransportStation NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine TransportStation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "Régie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gué / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ]  
}  
```  
#### TransportStation NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine TransportStation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": "Tram"  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07.00",  
        "closes": "22.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08.00",  
        "closes": "23.00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8.30",  
        "closes": "21.00"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8.00",  
        "closes": "21.30"  
      }  
    ],  
    "validFrom": "-01-01",  
    "validThrough": "-31-12"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompany": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "www.lignesdazur.com"  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": "lateral"  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": {  
      "tram": {  
        "type": "Property",  
        "value": [  
          "Tram 2 - CADAM / Nikaia",  
          "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
        ]  
      },  
      "train": {  
        "type": "Property",  
        "value": [  
          "Gare SNCF Nice Saint Augustin (600m)"  
        ]  
      },  
      "bus": {  
        "type": "Property",  
        "value": [  
          "L20 - Giono / Les Pugets",  
          "L20 - Centre Commercial St Isidore",  
          "L21 - Le Gué / Polygone Riviera",  
          "L54 - Centre Commercial Cap 3000 - St Jeannet",  
          "L90 - La Bolline",  
          "91 Auron",  
          "L92 - Isola 2000"  
        ]  
      }  
    }  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architect": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  }  
}  
```  
#### TransportStation NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine TransportStation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": "Tram"  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07.00",  
        "closes": "22.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08.00",  
        "closes": "23.00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8.30",  
        "closes": "21.00"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8.00",  
        "closes": "21.30"  
      }  
    ],  
    "validFrom": "-01-01",  
    "validThrough": "-31-12"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompagny": {  
    "type": "Property",  
    "value": "R\u00e9gie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "www.lignesdazur.com"  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "instalationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": "lateral"  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": {  
      "tram": {  
        "type": "Property",  
        "value": [  
          "Tram 2 - CADAM / Nikaia",  
          "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
        ]  
      },  
      "train": {  
        "type": "Property",  
        "value": [  
          "Gare SNCF Nice Saint Augustin (600m)"  
        ]  
      },  
      "bus": {  
        "type": "Property",  
        "value": [  
          "L20 - Giono / Les Pugets",  
          "L20 - Centre Commercial St Isidore",  
          "L21 - Le Gu\u00e9 / Polygone Riviera",  
          "L54 - Centre Commercial Cap 3000 - St Jeannet",  
          "L90 - La Bolline",  
          "91 Auron",  
          "L92 - Isola 2000"  
        ]  
      }  
    }  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architecte": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### TransportStation NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine TransportStation im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "R\u00e9gie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gu\u00e9 / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht