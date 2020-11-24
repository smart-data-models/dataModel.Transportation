Entidad: RoadSegment  
====================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad contiene una descripción geográfica y contextual armonizada de un segmento de carretera. Se utiliza una colección de segmentos de carretera para describir una carretera. Los segmentos de carretera pueden incluir varios carriles. Este modelo de datos permite transmitir segmentos de carretera compuestos por carriles heterogéneos (diferentes en su uso, velocidad, altura, etc.). Los carriles se identifican utilizando números enteros entre 1 y n, siendo el número 1 el carril de la derecha cuando se avanza. La dirección de avance es la dirección indicada por el vector que va desde el punto de inicio del segmento hasta el punto final del mismo. Esta es la misma convención que la utilizada por OpenStreetMap. Esta entidad se asocia principalmente con los segmentos verticales de Automoción y Smart City y las aplicaciones de IO relacionadas. Este modelo de datos se ha desarrollado en cooperación con los operadores móviles y la GSMA**.  

## Lista de propiedades  

`address`: La dirección postal.  `allowedVehicleType`:   `alternateName`: Un nombre alternativo para este artículo  `annotations`:   `areaServed`: La zona geográfica donde se presta un servicio o se ofrece un artículo.  `category`:   `color`: El color del producto.  `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `endKilometer`:   `endPoint`:   `id`:   `image`: Una imagen del artículo.  `laneUsage`:   `length`:   `location`:   `maximumAllowedHeight`:   `maximumAllowedSpeed`:   `maximumAllowedWeight`:   `minimumAllowedSpeed`:   `name`: El nombre de este artículo.  `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `refRoad`:   `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `startKilometer`:   `startPoint`:   `totalLaneNumber`:   `type`: NGSI Tipo de entidad  `width`:   ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road. Road segments can include several lanes. This data model allows to convey road segments made up of heterogeneous lanes (different in their usage, speed, height, etc.). Lanes are identified by using integer numbers between 1 and n, being number 1 the lane to the right when going forwards. The forward direction is the direction denoted by the vector which goes from the segment"s start point to the segment"s end point. This is the same convention as the one used by OpenStreetMap. This entity is primarily associated with the Automotive and Smart City vertical segments and related IoT applications. This data model has been developed in cooperation with mobile operators and the GSMA.'    
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
    allowedVehicleType:    
      items:    
        enum:    
          - agriculturalVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - tanker    
          - trailer    
          - van    
          - anyVehicle    
        type: string    
      type: array    
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
    category:    
      enum:    
        - oneway    
        - toll    
        - link    
      type: string    
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
    endKilometer:    
      minimum: 0    
      type: number    
    endPoint:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: &roadsegment_-_properties_-_location_-_oneof    
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
    id:    
      anyOf: &roadsegment_-_properties_-_owner_-_items_-_anyof    
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
    laneUsage:    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: array    
    length:    
      minimum: 0    
      type: number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    maximumAllowedHeight:    
      minimum: 0    
      type: number    
    maximumAllowedSpeed:    
      minimum: 0    
      type: number    
    maximumAllowedWeight:    
      minimum: 0    
      type: number    
    minimumAllowedSpeed:    
      minimum: 0    
      type: number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refRoad:    
      anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
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
    startKilometer:    
      minimum: 0    
      type: number    
    startPoint:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    totalLaneNumber:    
      minimum: 1    
      type: number    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - RoadSegment    
      type: string    
    width:    
      minimum: 0    
      type: number    
  required:    
    - id    
    - name    
    - type    
    - refRoad    
    - startPoint    
    - endPoint    
    - allowedVehicleType    
    - totalLaneNumber    
    - laneUsage    
  type: object    
```  
Aquí hay un ejemplo de un segmento de carretera en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": "oneway",  
  "refRoad": "Spain-Road-A62",  
  "totalLaneNumber": 2,  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "startPoint": {  
    "type": "Point",  
    "coordinates": [-4.7299180606009, 41.6844918725019]  
  },  
  "endPoint": {  
    "type": "Point",  
    "coordinates": [-4.55167335377909, 41.8570461783071]  
  },  
  "allowedVehicleType": [  
    "car",  
    "bus",  
    "lorry",  
    "trailer",  
    "tanker",  
    "van",  
    "caravan"  
  ],  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.7299180606009, 41.6844918725019],  
      [-4.72855890957602, 41.6860596957855],  
      [-4.5520357341647, 41.8569278186523],  
      [-4.55167335377909, 41.8570461783071]  
    ]  
  },  
  "laneUsage": ["forward", "forward"],  
  "source": "http://wwww.openstreetmap.org"  
}  
```  
He aquí un ejemplo de un segmento de carretera en formato JSON normalizado. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": "oneway"  
  },  
  "endPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.55167335377909, 41.8570461783071]  
    }  
  },  
  "name": {  
    "value": "Valladolid-Due\u00f1as"  
  },  
  "startPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.7299180606009, 41.6844918725019]  
    }  
  },  
  "allowedVehicleType": {  
    "value": ["car", "bus", "lorry", "trailer", "tanker", "van", "caravan"]  
  },  
  "source": {  
    "value": "http://wwww.openstreetmap.org"  
  },  
  "totalLaneNumber": {  
    "value": 2  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [-4.7299180606009, 41.6844918725019],  
        [-4.72855890957602, 41.6860596957855],  
        [-4.5520357341647, 41.8569278186523],  
        [-4.55167335377909, 41.8570461783071]  
      ]  
    }  
  },  
  "minimumAllowedSpeed": {  
    "value": 60  
  },  
  "refRoad": {  
    "type": "Relationship",  
    "value": "Spain-Road-A62"  
  },  
  "maximumAllowedSpeed": {  
    "value": 120  
  },  
  "laneUsage": {  
    "value": ["forward", "forward"]  
  }  
}  
```  
Aquí hay un ejemplo de un segmento de carretera en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "allowedVehicleType": ["car",  
                        "bus",  
                        "lorry",  
                        "trailer",  
                        "tanker",  
                        "van",  
                        "caravan"],  
 "category": "oneway",  
 "endPoint": {"coordinates": [-4.55167335377909, 41.8570461783071],  
              "type": "Point"},  
 "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
 "laneUsage": ["forward", "forward"],  
 "location": {"coordinates": [[-4.7299180606009, 41.6844918725019],  
                              [-4.72855890957602, 41.6860596957855],  
                              [-4.5520357341647, 41.8569278186523],  
                              [-4.55167335377909, 41.8570461783071]],  
              "type": "LineString"},  
 "maximumAllowedSpeed": 120,  
 "minimumAllowedSpeed": 60,  
 "name": "Valladolid-DueÃ±as",  
 "refRoad": "urn:ngsi-ld:Road:Spain-Road-A62",  
 "source": "http://wwww.openstreetmap.org",  
 "startPoint": {"coordinates": [-4.7299180606009, 41.6844918725019],  
                "type": "Point"},  
 "totalLaneNumber": 2,  
 "type": "RoadSegment"}  
