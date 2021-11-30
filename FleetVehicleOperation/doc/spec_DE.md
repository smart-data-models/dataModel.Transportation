Entität: FleetVehicleOperation  
==============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicleOperation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen Flottenfahrzeugbetriebs, z. B. einer Lieferung oder einer Postabholung. Diese Entität ist in erster Linie mit dem vertikalen Segment des Transport- und Logistiksektors verbunden, kann aber auch für viele andere verwandte IoT-Anwendungen verwendet werden.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `endedAt`: Datum und Uhrzeit des Endes des Ereignisses, wenn bekannt ist, dass das Ereignis oder der Vorgang beendet/abgeschlossen ist. Null/ausgelassen, wenn noch nicht beendet.  - `fleetVehicle`: Verweis auf die FleetVehicle-Entität, auf die sich dieser Vorgang bezieht.  - `fleetVehicleOperation`: Verweis auf die Entität FleetVehicleOperation, auf die sich diese Statusentität bezieht.  - `id`: Eindeutiger Bezeichner der Entität  - `initiatingLocation`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `operationType`: Der Freitexttyp des Ereignisses oder Vorgangs, z. B. Aufruf zu einem Krankentransport, Postabholung, Zustellung, in der Nähe eines Sperrgebiets, Geschwindigkeitsüberschreitung.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `responseTime`: Gibt die Zeit bis zur Reaktion auf ein Ereignis in Sekunden an. Der zugehörige observedAt-Zeitstempel gibt an, wann die letzte Aktualisierung aufgezeichnet wurde. Beispiel: Aufzeichnung der Reaktionszeit eines Krankenwagens bis zum Eintreffen bei einem Patienten  - `result`: Das Endergebnis des Ereignisses oder Vorgangs.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startedAt`: Datum und Uhrzeit, zu der das Ereignis oder der Vorgang ausgelöst wurde.  - `transportTime`: Zeigt die Zeit an, die das Flottenfahrzeug für den Transport von Personen oder Material für den aktuellen Einsatz verwendet hat. So wird z. B. die Zeit angegeben, die ein Krankenwagen mit dem Transport eines Patienten in die Notaufnahme eines Krankenhauses verbracht hat.  - `type`: NGSI-Kennung der Entität. Er muss FleetVehicleOperation lauten.    
Erforderliche Eigenschaften  
- `id`  - `type`    
Dieses Datenmodell stammt aus dem ursprünglichen GSMA IoT-Projekt, https://www.gsma.com/iot/iot-big-data/. Es wurden einige kleinere Anpassungen vorgenommen, um den Anforderungen intelligenter Datenmodelle zu entsprechen.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FleetVehicleOperation:    
  description: 'This entity contains a harmonised description of a generic fleet vehicle operation such as a delivery, or a postal collection. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    endedAt:    
      description: 'The end date and time of the event when the event or operation is known to be over/complete. Null/omitted if not yet ended.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    fleetVehicle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicle entity to which this operation relates.'    
      x-ngsi:    
        type: Relationship    
    fleetVehicleOperation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicleOperation entity to which this status entity relates.'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &fleetvehicleoperation_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    initiatingLocation:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &fleetvehicleoperation_-_properties_-_location_-_oneof    
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
      x-ngsi:    
        type: Geoproperty    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *fleetvehicleoperation_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'The free text type of the event or operation e.g. e.g. Call for a patient transportation, postal collection, delivery, close to a restricted area, overspeed.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *fleetvehicleoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    responseTime:    
      description: 'Indicates the time to respond to an event, in seconds. The associated observedAt timestamp indicates when the last update was recorded. E.g. records the response time for an ambulance to reach to a patient'    
      type: number    
      x-ngsi:    
        type: Property    
        units: seconds    
    result:    
      description: 'The final result of the event or operation.'    
      type: string    
      x-ngsi:    
        type: Property    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startedAt:    
      description: 'The start date and time when the event or operation was triggered.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    transportTime:    
      description: 'Indicates the time that the fleet vehicle has spent transporting people or supplies for the current operation. E.g. indicates the time an ambulance spent transporting a patient to a hospital emergency department.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be FleetVehicleOperation'    
      enum:    
        - FleetVehicleOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicleOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Beispiel-Nutzlasten  
#### FleetVehicleOperation NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine FleetVehicleOperation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleStatus": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286",  
  "initiatingLocation": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "Patient transportation",  
  "description": "An emergency transportation of a 3 year old boy",  
  "result": "Completed",  
  "responseTime": 2500,  
  "transportTime": 1220  
}  
```  
#### FleetVehicleOperation NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine FleetVehicleOperation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleStatus": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286"  
  },  
  "initiatingLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "@value": "2016-08-28T10:18:16Z"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "Patient transportation"  
  },  
  "description": {  
    "type": "Text",  
    "value": "An emergency transportation of a 3 year old boy"  
  },  
  "result": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "responseTime": {  
    "type": "Number",  
    "value": 2500  
  },  
  "transportTime": {  
    "type": "Number",  
    "value": 1220  
  }  
}  
```  
#### FleetVehicleOperation NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine FleetVehicleOperation im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleStatus": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286",  
  "initiatingLocation": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "Patient transportation",  
  "description": "An emergency transportation of a 3 year old boy",  
  "result": "Completed",  
  "responseTime": 2500,  
  "transportTime": 1220  
}  
```  
#### FleetVehicleOperation NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine FleetVehicleOperation im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleStatus": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286"  
  },  
  "initiatingLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "startedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "endedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "operationType": {  
    "type": "Property",  
    "value": "Patient transportation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "An emergency transportation of a 3 year old boy"  
  },  
  "result": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "responseTime": {  
    "type": "Property",  
    "value": 2500,  
    "unitCode": "SEC",  
    "observedAt": "2016-08-28T10:18:16Z"  
  },  
  "transportTime": {  
    "type": "Property",  
    "value": 1220,  
    "unitCode": "SEC",  
    "observedAt": "2016-08-28T10:18:16Z"  
  }  
}  
```  
