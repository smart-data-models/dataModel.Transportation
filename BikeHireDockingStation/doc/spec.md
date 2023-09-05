<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: BikeHireDockingStation  
==============================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Bike Hire Docking Station**  
version: 0.1.1  
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
- `agency_fare_url[string]`: URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)   - `agency_name[string]`: The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `agency_url[uri]`: The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableBikeNumber[number]`: The number of bikes available in the bike hire docking station to be hired by users  . Model: [https://schema.org/Number](https://schema.org/Number)- `contactPoint[object]`: The details to contact with the item  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: The geographic area where a service or offered item is provided. Supersedes serviceArea    
	- `availabilityRestriction[*]`: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Contact type of this item    
	- `email[idn-email]`: Email address of owner    
	- `faxNumber[string]`: The fax number  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: The name of this item    
	- `productSupported[string]`: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Telephone of this contact    
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `freeSlotNumber[number]`: The number of slots available for returning and parking bikes. It must lower or equal than `totalSlotNumber`  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `mediaURL[uri]`: URL providing further information of any image(s) or media of the complaint or place  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: The name of this item  - `observationDateTime[date-time]`: Last reported time of observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `openingHours[string]`: Opening hours of the docking station  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `outOfServiceSlotNumber[number]`: The number of slots that are out of order and cannot be used to hire or park a bike. It must lower or equal than `totalSlotNumber`  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `provider[string]`: Bike hire service provider  . Model: [https://schema.org/provider](https://schema.org/provider)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `stationCode[string]`: The station number or station code of the bike hire docking station corresponding to the observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `stationName[string]`: The name of the bike hire docking station corresponding to this observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `status[string]`: Status of the bike hire docking station. Enum:'working, outOfService, withIncidence, full, almostFull, empty, almostEmpty'. Or any other application specific  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalSlotNumber[number]`: The total number of slots offered by this bike docking station  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI Entity type. It has to be BikeHireDockingStation  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Many cities provide a bike hiring system for citizens. These can hire a bike base on different types of subscriptions. A bike hire docking station where subscribed users can hire and return a bike. It provides data about its main features and availability of bikes and free slots.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BikeHireDockingStation:    
  description: Bike Hire Docking Station    
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
    agency_fare_url:    
      description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) "    
      type: string    
      x-ngsi:    
        type: Property    
    agency_name:    
      description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    agency_url:    
      description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    availableBikeNumber:    
      description: The number of bikes available in the bike hire docking station to be hired by users    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    contactPoint:    
      description: The details to contact with the item    
      properties:    
        areaServed:    
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
          type: string    
          x-ngsi:    
            type: Property    
        availabilityRestriction:    
          anyOf:    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                format: uri    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
          x-ngsi:    
            model: http://schema.org/hoursAvailable    
            type: Relationship    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
          x-ngsi:    
            model: http://schema.org/availableLanguage    
            type: Property    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
          x-ngsi:    
            model: http://schema.org/contactOption    
            type: Property    
        contactType:    
          description: Contact type of this item    
          type: string    
          x-ngsi:    
            type: Property    
        email:    
          description: Email address of owner    
          format: idn-email    
          type: string    
          x-ngsi:    
            type: Property    
        faxNumber:    
          description: The fax number    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        name:    
          description: The name of this item    
          type: string    
          x-ngsi:    
            type: Property    
        productSupported:    
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        telephone:    
          description: Telephone of this contact    
          type: string    
          x-ngsi:    
            type: Property    
        url:    
          description: URL which provides a description or further information about this item    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
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
    freeSlotNumber:    
      description: The number of slots available for returning and parking bikes. It must lower or equal than `totalSlotNumber`    
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
    mediaURL:    
      description: URL providing further information of any image(s) or media of the complaint or place    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    openingHours:    
      description: Opening hours of the docking station    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
        type: Property    
    outOfServiceSlotNumber:    
      description: The number of slots that are out of order and cannot be used to hire or park a bike. It must lower or equal than `totalSlotNumber`    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    provider:    
      description: Bike hire service provider    
      type: string    
      x-ngsi:    
        model: https://schema.org/provider    
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
    stationCode:    
      description: The station number or station code of the bike hire docking station corresponding to the observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    stationName:    
      description: The name of the bike hire docking station corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    status:    
      description: 'Status of the bike hire docking station. Enum:''working, outOfService, withIncidence, full, almostFull, empty, almostEmpty''. Or any other application specific'    
      enum:    
        - almostEmpty    
        - almostFull    
        - empty    
        - full    
        - outOfService    
        - withIncidence    
        - working    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalSlotNumber:    
      description: The total number of slots offered by this bike docking station    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be BikeHireDockingStation    
      enum:    
        - BikeHireDockingStation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/BikeHireDockingStation/schema.json    
  x-model-tags: ""    
  x-version: 0.1.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### BikeHireDockingStation NGSI-v2 key-values Example    
