Entität: FareCollectionSystem  
=============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FareCollectionSystem/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

## Liste der Eigenschaften  

Erforderliche Eigenschaften  
- Keine erforderlichen Eigenschaften  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FareCollectionSystem:    
  description: 'A public transit fare collection system Data Model'    
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
    cardId:    
      description: 'Unique ticket Id of the transaction or Id of the smart card used in the transaction.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    currentTripCount:    
      description: 'The current count of trips made by the vehicle corresponding to this observation on the given day of operation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    destinationStopCategory:    
      description: 'Type of the destination bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopId:    
      description: 'Unique Id of the bus stop at which the passenger deboards from the bus corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopName:    
      description: 'The name of the destination bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    direction_id:    
      description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    entryAreaCode:    
      description: 'Area code of the passenger boarding stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or brts stop or other service type stop etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentCompanyCode:    
      description: 'Company/Agency code for the transaction equipment (used by fare collection agency). For example, 103 - CBS (city bus service),102 - BRTS etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentId:    
      description: 'Unique Id of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentSequenceNumber:    
      description: 'Sequence number for the given equipment.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    equipmentStopId:    
      description: 'Stop Id (BRTS) at which the equipment corresponding to this transaction is installed.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentType:    
      description: 'Type of equipment or the name of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentTypeCode:    
      description: 'Unique code indicating the type of equipment used in the transaction (used by fare collection agency).ENUM [1B, 42, 02, 08, 41] 1B - POS, 42 - HTT, 02- Mobile, 08- Fare Gate, 41- Pole Validator'    
      enum:    
        - 1B    
        - 42    
        - 02    
        - 08    
        - 41    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    exitAreaCode:    
      description: 'Area code of the passenger alighting stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or BRTS stop or other service type stop etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fareForAdult:    
      description: 'The fare for an adult in the journey corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fareForChild:    
      description: 'The fare for a child in the journey corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &farecollectionsystem_-_properties_-_owner_-_items_-_anyof    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    occupancyLevel:    
      description: 'Occupancy level in the public transit bus corresponding to this observation. ''Red'' indicates the congestion level in the bus is HIGH, ''Yellow'' indicates the congestion level in the bus is MODERATE and ''Green'' indicates the congestion level in the bus is LOW.'    
      enum:    
        - Red    
        - Yellow    
        - Green    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originDestinationCode:    
      description: 'The code for the origin and destination stops corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopCategory:    
      description: 'Type of the origin bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopId:    
      description: 'Unique Id of the bus stop at which the passenger boards into the bus corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopName:    
      description: 'The name of the origin bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *farecollectionsystem_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    passengerCount:    
      description: 'Number of passengers travelling in the public transit bus corresponding to this observation. This count is computed based on the realtime ticketing transactions in the public transit bus.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    route_id:    
      description: "Route Id assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    shiftOfOperation:    
      description: 'Shift of operation of the public transit vehicle operated by the fare collection agency/ public transit agency or the employee corresponding to this observation. Indicated as ''1'' when the vehicle operates in the first shift, ''2'' when the vehicle operates in the second shift and ''3'' when the vehicle operates in the third shift.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    stage:    
      description: 'Total number of stages from the origin bus stop to the destination bus stop.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ticketTypeCode:    
      description: 'Unique ticket type code of the corresponding trip.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionDateTime:    
      description: 'Date-time of the transaction corresponding to this observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionType:    
      description: 'Type of the transaction corresponding to this observation. For Eg - Issue, ReIssue, Entry, Exit etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionTypeDescription:    
      description: 'Description of the transaction type. Explanation of various transactionTypeId codes used in the data.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionVehicleNum:    
      description: 'Code used by fare collection agency for the vehicle number corresponding to the transaction.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    travelDistance:    
      description: 'The distance between the origin bus stop and the destination bus stop corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trip_id:    
      description: "Trip Id/Trip name alloted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be FareCollectionSystem'    
      enum:    
        - FareCollectionSystem    
      type: string    
      x-ngsi:    
        type: Property    
    vehicle_label:    
      description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required: []    
  type: object    
  version: 0.0.1    
