<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entität: OriginDestinationFlow  
=============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/OriginDestinationFlow/LICENSE.md)  

[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Stündliche Beobachtung der Bewegungsflüsse von Besuchern zwischen Herkunfts- und Zielgemeinden, aufgeschlüsselt nach Nationalität. Jede Entität stellt die Flusszahl zwischen zwei Orten während eines bestimmten Stundenintervalls dar.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Liste der Eigenschaften  


<sup><sub>[*] Wenn es in einem Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>  
- `address[object]`: Die Postadresse  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: Die Ortschaft, in der die Straßenadresse ist und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: Die Region, in der die Ortschaft liegt und die im Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird  
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: Die Straßenadresse  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Hausnummer, die eine bestimmte Liegenschaft auf einer öffentlichen Straße identifiziert  
- `aggregationDateType[string]`: Art der Datum-Aggregation (z. B. stündlich, täglich, monatlich)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  
- `areaServed[string]`: Das geografische Gebiet, in dem ein Dienst oder ein angebotenes Produkt bereitgestellt wird  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `countryCode[string]`: Ursprungslandcode, der den Personen zugeordnet ist, die mit dem Datenfluss in Verbindung stehen, z. B. ES, IT, FR usw.  
- `dataProvider[string]`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Datenentität identifiziert  
- `dateCreated[date-time]`: Zeitstempel für die Erstellung der Entität. Dieser wird in der Regel von der Speicherplattform zugewiesen  
- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform zugewiesen  
- `dateObserved[date-time]`: Datum und Uhrzeit der Beobachtung im ISO-8601-Format  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: Eine Beschreibung dieses Artikels  
- `destinationLocation[*]`: Geojson-Referenz zum Artikel. Es kann Punkt, Linienzug, Polygon, MultiPunkt, MultiLinienzug oder MultiPolygon sein  
- `destinationLocationCode[string]`: Offizieller Code der Zielgemeinde  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `destinationLocationName[string]`: Name der Zielgemeinde  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `flowCount[number]`: Gesamtzahl der Bewegungen/Flüsse zwischen Ursprung und Ziel während dieser Stunde  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `flowType[string]`: Art des Flusses. Enum: 'Tourismus, Pendeln, Geschäft, Migration, gemischt'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: Stunde des Tages (0-23) für diese Beobachtung  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: Eindeutiger Identifikator der Entität  
- `location[*]`: Geojson-Verweis auf das Element. Es kann Punkt, Linienzug, Polygon, MultiPunkt, MultiLinienzug oder MultiPolygon sein  
- `name[string]`: Der Name dieses Artikels  
- `nationality[string]`: Staatsangehörigkeit der Besucher, die die Bewegung ausführen. ISO-3166-1-Alpha-2-Ländercode (z. B. ES, FR, GB, PT, DE)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: Vollständiger Name des Nationalitätslandes (optional, für bessere Lesbarkeit)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `originLocation[*]`: Geojson-Referenz zum Artikel. Es kann Punkt, Linienzug, Polygon, MultiPunkt, MultiLinienzug oder MultiPolygon sein  
- `originLocationCode[string]`: Offizieller Code der Ursprungsgemeinde  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `originLocationName[string]`: Name der Ursprungsgemeinde  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: Eine Liste, die eine JSON-kodierte Zeichenfolge enthält, die auf die eindeutigen IDs des/die Eigentümer(s) verweist  
- `seeAlso[*]`: Liste von URIs, die auf zusätzliche Ressourcen über das Element verweisen  
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL zum Quellobjekt zu verwenden.  
- `type[string]`: NGSI-Entitätentyp. Es muss OriginDestinationFlow sein  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Erforderliche Eigenschaften  
- `id`  
- `Typ`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Datenmodellbeschreibung von Eigenschaften  

Sortiert alphabetisch (Klicken für Details)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
OriginDestinationFlow:    
  description: Hourly observation of visitor movement flows between origin and destination municipalities, segmented by nationality. Each entity represents the flow count between two locations during a specific hour.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    aggregationDateType:    
      description: Type of date aggregation (e.g., hourly, daily, monthly)    
      type: string    
      x-ngsi:    
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
    countryCode:    
      description: Origin country code associated to the people associated to the flow, eg. ES, IT, FR, etc...    
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
    dateObserved:    
      description: Date and time of the observation in ISO 8601 format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    destinationLocation:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    destinationLocationCode:    
      description: Official code of the destination municipality    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationLocationName:    
      description: Name of the destination municipality    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    flowCount:    
      description: Total number of movements/flows between origin and destination during this hour    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: movements    
    flowType:    
      description: Type of flow. Enum:'tourism, commuting, business, migration, mixed'    
      enum:    
        - tourism    
        - commuting    
        - business    
        - migration    
        - mixed    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hour:    
      description: Hour of the day (0-23) for this observation    
      maximum: 23    
      minimum: 0    
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
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    nationality:    
      description: Nationality of visitors making the movement. ISO 3166-1 alpha-2 country code (e.g., ES, FR, GB, PT, DE)    
      pattern: ^[A-Z]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    nationalityName:    
      description: Full name of the nationality country (optional, for human readability)    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originLocation:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    originLocationCode:    
      description: Official code of the origin municipality    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originLocationName:    
      description: Name of the origin municipality    
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
          type: Relationship    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be OriginDestinationFlow    
      enum:    
        - OriginDestinationFlow    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/OriginDestinationFlow/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/OriginDestinationFlow/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Beispielnutzlasten  

#### UrsprungZielFluss NGSI-v2 Schlüsselwerte Beispiel  

Hier ist ein Beispiel für einen OriginDestinationFlow im JSON-Format als Schlüssel-Werte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "OriginDestinationFlow:PT:CO0101:CO0102:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": "2024-12-31T10:30:00.00Z",  
  "aggregationDateType": "hourly",  
  "hour": 10,  
  "originLocationCode": "CO0101",  
  "originLocationName": "Coimbra",  
  "destinationLocationCode": "CO0102",  
  "destinationLocationName": "Figueira da Foz",  
  "nationality": "DE",  
  "nationalityName": "Germany",  
  "flowCount": 145,  
  "flowType": "tourism",  
  "countryCode": "PT",  
  "originLocation": {  
    "type": "Point",  
    "coordinates": [-8.4103, 40.2033]  
  },  
  "destinationLocation": {  
    "type": "Point",  
    "coordinates": [-8.8618, 40.1508]  
  },  
  "description": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00",  
  "source": "MobilityDataPlatform",  
  "dateCreated": "2024-12-31T11:00:00.00Z",  
  "dateModified": "2024-12-31T11:00:00.00Z"  
}  
```  
</details>  

#### UrsprungZielFluss NGSI-v2 normalisiertes Beispiel  

Hier ist ein Beispiel für einen OriginDestinationFlow im JSON-Format als normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und gibt die Kontextdaten einer einzelnen Entität zurück.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:OriginDestinationFlow:PT:CO0101:CO0102:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2024-12-31T10:30:00.00Z"  
  },  
  "aggregationDateType": {  
    "type": "Text",  
    "value": "hourly"  
  },  
  "hour": {  
    "type": "Number",  
    "value": 10  
  },  
  "originLocationCode": {  
    "type": "Text",  
    "value": "CO0101"  
  },  
  "originLocationName": {  
    "type": "Text",  
    "value": "Coimbra"  
  },  
  "destinationLocationCode": {  
    "type": "Text",  
    "value": "CO0102"  
  },  
  "destinationLocationName": {  
    "type": "Text",  
    "value": "Figueira da Foz"  
  },  
  "nationality": {  
    "type": "Text",  
    "value": "DE"  
  },  
  "nationalityName": {  
    "type": "Text",  
    "value": "Germany"  
  },  
  "flowCount": {  
    "type": "Number",  
    "value": 145  
  },  
  "flowType": {  
    "type": "Text",  
    "value": "tourism"  
  },  
  "countryCode": {  
    "type": "Text",  
    "value": "PT"  
  },  
  "originLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.4103,  
        40.2033  
      ]  
    }  
  },  
  "destinationLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.8618,  
        40.1508  
      ]  
    }  
  },  
  "description": {  
    "type": "Text",  
    "value": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00"  
  },  
  "source": {  
    "type": "Text",  
    "value": "MobilityDataPlatform"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2024-12-31T11:00:00.00Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2024-12-31T11:00:00.00Z"  
  }  
}  
```  
</details>  

