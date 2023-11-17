<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: APDSObservation    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/APDSObservation/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Entität modelliert eine bestimmte Beobachtung eines Satzes von ANPR-Kameras. Die Beobachtung kann mit mehreren ANPR-Kameras durchgeführt werden, ist aber auf die Beobachtung EINES Fahrzeugs beschränkt. Sie implementiert das APDS-Datenmodell https://www.allianceforparkingdatastandards.org/**    
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
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße      
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `creator[string]`: Id des aktuellen Fahrers.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `images[array]`: Array von Links zu Bildern. Das Array-Element enthält die URLs der Bilder und zusätzliche Informationen. Alternativ zur Bild-URL kann auch das Bild selbst in das binaryContent-Attribut aufgenommen werden.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `observationDateTime[date-time]`: Der Zeitstempel, an dem die Beobachtung gemacht wurde (UTC). Obligatorisch, wenn observationStartDateTime und observationEndDateTime nicht verwendet werden.  - `observationEndDateTime[date-time]`: Datum und Uhrzeit des Endes des Beobachtungsereignisses (in UTC) (z. B. wurde beobachtet, wie ein Fahrzeug um 9:33 Uhr eine Lieferzone verließ). Obligatorisch, wenn creationDateTime nicht verwendet wird.  - `observationStartDateTime[date-time]`: Datum und Uhrzeit des Beginns des Beobachtungsereignisses (in UTC) (z. B. wurde ein Auto beobachtet, das um 8:01 Uhr in eine Lieferzone einfuhr). Obligatorisch, wenn creationDateTime nicht verwendet wird.  - `observedCredentialCharacterConfidence[array]`: Die Zuverlässigkeit der Erkennung einzelner Zeichen. Wie bei observedCredentialConfidence ist dies herstellerspezifisch. Verwenden Sie die Metadaten, um anzugeben, wie die Konfidenzwerte interpretiert werden können.  - `observedCredentialConfidence[number]`: Das allgemeine Vertrauen in die Messung. Sie kann herstellerspezifisch sein, sollte aber immer auf einen Wert zwischen 0 und 1 skaliert werden. Verwenden Sie die Metadaten, um anzugeben, wie diese Zahl zu interpretieren ist. Arvoo: Bereich[0.0, 1.0] (höher ist besser).  - `observedCredentialCountry[string]`: Ländercode nach dem zweistelligen ISO3166-Standard (https://www.iban.com/country-codes). Es ist zu beachten, dass der internationale Fahrzeugzulassungscode nicht verwendet werden sollte, um Mehrdeutigkeiten zu vermeiden (https://en.wikipedia.org/wiki/International_vehicle_registration_code). Konnte der Ländercode nicht ermittelt werden, ist für dieses Attribut "XX" zu verwenden.  - `observedCredentialId[string]`: Spezifischer Identifikator für den referenzierten beobachteten Berechtigungsnachweis. Der Berechtigungsnachweis wird durch observedCredentialType angegeben und kann ein RFID-Tag, eine Ticketnummer von einem Kassenautomaten, ein Nummernschild usw. sein. Im Falle eines Nummernschildes sind nur alphanumerische Werte (keine Leerzeichen oder Bindestriche) zulässig. Optional kann ein ':' verwendet werden, um z. B. die Position des deutschen Stadtsiegels anzugeben (https://www.europeanplates.com/information/german-city-codes.html).  - `observedCredentialType[string]`: Typ des in der Beobachtung referenzierten Credentials. Die zulässigen Werte sind im APDS CredentialType angegeben. Enum:'barcode, bluetooth, eticket, hangtag, licensePlate, permit, qrCode, rfid, ticket, other'  - `observedHeading[*]`: Bezeichnet die Fahrtrichtung des Beobachters und wird in Dezimalgraden angegeben, wobei 0 <= "Fahrtrichtung" < 360, im Uhrzeigersinn relativ zum wahren Norden gezählt wird; wenn das Fahrzeug steht (d. h. der Wert des Attributs "Geschwindigkeit" ist "0"), muss der Wert des Attributs "Fahrtrichtung" gleich "-1" sein. (UN-Code DD)  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedLocation`:   	- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)    
	- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein      
- `observedLocationPDOP[number]`: Genauigkeit der GPS-Position des beobachteten Fahrzeugs. Dies wird als "Positionsverdünnung der Genauigkeit" ausgedrückt (https: //de.wikipedia.org/wiki/Dilution_of_precision_(navigation)). (UN-Code "MTR").  - `observedMethod[string]`: Die für dieses Beobachtungselement aufgezeichnete Beobachtungsmethode gemäß der Definition von APDS (ObservationType). Enum:'anpr, Kreide, visuell, Scanner, rfTranspoder, andere'  - `observedSpeed[*]`: Bezeichnet die Größe der horizontalen Komponente der aktuellen Geschwindigkeit des beobachteten Fahrzeugs und wird in Kilometern pro Stunde angegeben. Falls angegeben, muss der Wert des Attributs "Geschwindigkeit" eine nicht negative reelle Zahl sein. '-1' KANN verwendet werden, wenn die Geschwindigkeit aus irgendeinem Grund vorübergehend unbekannt ist. (UN-Code KMH).  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedVehicleColour[string]`: Die Farbe des beobachteten Fahrzeugs  - `observedVehicleMake[string]`: Die Marke des beobachteten Fahrzeugs  - `observedVehicleType[string]`: Fahrzeugtyp unter dem Gesichtspunkt seiner strukturellen Merkmale. Dies ist etwas anderes als die Fahrzeugklasse. Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, MotorradMitSeitenwagen, Motorroller, Kehrmaschine, Tankwagen, Dreiradfahrzeug, Anhänger, Straßenbahn, Zweiradfahrzeug, Draisine, Lieferwagen, FahrzeugOhneKatalysator, FahrzeugMitWohnwagen, FahrzeugMitAnhänger, mitGeradeNummernKennzeichen, mitUngeradeNummernKennzeichen, Sonstiges". Die folgenden Werte, die durch _VehicleTypeEnum_ und _VehicleTypeEnum2_, [DATEX 2 Version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) definiert und für andere Verwendungen erweitert wurden  . Model: [https://schema.org/Text](https://schema.org/Text)- `observer[string]`: Der Name oder die Kennung des Scansystems, das die in diesem Beobachtungselement aufgezeichnete Beobachtung vornimmt.  - `observerCameras[array]`: Die erste Kamera in der Liste hat die beste Erkennungsleistung. Verwenden Sie die folgenden Abkürzungen, um die Kamerapositionierung an einem Fahrzeug anzugeben: RF(Rechts vorne), RM(Rechts Mitte), RB(Rechts hinten), LF(Links vorne), LM(Links Mitte), LB(Links hinten).  - `observerDescription[string]`: Freitextbeschreibung für Details der Beobachtung oder des Beobachters. Kann z. B. als freundlicher Name für ein bestimmtes ANPR-Scanfahrzeug verwendet werden.  - `observerHeading[*]`: Bezeichnet die Fahrtrichtung des Beobachters und wird in Dezimalgraden angegeben, wobei 0 <= "Richtung" < 360, im Uhrzeigersinn relativ zum wahren Norden gezählt wird. Wenn das Fahrzeug steht (d. h. der Wert des Attributs "Geschwindigkeit" ist "0"), muss der Wert des Attributs "Richtung" gleich "-1" sein.  . Model: [https://schema.org/Number](https://schema.org/Number)- `observerLocation`:   	- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)    
	- `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein      
- `observerLocationPDOP[number]`: Genauigkeit der GPS-Position des Beobachters, ausgedrückt als 'Position Dilution Of Precision'(https: //de.wikipedia.org/wiki/Dilution_of_precision_(navigation))  - `observerSpeed[*]`: Bezeichnet die Größe der horizontalen Komponente der aktuellen Geschwindigkeit des Beobachters und wird in Kilometern pro Stunde angegeben. Falls angegeben, muss der Wert des Attributs speed eine nicht negative reelle Zahl sein. Der Wert '-1' KANN verwendet werden, wenn die Geschwindigkeit aus irgendeinem Grund vorübergehend unbekannt ist.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `towardsObserver[number]`: 1: Beobachtetes Fahrzeug bewegt sich in Richtung der Kamera, 0: Beobachtetes Fahrzeug entfernt sich von der Kamera, -1: Die Richtung des beobachteten Fahrzeugs wird nicht erkannt.  - `type[string]`: NGSI-Entitätstyp. Es muss APDSObservation sein.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Dieses Modell erfasst den Datensatz einer Beobachtung eines Fahrzeugs zu einem bestimmten Zeitpunkt an einem bestimmten Ort. Es ist von der APDS (Alliance for Parking DataStandard) Spezifikation abgeleitet. Die Beobachtungsmethode umfasst die Verwendung von ALPR-Kameras, visuelle Beobachtung, Scanner oder jede andere Art der Beobachtung.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
APDSObservation:      
  description: 'This entity models a particular observation of a set of ANPR camera. The Observation might be done with several ANPR cameras, but is limited to the observation of ONE vehicle. It implements the APDS data model https://www.allianceforparkingdatastandards.org/'      
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
    creator:      
      description: Id of current driver.      
      type: string      
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
    images:      
      description: 'Array of links to images. The array element contain the URLs of the images and additional info. As an alternative to the images URL, the image itself can be included in the binaryContent attribute.'      
      items:      
        items:      
          description: Every element in the array of images      
          properties:      
            URL:      
              description: Uri of the image      
              format: uri      
              type: string      
              x-ngsi:      
                type: Property      
            binaryContent:      
              description: Binary format of the image content      
              format: uuencoded      
              type: string      
              x-ngsi:      
                type: Property      
            camId:      
              description: Identifier of the camera. It can be specified by the camera position (also used in the 'camera' attribute)      
              type: string      
              x-ngsi:      
                type: Property      
            distance:      
              description: The distance in meters from the observer      
              type: number      
              x-ngsi:      
                type: Property      
                units: meters      
            expiryDateTime:      
              description: Timestamp until which the URL is valid      
              format: date-time      
              type: string      
              x-ngsi:      
                type: Property      
            imageContent:      
              description: It specifies the content of the image      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        type: array      
      type: array      
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
      description: The timestamp the Observation was made (UTC). Mandatory if observationStartDateTime and observationEndDateTime are not used.      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    observationEndDateTime:      
      description: 'The date and time of the observation event ended(in UTC).(e.g.a car was observed to exit a delivery zone at 9: 33am). Mandatory if creationDateTime is not used.'      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    observationStartDateTime:      
      description: 'The date and time of the observation(in UTC)event started.(e.g.a car was observed to enter a delivery zone at 8: 01am). Mandatory if creationDateTime is not used.'      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    observedCredentialCharacterConfidence:      
      description: The confidence of individual character recognition. As with observedCredentialConfidence this is vendor specific. Use the metadata to indicate how the confidences can be interpreted.      
      items:      
        description: Every observation of the credential character confidence      
        maximum: 1      
        minimum: 0      
        type: number      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    observedCredentialConfidence:      
      description: 'The overall confidence of the measurement. This can be vendor specific, but should always be rescaled to value between 0 en 1. Use the metadata to indicate how this number should be interpreted. Arvoo: range[0.0, 1.0](higher is better).'      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    observedCredentialCountry:      
      description: 'Country Code following the 2 character ISO3166 standard (https://www.iban.com/country-codes). Note that the International vehicle registration code should not be used to avoid ambiguity (https://en.wikipedia.org/wiki/International_vehicle_registration_code). If the country-code could not be determined, set ''XX'' as for this attribute.'      
      type: string      
      x-ngsi:      
        type: Property      
    observedCredentialId:      
      description: 'Specific identifier to the referenced observed credential. The credential is specified by observedCredentialType and may be an RFID tag, ticket number from a paystation, license plate number, etc. In case of a licensePlate only alpha numerical values (no spaces or hyphens) are allowed. Optionally an '':'' can be used to indicate the position of e.g. the German City Seal (https://www.europeanplates.com/information/german-city-codes.html).'      
      type: string      
      x-ngsi:      
        type: Property      
    observedCredentialType:      
      description: 'Type of the credential referenced within  the observation. Allowed values are specified in the APDS CredentialType. Enum:''barcode, bluetooth, eticket, hangtag, licensePlate, permit, qrCode, rfid, ticket, other'''      
      enum:      
        - barcode      
        - bluetooth      
        - eticket      
        - hangtag      
        - licensePlate      
        - permit      
        - qrCode      
        - rfid      
        - ticket      
        - other      
      type: string      
      x-ngsi:      
        type: Property      
    observedHeading:      
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north.If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1''. (UN code DD)'      
      oneOf:      
        - exclusiveMaximum: 360      
          maximum: 360      
          minimum: 0      
          type: number      
        - enum:      
            - -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Degrees      
    observedLocation:      
      description: GPS position of the middle position of the scanned vehicle.      
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
        areaServed:      
          description: The geographic area where a service or offered item is provided      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        location:      
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
          oneOf:      
            - bbox:      
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
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type:      
                enum:      
                  - Polygon      
                type: string      
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 2      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiLineString      
                type: string      
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 4      
                    type: array      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiPolygon      
                type: string      
          x-ngsi:      
            type: GeoProperty      
      type: object      
      x-ngsi:      
        type: GeoProperty      
    observedLocationPDOP:      
      description: 'Accuracy of GPS position of the observed vehicle. This is expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation)). (UN code ''MTR''). '      
      type: number      
      x-ngsi:      
        type: Property      
        units: meters      
    observedMethod:      
      description: 'The method of observation recorded for this observation element as defined by APDS (ObservationType). Enum:''anpr, chalk, visual, scanner, rfTranspoder, other'''      
      enum:      
        - anpr      
        - chalk      
        - other      
        - rfTranspoder      
        - scanner      
        - visual      
      type: string      
      x-ngsi:      
        type: Property      
    observedSpeed:      
      description: 'Denotes the magnitude of the horizontal component of the observed vehicles current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number.''-1'' MAY be used if speed is transiently unknown for some reason. (UN Code KMH).'      
      oneOf:      
        - minimum: 0      
          type: number      
        - maximum: -1      
          minimum: -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: km/h      
    observedVehicleColour:      
      description: The colour of the observed vehicle      
      type: string      
      x-ngsi:      
        type: Property      
    observedVehicleMake:      
      description: The make of the observed vehicle      
      type: string      
      x-ngsi:      
        type: Property      
    observedVehicleType:      
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses'      
      enum:      
        - agriculturalVehicle      
        - ambulance      
        - anyVehicle      
        - articulatedVehicle      
        - autorickshaw      
        - bicycle      
        - binTrolley      
        - BRT mini busÂ·      
        - BRT bus      
        - bus      
        - car      
        - caravan      
        - carOrLightVehicle      
        - carWithCaravan      
        - carWithTrailer      
        - cleaningTrolley      
        - compactor      
        - constructionOrMaintenanceVehicle      
        - dumper      
        - e-moped      
        - e-scooter      
        - e-motorcycle      
        - fireTender      
        - fourWheelDrive      
        - highSidedVehicle      
        - hopper      
        - lorry      
        - minibus      
        - moped      
        - motorcycle      
        - motorcycleWithSideCar      
        - motorscooter      
        - policeVan      
        - publicMotor      
        - sweepingMachine      
        - tanker      
        - tempo      
        - threeWheeledVehicle      
        - tipper      
        - trailer      
        - tram      
        - trolley      
        - twoWheeledVehicle      
        - van      
        - vehicleWithoutCatalyticConverter      
        - vehicleWithCaravan      
        - vehicleWithTrailer      
        - withEvenNumberedRegistrationPlates      
        - withOddNumberedRegistrationPlates      
        - other      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    observer:      
      description: The name or identification of the scanning system making the observation recorded in this observation element.      
      type: string      
      x-ngsi:      
        type: Property      
    observerCameras:      
      description: 'Array of camera positions that detected the vehicle.The first camera in the list has the best recognition.Use the following abbreviations to indicate the camera positioning on a car: RF(Right Front), RM(Right Middle), RB(Right Back), LF(Left Front), LM(Left Middle), LB(Left Back).'      
      items:      
        description: Every camera position      
        type: string      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    observerDescription:      
      description: Free-text description for details of the observation or observer. Can e.g.be used as a friendly name of a specific ANPR scan car.      
      type: string      
      x-ngsi:      
        type: Property      
    observerHeading:      
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north. If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1'''      
      oneOf:      
        - exclusiveMaximum: 360      
          maximum: 360      
          minimum: 0      
          type: number      
        - enum:      
            - -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Degree.      
    observerLocation:      
      description: GPS position of the person or car equipped with the Camera/s that produce the observation.      
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
        areaServed:      
          description: The geographic area where a service or offered item is provided      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        location:      
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
          oneOf:      
            - bbox:      
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
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type:      
                enum:      
                  - Polygon      
                type: string      
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 2      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiLineString      
                type: string      
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 4      
                    type: array      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiPolygon      
                type: string      
          x-ngsi:      
            type: GeoProperty      
      type: object      
      x-ngsi:      
        type: GeoProperty      
    observerLocationPDOP:      
      description: 'Accuracy of the GPS position of the observer, expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation))'      
      type: number      
      x-ngsi:      
        type: Property      
        units: meters.      
    observerSpeed:      
      description: 'Denotes the magnitude of the horizontal component of the observer current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number. ''-1'' MAY be used if speed is transiently unknown for some reason'      
      oneOf:      
        - minimum: 0      
          type: number      
        - maximum: -1      
          minimum: -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: 'KMH '      
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
    towardsObserver:      
      description: '1: Observed vehicle moves in direction of camera, 0: Observed vehicle moves away direction of camera, -1: Observed vehicle direction not detected.'      
      enum:      
        - -1      
        - 0      
        - 1      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be APDSObservation      
      enum:      
        - APDSObservation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://www.allianceforparkingdatastandards.org/      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/APDSObservation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/APDSObservation/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### APDSObservation NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine APDSObservation im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
  "type": "APDSObservation",  
  "creator": "25399",  
  "images": [  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "ANPR"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Overview"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Plate"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Panorama"  
      },  
      {  
        "distance": -5.22  
      }  
    ]  
  ],  
  "observationDateTime": "2020-09-11T10:45:00.00Z",  
  "observedCredentialCharacterConfidence": [  
    0.944,  
    0.851,  
    0.876,  
    0.95,  
    0.932,  
    0.936,  
    0.901  
  ],  
  "observedCredentialConfidence": 0.851,  
  "observedCredentialCountry": "BE",  
  "observedCredentialId": "1ENC003",  
  "observedCredentialType": "licensePlate",  
  "observedHeading": 175,  
  "observedLocation": {  
    "coordinates": [  
      4.00412077,  
      51.00216632  
    ],  
    "type": "Point"  
  },  
  "observedLocationPDOP": 0.2959945752,  
  "observedMethod": "anpr",  
  "observedSpeed": -1,  
  "observer": "Arvoo",  
  "observerCameras": [  
    "LF,LB"  
  ],  
  "observerDescription": "Scangenius Auto-26",  
  "observerHeading": 175,  
  "observerLocation": {  
    "coordinates": [  
      4.412077,  
      51.216632  
    ],  
    "type": "Point"  
  },  
  "observerLocationPDOP": 0.2959945752,  
  "observerSpeed": 26  
}  
```  
</details>    
#### APDSObservation NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für eine APDSObservation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Text",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Text",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Text",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Text",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Number",  
		"value": 0.851,  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo. Higher is better."  
			}  
		}  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "array",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		],  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo"  
			}  
		}  
	},  
	"observer": {  
		"type": "Text",  
		"value": "Arvoo",  
		"metadata": {}  
	},  
	"observerDescription": {  
		"type": "Text",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Text",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Array",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "DateTime",  
		"value": "2020-09-11T10:45:00.00Z"  
	},  
	"observerLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observerHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Number",  
		"value": 26,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "KMH"  
			}  
		}  
	},  
	"observedLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observedHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Number",  
		"value": -1  
	},  
	"images": {  
		"type": "array",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	}  
}  
```  
</details>    
#### APDSObservation NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine APDSObservation im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
  "type": "APDSObservation",  
  "creator": "25399",  
  "images": [  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "ANPR"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Overview"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Plate"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Panorama"  
      },  
      {  
        "distance": -5.22  
      }  
    ]  
  ],  
  "observationDateTime": "2020-09-11T10:45:00.00Z",  
  "observedCredentialCharacterConfidence": [  
    0.944,  
    0.851,  
    0.876,  
    0.95,  
    0.932,  
    0.936,  
    0.901  
  ],  
  "observedCredentialConfidence": 0.851,  
  "observedCredentialCountry": "BE",  
  "observedCredentialId": "1ENC003",  
  "observedCredentialType": "licensePlate",  
  "observedHeading": 175,  
  "observedLocation": {  
    "coordinates": [  
      4.00412077,  
      51.00216632  
    ],  
    "type": "Point"  
  },  
  "observedLocationPDOP": 0.2959945752,  
  "observedMethod": "anpr",  
  "observedSpeed": -1,  
  "observer": "Arvoo",  
  "observerCameras": [  
    "LF,LB"  
  ],  
  "observerDescription": "Scangenius Auto-26",  
  "observerHeading": 175,  
  "observerLocation": {  
    "coordinates": [  
      4.412077,  
      51.216632  
    ],  
    "type": "Point"  
  },  
  "observerLocationPDOP": 0.2959945752,  
  "observerSpeed": 26,  
  "@context": [  
    "https://raw.githubusercontent.com/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### APDSObservation NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für eine APDSObservation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Property",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Property",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Property",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Property",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Property",  
		"value": 0.851  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "Property",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		]  
	},  
	"observer": {  
		"type": "Property",  
		"value": "Arvoo"  
	},  
	"observerDescription": {  
		"type": "Property",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Property",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Property",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "Property",  
		"value": {  
			"@type": "DateTime",  
			"@value": "2020-09-11T10:45:00.00Z"  
		}  
	},  
	"observerLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observerHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Property",  
		"value": 26  
	},  
	"observedLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observedHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Property",  
		"value": -1  
	},  
	"images": {  
		"type": "Property",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	},  
	 "@context": [  
        ""  
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
