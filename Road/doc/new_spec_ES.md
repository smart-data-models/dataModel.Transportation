Entidad: Carretera  
==================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad contiene una descripción geográfica y contextual armonizada de una carretera. Las carreteras están compuestas por una o más entidades del segmento de carreteras. Los segmentos de carretera suelen utilizarse para modelar las diferentes calzadas de las autopistas, por ejemplo. La presencia de carriles bici dedicados debe ser modelada utilizando también segmentos de carretera. Los segmentos de carretera también desempeñan un papel importante en la modelización de carreteras con segmentos heterogéneos, por ejemplo, segmentos en los que los límites de velocidad son diferentes. Esta entidad se asocia principalmente con los segmentos verticales de automoción y de ciudad inteligente y las aplicaciones de IO conexas. Este modelo de datos se ha desarrollado en cooperación con los operadores móviles y la GSMA**.  

## Lista de propiedades  

`address`: La dirección postal.  `alternateName`: Un nombre alternativo para este artículo  `annotations`:   `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `color`: El color del producto.  `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `id`:   `image`: Una imagen del artículo.  `length`:   `location`:   `name`: El nombre de este artículo.  `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `refRoadSegment`:   `responsible`:   `roadClass`:   `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `type`: NGSI Tipo de entidad  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
Road:    
  description: 'This entity contains a harmonised geographic and contextual description of a road. Roads are made up of one or more RoadSegment entities. Road segments are usually used to model the different carriageways of highways, for instance. The presence of dedicated bicycle lanes should be modelled using road segments as well. Road segments also play an important role when modelling roads with heterogeneous segments, for instance segments on which speed limits are different. This entity is primarily associated with the Automotive and Smart City vertical segments and related IoT applications. This data model has been developed in cooperation with mobile operators and the GSMA.'    
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
    annotations:    
      items:    
        type: string    
      type: array    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    color:    
      description: 'The color of the product.'    
      type: string    
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
    id:    
      anyOf: &road_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      description: 'An image of the item.'    
      format: uri    
      type: string    
    length:    
      minimum: 0    
      type: number    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *road_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refRoadSegment:    
      items:    
        anyOf: *road_-_properties_-_owner_-_items_-_anyof    
      type: array    
    responsible:    
      type: string    
    roadClass:    
      enum:    
        - motorway    
        - trunk    
        - primary    
        - secondary    
        - tertiary    
        - unclassified    
        - residential    
        - service    
      type: string    
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
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Road    
      type: string    
  required: []    
  type: object    
```  
Aquí hay un ejemplo de un camino en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Spain-Road-A62",  
  "type": "Road",  
  "name": "A-62",  
  "alternateName": "E-80",  
  "description": "Autovía de Castilla",  
  "roadClass": "motorway",  
  "length": 355,  
  "refRoadSegment": [  
    "Spain-RoadSegment-A62-0-355-forwards",  
    "Spain-RoadSegment-A62-0-355-backwards"  
  ],  
  "responsible": "Ministerio de Fomento - Gobierno de España"  
}  
```  
Aquí hay un ejemplo de un camino en formato JSON como normalizado. Es compatible con NGSI V2 cuando se utiliza `opciones=valores clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Spain-Road-A62",  
  "type": "Road",  
  "refRoadSegment": {  
    "type": "Relationship",  
    "value": [  
      "Spain-RoadSegment-A62-0-355-forwards",  
      "Spain-RoadSegment-A62-0-355-backwards"  
    ]  
  },  
  "roadClass": {  
    "value": "motorway"  
  },  
  "description": {  
    "value": "Autov\u00eda de Castilla"  
  },  
  "responsible": {  
    "value": "Ministerio de Fomento - Gobierno de Espa\u00f1a"  
  },  
  "length": {  
    "value": 355  
  },  
  "alternateName": {  
    "value": "E-80"  
  },  
  "name": {  
    "value": "A-62"  
  }  
}  
```  
Aquí hay un ejemplo de un camino en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "alternateName": "E-80",  
 "description": "Autovía de Castilla",  
 "id": "urn:ngsi-ld:Road:Spain-Road-A62",  
 "length": 355,  
 "name": "A-62",  
 "refRoadSegment": ["urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-0-355-forwards",  
                    "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-0-355-backwards"],  
 "responsible": "Ministerio de Fomento - Gobierno de España",  
 "roadClass": "motorway",  
 "type": "Road"}  
```  
Aquí hay un ejemplo de un camino en formato JSON-LD como normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Road:Spain-Road-A62",  
    "type": "Road",  
    "refRoadSegment": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-0-355-forwards",  
            "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-0-355-backwards"  
        ]  
    },  
    "roadClass": {  
        "type": "Property",  
        "value": "motorway"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Autovía de Castilla"  
    },  
    "responsible": {  
        "type": "Property",  
        "value": "Ministerio de Fomento - Gobierno de España"  
    },  
    "length": {  
        "type": "Property",  
        "value": 355  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "E-80"  
    },  
    "name": {  
        "type": "Property",  
        "value": "A-62"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
