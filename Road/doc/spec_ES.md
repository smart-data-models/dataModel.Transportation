Entidad: Carretera  
==================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/Road/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esta entidad contiene una descripción geográfica y contextual armonizada de una carretera.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `color`: El color del producto  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `length`: Longitud total de esta carretera en kilómetros  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refRoadSegment`: Segmentos de carretera que definen esta carretera. Lista de referencias a entidades de tipo RoadSegment  - `responsible`: Responsable de la carretera, es decir, el organismo o empresa encargada de su mantenimiento  - `roadClass`: La clasificación de esta carretera. Enum:'autopista, primaria, residencial, secundaria, de servicio, terciaria, troncal, sin clasificar'.  Valores permitidos: Los descritos por [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Key:highway).  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI. Tiene que ser Road    
Propiedades requeridas  
Las carreteras están formadas por una o varias entidades RoadSegment. Los segmentos de carretera suelen utilizarse para modelar las diferentes calzadas de las autopistas, por ejemplo. La presencia de carriles exclusivos para bicicletas debe modelarse también mediante segmentos de carretera. Los segmentos de carretera también desempeñan un papel importante cuando se modelan carreteras con segmentos heterogéneos, por ejemplo, segmentos en los que los límites de velocidad son diferentes. Esta entidad está asociada principalmente a los segmentos verticales de Automoción y Ciudad Inteligente y a las aplicaciones IoT relacionadas. Este modelo de datos se ha desarrollado en colaboración con los operadores de telefonía móvil y la GSMA.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Road:    
  description: 'This entity contains a harmonised geographic and contextual description of a road.'    
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
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    length:    
      description: 'Total length of this road in kilometers'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: 'Kilometer (Km)'    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *road_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refRoadSegment:    
      description: 'Road segments which define this road. List of references to entities of type RoadSegment'    
      items:    
        anyOf: *road_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    responsible:    
      description: 'Responsible for the road i.e. the organism or company in charge of its maintenance'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    roadClass:    
      description: 'The classification of this road. Enum:''motorway, primary, residential, secondary, service, tertiary, trunk, unclassified''.  Allowed values: Those described by [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Key:highway).'    
      enum:    
        - motorway    
        - primary    
        - residential    
        - secondary    
        - service    
        - tertiary    
        - trunk    
        - unclassified    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'NGSI Entity type. It has to be Road'    
      enum:    
        - Road    
      type: Property    
  required: []    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### Road NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una carretera en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Camino NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de una carretera en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Camino NGSI-LD valores-clave Ejemplo  
Aquí hay un ejemplo de una carretera en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
    "value": "Autov\u00eda de Castilla"  
  },  
  "responsible": {  
    "type": "Property",  
    "value": "Ministerio de Fomento - Gobierno de Espa\u00f1a"  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Camino NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una carretera en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "alternateName": "E-80",  
  "description": "Autov\u00eda de Castilla",  
  "id": "urn:ngsi-ld:Road:Spain-Road-A62",  
  "length": 355,  
  "name": "A-62",  
  "refRoadSegment": [  
    "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-0-355-forwards",  
    "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-0-355-backwards"  
  ],  
  "responsible": "Ministerio de Fomento - Gobierno de Espa\u00f1a",  
  "roadClass": "motorway",  
  "type": "Road"  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud