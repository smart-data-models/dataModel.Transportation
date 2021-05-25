Entidad: BikeHireDockingStation  
===============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Estación de alquiler de bicicletas**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `availableBikeNumber`: El número de bicicletas disponibles en la estación de alquiler de bicicletas para ser alquiladas por los usuarios  - `contactPoint`: Punto de contacto del servicio de alquiler de bicicletas  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `freeSlotNumber`: El número de ranuras disponibles para devolver y aparcar bicicletas. Debe ser menor o igual que `totalSlotNumber`.  - `id`: Identificador único de la entidad  - `location`:   - `name`: El nombre de este artículo.  - `openingHours`: Horarios de apertura de la estación de acoplamiento  - `outOfServiceSlotNumber`: El número de ranuras que están fuera de servicio y no pueden ser utilizadas para alquilar o aparcar una bicicleta. Debe ser menor o igual que `totalSlotNumber`.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `provider`: Proveedor de servicios de alquiler de bicicletas  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `status`: Estado de la estación de alquiler de bicicletas. Enum:'working, outOfService, withIncidence, full, almostFull, empty, almostEmpty'. O cualquier otro específico de la aplicación.  - `totalSlotNumber`: El número total de ranuras que ofrece esta estación de acoplamiento de bicicletas  - `type`: Tipo de entidad NGSI. Tiene que ser BikeHireDockingStation    
Propiedades requeridas  
- `id`  - `type`    
Muchas ciudades ofrecen un sistema de alquiler de bicicletas para los ciudadanos. Estos pueden alquilar una bicicleta en base a diferentes tipos de abonos. Una estación de alquiler de bicicletas en la que los usuarios abonados pueden alquilar y devolver una bicicleta. Ofrece datos sobre sus principales características y la disponibilidad de bicicletas y plazas libres.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BikeHireDockingStation:    
  description: 'Bike Hire Docking Station'    
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
    availableBikeNumber:    
      description: 'The number of bikes available in the bike hire docking station to be hired by users'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    contactPoint:    
      description: 'Bike hire service contact point'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/contactPoint    
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
    description:    
      description: 'A description of this item'    
      type: Property    
    freeSlotNumber:    
      description: 'The number of slots available for returning and parking bikes. It must lower or equal than `totalSlotNumber`'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    id:    
      anyOf: &bikehiredockingstation_-_properties_-_owner_-_items_-_anyof    
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
    openingHours:    
      description: 'Opening hours of the docking station'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/openingHours.    
    outOfServiceSlotNumber:    
      description: 'The number of slots that are out of order and cannot be used to hire or park a bike. It must lower or equal than `totalSlotNumber`'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *bikehiredockingstation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    provider:    
      description: 'Bike hire service provider'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/provider.    
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
    status:    
      description: 'Status of the bike hire docking station. Enum:''working, outOfService, withIncidence, full, almostFull, empty, almostEmpty''. Or any other application specific.'    
      enum:    
        - almostEmpty    
        - almostFull    
        - empty    
        - full    
        - outOfService    
        - withIncidence    
        - working    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    totalSlotNumber:    
      description: 'The total number of slots offered by this bike docking station'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    type:    
      description: 'NGSI Entity type. It has to be BikeHireDockingStation'    
      enum:    
        - BikeHireDockingStation    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### BikeHireDockingStation NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un BikeHireDockingStation en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
        "id": "Bcn-BikeHireDockingStation-1",  
        "type": "BikeHireDockingStation",  
        "address": {  
            "addressCountry": "ES",  
            "addressLocality": "Barcelona",  
            "streetAddress": "Gran Via Corts Catalanes,760"  
        },  
        "availableBikeNumber": 20,  
        "freeSlotNumber": 10,  
        "location": {  
            "type": "Point",  
            "coordinates": [  
                2.180042,  
                41.397952  
            ]  
        },  
        "status": "working"  
}  
```  
#### BikeHireDockingStation NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de BikeHireDockingStation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",   
    "status": {  
        "value": "working"  
    },   
    "availableBikeNumber": {  
        "value": 20,  
        "metadata": {  
            "timestamp": {  
                "type": "DateTime",  
                "value": "2018-09-25T12:00:00"  
            }  
        }  
    },   
    "freeSlotNumber": {  
        "value": 10  
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
    }  
}  
```  
#### BikeHireDockingStation NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un BikeHireDockingStation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:BikeHireDockingStation:Bcn-BikeHireDockingStation-1",  
  "type": "BikeHireDockingStation",  
  "status": {  
    "type": "Property",  
    "value": "working"  
  },  
  "availableBikeNumber": {  
    "type": "Property",  
    "value": 20,  
    "observedAt": "2018-09-25T12:00:00Z"  
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
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Barcelona",  
      "streetAddress": "Gran Via Corts Catalanes,760",  
      "type": "PostalAddress"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BikeHireDockingStation NGSI-LD normalizado Ejemplo  
Este es un ejemplo de BikeHireDockingStation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Barcelona",  
    "streetAddress": "Gran Via Corts Catalanes,760",  
    "type": "PostalAddress"  
  },  
  "availableBikeNumber": 20,  
  "freeSlotNumber": 10,  
  "id": "urn:ngsi-ld:BikeHireDockingStation:Bcn-BikeHireDockingStation-1",  
  "location": {  
    "coordinates": [  
      2.180042,  
      41.397952  
    ],  
    "type": "Point"  
  },  
  "status": "working",  
  "type": "BikeHireDockingStation"  
}  
```  
