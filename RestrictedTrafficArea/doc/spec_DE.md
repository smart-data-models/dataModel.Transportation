<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: RestrictedTrafficArea  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RestrictedTrafficArea/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Allgemeine Beschreibung: **Ein Gebiet in einer Stadt, in dem der von Autos oder anderen Fahrzeugen erzeugte Verkehr eingeschränkt ist.  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Kategorie(n) des eingeschränkten Verkehrsbereichs. Dieses Feld dient der allgemeinen Kennzeichnung von Einheiten des eingeschränkten Verkehrsraums. Besonderheiten und ausführliche Beschreibungen finden sich unter den entsprechenden spezifischen Attributen  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `notAllowedVehicleType[array]`: Fahrzeugtyp(en), die den gesperrten Bereich nicht durchqueren dürfen  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `regulation[uri]`: eine URL, die auf die Verordnung für das betreffende Verkehrsbeschränkungsgebiet verweist  - `restrictionExceptions[array]`: Einzelne Fahrzeugtypen, die den gesperrten Bereich in einem bestimmten Zeitfenster passieren dürfen  - `restrictionValidityHours[string]`: Wochentage und Stunden, an denen die Verkehrsbeschränkung aktiv ist  - `security[array]`: Sicherheitsaspekte, die dieser verkehrsberuhigte Bereich bietet  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `specialRestrictions[array]`: Einzelne Fahrzeugtypen, die die Sperrzone in einem bestimmten Zeitfenster nicht durchqueren dürfen  - `type[string]`: NGSI-Entitätstyp. Es muss RestrictedTrafficArea sein.  - `validityEndDate[date-time]`: Das Datum, an dem die Beschränkung aufgehoben wird  - `validityStartDate[date-time]`: Das Datum, ab dem die Beschränkung angewendet wird  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Datenmodell aus dem Synchronizitätsprojekt  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RestrictedTrafficArea:    
  description: An area of a city in which the traffic generated by cars or any other kind of vehicles is subjected to limitation.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Restricted traffic area''s category(ies). The purpose of this field is to allow to tag, generally speaking, restricted traffic area entities. Particularities and detailed descriptions should be found under the corresponding specific attributes'    
      items:    
        enum:    
          - barrierAccess    
          - forBikes    
          - forCustomers    
          - forDisabled    
          - forElectricalVehicles    
          - forEmployees    
          - forMembers    
          - forPedestrian    
          - forVisitors    
          - forResidents    
          - forStudents    
          - gateAccess    
          - guarded    
          - onlyElectricalVehicles    
          - onlyPedestrian    
          - onlyResident    
          - onlyResidents    
          - onlyWithPermit    
          - private    
          - public    
          - publicPrivate    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    notAllowedVehicleType:    
      description: Vehicle type(s) not allowed to cross the restricted traffic area    
      items:    
        enum:    
          - anyVehicle    
          - agriculturalVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - dieselCarEuro0    
          - dieselCarEuro1    
          - dieselCarEuro2    
          - dieselCarEuro3    
          - dieselCarEuro4    
          - dieselCarEuro5a    
          - dieselCarEuro5b    
          - dieselCarEuro6    
          - freightTransportVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - petrolCarEuro0    
          - petrolCarEuro1    
          - petrolCarEuro2    
          - petrolCarEuro3    
          - petrolCarEuro4    
          - petrolCarEuro5    
          - petrolCarEuro6    
          - tanker    
          - trailer    
          - van    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    regulation:    
      description: A URL pointing to the regulation for the specific restricted traffic area    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    restrictionExceptions:    
      description: Individual vehicle type allowed to cross the restricted traffic area in a specific time slot    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Relationship    
    restrictionValidityHours:    
      description: Days of the week and hours in which the traffic restriction is active    
      type: string    
      x-ngsi:    
        type: Property    
    security:    
      description: Security aspects provided by this restricted traffic area    
      items:    
        enum:    
          - bollard    
          - camera    
          - cctv    
          - dog    
          - externalSecurity    
          - fencesareaSeperatedFromSurroundings    
          - floodLight    
          - guard24hours    
          - lighting    
          - patrolled    
          - securityStaff    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    specialRestrictions:    
      description: Individual vehicle type not allowed to cross the restricted traffic area in a specific time slot    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI Entity type. It has to be RestrictedTrafficArea    
      enum:    
        - RestrictedTrafficArea    
      type: string    
      x-ngsi:    
        type: Property    
    validityEndDate:    
      description: The date at which the restriction is dismissed    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validityStartDate:    
      description: The date from which the restriction is applied    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RestrictedTrafficArea/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RestrictedTrafficArea/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### RestrictedTrafficArea NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein RestrictedTrafficArea im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1",  
  "type": "RestrictedTrafficArea",  
  "category": [  
    "onlyPedestrian"  
  ],  
  "description": "Panel:AP - Stretches:lato civici dispari da piazza Tricolore a via Kramer - Bollards: - Notes:",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      9.214544,  
      45.483353  
    ]  
  },  
  "name": "Corso Concordia Area",  
  "notAllowedVehicleType": [  
    "anyVehicle"  
  ],  
  "regulation": "Decree:54785/2004, Deliberation:425/2004",  
  "source": "https://dati.comune.milano.it/dataset/ds51_trafficotrasporti_aree_pedonali_ztl_zone_30_",  
  "validityEndDate": "2049-12-31T23:00:00.00Z"  
}  
```  
</details>  
#### RestrictedTrafficArea NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine RestrictedTrafficArea im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1",  
  "type": "RestrictedTrafficArea",  
  "category": {  
    "type": "array",  
    "value": [  
      "onlyPedestrian"  
    ]  
  },  
  "description": {  
    "type": "string",  
    "value": "Panel:AP - Stretches:lato civici dispari da piazza Tricolore a via Kramer - Bollards: - Notes:"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        9.214544,  
        45.483353  
      ]  
    }  
  },  
  "name": {  
    "type": "string",  
    "value": "Corso Concordia Area"  
  },  
  "notAllowedVehicleType": {  
    "type": "array",  
    "value": [  
      "anyVehicle"  
    ]  
  },  
  "regulation": {  
    "type": "string",  
    "value": "Decree:54785/2004, Deliberation:425/2004"  
  },  
  "source": {  
    "type": "string",  
    "value": "https://dati.comune.milano.it/dataset/ds51_trafficotrasporti_aree_pedonali_ztl_zone_30_"  
  },  
  "validityEndDate": {  
    "type": "DateTime",  
    "value": "2049-12-31T23:00:00.00Z"  
  }  
}  
```  
</details>  
#### RestrictedTrafficArea NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine RestrictedTrafficArea im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1",  
    "type": "RestrictedTrafficArea",  
    "category": {  
        "type": "array",  
        "value": [  
            "onlyPedestrian"  
        ]  
    },  
    "description": {  
        "type": "string",  
        "value": "Panel:AP - Stretches:lato civici dispari da piazza Tricolore a via Kramer - Bollards: - Notes:"  
    },  
    "location": {  
        "type": "geo:json",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                9.214544,  
                45.483353  
            ]  
        }  
    },  
    "name": {  
        "type": "string",  
        "value": "Corso Concordia Area"  
    },  
    "notAllowedVehicleType": {  
        "type": "array",  
        "value": [  
            "anyVehicle"  
        ]  
    },  
    "regulation": {  
        "type": "string",  
        "value": "Decree:54785/2004, Deliberation:425/2004"  
    },  
    "source": {  
        "type": "string",  
        "value": "https://dati.comune.milano.it/dataset/ds51_trafficotrasporti_aree_pedonali_ztl_zone_30_"  
    },  
    "validityEndDate": {  
        "type": "DateTime",  
        "value": "2049-12-31T23:00:00.00Z"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RestrictedTrafficArea NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine RestrictedTrafficArea im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RestrictedTrafficArea:Milan:RestrictedTrafficAreas:GeoJson:ds51-1",  
    "type": "RestrictedTrafficArea",  
    "category": [  
        "onlyPedestrian"  
    ],  
    "description": "Panel:AP - Stretches:lato civici dispari da piazza Tricolore a via Kramer - Bollards: - Notes:",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            9.214544,  
            45.483353  
        ]  
    },  
    "name": "Corso Concordia Area",  
    "notAllowedVehicleType": [  
        "anyVehicle"  
    ],  
    "regulation": "Decree:54785/2004, Deliberation:425/2004",  
    "source": "https://dati.comune.milano.it/dataset/ds51_trafficotrasporti_aree_pedonali_ztl_zone_30_",  
    "validityEndDate": "2049-12-31T23:00:00.00Z",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
