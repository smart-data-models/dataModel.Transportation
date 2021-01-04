Entidad: RoadSegment  
====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción geográfica y contextual armonizada de un segmento de carretera. Una colección de segmentos de carretera se utilizan para describir una carretera.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `allowedVehicleType`: Tipo(s) de vehículo(s) permitido(s) a transitar por este segmento de la carretera. Enum:'agrícolaVehículo, bicicleta, autobús, coche, caravana, cocheConCaravana, cocheConRemolque, construcciónOrMantenimientoVehículo, camión, ciclomotor, motocicleta, motocicletaConCoche lateral, motocooter, camión cisterna, remolque, furgoneta, cualquierVehículo'. Valores permitidos: Los siguientes valores definidos por _VehicleTypeEnum_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/):  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `category`: Permite transmitir las características adicionales de un segmento de carretera. Enum:'carretera, peaje, enlace'.  "Autopista": Indica si el segmento de la carretera sólo puede ser usado en una dirección. Si no está presente, significa que el segmento de carretera puede ser utilizado en ambas direcciones (hacia adelante y hacia atrás). Véase también [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). "Peaje": Indica si el segmento de la carretera está sujeto a peaje. "Enlace": Indica si este segmento de la carretera es un segmento de enlace auxiliar para salir o entrar en una carretera. Ver [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Cualquier otro valor significativo para una aplicación.  - `color`: El color del producto  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `endKilometer`: El número de kilómetros (medido desde el punto de inicio de la carretera) donde termina este segmento de la carretera.  - `endPoint`:   - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `laneUsage`: Este atributo puede utilizarse para transmitir parámetros específicos que describan cada carril. Debe contener una cadena por cada carril del segmento de carretera. El elemento 0 de la matriz debe contener la información del carril 1, y así sucesivamente. El formato de la cadena referida debe ser: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> es una cadena de texto con los siguientes valores permitidos: "Adelante". El carril se utiliza actualmente en la dirección "adelante". "Hacia atrás". El carril se utiliza actualmente en la dirección "hacia atrás". El único parámetro obligatorio es "dirección_de_calle". Si no se especifica, el resto de los parámetros pueden asumirse como iguales a los especificados a nivel de entidad.  - `length`: La longitud total de este segmento de carretera en kilómetros  - `location`:   - `maximumAllowedHeight`: Altura máxima permitida para los vehículos que transitan por este segmento de carretera  - `maximumAllowedSpeed`: Máxima velocidad permitida mientras se transita por este segmento de la carretera. Podrían aplicarse límites más restrictivos a tipos de vehículos específicos (camiones, caravanas, etc.)  - `maximumAllowedWeight`: Peso máximo permitido para los vehículos que transitan por este tramo de carretera  - `minimumAllowedSpeed`: La velocidad mínima permitida mientras se transita por este segmento de la carretera  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `refRoad`: Carretera a la que pertenece este segmento de la carretera.  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `startKilometer`: El número de kilómetros (medido desde el punto de inicio de la carretera) donde comienza este segmento de la carretera.  - `startPoint`:   - `totalLaneNumber`: Número total de carriles que ofrece este segmento de la carretera  - `type`: Tipo de entidad NGSI. Tiene que ser un segmento de carretera  - `width`: El ancho del segmento de la carretera.    
Propiedades requeridas  
- `allowedVehicleType`  - `endPoint`  - `id`  - `laneUsage`  - `name`  - `refRoad`  - `startPoint`  - `totalLaneNumber`  - `type`    
Los segmentos de carretera pueden incluir varios carriles. Este modelo de datos permite transmitir segmentos de carretera compuestos por carriles heterogéneos (diferentes en su uso, velocidad, altura, etc.). Los carriles se identifican utilizando números enteros entre 1 y n, siendo el número 1 el carril de la derecha cuando se avanza. La dirección de avance es la dirección indicada por el vector que va desde el punto de inicio del segmento hasta el punto final del mismo. Esta es la misma convención que la utilizada por OpenStreetMap. Esta entidad se asocia principalmente con los segmentos verticales de Automoción y Smart City y las aplicaciones de IO relacionadas. Este modelo de datos ha sido desarrollado en cooperación con los operadores móviles y la GSMA.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.'    
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
    allowedVehicleType:    
      description: 'Vehicle type(s) allowed to transit through this road segment. Enum:''agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle''. Allowed values: The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/):'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application.'    
      items:    
        enum:    
          - oneway    
          - toll    
          - link    
        type: string    
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
    endKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment ends. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level.'    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    length:    
      description: 'Total length of this road segment in kilometers'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: 'Kilometer (Km)'    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles transiting this road segment'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/height    
        units: 'Meter (m)'    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed while transiting this road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    maximumAllowedWeight:    
      description: 'Maximum allowed weight for vehicles transiting this road segment'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/weight    
        units: 'Kilogram (Kg)'    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refRoad:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Road to which this road segment belongs to. '    
      type: Property    
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
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    startPoint:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    type:    
      description: 'NGSI Entity type. It has to be RoadSegment'    
      enum:    
        - RoadSegment    
      type: Property    
    width:    
      description: 'Road''s segment width.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Meter (m)'    
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
</details>    
Las propiedades "laneUsage" y las que transmiten los parámetros máximos permitidos pueden ser dinámicas, por ejemplo, se puede cambiar temporalmente la dirección de un carril para mejorar las condiciones del tráfico.  
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave del segmento de carretera NGSI V2  
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
#### Segmento de carretera NGSI V2 normalizado Ejemplo  
He aquí un ejemplo de un segmento de carretera en formato JSON normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Segmento de carretera NGSI-LD valores clave Ejemplo  
Aquí hay un ejemplo de un segmento de carretera en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
#### Segmento de carretera NGSI-LD normalizado Ejemplo  
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
