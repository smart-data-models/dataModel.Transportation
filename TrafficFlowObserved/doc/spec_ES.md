Entidad: TrafficFlowObserved  
============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TrafficFlowObserved/LICENSE.md)  
Descripción global: **Una observación de las condiciones del flujo de tráfico en un determinado lugar y momento.  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `averageGapDistance`: Distancia media de separación entre vehículos consecutivos  - `averageHeadwayTime`: Tiempo medio de avance. El tiempo de avance es el tiempo transcurrido entre dos vehículos consecutivos  - `averageVehicleLength`: La longitud media de los vehículos que transitan durante  
    el período de observación  - `averageVehicleSpeed`: Velocidad media de los vehículos que transitan durante el período de observación  - `congested`:  Indica si hubo una congestión de tráfico durante el período de observación en el carril mencionado. La ausencia de este atributo significa que no hay congestión de tráfico  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateObserved`: La fecha y la hora de esta observación en formato ISO8601 UTC. Puede ser representada por un instante de tiempo específico o por un intervalo ISO8601. Como solución para la falta de apoyo del Orion Context Broker para los intervalos de fecha y hora, se pueden utilizar dos atributos separados: "dateObservedFrom", "dateObservedTo". DateTime](https://schema.org/DateTime) o un intervalo ISO8601 representado como [Text](https://schema.org/Text)  - `dateObservedFrom`: Fecha y hora de inicio del período de observación. Ver "Fecha de observación  - `dateObservedTo`: Fecha y hora de finalización del período de observación. Ver "Fecha de observación  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `intensity`: Número total de vehículos detectados durante este período de observación  - `laneDirection`: Dirección habitual de viaje en el carril al que se refiere esta observación. Este atributo es útil cuando la observación no se refiere a ningún segmento de carretera, permitiendo conocer la dirección de viaje del flujo de tráfico observado. Enum:adelante, atrás'. Véase RoadSegment para una descripción de la semántica de estos valores.  - `laneId`: Identificador de carril. La identificación de carriles se realiza utilizando las convenciones definidas por la entidad RoadSegment que se basan en [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).  - `location`:   - `name`: El nombre de este artículo.  - `occupancy`: Fracción del tiempo de observación en que un vehículo ha estado ocupando el carril observado  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refRoadSegment`: Segmento de carretera en el que se ha hecho la observación. Referencia a una entidad de tipo Segmento de carretera  - `reversedLane`: Indica si el tráfico en el carril se invirtió durante el período de observación. La ausencia de este atributo significa que no hay reversión de carril  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser TrafficFlowObserved  - `vehicleSubType`: Permite especificar un subtipo de "tipo de vehículo", por ejemplo, si el "tipo de vehículo" está configurado como "camión", el "subtipo de vehículo" puede ser "OGV1" o "OGV2" para transmitir más información sobre el tipo exacto de vehículo.  - `vehicleType`: Tipo de vehículo desde el punto de vista de sus características estructurales. Enum:'agrícolaVehículo, bicicleta, autobús, minibús, coche, caravana, tranvía, cisterna, cocheConCaravana, cocheConRemolque, camión, ciclomotor, motocicleta, motocicletaConCoche lateral, motocooter, remolque, furgoneta, construcciónOrMaintenanceVehículo, carro, binTrolley, barredora, limpiezaTrolley    