#### UrsprungZielFluss NGSI-LD Schlüsselwert Beispiel  

Hier ist ein Beispiel für einen OriginDestinationFlow im JSON-LD-Format als Schlüssel-Werte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und die Kontextdaten einer einzelnen Entität zurückgibt.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:OriginDestinationFlow:PT:0602:0406:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": "2024-12-31T10:00:00.00Z",  
  "aggregationDateType": "hourly",  
  "hour": 10,  
  "originLocationCode": "0602",  
  "originLocationName": "Coimbra",  
  "destinationLocationCode": "0406",  
  "destinationLocationName": "Figueira da Foz",  
  "nationality": "DE",  
  "nationalityName": "Germany",  
  "flowCount": 145,  
  "flowType": "tourism",  
  "countryCode": "PT",  
  "originLocation": {  
    "type": "Point",  
    "coordinates": [-8.4103, 40.2033]  
  },  
  "destinationLocation": {  
    "type": "Point",  
    "coordinates": [-8.8618, 40.1508]  
  },  
  "description": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00",  
  "source": "MobilityDataPlatform",  
  "dateCreated": "2024-12-31T11:00:00.00Z",  
  "dateModified": "2024-12-31T11:00:00.00Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  

#### UrsprungZielFluss NGSI-LD normalisiertes Beispiel  

