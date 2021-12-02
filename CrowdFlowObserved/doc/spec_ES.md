Entidad: CrowdFlowObserved  
==========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/CrowdFlowObserved/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **CrowdFlowObserved**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `averageCrowdSpeed`: Velocidad media de la multitud que transita durante el periodo de observación  - `averageHeadwayTime`: Tiempo medio de recorrido. El tiempo de recorrido es el tiempo  
    transcurrido entre dos personas consecutivas  - `congested`: Indica si hubo congestión de público durante el periodo de observación en el pasillo referido. La ausencia de este atributo significa que no hubo congestión de multitudes  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved`: La fecha y la hora de esta observación en formato ISO8601 UTC. Puede representarse mediante un instante de tiempo específico o mediante un intervalo ISO8601. Como solución a la falta de soporte de Orion Context Broker para los intervalos de fecha, se pueden utilizar dos atributos separados: `dateObservedFrom`, `dateObservedTo`.  - `dateObservedFrom`: Fecha y hora de inicio del periodo de observación. Véase `fechaObservada`.  - `dateObservedTo`: Fecha y hora de finalización del periodo de observación. Véase `fechaObservada`.  - `description`: Una descripción de este artículo  - `direction`: Sentido habitual de la marcha en el paseo al que se refiere esta observación con respecto al centro de la ciudad. Enum:'entrada, salida'  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `occupancy`: Fracción del tiempo de observación en el que una persona ha estado ocupando el pasillo observado  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `peopleCount`: Tramo de carretera afectado en el que se ha realizado la observación  - `refRoadSegment`: Tramo de carretera afectado en el que se ha realizado la observación  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI. Tiene que ser CrowdFlowObserved    
Propiedades requeridas  
- `dateObserved`  - `id`  - `type`    
Una observación relacionada con el movimiento de personas en un lugar y momento determinados.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CrowdFlowObserved:    
  description: CrowdFlowObserved    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    averageCrowdSpeed:    
      description: 'Average speed of the crowd transiting during the observation period'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h).'    
    averageHeadwayTime:    
      description: |-    
        Average headway time. Headway time is the time    
            elapsed between two consecutive persons    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'second (s)'    
    congested:    
      description: 'Flags whether there was a crowd congestion during the observation period in the referred walkway. The absence of this attribute means no crowd congestion'    
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
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL.    
    dateObservedFrom:    
      description: 'Observation period start date and time. See `dateObserved`.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateObservedTo:    
      description: 'Observation period end date and time. See `dateObserved`.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime.    
    description:    
      description: 'A description of this item'    
      type: Property    
    direction:    
      description: 'Usual direction of travel in the walkway referred by this observation with respect to the city center. Enum:''inbound, outbound'''    
      enum:    
        - inbound    
        - outbound    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    id:    
      anyOf: &crowdflowobserved_-_properties_-_owner_-_items_-_anyof    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancy:    
      description: 'Fraction of the observation time where a person has been occupying the observed walkway'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number)    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *crowdflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    peopleCount:    
      description: 'Concerned road segment on which the observation has been made'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
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
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL.    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be CrowdFlowObserved'    
      enum:    
        - CrowdFlowObserved    
      type: Property    
  required:    
    - id    
    - type    
    - dateObserved    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### CrowdFlowObserved NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un CrowdFlowObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "dateObserved": "2018-08-07T11:10:00/2018-08-07T11:15:00",  
  "dateObservedFrom": "2018-08-07T11:10:00Z",  
  "dateObservedTo": "2018-08-07T11:15:00Z",  
  "peopleCount": 100,  
  "averageHeadwayTime": 5,  
  "congested": false,  
  "direction": "inbound",  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.73735395519672, 41.6538181849672],  
      [-4.73414858659993, 41.6600594193478],  
      [-4.73447575302641, 41.659585195093]  
    ]  
  }  
}  
```  
#### CrowdFlowObserved NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un CrowdFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "dateObserved": {  
    "value": "2018-08-07T11:10:00/2018-08-07T11:15:00"  
  },  
  "direction": {  
    "value": "inbound"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2018-08-07T11:10:00Z"  
  },  
  "peopleCount": {  
    "value": 100  
  },  
  "averageHeadwayTime": {  
    "value": 5  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2018-08-07T11:15:00Z"  
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
  "congested": {  
    "value": false  
  }  
}  
```  
#### CrowdFlowObserved NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un CrowdFlowObserved en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": "2018-08-07T11:10:00/2018-08-07T11:15:00"  
  },  
  "direction": {  
    "type": "Property",  
    "value": "inbound"  
  },  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-08-07T11:10:00Z"  
    }  
  },  
  "peopleCount": {  
    "type": "Property",  
    "value": 100  
  },  
  "averageHeadwayTime": {  
    "type": "Property",  
    "value": 5  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-08-07T11:15:00Z"  
    }  
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
  "congested": {  
    "type": "Property",  
    "value": false  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### CrowdFlowObserved NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un CrowdFlowObserved en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "averageHeadwayTime": 5,  
  "congested": false,  
  "dateObserved": "2018-08-07T11:10:00/2018-08-07T11:15:00",  
  "dateObservedFrom": {  
    "@type": "DateTime",  
    "@value": "2018-08-07T11:10:00Z"  
  },  
  "dateObservedTo": {  
    "@type": "DateTime",  
    "@value": "2018-08-07T11:15:00Z"  
  },  
  "direction": "inbound",  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
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
  "peopleCount": 100,  
  "type": "CrowdFlowObserved"  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud