<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: AnprFlowObserved  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **The data model represents an observation linked to the passing of a vehicle at a certain location and at a given time. This Data Model is based on the [dataModel.Transportation/ItemFlowObserved], extended with ANPR specific properties and links to the observation images.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `dateObserved[date-time]`: Date of the observed entity defined by the user  - `dateReceived[date-time]`: Timestamp when the observation has been received by the platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `laneId[string]`: Lane identifier. Lane identification provided by the observer  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `observedBy[*]`: The entity or device which has reported this observation  - `observedVehicle[object]`: Information about the observed vehicle  	- `brand[object]`: Detected brand of the observed vehicle    
	- `color[object]`: Detected color of the observed vehicle    
	- `country[object]`: Detected country of the observed vehicle    
	- `direction[string]`: Detected direction of the observed vehicle    
	- `licensePlate[object]`: Detected license plate of the observed vehicle    
	- `model[object]`: Detected brand model of the observed vehicle    
	- `speed[number]`: Detected speed of the observed vehicle    
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refImages[array]`: Array of multiple objects that refer to images  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI Entity type. It has to be AnprFlowObserved  - `vehiclePlateNotRead[boolean]`: Indicates if a license could not be read  - `zonesServed[array]`: Array of zones that are able to receive or read the observations  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
This data model describes the main entities involved with smart applications that deal with police issues. This set of entities is primarily associated with the Automotive and Smart City vertical segments and related IoT applications. When feasible, references to existing schema.org entity types and attributes are included. This model has been devised to be as generic as possible, thus allowing to  be used by different police departements and zones like ANPR,  Trajectory control and Police Vehicles  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnprFlowObserved:    
  description: 'The data model represents an observation linked to the passing of a vehicle at a certain location and at a given time. This Data Model is based on the [dataModel.Transportation/ItemFlowObserved], extended with ANPR specific properties and links to the observation images.'    
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
    dateReceived:    
      description: Timestamp when the observation has been received by the platform    
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
    laneId:    
      description: Lane identifier. Lane identification provided by the observer    
      type: string    
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
    observedBy:    
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
      description: The entity or device which has reported this observation    
      x-ngsi:    
        type: Relationship    
    observedVehicle:    
      description: Information about the observed vehicle    
      properties:    
        brand:    
          description: Detected brand of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Brand name identified    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        color:    
          description: Detected color of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Color name    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        country:    
          description: Detected country of the observed vehicle    
          properties:    
            code:    
              description: Country code according to ISO 3166-1 alpha-2    
              type: string    
              x-ngsi:    
                type: Property    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        direction:    
          description: Detected direction of the observed vehicle    
          enum:    
            - away    
            - towards    
          type: string    
          x-ngsi:    
            type: Property    
        licensePlate:    
          description: Detected license plate of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: 'Sequence of position points describing this location, expressed in coordinate system'    
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
                type: Property    
            identifier:    
              description: License plate identifier    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        model:    
          description: Detected brand model of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Model name    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        speed:    
          description: Detected speed of the observed vehicle    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
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
    refImages:    
      description: Array of multiple objects that refer to images    
      items:    
        properties:    
          contentType:    
            description: Content type according to IANA Media Types    
            type: string    
            x-ngsi:    
              type: Property    
          imageType:    
            description: Type of image    
            enum:    
              - plate    
              - overview    
              - anpr    
            type: string    
            x-ngsi:    
              type: Property    
          url:    
            description: URL referencing to the image    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Relationship    
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
    type:    
      description: NGSI Entity type. It has to be AnprFlowObserved    
      enum:    
        - AnprFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclePlateNotRead:    
      description: Indicates if a license could not be read    
      type: boolean    
      x-ngsi:    
        type: Property    
    zonesServed:    
      description: Array of zones that are able to receive or read the observations    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/AnprFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### AnprFlowObserved NGSI-v2 key-values Example    
Here is an example of a AnprFlowObserved in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed": "Antwerp",  
  "zonesServed": [  
    "Antwerp"  
  ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand": {  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model": {  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color": {  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country": {  
      "code": "BE",  
      "confidence": 0.95  
    },  
    "licensePlate": {  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages": [  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-v2 normalized Example    
Here is an example of a AnprFlowObserved in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2022-09-01T16:30:00Z"  
  },  
  "laneId": {  
    "type": "Text",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "StructuredValue",  
    "value": [  
      "Antwerp"  
    ]  
  },  
  "vehiclePlateNotRead": {  
    "type": "Boolean",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "StructuredValue",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": {  
        "name": "Audi",  
        "confidence": 0.97  
      },  
      "model": {  
        "name": "A3",  
        "confidence": 0.98  
      },  
      "color": {  
        "name": "black",  
        "confidence": 0.95  
      },  
      "country": {  
        "code": "BE",  
        "confidence": 0.95  
      },  
      "licensePlate": {  
        "identifier": "1-ABC-123",  
        "confidence": 0.96  
      }  
    }  
  },  
  "refImages": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "url": "s3://bucket/object-xxx-plate",  
        "contentType": "image/jpg",  
        "imageType": "anpr"  
      }  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ],  
      "type": "Point"  
    }  
  }  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD key-values Example    
Here is an example of a AnprFlowObserved in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed": "Antwerp",  
  "zonesServed": [  
    "Antwerp"  
  ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand": {  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model": {  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color": {  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country": {  
      "code": "BE",  
      "confidence": 0.95  
    },  
    "licensePlate": {  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    }  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages": [  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD normalized Example    
Here is an example of a AnprFlowObserved in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-09-01T16:30:00Z"  
    }  
  },  
  "laneId": {  
    "type": "Property",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "Property",  
    "value": {  
      "type": "string",  
      "coordinates": [  
        "Antwerp"  
      ]  
    }  
  },  
  "vehiclePlateNotRead": {  
    "type": "Property",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "Property",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": "Audi",  
      "model": "A3",  
      "color": "black",  
      "country": "BE",  
      "licensePlate": "1-ABC-123"  
    }  
  },  
  "refImages": {  
    "type": "Property",  
    "value": [  
      {  
        "type": "s3://bucket/object-xxx-plate",  
        "contentType": "image/jpg",  
        "imageType": "anpr"  
      }  
    ]  
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