Hier ist ein Beispiel für einen OriginDestinationFlow im JSON-LD-Format als normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und gibt die Kontextdaten einer einzelnen Entität zurück.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:OriginDestinationFlow:PT:CO0101:CO0102:DE:20241231T10",  
  "type": "OriginDestinationFlow",  
  "dateObserved": {  
    "type": "Property",  
    "value": "2024-12-31T10:30:00.00Z"  
  },  
  "aggregationDateType": {  
    "type": "Property",  
    "value": "hourly"  
  },  
  "hour": {  
    "type": "Property",  
    "value": 10  
  },  
  "originLocationCode": {  
    "type": "Property",  
    "value": "CO0101"  
  },  
  "originLocationName": {  
    "type": "Property",  
    "value": "Coimbra"  
  },  
  "destinationLocationCode": {  
    "type": "Property",  
    "value": "CO0102"  
  },  
  "destinationLocationName": {  
    "type": "Property",  
    "value": "Figueira da Foz"  
  },  
  "nationality": {  
    "type": "Property",  
    "value": "DE"  
  },  
  "nationalityName": {  
    "type": "Property",  
    "value": "Germany"  
  },  
  "flowCount": {  
    "type": "Property",  
    "value": 145  
  },  
  "flowType": {  
    "type": "Property",  
    "value": "tourism"  
  },  
  "countryCode": {  
    "type": "Property",  
    "value": "PT"  
  },  
  "originLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.4103,  
        40.2033  
      ]  
    }  
  },  
  "destinationLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -8.8618,  
        40.1508  
      ]  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "Hourly visitor flow from Coimbra to Figueira da Foz (German tourists) on 2024-12-31 at 10:00-11:00"  
  },  
  "source": {  
    "type": "Property",  
    "value": "MobilityDataPlatform"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2024-12-31T11:00:00.00Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2024-12-31T11:00:00.00Z"  
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
  

See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
  
