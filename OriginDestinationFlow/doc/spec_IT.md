<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entità: OriginDestinationFlow  
=============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licenza aperta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/OriginDestinationFlow/LICENSE.md)  

[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Osservazione oraria dei flussi di movimento dei visitatori tra comuni di origine e di destinazione, suddivisi per nazionalità. Ogni entità rappresenta il conteggio del flusso tra due località durante un'ora specifica.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Elenco delle proprietà  


<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o formati/modello diversi</sub></sup>  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)  
	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo di via e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestito dal governo locale  
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo di via  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica in una strada pubblica  
- `aggregationDateType[string]`: Tipo di aggregazione delle date (ad esempio, orario, giornaliero, mensile)  
- `alternateName[string]`: Un nome alternativo per questo elemento  
- `areaServed[string]`: L'area geografica in cui viene fornito un servizio o un articolo offerto  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `countryCode[string]`: Codice del paese di origine associato alle persone associate al flusso, ad es. ES, IT, FR, ecc...  
- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  
- `dateCreated[date-time]`: Timestamp di creazione dell'entità. Questo verrà solitamente assegnato dalla piattaforma di archiviazione  
- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Questo sarà solitamente assegnato dalla piattaforma di archiviazione  
- `dateObserved[date-time]`: Data e ora dell'osservazione in formato ISO 8601  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)  
- `description[string]`: Una descrizione di questo articolo  
- `destinationLocation[*]`: Riferimento Geojson all'elemento. Può essere Punto, LineString, Poligono, MultiPunto, MultiLineString o MultiPoligono  
- `destinationLocationCode[string]`: Codice ufficiale del comune di destinazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `destinationLocationName[string]`: Nome del comune di destinazione  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `flowCount[number]`: Numero totale di movimenti/flussi tra origine e destinazione durante questa ora  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `flowType[string]`: Tipo di flusso. Enum: 'turismo, pendolarismo, business, migrazione, misto'  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `hour[number]`: Ora del giorno (0-23) per questa osservazione  . Model: [https://schema.org/Number](https://schema.org/Number)  
- `id[*]`: Identificatore univoco dell'entità  
- `location[*]`: Riferimento Geojson all'elemento. Può essere Punto, LineString, Poligono, MultiPunto, MultiLineString o MultiPoligono  
- `name[string]`: Il nome di questo articolo  
- `nationality[string]`: Nazionalità dei visitatori che effettuano il movimento. Codice paese ISO 3166-1 alpha-2 (ad esempio, ES, FR, GB, PT, DE)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `nationalityName[string]`: Nome completo della nazione di cittadinanza (opzionale, per leggibilità umana)  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `originLocation[*]`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  
- `originLocationCode[string]`: Codice ufficiale del comune di origine  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `originLocationName[string]`: Nome del comune di origine  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `owner[array]`: Una lista che contiene una sequenza di caratteri codificata in JSON che fa riferimento agli Id univoci del/dei proprietario/i  
- `seeAlso[*]`: Elenco di uri che puntano a risorse aggiuntive sull'elemento  
- `source[string]`: Una sequenza di caratteri che fornisce la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del fornitore di origine o l'URL dell'oggetto di origine  
- `type[string]`: Tipo di entità NGSI. Deve essere OriginDestinationFlow  
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Proprietà richieste  
- `id`  
- `tipo`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Descrizione del modello di dati delle proprietà  

Ordinati in ordine alfabetico (clicca per i dettagli)  
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
  

## Payload di esempio  

#### OrigineDestinazioneFlusso Esempio di valori chiave NGSI-v2  

Ecco un esempio di OriginDestinationFlow in formato JSON come chiavi-valori. Ciò è compatibile con NGSI-v2 quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
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

#### OrigineDestinazioneFlusso Esempio NGSI-v2 normalizzato  

Ecco un esempio di un OriginDestinationFlow in formato JSON come normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
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

#### OrigineDestinazioneFlusso Esempio di valori chiave NGSI-LD  

Ecco un esempio di un OriginDestinationFlow in formato JSON-LD come chiavi-valori. Ciò è compatibile con NGSI-LD quando si utilizza `options=keyValues` e restituisce i dati di contesto di un'entità individuale.  
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

#### OrigineDestinazioneFlusso Esempio normalizzato NGSI-LD  

Ecco un esempio di un OriginDestinationFlow in formato JSON-LD normalizzato. Ciò è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di un'entità individuale.  
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
  