```  
He aquí un ejemplo de un segmento de carretera en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
    "type": "RoadSegment",  
    "category": {  
        "type": "Property",  
        "value": "oneway"  
    },  
    "endPoint": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -4.55167335377909,  
                41.8570461783071  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Valladolid-DueÃ±as"  
    },  
    "startPoint": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -4.7299180606009,  
                41.6844918725019  
            ]  
        }  
    },  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": [  
            "car",  
            "bus",  
            "lorry",  
            "trailer",  
            "tanker",  
            "van",  
            "caravan"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://wwww.openstreetmap.org"  
    },  
    "totalLaneNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "LineString",  
            "coordinates": [  
                [  
                    -4.7299180606009,  
                    41.6844918725019  
                ],  
                [  
                    -4.72855890957602,  
                    41.6860596957855  
                ],  
                [  
                    -4.5520357341647,  
                    41.8569278186523  
                ],  
                [  
                    -4.55167335377909,  
                    41.8570461783071  
                ]  
            ]  
        }  
    },  
    "minimumAllowedSpeed": {  
        "type": "Property",  
        "value": 60  
    },  
    "refRoad": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Road:Spain-Road-A62"  
    },  
    "maximumAllowedSpeed": {  
        "type": "Property",  
        "value": 120  
    },  
    "laneUsage": {  
        "type": "Property",  
        "value": [  
            "forward",  
            "forward"  
        ]  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
