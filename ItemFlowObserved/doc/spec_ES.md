Entidad: ItemFlowObserved  
=========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ItemFlowObserved/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Modelo de datos destinado a medir una observación vinculada al movimiento de un elemento en un lugar determinado y durante un período determinado. Este modelo de datos propone una evolución de dos modelos de datos fusionándolos e integrando todos los atributos de la versión inicial de [TrafficFlowObserved] y [CrowFlowObserved] y por extensión cualquier tipo de elemento que queramos analizar los movimientos. Los atributos `vehicleType` y `vehicleSubType` se eliminan del modelo de datos inicial para convertirse en `itemType` y `itemSubType` genéricos de posibles valores. (personas, Tipo de vehículo, Tipo de barco, Tipo de avión, ...).**.  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `averageGapDistance`: Distancia media de separación entre 2 elementos consecutivos detectados. El código de la unidad (texto) se indica utilizando los [Códigos comunes de la ONU/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Meter.  - `averageHeadwayTime`: Tiempo medio de alejamiento. El tiempo de alejamiento es el tiempo transcurrido entre dos partidas consecutivas. El código de la unidad (texto) se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **SEC** representa el segundo.  - `averageLength`: Longitud media de los elementos detectados en tránsito durante el periodo de observación. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Meter.  - `averageSpeed`: Velocidad media de los elementos detectados en tránsito durante el período de observación. El código de la unidad (texto) se da utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Dependiendo del tipo de flujo, el valor puede ser **KMH** f(vehículo, peatón, etc.) representa el kilómetro por hora (km/h) o **KNT** representa el nudo (barco).  - `congested`: Indica si hubo congestión de público durante el periodo de observación en el pasillo referido. La ausencia de este atributo significa que no hubo congestión de multitudes  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved`: Fecha de la entidad observada definida por el usuario.  - `dateObservedFrom`: Período de observación : Fecha y hora de inicio en formato ISO8601 UTC.  - `dateObservedTo`: Período de observación : Fecha y hora de finalización en formato ISO8601 UTC.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `intensity`: Número total de elementos detectados durante este periodo de observación  - `itemSubType`: Referencia a un identificador de un atributo de "subtipo" existente de una entidad NGSI (Vehículo / Tipo de barco / Persona ) o de una entidad futura que enumere un "subtipo" de elemento que deba contarse.  - `itemType`: Referencia a un identificador de un atributo "Tipo" existente de una entidad NGSI (Vehículo / BarcoTipo / Persona) o de una futura entidad que enumere un "Tipo" de elemento a contabilizar. Enum:'personas, barco, vehículo, yate'  - `laneDirection`: Sentido habitual de la marcha en el carril al que se refiere esta observación. Este atributo es útil cuando la observación no hace referencia a ningún segmento de carretera, permitiendo conocer el sentido de la marcha del flujo de tráfico observado. Véase RoadSegment para una descripción de la semántica de estos valores.  - `laneId`: Identificador de carriles. La identificación de los carriles se realiza utilizando las convenciones definidas por la entidad RoadSegment que se basan en [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `occupancy`: Fracción del tiempo de observación en el que un artículo ha estado ocupando el carril observado  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refDevice`: El dispositivo o dispositivos utilizados para obtener los datos expresados por este registro  - `refRoadSegment`: Tramo de carretera afectado en el que se ha realizado la observación  - `reversedLane`: Indica si el tráfico en el carril se invirtió durante el período de observación. La ausencia de este atributo significa que no hubo reversión de carril  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `speedMax`: Velocidad máxima detectada durante el periodo de observación. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Dependiendo del tipo de flujo, el valor puede ser **KMH** (vehículo, peatón, ...) representa el kilómetro por hora (km/h) o **KNT** representa el nudo (barco).  - `speedMin`: Velocidad mínima detectada durante el periodo de observación. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Dependiendo del tipo de flujo, el valor puede ser **KMH** (vehículo, peatón, ...) representa el kilómetro por hora (km/h) o **KNT** representa el nudo (barco).  - `type`: Tipo de entidad NGSI. Tiene que ser ItemFlowObserved    
Propiedades requeridas  
- `dateObserved`  - `id`  - `laneId`  - `location`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ItemFlowObserved:    
  description: 'The data model intended to measure an observation linked to the movement of an item at a certain location and over a given period. This Data Model proposes an evolution of two Data Model by merging them and integrating all the attributes of the initial version of [TrafficFlowObserved] and [CrowFlowObserved] and by extension any type of item that we want to analyze the movements. Attributes `vehicleType` and `vehicleSubType` are removed from the initial data Model in order to become generic `itemType` and `itemSubType` of possible values. (people, Type of vehicle, Type of boat, Type of plane, ...).'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    averageGapDistance:    
      description: 'Average gap distance between consecutive 2 detected items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageHeadwayTime:    
      description: 'Average headway time. Head away time is the time elapsed between two consecutive items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **SEC** represents Second.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageLength:    
      description: 'Average length of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    averageSpeed:    
      description: 'Average speed of detected items transiting during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** f(vehicule, pedestrian, etc.) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    congested:    
      description: 'Flags whether there was a crowd congestion during the observation period in the referred walkway. The absence of this attribute means no crowd congestion'    
      type: boolean    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'Date of the observed entity defined by the user.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period : Start date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObservedTo:    
      description: 'Observation period : End date and time in an ISO8601 UTC format.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &itemflowobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    intensity:    
      description: 'Total number of items detected during this observation period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    itemSubType:    
      description: 'Reference to an identifier of an existing ''subType'' attribute of an NGSI entity (Vehicle / BoatType / Person ) or of a future entity listing an item ''subType'' to be counted.'    
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
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. See RoadSegment for a description of the semantics of these values.'    
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
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).'    
      min: 1    
      type: integer    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    occupancy:    
      description: 'Fraction of the observation time where a item has been occupying the observed lane'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *itemflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The device or devices used to obtain the data expressed by this record'    
      x-ngsi:    
        type: Relationship    
    refRoadSegment:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Concerned road segment on which the observation has been made'    
      x-ngsi:    
        type: Relationship    
    reversedLane:    
      description: 'Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion'    
      type: boolean    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    speedMax:    
      description: 'Maximum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    speedMin:    
      description: 'Minimum speed detected during the observation period. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Depending the type of Flow, the value can be **KMH** (vehicule, pedestrian, ...) represents Kilometer per hour (km/h) or **KNT** represents Knot (Boat).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be ItemFlowObserved'    
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
```  
</details>    
## Ejemplo de carga útil  
#### ItemFlowObserved NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un ItemFlowObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### ItemFlowObserved NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un ItemFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### ItemFlowObserved NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un ItemFlowObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
  "itemType": "yacht",  
  "itemSubtype": "monoHull",  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### ItemFlowObserved NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un ItemFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "FlowObserved:BFO-NCE-MNCA-SP-001",  
  "type": "ItemFlowObserved",  
  "name": {  
    "type": "Property",  
    "value": "BFO-NCE-MNCA-SP-001"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Boat Flow Observed from Nice Harbor."  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        7.196545,  
        43.664809  
      ]  
    }  
  },  
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
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:BFO-NCE-MNCA-SP-001-Dev-02"  
  },  
  "itemType": {  
    "type": "Property",  
    "value": "yatching"  
  },  
  "itemSubType": {  
    "type": "Property",  
    "value": "monoHull"  
  },  
  "laneId": {  
    "type": "Property",  
    "value": 1  
  },  
  "laneDirection": {  
    "type": "Property",  
    "value": "outbound"  
  },  
  "reverseLane": {  
    "type": "Property",  
    "value": false  
  },  
  "intensity": {  
    "type": "Property",  
    "value": 12  
  },  
  "occupancy": {  
    "type": "Property",  
    "value": 0.1562  
  },  
  "congested": {  
    "type": "Property",  
    "value": false  
  },  
  "averageSpeed": {  
    "type": "Property",  
    "value": 2.7,  
    "unitCode": "KNT"  
  },  
  "averageLength": {  
    "type": "Property",  
    "value": 7.44,  
    "unitCode": "MTR"  
  },  
  "averageHeadwayTime": {  
    "type": "Property",  
    "value": 156,  
    "unitCode": "SEC"  
  },  
  "averageGapDistance": {  
    "type": "Property",  
    "value": 35.28,  
    "unitCode": "MTR"  
  },  
  "minSpeed": {  
    "type": "Property",  
    "value": 2.6,  
    "unitCode": "KNT"  
  },  
  "maxSpeed": {  
    "type": "Property",  
    "value": 3.8,  
    "unitCode": "KNT"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud