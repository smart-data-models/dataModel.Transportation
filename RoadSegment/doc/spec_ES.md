Entidad: Segmento de carretera  
==============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Esta entidad contiene una descripción geográfica y contextual armonizada de un segmento de carretera. Se utiliza una colección de segmentos de carretera para describir una Carretera.**  

## Lista de propiedades  

- `address`: La dirección postal  - `allowedVehicleType`: Tipo(s) de vehículo(s) autorizado(s) a transitar por este segmento de carretera. Enum:'vehículo agrícola, bicicleta, autobús, coche, caravana, cocheConCaravana, cocheConRemolque, vehículoDeConstrucciónOdeMantenimiento, camión, ciclomotor, motocicleta, motocicletaConCocheLateral, motocarro, cisterna, remolque, furgoneta, cualquierVehículo'. Valores permitidos: Los siguientes valores definidos por _VehicleTypeEnum_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/):  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `category`: Permite transmitir características adicionales de un segmento de carretera. Enum:'oneway, toll, link'.  `oneway`: Indica si el segmento de carretera sólo puede utilizarse en una dirección. Si no está presente, significa que el segmento de carretera puede utilizarse en ambas direcciones (hacia delante y hacia atrás). Véase también [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Indica si el tramo de carretera está sujeto a peaje. `link` : Indica si este segmento de carretera es un segmento de enlace auxiliar para salir o entrar en una carretera. Véase [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Cualquier otro valor significativo para una aplicación.  - `color`: El color del producto  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `endKilometer`: El número de kilómetro (medido desde el punto de inicio de la carretera) donde termina este segmento de carretera.  - `endPoint`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `laneUsage`: Este atributo puede utilizarse para transmitir parámetros específicos que describan cada carril. Debe contener una cadena por carril del segmento de carretera. El elemento 0 de la matriz debe contener la información del carril 1, y así sucesivamente. El formato de la cadena referida debe ser: <carril_dirección>, <carril_velocidad mínima permitida>, <carril_velocidad máxima permitida>, <carril_altura máxima permitida>, <carril_altura máxima permitida>. <lane_direction> es una cadena de texto con los siguientes valores permitidos: `hacia adelante`. El carril se utiliza actualmente en la dirección "hacia adelante". hacia atrás". El carril se utiliza actualmente en la dirección "hacia atrás". El único parámetro obligatorio es `lane_direction`. Si no se especifica, se puede asumir que el resto de parámetros son iguales a los especificados a nivel de entidad.  - `length`: Longitud total de este segmento de carretera en kilómetros  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maximumAllowedHeight`: Altura máxima permitida para los vehículos que transitan por este tramo de carretera  - `maximumAllowedSpeed`: Velocidad máxima permitida al transitar por este segmento de carretera. Pueden aplicarse límites más restrictivos a determinados tipos de vehículos (camiones, caravanas, etc.)  - `maximumAllowedWeight`: Peso máximo permitido para los vehículos que transitan por este tramo de carretera  - `minimumAllowedSpeed`: Velocidad mínima permitida al transitar por este tramo de carretera  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refRoad`: Carretera a la que pertenece este segmento de carretera.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `startKilometer`: El número de kilómetro (medido desde el punto de inicio de la carretera) donde comienza este segmento de carretera.  - `startPoint`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `totalLaneNumber`: Número total de carriles que ofrece este segmento de carretera  - `type`: Tipo de entidad NGSI. Tiene que ser RoadSegment  - `width`: Anchura del segmento de la carretera.    
Propiedades requeridas  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`    
Los segmentos de carretera pueden incluir varios carriles. Este modelo de datos permite transmitir segmentos de carretera formados por carriles heterogéneos (diferentes en su uso, velocidad, altura, etc.). Los carriles se identifican utilizando números enteros entre 1 y n, siendo el número 1 el carril de la derecha cuando se avanza. El sentido de avance es la dirección denotada por el vector que va desde el punto de inicio del segmento hasta el punto final del mismo. Se trata de la misma convención que utiliza OpenStreetMap. Esta entidad está asociada principalmente a los segmentos verticales de Automoción y Ciudades Inteligentes y a las aplicaciones IoT relacionadas. Este modelo de datos se ha desarrollado en colaboración con los operadores de telefonía móvil y la GSMA.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.'    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application.'    
      items:    
        enum:    
          - oneway    
          - toll    
          - link    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    endKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment ends. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    endPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &roadsegment_-_properties_-_location_-_oneof    
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
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level.'    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    length:    
      description: 'Total length of this road segment in kilometers'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: 'Kilometer (Km)'    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
        units: 'Meter (m)'    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed while transiting this road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    maximumAllowedWeight:    
      description: 'Maximum allowed weight for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: 'Kilogram (Kg)'    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      description: 'Road to which this road segment belongs to.'    
      x-ngsi:    
        type: Relationship    
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
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    startPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RoadSegment'    
      enum:    
        - RoadSegment    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: 'Road''s segment width.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Meter (m)'    
  required:    
    - id    
    - name    
    - type    
    - refRoad    
    - startPoint    
    - endPoint    
    - allowedVehicleType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadSegment/schema.json    
  x-model-tags: ""    
  x-version: 0.2.0    
```  
</details>    
Las propiedades `laneUsage` y las que transmiten los parámetros máximos permitidos pueden ser dinámicas, por ejemplo, se puede cambiar temporalmente la dirección de un carril para mejorar las condiciones del tráfico.  
## Ejemplo de carga útil  
#### RoadSegment NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un RoadSegment en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": ["oneway"],  
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
#### RoadSegment NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un RoadSegment en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": ["oneway"]  
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
#### RoadSegment NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un RoadSegment en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "type": "Property",  
    "value": [  
      "oneway"  
    ]  
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
    "value": "Valladolid-Due\u00f1as"  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### RoadSegment NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un RoadSegment en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "allowedVehicleType": [  
    "car",  
    "bus",  
    "lorry",  
    "trailer",  
    "tanker",  
    "van",  
    "caravan"  
  ],  
  "category": [  
    "oneway"  
  ],  
  "endPoint": {  
    "coordinates": [  
      -4.55167335377909,  
      41.8570461783071  
    ],  
    "type": "Point"  
  },  
  "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
  "laneUsage": [  
    "forward",  
    "forward"  
  ],  
  "location": {  
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
    ],  
    "type": "LineString"  
  },  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "name": "Valladolid-Due\u00f1as",  
  "refRoad": "urn:ngsi-ld:Road:Spain-Road-A62",  
  "source": "http://wwww.openstreetmap.org",  
  "startPoint": {  
    "coordinates": [  
      -4.7299180606009,  
      41.6844918725019  
    ],  
    "type": "Point"  
  },  
  "totalLaneNumber": 2,  
  "type": "RoadSegment"  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud