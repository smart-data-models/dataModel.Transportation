<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: ItemFlowObserved  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell dient der Messung einer Beobachtung im Zusammenhang mit der Bewegung eines Objekts an einem bestimmten Ort und in einem bestimmten Zeitraum. Dieses Datenmodell schlägt eine Weiterentwicklung von zwei Datenmodellen vor, indem es diese zusammenführt und alle Attribute der ursprünglichen Version von [TrafficFlowObserved] und [CrowFlowObserved] und damit jede Art von Objekt integriert, das wir zur Analyse der Bewegungen verwenden wollen. Die Attribute `vehicleType` und `vehicleSubType` werden aus dem ursprünglichen Datenmodell entfernt, um zu generischen `itemType` und `itemSubType` mit möglichen Werten zu werden. (Personen, Fahrzeugtyp, Bootstyp, Flugzeugtyp, ...).**  
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageGapDistance[number]`: Durchschnittlicher Abstand zwischen 2 aufeinanderfolgenden erkannten Elementen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  - `averageHeadwayTime[number]`: Durchschnittliche Vorlaufzeit. Die Abfahrtszeit ist die Zeit, die zwischen zwei aufeinanderfolgenden Sendungen vergeht. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **SEC** für Sekunde  - `averageLength[number]`: Durchschnittliche Länge der entdeckten Objekte, die sich während des Beobachtungszeitraums im Transit befinden. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  - `averageSpeed[number]`: Durchschnittliche Geschwindigkeit der erfassten Objekte, die sich während des Beobachtungszeitraums im Transit befinden. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Je nach Art des Flusses kann der Wert **KMH** f(Fahrzeug, Fußgänger, usw.) für Kilometer pro Stunde (km/h) oder **KNT** für Knoten (Boot) stehen.  - `congested[boolean]`: Zeigt an, ob während des Beobachtungszeitraums auf dem betreffenden Gehweg ein Menschenauflauf stattgefunden hat. Das Fehlen dieses Attributs bedeutet, dass keine Menschenansammlung vorlag.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `dateObserved[date-time]`: Datum der vom Benutzer definierten beobachteten Einheit  - `dateObservedFrom[date-time]`: Beobachtungszeitraum : Startdatum und -zeit im ISO8601 UTC-Format  - `dateObservedTo[date-time]`: Beobachtungszeitraum : Enddatum und -zeit im ISO8601 UTC-Format  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `intensity[number]`: Gesamtzahl der in diesem Beobachtungszeitraum entdeckten Objekte  - `itemSubType[string]`: Verweis auf einen Identifikator eines bestehenden "subType"-Attributs einer NGSI-Entität (Vehicle / BoatType / Person ) oder einer zukünftigen Entität, die einen zu zählenden "subType" auflistet  - `itemType[string]`: Verweis auf einen Bezeichner eines bestehenden Attributs "Typ" einer NGSI-Entität (Fahrzeug / Bootstyp / Person) oder einer künftigen Entität, die einen zu zählenden "Typ" enthält. Enum:'Personen, Schiffe, Fahrzeuge, Yachten'.  - `laneDirection[string]`: Übliche Fahrtrichtung auf dem von dieser Beobachtung betroffenen Fahrstreifen. Dieses Attribut ist nützlich, wenn sich die Beobachtung nicht auf einen Straßenabschnitt bezieht, so dass die Fahrtrichtung des beobachteten Verkehrsflusses ermittelt werden kann. Siehe RoadSegment für eine Beschreibung der Semantik dieser Werte  - `laneId[number]`: Fahrspur-Bezeichner. Die Identifizierung der Fahrspur erfolgt anhand der von der RoadSegment-Entität definierten Konventionen, die auf [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right) beruhen.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `occupancy[number]`: Anteil der Beobachtungszeit, in der ein Gegenstand die beobachtete Spur belegt hat  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refDevice[*]`: Das Gerät oder die Geräte, die zur Gewinnung der in diesem Datensatz enthaltenen Daten verwendet wurden  - `refRoadSegment[*]`: Betroffener Straßenabschnitt, auf dem die Beobachtung gemacht wurde  - `reversedLane[boolean]`: Zeigt an, ob der Verkehr auf dem Fahrstreifen während des Beobachtungszeitraums umgekehrt wurde. Das Fehlen dieses Attributs bedeutet, dass keine Fahrspurumkehr stattfand.  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `speedMax[number]`: Während des Beobachtungszeitraums ermittelte Höchstgeschwindigkeit. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Je nach Art des Flusses kann der Wert **KMH** (Fahrzeug, Fußgänger, ...) für Kilometer pro Stunde (km/h) oder **KNT** für Knoten (Boot) stehen.  - `speedMin[number]`: Während des Beobachtungszeitraums festgestellte Mindestgeschwindigkeit. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Je nach Art des Flusses kann der Wert **KMH** (Fahrzeug, Fußgänger, ...) für Kilometer pro Stunde (km/h) oder **KNT** für Knoten (Boot) stehen.  - `type[string]`: NGSI-Entitätstyp. Es muss ItemFlowObserved sein  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `dateObserved`  - `id`  - `laneId`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ItemFlowObserved:    
  description: 'The data model intended to measure an observation linked to the movement of an item at a certain location and over a given period. This Data Model proposes an evolution of two Data Model by merging them and integrating all the attributes of the initial version of [TrafficFlowObserved] and [CrowFlowObserved] and by extension any type of item that we want to analyze the movements. Attributes `vehicleType` and `vehicleSubType` are removed from the initial data Model in order to become generic `itemType` and `itemSubType` of possible values. (people, Type of vehicle, Type of boat, Type of plane, ...).'    
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
    averageGapDistance:    
      description: 'Average gap distance between consecutive 2 detected items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageHeadwayTime:    
      description: 'Average headway time. Head away time is the time elapsed between two consecutive items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageLength:    
      description: 'Average length of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageSpeed:    
      description: 'Average speed of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** f(vehicule, pedestrian, etc.) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    congested:    
      description: Flags whether there was a crowd congestion during the observation period in the referred walkway. The absence of this attribute means no crowd congestion    
      type: boolean    
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
    dateObserved:    
      description: Date of the observed entity defined by the user    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format'    
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
    intensity:    
      description: Total number of items detected during this observation period    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    itemSubType:    
      description: Reference to an identifier of an existing 'subType' attribute of an NGSI entity (Vehicle / BoatType / Person ) or of a future entity listing an item 'subType' to be counted    
      type: string    
      x-ngsi:    
        type: Property    
    itemType:    
      description: 'Reference to an identifier of an existing ''Type'' attribute of an NGSI entity (Vehicle / BoatType / Person) or of a future entity listing an item ''Type'' to be counted. Enum:''people, ship, vehicle, yacht'''    
      enum:    
        - people    
        - ship    
        - vehicle    
        - yacht    
      type: string    
      x-ngsi:    
        type: Property    
    laneDirection:    
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. See RoadSegment for a description of the semantics of these values'    
      enum:    
        - forward    
        - backward    
        - inbound    
        - outbound    
        - right    
        - left    
      type: string    
      x-ngsi:    
        type: Property    
    laneId:    
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right)'    
      min: 1    
      type: number    
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
    occupancy:    
      description: Fraction of the observation time where a item has been occupying the observed lane    
      maximum: 1    
      minimum: 0    
      type: number    
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
    refDevice:    
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
      description: The device or devices used to obtain the data expressed by this record    
      x-ngsi:    
        type: Relationship    
    refRoadSegment:    
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
      description: Concerned road segment on which the observation has been made    
      x-ngsi:    
        type: Relationship    
    reversedLane:    
      description: Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion    
      type: boolean    
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
    speedMax:    
      description: 'Maximum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    speedMin:    
      description: 'Minimum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ItemFlowObserved    
      enum:    
        - ItemFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - laneId    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Transportation/ItemFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### ItemFlowObserved NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen ItemFlowObserved im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
  "type": "ItemFlowObserved",  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Port Lympia"  
  },  
  "areaServed": "Nice Harbor",  
  "averageGapDistance": 35.28,  
  "averageHeadwayTime": 156,  
  "averageLength": 7.44,  
  "averageSpeed": 2.7,  
  "congested": false,  
  "dateObserved": "2020-03-20T16:30:00Z",  
  "dateObservedFrom": "2020-03-20T16:30:00Z",  
  "dateObservedTo": "2020-03-20T22:30:00Z",  
  "description": "Boat Flow Observed from Nice Harbor.",  
  "itemSubType": "monoHull",  
  "itemType": "yacht",  
  "intensity": 12,  
  "laneDirection": "outbound",  
  "laneId": 1,  
  "location": {  
    "coordinates": [  
      7.196545,  
      43.664809  
    ],  
    "type": "Point"  
  },  
  "maxSpeed": 3.8,  
  "minSpeed": 2.6,  
  "name": "BFO-NCE-MNCA-SP-001",  
  "occupancy": 0.1562,  
  "refDevice": "Device:BFO-NCE-MNCA-SP-001-Dev-02",  
  "reverseLane": false  
}  
```  
</details>  
#### ItemFlowObserved NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein ItemFlowObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
  "type": "ItemFlowObserved",  
  "name": {  
    "type": "Text",  
    "value": "BFO-NCE-MNCA-SP-001"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Boat Flow Observed from Nice Harbor."  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.196545,  
        43.664809  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Port Lympia",  
      "addressLocality": "Nice",  
      "addressCountry": "FR"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Harbor"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-20T16:30:00Z"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2020-03-20T16:30:00Z"  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2020-03-20T22:30:00Z"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "Device:BFO-NCE-MNCA-SP-001-Dev-02"  
  },  
  "itemType": {  
    "type": "Text",  
    "value": "yacht"  
  },  
  "itemSubType": {  
    "type": "Text",  
    "value": "monoHull"  
  },  
  "laneId": {  
    "type": "Integer",  
    "value": 1  
  },  
  "laneDirection": {  
    "type": "Text",  
    "value": "outbound"  
  },  
  "reverseLane": {  
    "type": "Boolean",  
    "value": false  
  },  
  "intensity": {  
    "type": "Number",  
    "value": 12  
  },  
  "occupancy": {  
    "type": "Number",  
    "value": 0.1562  
  },  
  "congested": {  
    "type": "Boolean",  
    "value": false  
  },  
  "averageSpeed": {  
    "type": "Number",  
    "value": 2.7  
  },  
  "averageLength": {  
    "type": "Number",  
    "value": 7.44  
  },  
  "averageHeadwayTime": {  
    "type": "Number",  
    "value": 156  
  },  
  "averageGapDistance": {  
    "type": "Number",  
    "value": 35.28  
  },  
  "minSpeed": {  
    "type": "Number",  
    "value": 2.6  
  },  
  "maxSpeed": {  
    "type": "Number",  
    "value": 3.8  
  }  
}  
```  
</details>  
#### ItemFlowObserved NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen ItemFlowObserved im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "itemFlowObserved:BFO-NCE-MNCA-SP-001",  
    "type": "ItemFlowObserved",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Port Lympia"  
    },  
    "areaServed": "Nice Harbor",  
    "averageGapDistance": 35.28,  
    "averageHeadwayTime": 156,  
    "averageLength": 7.44,  
    "averageSpeed": 2.7,  
    "congested": false,  
    "dateObserved": "2020-03-20T16:30:00Z",  
    "dateObservedFrom": "2020-03-20T16:30:00Z",  
    "dateObservedTo": "2020-03-20T22:30:00Z",  
    "description": "Boat Flow Observed from Nice Harbor.",  
    "intensity": 12,  
    "itemSubtype": "monoHull",  
    "itemType": "yacht",  
    "laneDirection": "outbound",  
    "laneId": 1,  
    "location": {  
        "coordinates": [  
            7.196545,  
            43.664809  
        ],  
        "type": "Point"  
    },  
    "maxSpeed": 3.8,  
    "minSpeed": 2.6,  
    "name": "BFO-NCE-MNCA-SP-001",  
    "occupancy": 0.1562,  
    "refDevice": "Device:BFO-NCE-MNCA-SP-001-Dev-02",  
    "reverseLane": false,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### ItemFlowObserved NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein ItemFlowObserved im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
    "type": "ItemFlowObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Port Lympia",  
            "addressLocality": "Nice",  
            "addressCountry": "FR"  
        }  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Harbor"  
    },  
    "averageGapDistance": {  
        "type": "Property",  
        "value": 35.28,  
        "unitCode": "MTR"  
    },  
    "averageHeadwayTime": {  
        "type": "Property",  
        "value": 156,  
        "unitCode": "SEC"  
    },  
    "averageLength": {  
        "type": "Property",  
        "value": 7.44,  
        "unitCode": "MTR"  
    },  
    "averageSpeed": {  
        "type": "Property",  
        "value": 2.7,  
        "unitCode": "KNT"  
    },  
    "congested": {  
        "type": "Property",  
        "value": false  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T16:30:00Z"  
        }  
    },  
    "dateObservedFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T16:30:00Z"  
        }  
    },  
    "dateObservedTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-03-20T22:30:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Boat Flow Observed from Nice Harbor."  
    },  
    "intensity": {  
        "type": "Property",  
        "value": 12  
    },  
    "itemSubType": {  
        "type": "Property",  
        "value": "monoHull"  
    },  
    "itemType": {  
        "type": "Property",  
        "value": "yatching"  
    },  
    "laneDirection": {  
        "type": "Property",  
        "value": "outbound"  
    },  
    "laneId": {  
        "type": "Property",  
        "value": 1  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                7.196545,  
                43.664809  
            ]  
        }  
    },  
    "maxSpeed": {  
        "type": "Property",  
        "value": 3.8,  
        "unitCode": "KNT"  
    },  
    "minSpeed": {  
        "type": "Property",  
        "value": 2.6,  
        "unitCode": "KNT"  
    },  
    "name": {  
        "type": "Property",  
        "value": "BFO-NCE-MNCA-SP-001"  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.1562  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:BFO-NCE-MNCA-SP-001-Dev-02"  
    },  
    "reverseLane": {  
        "type": "Property",  
        "value": false  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
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
