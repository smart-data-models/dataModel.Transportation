<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: ItemFlowObserved  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Modelo de datos destinado a medir una observación vinculada al movimiento de un elemento en un lugar y durante un periodo determinados. Este Modelo de Datos propone una evolución de dos Modelos de Datos fusionándolos e integrando todos los atributos de la versión inicial de [TrafficFlowObserved] y [CrowFlowObserved] y por extensión cualquier tipo de ítem que queramos analizar los movimientos. Los atributos `vehicleType` y `vehicleSubType` se eliminan del Modelo de datos inicial para convertirse en `itemType` y `itemSubType` genéricos de posibles valores. (personas, Tipo de vehículo, Tipo de barco, Tipo de avión, ...).**.  
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
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageGapDistance[number]`: Distancia media de separación entre 2 elementos consecutivos detectados. El código de unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Metro  - `averageHeadwayTime[number]`: Tiempo medio de alejamiento. El tiempo de alejamiento es el tiempo transcurrido entre dos partidas consecutivas. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **SEC** representa Segundo  - `averageLength[number]`: Longitud media de los elementos detectados en tránsito durante el periodo de observación. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Metro  - `averageSpeed[number]`: Velocidad media de los objetos detectados en tránsito durante el periodo de observación. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Según el tipo de Flujo, el valor puede ser **KMH** f(vehículo, peatón, etc.) representa Kilómetro por hora (km/h) o **KNT** representa Nudo (Barco)  - `congested[boolean]`: Indica si ha habido aglomeraciones durante el periodo de observación en el pasillo en cuestión. La ausencia de este atributo significa que no hubo aglomeraciones.  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `dateObserved[date-time]`: Fecha de la entidad observada definida por el usuario  - `dateObservedFrom[date-time]`: Período de observación : Fecha y hora de inicio en formato ISO8601 UTC  - `dateObservedTo[date-time]`: Período de observación : Fecha y hora de finalización en formato ISO8601 UTC  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `intensity[number]`: Número total de artículos detectados durante este periodo de observación  - `itemSubType[string]`: Referencia a un identificador de un atributo "subTipo" existente de una entidad NGSI (Vehículo / BarcoTipo / Persona ) o de una futura entidad que enumere un "subTipo" de elemento a contabilizar.  - `itemType[string]`: Referencia a un identificador de un atributo "Tipo" existente de una entidad NGSI (Vehículo / BarcoTipo / Persona) o de una entidad futura que enumere un "Tipo" de elemento que deba contabilizarse. Enum:'personas, barco, vehículo, yate'  - `laneDirection[string]`: Sentido habitual de circulación en el carril al que se refiere esta observación. Este atributo es útil cuando la observación no hace referencia a ningún segmento de carretera, permitiendo conocer el sentido de circulación del flujo de tráfico observado. Véase RoadSegment para una descripción de la semántica de estos valores  - `laneId[number]`: Identificador de carriles. La identificación de los carriles se realiza utilizando las convenciones definidas por la entidad RoadSegment que se basan en [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right)  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `occupancy[number]`: Fracción del tiempo de observación en la que un artículo ha ocupado el carril observado  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `refDevice[*]`: El dispositivo o dispositivos utilizados para obtener los datos expresados por este registro  - `refRoadSegment[*]`: Tramo de carretera afectado en el que se ha realizado la observación  - `reversedLane[boolean]`: Indica si el tráfico en el carril se invirtió durante el período de observación. La ausencia de este atributo significa que no hubo inversión de carril  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `speedMax[number]`: Velocidad máxima detectada durante el periodo de observación. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Según el tipo de Flujo, el valor puede ser **KMH** (vehículo, peatón, ...) representa Kilómetro por hora (km/h) o **KNT** representa Nudo (Barco)  - `speedMin[number]`: Velocidad mínima detectada durante el periodo de observación. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Según el tipo de Flujo, el valor puede ser **KMH** (vehículo, peatón, ...) representa Kilómetro por hora (km/h) o **KNT** representa Nudo (Barco)  - `type[string]`: Tipo de entidad NGSI. Tiene que ser ItemFlowObserved  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `dateObserved`  - `id`  - `laneId`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
    maxSpeed:    
      description: 'Maximum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    minSpeed:    
      description: 'Minimum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
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
    reverseLane:    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Transportation/ItemFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### ItemFlowObserved NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un ItemFlowObserved en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### ItemFlowObserved NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de ItemFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "type": "StructuredValue",  
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
    "type": "Text",  
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
    "type": "Boolean",  
    "value": true  
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
#### ItemFlowObserved NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un ItemFlowObserved en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### ItemFlowObserved NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de ItemFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