Propiedades requeridas  
- `dateObserved`  - `id`  - `type`    
Esta entidad está principalmente asociada con los segmentos verticales de Automoción y Ciudad Inteligente y las aplicaciones de IO relacionadas.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TrafficFlowObserved:    
  description: 'An observation of traffic flow conditions at a certain place and time.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    averageGapDistance:    
      description: 'Average gap distance between consecutive vehicles'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'meter (m)'    
    averageHeadwayTime:    
      description: 'Average headway time. Headway time is the time ellapsed between two consecutive vehicles'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'second (s)'    
    averageVehicleLength:    
      description: |-    
        Average length of the vehicles transiting during    
            the observation period    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'meter (m)'    
    averageVehicleSpeed:    
      description: 'Average speed of the vehicles transiting during the observation period'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    congested:    
      description: ' Flags whether there was a traffic congestion during the observation period in the referred lane. The absence of this attribute means no traffic congestion'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean.    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`. [DateTime](https://schema.org/DateTime) or an ISO8601 interval represented as [Text](https://schema.org/Text)'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime.    
    dateObservedFrom:    
      description: 'Observation period start date and time. See `dateObserved`'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Datetime.    
    dateObservedTo:    
      description: 'Observation period end date and time. See `dateObserved`'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Datetime.    
    description:    
      description: 'A description of this item'    
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
      type: Property    
    intensity:    
      description: 'Total number of vehicles detected during this observation period'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    laneDirection:    
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. Enum:forward, backward''. See RoadSegment for a description of the semantics of these values.'    
      enum:    
        - forward    
        - backward    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    laneId:    
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancy:    
      description: 'Fraction of the observation time where a vehicle has been occupying the observed lane'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *trafficflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refRoadSegment:    
      description: 'Concerned road segment on which the observation has been made. Reference to an entity of type RoadSegment'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    reversedLane:    
      description: 'Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean.    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be TrafficFlowObserved'    
      enum:    
        - TrafficFlowObserved    
      type: Property    
    vehicleSubType:    
      description: 'It allows to specify a sub type of `vehicleType`, eg if the `vehicleType` is set to `Lorry` the `vehicleSubType` may be `OGV1` or `OGV2` to convey more information about the exact type of vehicle.'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
  required:    
    - id    
    - type    
    - dateObserved    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### TrafficFlowObserved NGSI V2 key-values Example  
Aquí hay un ejemplo de un TrafficFlowObserved en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
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
#### TrafficFlowObserved NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un TrafficFlowObserved en formato JSON como normalizado. Este es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### TrafficFlowObserved NGSI-LD key-values Example  
Aquí hay un ejemplo de un TrafficFlowObserved en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Valladolid",  
             "streetAddress": "Avenida de Salamanca",  
             "type": "PostalAddress"},  
 "averageHeadwayTime": 0.5,  
 "averageVehicleLength": 9.87,  
 "averageVehicleSpeed": 52.6,  
 "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",  
 "dateObservedFrom": {"@type": "DateTime", "@value": "2016-12-07T11:10:00Z"},  
 "dateObservedTo": {"@type": "DateTime", "@value": "2016-12-07T11:15:00Z"},  
 "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
 "intensity": 197,  
 "laneDirection": "forward",  
 "laneId": 1,  
 "location": {"coordinates": [[-4.73735395519672, 41.6538181849672],  
                              [-4.73414858659993, 41.6600594193478],  
                              [-4.73447575302641, 41.659585195093]],  
              "type": "LineString"},  
 "occupancy": 0.76,  
 "reversedLane": False,  
 "type": "TrafficFlowObserved"}  
```  
#### TrafficFlowObserved NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un TrafficFlowObserved en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
    "type": "TrafficFlowObserved",  
    "dateObserved": {  
        "type": "Property",  
        "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
    },  
    "laneDirection": {  
        "type": "Property",  
        "value": "forward"  
    },  
    "dateObservedFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-12-07T11:10:00Z"  
        }  
    },  
    "averageVehicleLength": {  
        "type": "Property",  
        "value": 9.87  
    },  
    "averageHeadwayTime": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "occupancy": {  
        "type": "Property",  
        "value": 0.76  
    },  
    "reversedLane": {  
        "type": "Property",  
        "value": false  
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
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Valladolid",  
            "addressCountry": "ES",  
            "streetAddress": "Avenida de Salamanca",  
            "type": "PostalAddress"  
        }  
    },  
    "averageVehicleSpeed": {  
        "type": "Property",  
        "value": 52.6  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
