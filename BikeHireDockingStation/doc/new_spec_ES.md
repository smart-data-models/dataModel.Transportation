Entidad: BikeHireDockingStation  
===============================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Bike Hire Docking Station**  

## Lista de propiedades  

`address`: La dirección postal.  `alternateName`: Un nombre alternativo para este artículo  `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `availableBikeNumber`:   `contactPoint`:   `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `freeSlotNumber`:   `id`:   `location`:   `name`: El nombre de este artículo.  `openingHours`:   `outOfServiceSlotNumber`:   `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `provider`:   `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `status`:   `totalSlotNumber`:   `type`: NGSI Tipo de entidad  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
BikeHireDockingStation:    
  description: 'Bike Hire Docking Station'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    availableBikeNumber:    
      minimum: 0    
      type: integer    
    contactPoint:    
      type: object    
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
      minimum: 0    
      type: integer    
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
      type: string    
    outOfServiceSlotNumber:    
      minimum: 0    
      type: integer    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *bikehiredockingstation_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    provider:    
      type: object    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    status:    
      enum:    
        - working    
        - outOfService    
        - withIncidence    
        - full    
        - almostFull    
        - empty    
        - almostEmpty    
      type: string    
    totalSlotNumber:    
      minimum: 1    
      type: integer    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - BikeHireDockingStation    
      type: string    
  required:    
    - id    
    - type    
  type: object    
```  
Aquí hay un ejemplo de una BikeHireDockingStation en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de una estación de carga BikeHireDockingStation en formato JSON normalizado. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores clave" y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de una BikeHireDockingStation en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Barcelona",  
             "streetAddress": "Gran Via Corts Catalanes,760",  
             "type": "PostalAddress"},  
 "availableBikeNumber": 20,  
 "freeSlotNumber": 10,  
 "id": "urn:ngsi-ld:BikeHireDockingStation:Bcn-BikeHireDockingStation-1",  
 "location": {"coordinates": [2.180042, 41.397952], "type": "Point"},  
 "status": "working",  
 "type": "BikeHireDockingStation"}  
```  
Este es un ejemplo de una estación de acoplamiento BikeHire en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