```  
</details>    
## Beispiel-Nutzlasten  
#### FareCollectionSystem NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein FareCollectionSystem im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "addressRegion": "Provenza-Alpes-Costa Azul",  
    "postOfficeBoxNumber": "",  
    "postalCode": "06000",  
    "streetAddress": "Av. Nicolas II"  
  },  
  "alternateName": "",  
  "areaServed": "Nice",  
  "cardId": "987201910",  
  "currentTripCount": 12,  
  "dataProvider": "",  
  "dateCreated": "2020-11-02T06:16:42Z",  
  "dateModified": "2020-12-27T15:13:17Z",  
  "description": "Fare collection system Nize for regional routes",  
  "destinationStopCategory": "Airport",  
  "destinationStopId": "Nice-Airport",  
  "destinationStopName": "Hour risk somebody deal system discussion other plan. Stage the film occur.",  
  "direction_id": 1,  
  "entryAreaCode": "city-bus-service",  
  "equipmentCompanyCode": "103",  
  "equipmentId": "S23",  
  "equipmentSequenceNumber": 2,  
  "equipmentStopId": "BRTS-Sen-23",  
  "equipmentType": "Entry sensor",  
  "equipmentTypeCode": "42",  
  "exitAreaCode": "city-bus-service",  
  "fareForAdult": 4.5,  
  "fareForChild": 3.6,  
  "location": {  
    "coordinates": [  
      43.7034,  
      7.2663  
    ],  
    "type": "Point"  
  },  
  "name": "Fare collection system Nize",  
  "observationDateTime": "1988-12-24T07:06:19Z",  
  "occupancyLevel": "Green",  
  "originDestinationCode": "23",  
  "originStopCategory": "Bus stop",  
  "originStopId": "9",  
  "originStopName": "Vauban",  
  "owner": [  
    "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
    "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
  ],  
  "passengerCount": 6,  
  "route_id": "4",  
  "seeAlso": [  
    "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
    "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
  ],  
  "shiftOfOperation": "2",  
  "source": "",  
  "stage": 4,  
  "ticketTypeCode": "Normal",  
  "transactionDateTime": "2021-08-20T15:45:22Z",  
  "transactionType": "Issue",  
  "transactionTypeDescription": "Regular Fare.",  
  "transactionTypeId": "2401",  
  "transactionVehicleNum": 23,  
  "travelDistance": 7.5,  
  "trip_id": "4A",  
  "vehicle_label": "5821JZS"  
}  
```  
Nicht verfügbar ist das Beispiel eines FareCollectionSystem im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
#### FareCollectionSystem NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein FareCollectionSystem im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "addressRegion": "Provenza-Alpes-Costa Azul",  
    "postOfficeBoxNumber": "",  
    "postalCode": "06000",  
    "streetAddress": "Av. Nicolas II"  
  },  
  "alternateName": "",  
  "areaServed": "Nice",  
  "cardId": "987201910",  
  "currentTripCount": 12,  
  "dataProvider": "",  
  "dateCreated": "2020-11-02T06:16:42Z",  
  "dateModified": "2020-12-27T15:13:17Z",  
  "description": "Fare collection system Nize for regional routes",  
  "destinationStopCategory": "Airport",  
  "destinationStopId": "Nice-Airport",  
  "destinationStopName": "Hour risk somebody deal system discussion other plan. Stage the film occur.",  
  "direction_id": 1,  
  "entryAreaCode": "city-bus-service",  
  "equipmentCompanyCode": "103",  
  "equipmentId": "S23",  
  "equipmentSequenceNumber": 2,  
  "equipmentStopId": "BRTS-Sen-23",  
  "equipmentType": "Entry sensor",  
  "equipmentTypeCode": "42",  
  "exitAreaCode": "city-bus-service",  
  "fareForAdult": 4.5,  
  "fareForChild": 3.6,  
  "location": {  
    "coordinates": [  
      43.7034,  
      7.2663  
    ],  
    "type": "Point"  
  },  
  "name": "Fare collection system Nize",  
  "observationDateTime": "1988-12-24T07:06:19Z",  
  "occupancyLevel": "Green",  
  "originDestinationCode": "23",  
  "originStopCategory": "Bus stop",  
  "originStopId": "9",  
  "originStopName": "Vauban",  
  "owner": [  
    "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
    "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
  ],  
  "passengerCount": 6,  
  "route_id": "4",  
  "seeAlso": [  
    "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
    "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
  ],  
  "shiftOfOperation": "2",  
  "source": "",  
  "stage": 4,  
  "ticketTypeCode": "Normal",  
  "transactionDateTime": "2021-08-20T15:45:22Z",  
  "transactionType": "Issue",  
  "transactionTypeDescription": "Regular Fare.",  
  "transactionTypeId": "2401",  
  "transactionVehicleNum": 23,  
  "travelDistance": 7.5,  
  "trip_id": "4A",  
  "vehicle_label": "5821JZS",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### FareCollectionSystem NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein FareCollectionSystem im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-11-02T06:16:42Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-27T15:13:17Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "Fare collection system Nize"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "Fare collection system Nize for regional routes"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
      "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
      "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.7034,  
        7.2663  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Av. Nicolas II",  
      "addressLocality": "Nice",  
      "addressRegion": "Provenza-Alpes-Costa Azul",  
      "addressCountry": "France",  
      "postalCode": "06000",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice"  
  },  
  "destinationStopName": {  
    "type": "Property",  
    "value": "Hour risk somebody deal system discussion other plan. Stage the film occur."  
  },  
  "occupancyLevel": {  
    "type": "Property",  
    "value": "Green"  
  },  
  "travelDistance": {  
    "type": "Property",  
    "value": 7.5  
  },  
  "passengerCount": {  
    "type": "Property",  
    "value": 6  
  },  
  "transactionType": {  
    "type": "Property",  
    "value": "Issue"  
  },  
  "ticketTypeCode": {  
    "type": "Property",  
    "value": "Normal"  
  },  
  "originStopName": {  
    "type": "Property",  
    "value": "Vauban"  
  },  
  "entryAreaCode": {  
    "type": "Property",  
    "value": "city-bus-service"  
  },  
  "cardId": {  
    "type": "Property",  
    "value": "987201910"  
  },  
  "transactionTypeId": {  
    "type": "Property",  
    "value": "2401"  
  },  
  "stage": {  
    "type": "Property",  
    "value": 4  
  },  
  "equipmentId": {  
    "type": "Property",  
    "value": "S23"  
  },  
  "direction_id": {  
    "type": "Property",  
    "value": 1  
  },  
  "equipmentSequenceNumber": {  
    "type": "Property",  
    "value": 2  
  },  
  "shiftOfOperation": {  
    "type": "Property",  
    "value": "2"  
  },  
  "route_id": {  
    "type": "Property",  
    "value": "4"  
  },  
  "trip_id": {  
    "type": "Property",  
    "value": "4A"  
  },  
  "originStopCategory": {  
    "type": "Property",  
    "value": "Bus stop"  
  },  
  "vehicle_label": {  
    "type": "Property",  
    "value": "5821JZS"  
  },  
  "fareForChild": {  
    "type": "Property",  
    "value": 3.6  
  },  
  "transactionDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-08-20T15:45:22Z"  
    }  
  },  
  "destinationStopId": {  
    "type": "Property",  
    "value": "Nice-Airport"  
  },  
  "originDestinationCode": {  
    "type": "Property",  
    "value": "23"  
  },  
  "currentTripCount": {  
    "type": "Property",  
    "value": 12  
  },  
  "equipmentTypeCode": {  
    "type": "Property",  
    "value": "42"  
  },  
  "destinationStopCategory": {  
    "type": "Property",  
    "value": "Airport"  
  },  
  "transactionVehicleNum": {  
    "type": "Property",  
    "value": 23  
  },  
  "fareForAdult": {  
    "type": "Property",  
    "value": 4.5  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1988-12-24T07:06:19Z"  
    }  
  },  
  "equipmentCompanyCode": {  
    "type": "Property",  
    "value": "103"  
  },  
  "transactionTypeDescription": {  
    "type": "Property",  
    "value": "Regular Fare."  
  },  
  "exitAreaCode": {  
    "type": "Property",  
    "value": "city-bus-service"  
  },  
  "equipmentType": {  
    "type": "Property",  
    "value": "Entry sensor"  
  },  
  "equipmentStopId": {  
    "type": "Property",  
    "value": "BRTS-Sen-23"  
  },  
  "originStopId": {  
    "type": "Property",  
    "value": "9"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht