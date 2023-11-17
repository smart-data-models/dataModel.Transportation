<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: AnprFlowObserved    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **El modelo de datos representa una observación vinculada al paso de un vehículo en un lugar y momento determinados. Este modelo de datos se basa en el [dataModel.Transportation/ItemFlowObserved], ampliado con propiedades específicas ANPR y enlaces a las imágenes de observación.**.    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública      
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `dateObserved[date-time]`: Fecha de la entidad observada definida por el usuario  - `dateReceived[date-time]`: Fecha y hora en que la plataforma ha recibido la observación  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `laneId[string]`: Identificador de carril. Identificación de carril proporcionada por el observador  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `observedBy[*]`: La entidad o dispositivo que ha notificado esta observación  - `observedVehicle[object]`: Información sobre el vehículo observado  	- `brand[object]`: Marca detectada del vehículo observado      
	- `color[object]`: Color detectado del vehículo observado      
	- `country[object]`: País detectado del vehículo observado      
	- `direction[string]`: Dirección detectada del vehículo observado      
	- `licensePlate[object]`: Matrícula detectada del vehículo observado      
	- `model[object]`: Modelo de marca detectado del vehículo observado      
	- `speed[number]`: Velocidad detectada del vehículo observado      
- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `refImages[array]`: Matriz de objetos múltiples que hacen referencia a imágenes  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser AnprFlowObserved  - `vehiclePlateNotRead[boolean]`: Indica si no se ha podido leer una licencia  - `zonesServed[array]`: Conjunto de zonas que pueden recibir o leer las observaciones  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Este modelo de datos describe las principales entidades relacionadas con las aplicaciones inteligentes que se ocupan de cuestiones policiales. Este conjunto de entidades se asocia principalmente con los segmentos verticales de Automoción y Ciudad Inteligente y las aplicaciones IoT relacionadas. Cuando es factible, se incluyen referencias a tipos de entidades y atributos existentes en schema.org. Este modelo ha sido concebido para ser lo más genérico posible, permitiendo así ser utilizado por diferentes departamentos de policía y zonas como ANPR, Control de Trayectoria y Vehículos Policiales.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
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
          required:      
            - identifier      
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
        required:      
          - url      
          - contentType      
          - imageType      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/AnprFlowObserved/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### AnprFlowObserved NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un AnprFlowObserved en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### AnprFlowObserved NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un AnprFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
#### AnprFlowObserved NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de un AnprFlowObserved en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### AnprFlowObserved NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un AnprFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