Here is an example of a BikeHireDockingStation in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "status": "working",  
    "provider": "University of Mumbay",  
    "contactPoint": {  
        "url": "uri:ngsi:www.lignesdazur.com"  
    },  
    "availableBikeNumber": 20,  
    "freeSlotNumber": 10,  
    "openingHours": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            2.180042,  
            41.397952  
        ]  
    },  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Barcelona",  
        "streetAddress": "Gran Via Corts Catalanes,760"  
    },  
    "totalSlotNumber": 100,  
    "outOfServiceSlotNumber": 21,  
    "stationName": "Pune",  
    "mediaURL": "http://pedalsaddle.in/",  
    "agency_url": "http://pedalsaddle.in/",  
    "agency_name": "PedalSaddle",  
    "stationCode": "2",  
    "observationDate": "2021-03-11T15:51:02+05:30",  
    "agency_fare_url": ""  
}  
```  
</details>  
#### BikeHireDockingStation NGSI-v2 normalized Example    
Here is an example of a BikeHireDockingStation in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
  "type": "BikeHireDockingStation",  
  "status": {  
    "type": "Text",  
    "value": "working"  
  },  
  "provider": {  
    "type": "Text",  
    "value": "University of Mumbay"  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "url": "uri:ngsi:www.lignesdazur.com"  
    }  
  },  
  "availableBikeNumber": {  
    "type": "Number",  
    "value": 20  
  },  
  "freeSlotNumber": {  
    "type": "Number",  
    "value": 10  
  },  
  "openingHours": {  
    "type": "Text",  
    "value": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        2.180042,  
        41.397952  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Barcelona",  
      "streetAddress": "Gran Via Corts Catalanes,760"  
    }  
  },  
  "totalSlotNumber": {  
    "type": "Number",  
    "value": 100  
  },  
  "outOfServiceSlotNumber": {  
    "type": "Number",  
    "value": 21  
  },  
  "stationName": {  
    "type": "Text",  
    "value": "Pune"  
  },  
  "mediaURL": {  
    "type": "Text",  
    "value": "http://pedalsaddle.in/"  
  },  
  "agency_url": {  
    "type": "Text",  
    "value": "http://pedalsaddle.in/"  
  },  
  "agency_name": {  
    "type": "Text",  
    "value": "PedalSaddle"  
  },  
  "stationCode": {  
    "type": "Number",  
    "value": "2"  
  },  
  "observationDate": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "agency_fare_url": {  
    "type": "Text",  
    "value": ""  
  }  
}  
```  
</details>  
#### BikeHireDockingStation NGSI-LD key-values Example    
Here is an example of a BikeHireDockingStation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Barcelona",  
        "streetAddress": "Gran Via Corts Catalanes,760"  
    },  
    "agency_fare_url": "",  
    "agency_name": "PedalSaddle",  
    "agency_url": "http://pedalsaddle.in/",  
    "availableBikeNumber": 20,  
    "contactPoint": {  
        "url": "uri:ngsi:www.lignesdazur.com"  
    },  
    "freeSlotNumber": 10,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            2.180042,  
            41.397952  
        ]  
    },  
    "mediaURL": "http://pedalsaddle.in/",  
    "observationDate": "2021-03-11T15:51:02+05:30",  
    "openingHours": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00",  
    "outOfServiceSlotNumber": 21,  
    "provider": "University of Mumbay",  
    "stationCode": "2",  
    "stationName": "Pune",  
    "status": "working",  
    "totalSlotNumber": 100,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### BikeHireDockingStation NGSI-LD normalized Example    
Here is an example of a BikeHireDockingStation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "Barcelona",  
            "streetAddress": "Gran Via Corts Catalanes,760"  
        }  
    },  
    "agency_fare_url": {  
        "type": "Property",  
        "value": ""  
    },  
    "agency_name": {  
        "type": "Property",  
        "value": "PedalSaddle"  
    },  
    "agency_url": {  
        "type": "Property",  
        "value": "http://pedalsaddle.in/"  
    },  
    "availableBikeNumber": {  
        "type": "Property",  
        "value": 20  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": {  
            "url": "uri:ngsi:www.lignesdazur.com"  
        }  
    },  
    "freeSlotNumber": {  
        "type": "Property",  
        "value": 10  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                2.180042,  
                41.397952  
            ]  
        }  
    },  
    "mediaURL": {  
        "type": "Property",  
        "value": "http://pedalsaddle.in/"  
    },  
    "observationDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "openingHours": {  
        "type": "Property",  
        "value": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00"  
    },  
    "outOfServiceSlotNumber": {  
        "type": "Property",  
        "value": 21  
    },  
    "provider": {  
        "type": "Property",  
        "value": "University of Mumbay"  
    },  
    "stationCode": {  
        "type": "Property",  
        "value": "2"  
    },  
    "stationName": {  
        "type": "Property",  
        "value": "Pune"  
    },  
    "status": {  
        "type": "Property",  
        "value": "working"  
    },  
    "totalSlotNumber": {  
        "type": "Property",  
        "value": 100  
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
