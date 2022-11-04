<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: TrafficFlowObserved  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TrafficFlowObserved/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Una observación de las condiciones del flujo de tráfico en un lugar y momento determinados.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `averageGapDistance[number]`: Distancia media entre vehículos consecutivos  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageHeadwayTime[number]`: Tiempo medio de recorrido. El tiempo de paso es el tiempo transcurrido entre dos vehículos consecutivos  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageVehicleLength[number]`: Longitud media de los vehículos que transitan durante  
    el periodo de observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `averageVehicleSpeed[number]`: Velocidad media de los vehículos que transitan durante el periodo de observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `congested[boolean]`:  Indica si hubo una congestión de tráfico durante el período de observación en el carril en cuestión. La ausencia de este atributo significa que no hubo congestión de tráfico  . Model: [https://schema.org/Boolean.](https://schema.org/Boolean.)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved[string]`: La fecha y la hora de esta observación en formato ISO8601 UTC. Puede representarse mediante un instante de tiempo específico o mediante un intervalo ISO8601. Como solución a la falta de soporte de Orion Context Broker para los intervalos de fecha, se pueden utilizar dos atributos separados: `dateObservedFrom`, `dateObservedTo`. [DateTime](https://schema.org/DateTime) o un intervalo ISO8601 representado como [Texto](https://schema.org/Text)  . Model: [https://schema.org/DateTime.](https://schema.org/DateTime.)- `dateObservedFrom[string]`: Fecha y hora de inicio del periodo de observación. Ver `fechaObservada`.  . Model: [https://schema.org/Datetime.](https://schema.org/Datetime.)- `dateObservedTo[string]`: Fecha y hora de finalización del periodo de observación. Ver "fecha observada".  . Model: [https://schema.org/Datetime.](https://schema.org/Datetime.)- `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `intensity[number]`: Número total de vehículos detectados durante este periodo de observación  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `laneDirection[string]`: Sentido habitual de la marcha en el carril al que se refiere esta observación. Este atributo es útil cuando la observación no hace referencia a ningún segmento de carretera, permitiendo conocer el sentido de la marcha del flujo de tráfico observado. Enum:hacia adelante, hacia atrás". Véase RoadSegment para una descripción de la semántica de estos valores.  . Model: [https://schema.org/Text](https://schema.org/Text)- `laneId[integer]`: Identificador de carriles. La identificación de los carriles se realiza utilizando las convenciones definidas por la entidad RoadSegment que se basan en [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).  . Model: [https://schema.org/Number](https://schema.org/Number)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `occupancy[number]`: Fracción del tiempo de observación en el que un vehículo ha estado ocupando el carril observado  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refRoadSegment[string]`: Tramo de carretera en el que se ha realizado la observación. Referencia a una entidad de tipo RoadSegment  . Model: [https://schema.org/URL](https://schema.org/URL)- `reversedLane[boolean]`: Indica si el tráfico en el carril se invirtió durante el período de observación. La ausencia de este atributo significa que no hubo reversión de carril  . Model: [https://schema.org/Boolean.](https://schema.org/Boolean.)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Debe ser TrafficFlowObserved  - `vehicleSubType[string]`: Permite especificar un subtipo de `vehicleType`, por ejemplo, si el `vehicleType` se establece como `Lorry` el `vehicleSubType` puede ser `OGV1` o `OGV2` para transmitir más información sobre el tipo exacto de vehículo.  - `vehicleType[string]`: Tipo de vehículo desde el punto de vista de sus características estructurales. Enum:'vehículo agrícola, bicicleta, autobús, minibús, coche, caravana, tranvía, cisterna, cocheConCaravana, cocheConRemolque, camión, ciclomotor, motocicleta, motocicletaConCarga, motocarro, remolque, furgoneta, vehículo de construcción o de mantenimiento, carro, carro de basura, máquina barredora, carro de limpieza'.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `dateObserved`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Esta entidad está asociada principalmente a los segmentos verticales de Automoción y Ciudades Inteligentes y a las aplicaciones de IoT relacionadas.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TrafficFlowObserved:    
  description: 'An observation of traffic flow conditions at a certain place and time.'    
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
      description: 'Average gap distance between consecutive vehicles'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'meter (m)'    
    averageHeadwayTime:    
      description: 'Average headway time. Headway time is the time ellapsed between two consecutive vehicles'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'second (s)'    
    averageVehicleLength:    
      description: |-    
        Average length of the vehicles transiting during    
            the observation period    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'meter (m)'    
    averageVehicleSpeed:    
      description: 'Average speed of the vehicles transiting during the observation period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    congested:    
      description: ' Flags whether there was a traffic congestion during the observation period in the referred lane. The absence of this attribute means no traffic congestion'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean.    
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
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`. [DateTime](https://schema.org/DateTime) or an ISO8601 interval represented as [Text](https://schema.org/Text)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime.    
        type: Property    
    dateObservedFrom:    
      description: 'Observation period start date and time. See `dateObserved`'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime.    
        type: Property    
    dateObservedTo:    
      description: 'Observation period end date and time. See `dateObserved`'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Datetime.    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &trafficflowobserved_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Total number of vehicles detected during this observation period'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    laneDirection:    
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. Enum:forward, backward''. See RoadSegment for a description of the semantics of these values.'    
      enum:    
        - forward    
        - backward    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    laneId:    
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    occupancy:    
      description: 'Fraction of the observation time where a vehicle has been occupying the observed lane'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *trafficflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refRoadSegment:    
      description: 'Concerned road segment on which the observation has been made. Reference to an entity of type RoadSegment'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reversedLane:    
      description: 'Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean.    
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
    type:    
      description: 'NGSI Entity type. It has to be TrafficFlowObserved'    
      enum:    
        - TrafficFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleSubType:    
      description: 'It allows to specify a sub type of `vehicleType`, eg if the `vehicleType` is set to `Lorry` the `vehicleSubType` may be `OGV1` or `OGV2` to convey more information about the exact type of vehicle.'    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. Enum:''agriculturalVehicle, bicycle, bus, minibus, car, caravan, tram, tanker, carWithCaravan, carWithTrailer, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, trailer, van, constructionOrMaintenanceVehicle, trolley, binTrolley, sweepingMachine, cleaningTrolley'''    
      enum:    
        - agriculturalVehicle    
        - bicycle    
        - bus    
        - minibus    
        - car    
        - caravan    
        - tram    
        - tanker    
        - carWithCaravan    
        - carWithTrailer    
        - lorry    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - trailer    
        - van    
        - constructionOrMaintenanceVehicle    
        - trolley    
        - binTrolley    
        - sweepingMachine    
        - cleaningTrolley    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/TrafficFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/TrafficFlowObserved/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### TrafficFlowObserved NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un TrafficFlowObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "laneId": 1,  
  "address": {  
    "streetAddress": "Avenida de Salamanca",  
    "addressLocality": "Valladolid",  
    "addressCountry": "ES"  
  },  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.73735395519672, 41.6538181849672],  
      [-4.73414858659993, 41.6600594193478],  
      [-4.73447575302641, 41.659585195093]  
    ]  
  },  
  "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",  
  "dateObservedFrom": "2016-12-07T11:10:00Z",  
  "dateObservedTo": "2016-12-07T11:15:00Z",  
  "averageHeadwayTime": 0.5,  
  "intensity": 197,  
  "occupancy": 0.76,  
  "averageVehicleSpeed": 52.6,  
  "averageVehicleLength": 9.87,  
  "reversedLane": false,  
  "laneDirection": "forward"  
}  
```  
</details>  
#### TrafficFlowObserved NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un TrafficFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "dateObserved": {  
    "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
  },  
  "laneDirection": {  
    "value": "forward"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:10:00Z"  
  },  
  "averageVehicleLength": {  
    "value": 9.87  
  },  
  "averageHeadwayTime": {  
    "value": 0.5  
  },  
  "occupancy": {  
    "value": 0.76  
  },  
  "reversedLane": {  
    "value": false  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:15:00Z"  
  },  
  "intensity": {  
    "value": 197  
  },  
  "laneId": {  
    "value": 1  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [-4.73735395519672, 41.6538181849672],  
        [-4.73414858659993, 41.6600594193478],  
        [-4.73447575302641, 41.659585195093]  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES",  
      "streetAddress": "Avenida de Salamanca"  
    }  
  },  
  "averageVehicleSpeed": {  
    "value": 52.6  
  }  
}  
```  
</details>  
#### TrafficFlowObserved NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un TrafficFlowObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
    "type": "TrafficFlowObserved",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Valladolid",  
            "addressCountry": "ES",  
            "streetAddress": "Avenida de Salamanca",  
            "type": "PostalAddress"  
        }  
    },  
    "averageHeadwayTime": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "averageVehicleLength": {  
        "type": "Property",  
        "value": 9.87  
    },  
    "averageVehicleSpeed": {  
        "type": "Property",  
        "value": 52.6  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
    },  
    "dateObservedFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-07T11:10:00Z"  
        }  
    },  
    "dateObservedTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-07T11:15:00Z"  
        }  
    },  
    "intensity": {  
        "type": "Property",  
        "value": 197  
    },  
    "laneDirection": {  
        "type": "Property",  
        "value": "forward"  
    },  
    "laneId": {  
        "type": "Property",  
        "value": 1  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "LineString",  
            "coordinates": [  
                [  
                    -4.73735395519672,  
                    41.6538181849672  
                ],  
                [  
                    -4.73414858659993,  
                    41.6600594193478  
                ],  
                [  
                    -4.73447575302641,  
                    41.659585195093  
                ]  
            ]  
        }  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.76  
    },  
    "reversedLane": {  
        "type": "Property",  
        "value": false  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TrafficFlowObserved NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un TrafficFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
    "type": "TrafficFlowObserved",  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Valladolid",  
        "streetAddress": "Avenida de Salamanca",  
        "type": "PostalAddress"  
    },  
    "averageHeadwayTime": 0.5,  
    "averageVehicleLength": 9.87,  
    "averageVehicleSpeed": 52.6,  
    "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",  
    "dateObservedFrom": {  
        "@type": "DateTime",  
        "@value": "2016-12-07T11:10:00Z"  
    },  
    "dateObservedTo": {  
        "@type": "DateTime",  
        "@value": "2016-12-07T11:15:00Z"  
    },  
    "intensity": 197,  
    "laneDirection": "forward",  
    "laneId": 1,  
    "location": {  
        "coordinates": [  
            [  
                -4.73735395519672,  
                41.6538181849672  
            ],  
            [  
                -4.73414858659993,  
                41.6600594193478  
            ],  
            [  
                -4.73447575302641,  
                41.659585195093  
            ]  
        ],  
        "type": "LineString"  
    },  
    "occupancy": 0.76,  
    "reversedLane": false,  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
