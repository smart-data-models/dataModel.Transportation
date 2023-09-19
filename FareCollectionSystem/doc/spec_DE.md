<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: FareCollectionSystem  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/FareCollectionSystem/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Ein Fahrgeldmanagementsystem für den öffentlichen Nahverkehr Datenmodell**  
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `cardId[string]`: Eindeutige Ticket-ID der Transaktion oder ID der bei der Transaktion verwendeten Smartcard  . Model: [https://schema.org/Text](https://schema.org/Text)- `currentTripCount[number]`: Die aktuelle Anzahl der Fahrten, die von dem Fahrzeug, das dieser Beobachtung entspricht, an dem jeweiligen Betriebstag durchgeführt wurden  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `destinationStopCategory[string]`: Typ der dieser Beobachtung entsprechenden Zielhaltestelle  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationStopId[string]`: Eindeutige Kennung der Haltestelle, an der der Fahrgast aus dem Bus aussteigt, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationStopName[string]`: Der Name der Zielhaltestelle, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction_id[number]`: Gibt die Fahrtrichtung des Fahrzeugs an, das dieser Beobachtung entspricht; kann aus dem statischen GTFS-Feed trips.txt entnommen werden. Gleich wie: Feld "direction_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Number](https://schema.org/Number)- `entryAreaCode[string]`: Gebietscode der Haltestelle, an der der Fahrgast einsteigt (wird von der Fahrgeldeinzugszentrale verwendet). Zum Beispiel, ob es sich um eine Stadtbus-Haltestelle, eine Haltestelle der Busse oder eine andere Haltestelle handelt usw.  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentCompanyCode[string]`: Unternehmens-/Agenturcode für das Transaktionsgerät (verwendet von der Fahrgeldeinzugszentrale). Zum Beispiel 103 - CBS (Stadtbusdienst), 102 - BRTS usw.  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentId[string]`: Eindeutige Kennung des Geräts, das dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentSequenceNumber[number]`: Laufende Nummer für das angegebene Gerät  . Model: [https://schema.org/Number](https://schema.org/Number)- `equipmentStopId[string]`: Haltestellennummer (BRTS), an der das dieser Transaktion entsprechende Gerät installiert ist  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentType[string]`: Typ des Geräts oder Name des Geräts, das dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentTypeCode[string]`: Eindeutiger Code, der die Art des bei der Transaktion verwendeten Geräts angibt (von der Fahrpreisagentur verwendet).ENUM [1B, 42, 02, 08, 41] 1B - POS, 42 - HTT, 02- Mobile, 08- Fare Gate, 41- Pole Validator  . Model: [https://schema.org/Text](https://schema.org/Text)- `exitAreaCode[string]`: Gebietscode der Haltestelle, an der der Fahrgast aussteigt (wird von der Fahrgeldeinzugszentrale verwendet). Zum Beispiel, ob es sich um eine Stadtbus-Haltestelle, eine BRTS-Haltestelle oder eine andere Haltestelle handelt usw.  . Model: [https://schema.org/Text](https://schema.org/Text)- `fareForAdult[number]`: Der Fahrpreis für einen Erwachsenen auf der Reise, die dieser Beobachtung entspricht  . Model: [https://schema.org/Number](https://schema.org/Number)- `fareForChild[number]`: Der Fahrpreis für ein Kind auf der Reise, die dieser Beobachtung entspricht  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `observationDateTime[date-time]`: Letzter gemeldeter Zeitpunkt der Beobachtung  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancyLevel[string]`: Auslastung des Busses im öffentlichen Nahverkehr entsprechend dieser Beobachtung. Rot" bedeutet, dass die Überlastung des Busses HOCH ist, "Gelb" bedeutet, dass die Überlastung des Busses MÄSSIG ist und "Grün" bedeutet, dass die Überlastung des Busses NIEDRIG ist.  . Model: [https://schema.org/Text](https://schema.org/Text)- `originDestinationCode[string]`: Der dieser Beobachtung entsprechende Code für die Ausgangs- und Zielhaltestelle  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopCategory[string]`: Typ der Ursprungshaltestelle, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopId[string]`: Eindeutige Kennung der Bushaltestelle, an der der Fahrgast in den Bus einsteigt, der dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopName[string]`: Der Name der Bushaltestelle, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `passengerCount[number]`: Anzahl der Fahrgäste im Linienbus, die mit dieser Beobachtung übereinstimmen. Diese Zahl wird auf der Grundlage der Echtzeit-Ticket-Transaktionen im Linienbus errechnet  . Model: [https://schema.org/Number](https://schema.org/Number)- `route_id[string]`: Strecken-ID, die der Strecke zugeordnet ist, auf der der Bus/das Fahrzeug, der/das dem Bus in dieser Beobachtung entspricht, derzeit fährt. SameAs: Feld "route_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `shiftOfOperation[string]`: Betriebsschicht des von der Fahrgeldeinzugszentrale/dem Verkehrsunternehmen oder dem Arbeitnehmer betriebenen ÖPNV-Fahrzeugs, die dieser Beobachtung entspricht. Angegeben als "1", wenn das Fahrzeug in der ersten Schicht eingesetzt wird, "2", wenn das Fahrzeug in der zweiten Schicht eingesetzt wird und "3", wenn das Fahrzeug in der dritten Schicht eingesetzt wird.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `stage[number]`: Gesamtzahl der Etappen von der Ausgangsbushaltestelle bis zur Zielhaltestelle  . Model: [https://schema.org/Number](https://schema.org/Number)- `ticketTypeCode[string]`: Eindeutiger Ticket-Typ-Code der entsprechenden Reise  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionDateTime[date-time]`: Datum und Uhrzeit der Transaktion, die dieser Beobachtung entspricht  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionType[string]`: Art der Transaktion, die dieser Beobachtung entspricht. Zum Beispiel - Ausgabe, Neuausgabe, Zugang, Abgang usw.  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionTypeDescription[string]`: Beschreibung der Transaktionsart. Erläuterung der verschiedenen in den Daten verwendeten transactionTypeId-Codes  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionVehicleNum[number]`: Von der Gebühreneinzugszentrale verwendeter Code für die der Transaktion entsprechende Fahrzeugnummer  . Model: [https://schema.org/Number](https://schema.org/Number)- `travelDistance[number]`: Die Entfernung zwischen der Ausgangshaltestelle und der Zielhaltestelle, die dieser Beobachtung entspricht  . Model: [https://schema.org/Number](https://schema.org/Number)- `trip_id[string]`: Fahrtennummer/Fahrtenname, die dem Bus, der dieser Beobachtung entspricht, unter Berücksichtigung der Tageszeit und der Fahrtrichtung auf der angegebenen routeId zugewiesen werden. SameAs: Feld "trip_id" aus GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss FareCollectionSystem sein.  - `vehicle_label[string]`: Vom Benutzer sichtbare Kennzeichnung, d.h. etwas, das dem Fahrgast gezeigt werden muss, um das richtige Fahrzeug zu identifizieren. SameAs: Feld "label" aus GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FareCollectionSystem:    
  description: A public transit fare collection system Data Model    
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
    cardId:    
      description: Unique ticket Id of the transaction or Id of the smart card used in the transaction    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    currentTripCount:    
      description: The current count of trips made by the vehicle corresponding to this observation on the given day of operation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    destinationStopCategory:    
      description: Type of the destination bus stop corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopId:    
      description: Unique Id of the bus stop at which the passenger deboards from the bus corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopName:    
      description: The name of the destination bus stop corresponding to this observation    
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
      description: 'Area code of the passenger boarding stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or brts stop or other service type stop etc'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentCompanyCode:    
      description: 'Company/Agency code for the transaction equipment (used by fare collection agency). For example, 103 - CBS (city bus service),102 - BRTS etc'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentId:    
      description: Unique Id of the equipment corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentSequenceNumber:    
      description: Sequence number for the given equipment    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    equipmentStopId:    
      description: Stop Id (BRTS) at which the equipment corresponding to this transaction is installed    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentType:    
      description: Type of equipment or the name of the equipment corresponding to this observation    
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
      description: 'Area code of the passenger alighting stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or BRTS stop or other service type stop etc'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fareForAdult:    
      description: The fare for an adult in the journey corresponding to this observation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fareForChild:    
      description: The fare for a child in the journey corresponding to this observation    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    occupancyLevel:    
      description: 'Occupancy level in the public transit bus corresponding to this observation. ''Red'' indicates the congestion level in the bus is HIGH, ''Yellow'' indicates the congestion level in the bus is MODERATE and ''Green'' indicates the congestion level in the bus is LOW'    
      enum:    
        - Red    
        - Yellow    
        - Green    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originDestinationCode:    
      description: The code for the origin and destination stops corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopCategory:    
      description: Type of the origin bus stop corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopId:    
      description: Unique Id of the bus stop at which the passenger boards into the bus corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopName:    
      description: The name of the origin bus stop corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    passengerCount:    
      description: Number of passengers travelling in the public transit bus corresponding to this observation. This count is computed based on the realtime ticketing transactions in the public transit bus    
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
    shiftOfOperation:    
      description: 'Shift of operation of the public transit vehicle operated by the fare collection agency/ public transit agency or the employee corresponding to this observation. Indicated as ''1'' when the vehicle operates in the first shift, ''2'' when the vehicle operates in the second shift and ''3'' when the vehicle operates in the third shift'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stage:    
      description: Total number of stages from the origin bus stop to the destination bus stop    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ticketTypeCode:    
      description: Unique ticket type code of the corresponding trip    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionDateTime:    
      description: Date-time of the transaction corresponding to this observation    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionType:    
      description: 'Type of the transaction corresponding to this observation. For Eg - Issue, ReIssue, Entry, Exit etc'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionTypeDescription:    
      description: Description of the transaction type. Explanation of various transactionTypeId codes used in the data    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionVehicleNum:    
      description: Code used by fare collection agency for the vehicle number corresponding to the transaction    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    travelDistance:    
      description: The distance between the origin bus stop and the destination bus stop corresponding to this observation    
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
      description: NGSI entity type. It has to be FareCollectionSystem    
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
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FareCollectionSystem/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FareCollectionSystem/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### FareCollectionSystem NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein FareCollectionSystem im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### FareCollectionSystem NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein FareCollectionSystem im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2020-11-02T06:16:42Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2020-12-27T15:13:17Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Fare collection system Nize"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Fare collection system Nize for regional routes"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
      "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
      "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.7034,  
        7.2663  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
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
    "type": "Text",  
    "value": "Nice"  
  },  
  "destinationStopName": {  
    "type": "Text",  
    "value": "Hour risk somebody deal system discussion other plan. Stage the film occur."  
  },  
  "occupancyLevel": {  
    "type": "Text",  
    "value": "Green"  
  },  
  "travelDistance": {  
    "type": "number",  
    "value": 7.5  
  },  
  "passengerCount": {  
    "type": "number",  
    "value": 6  
  },  
  "transactionType": {  
    "type": "Text",  
    "value": "Issue"  
  },  
  "ticketTypeCode": {  
    "type": "Text",  
    "value": "Normal"  
  },  
  "originStopName": {  
    "type": "Text",  
    "value": "Vauban"  
  },  
  "entryAreaCode": {  
    "type": "Text",  
    "value": "city-bus-service"  
  },  
  "cardId": {  
    "type": "Text",  
    "value": "987201910"  
  },  
  "transactionTypeId": {  
    "type": "Text",  
    "value": "2401"  
  },  
  "stage": {  
    "type": "number",  
    "value": 4  
  },  
  "equipmentId": {  
    "type": "Text",  
    "value": "S23"  
  },  
  "direction_id": {  
    "type": "number",  
    "value": 1  
  },  
  "equipmentSequenceNumber": {  
    "type": "number",  
    "value": 2  
  },  
  "shiftOfOperation": {  
    "type": "Text",  
    "value": "2"  
  },  
  "route_id": {  
    "type": "Text",  
    "value": "4"  
  },  
  "trip_id": {  
    "type": "Text",  
    "value": "4A"  
  },  
  "originStopCategory": {  
    "type": "Text",  
    "value": "Bus stop"  
  },  
  "vehicle_label": {  
    "type": "Text",  
    "value": "5821JZS"  
  },  
  "fareForChild": {  
    "type": "number",  
    "value": 3.6  
  },  
  "transactionDateTime": {  
    "type": "DateTime",  
    "value":  "2021-08-20T15:45:22Z"  
  },  
  "destinationStopId": {  
    "type": "Text",  
    "value": "Nice-Airport"  
  },  
  "originDestinationCode": {  
    "type": "Text",  
    "value": "23"  
  },  
  "currentTripCount": {  
    "type": "number",  
    "value": 12  
  },  
  "equipmentTypeCode": {  
    "type": "Text",  
    "value": "42"  
  },  
  "destinationStopCategory": {  
    "type": "Text",  
    "value": "Airport"  
  },  
  "transactionVehicleNum": {  
    "type": "number",  
    "value": 23  
  },  
  "fareForAdult": {  
    "type": "number",  
    "value": 4.5  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "1988-12-24T07:06:19Z"  
  },  
  "equipmentCompanyCode": {  
    "type": "Text",  
    "value": "103"  
  },  
  "transactionTypeDescription": {  
    "type": "Text",  
    "value": "Regular Fare."  
  },  
  "exitAreaCode": {  
    "type": "Text",  
    "value": "city-bus-service"  
  },  
  "equipmentType": {  
    "type": "Text",  
    "value": "Entry sensor"  
  },  
  "equipmentStopId": {  
    "type": "Text",  
    "value": "BRTS-Sen-23"  
  },  
  "originStopId": {  
    "type": "Text",  
    "value": "9"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### FareCollectionSystem NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein FareCollectionSystem im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### FareCollectionSystem NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein FareCollectionSystem im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
    "type": "FareCollectionSystem",  
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
    "alternateName": {  
        "type": "Property",  
        "value": ""  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice"  
    },  
    "cardId": {  
        "type": "Property",  
        "value": "987201910"  
    },  
    "currentTripCount": {  
        "type": "Property",  
        "value": 12  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": ""  
    },  
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
    "description": {  
        "type": "Property",  
        "value": "Fare collection system Nize for regional routes"  
    },  
    "destinationStopCategory": {  
        "type": "Property",  
        "value": "Airport"  
    },  
    "destinationStopId": {  
        "type": "Property",  
        "value": "Nice-Airport"  
    },  
    "destinationStopName": {  
        "type": "Property",  
        "value": "Hour risk somebody deal system discussion other plan. Stage the film occur."  
    },  
    "direction_id": {  
        "type": "Property",  
        "value": 1  
    },  
    "entryAreaCode": {  
        "type": "Property",  
        "value": "city-bus-service"  
    },  
    "equipmentCompanyCode": {  
        "type": "Property",  
        "value": "103"  
    },  
    "equipmentId": {  
        "type": "Property",  
        "value": "S23"  
    },  
    "equipmentSequenceNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "equipmentStopId": {  
        "type": "Property",  
        "value": "BRTS-Sen-23"  
    },  
    "equipmentType": {  
        "type": "Property",  
        "value": "Entry sensor"  
    },  
    "equipmentTypeCode": {  
        "type": "Property",  
        "value": "42"  
    },  
    "exitAreaCode": {  
        "type": "Property",  
        "value": "city-bus-service"  
    },  
    "fareForAdult": {  
        "type": "Property",  
        "value": 4.5  
    },  
    "fareForChild": {  
        "type": "Property",  
        "value": 3.6  
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
    "name": {  
        "type": "Property",  
        "value": "Fare collection system Nize"  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1988-12-24T07:06:19Z"  
        }  
    },  
    "occupancyLevel": {  
        "type": "Property",  
        "value": "Green"  
    },  
    "originDestinationCode": {  
        "type": "Property",  
        "value": "23"  
    },  
    "originStopCategory": {  
        "type": "Property",  
        "value": "Bus stop"  
    },  
    "originStopId": {  
        "type": "Property",  
        "value": "9"  
    },  
    "originStopName": {  
        "type": "Property",  
        "value": "Vauban"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
            "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
        ]  
    },  
    "passengerCount": {  
        "type": "Property",  
        "value": 6  
    },  
    "route_id": {  
        "type": "Property",  
        "value": "4"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
            "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
        ]  
    },  
    "shiftOfOperation": {  
        "type": "Property",  
        "value": "2"  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "stage": {  
        "type": "Property",  
        "value": 4  
    },  
    "ticketTypeCode": {  
        "type": "Property",  
        "value": "Normal"  
    },  
    "transactionDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-08-20T15:45:22Z"  
        }  
    },  
    "transactionType": {  
        "type": "Property",  
        "value": "Issue"  
    },  
    "transactionTypeDescription": {  
        "type": "Property",  
        "value": "Regular Fare."  
    },  
    "transactionTypeId": {  
        "type": "Property",  
        "value": "2401"  
    },  
    "transactionVehicleNum": {  
        "type": "Property",  
        "value": 23  
    },  
    "travelDistance": {  
        "type": "Property",  
        "value": 7.5  
    },  
    "trip_id": {  
        "type": "Property",  
        "value": "4A"  
    },  
    "vehicle_label": {  
        "type": "Property",  
        "value": "5821JZS"  
    },  
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
