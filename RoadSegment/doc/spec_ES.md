<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: RoadSegment  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Esta entidad contiene una descripción geográfica y contextual armonizada de un segmento de carretera. Se utiliza una colección de segmentos de carretera para describir una Carretera.**  
versión: 0.4.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `agency_name[string]`: El campo agency_name contiene el nombre completo de la agencia u organización responsable del mantenimiento de la entidad considerada. Igual que: Campo 'agency_name' de la definición de campo estático GTFS - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `allowedVehicleType[array]`: Tipo(s) de vehículo(s) autorizado(s) a transitar por este segmento de carretera. Enum:'vehículo agrícola, bicicleta, autobús, coche, caravana, cocheConCaravana, cocheConRemolque, vehículoDeConstrucciónOdeMantenimiento, camión, ciclomotor, motocicleta, motocicletaConCocheLateral, motocarro, cisterna, remolque, furgoneta, cualquierVehículo'. Valores permitidos: Los siguientes valores definidos por _VehicleTypeEnum_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/):  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Un nombre alternativo para este artículo  - `annotations[array]`: Anotaciones sobre el artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `bridgeCount[number]`: Número de puentes en el segmento de carretera correspondiente a esta observación. Toma 0 (cero) como valor cuando el segmento de carretera no tiene puentes.  - `carriagewayLength[number]`: Longitud total de la vía del segmento de carretera correspondiente a esta observación.  - `carriagewayWidth[number]`: Anchura total de la calzada del segmento de carretera correspondiente a esta observación.  - `category[array]`: Permite transmitir características adicionales de un segmento de carretera. Enum:'oneway, toll, link'.  `oneway`: Indica si el segmento de carretera sólo puede utilizarse en una dirección. Si no está presente, significa que el segmento de carretera puede utilizarse en ambas direcciones (hacia delante y hacia atrás). Véase también [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Indica si el tramo de carretera está sujeto a peaje. `link` : Indica si este segmento de carretera es un segmento de enlace auxiliar para salir o entrar en una carretera. Véase [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Cualquier otro valor significativo para una aplicación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: El color del producto  . Model: [https://schema.org/color](https://schema.org/color)- `culvertCount[number]`: Número de alcantarillas que prevalecen en el trazado de la carretera correspondiente a esta observación.  - `cyclePathLeftHeight[number]`: Altura del carril bici en el borde izquierdo de la carretera correspondiente a esta observación.  - `cyclePathLeftWidth[number]`: Anchura del carril bici en el borde izquierdo de la carretera correspondiente a esta observación.  - `cyclePathMaterial[string]`: Material de construcción utilizado para la colocación del carril bici en los laterales de la carretera correspondiente a esta observación.  - `cyclePathPlacement[string]`: Describe la ubicación del carril bici a lo largo del segmento de carretera correspondiente a esta observación. Enum:' ['DERECHA, IZQUIERDA, AMBAS, NOT_AVAILABLE'  - `cyclePathRightHeight[number]`: Altura del carril bici en el borde derecho de la carretera correspondiente a esta observación.  - `cyclePathRightWidth[number]`: Anchura del carril bici en el borde derecho de la carretera correspondiente a esta observación.  - `dataDescriptor[*]`: URI que apunta a la entidad descriptora de datos  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `endKilometer[number]`: El número de kilómetro (medido desde el punto de inicio de la carretera) donde termina este segmento de carretera.  . Model: [https://schema.org/Number](https://schema.org/Number)- `endPoint[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `id[*]`: Identificador único de la entidad  - `image[string]`: Una imagen del artículo  . Model: [https://schema.org/URL](https://schema.org/URL)- `laneInfo[object]`: Describe los aspectos de los carriles de la carretera correspondientes a esta observación.  - `laneUsage[array]`: Este atributo puede utilizarse para transmitir parámetros específicos que describan cada carril. Debe contener una cadena por carril del segmento de carretera. El elemento 0 de la matriz debe contener la información del carril 1, y así sucesivamente. El formato de la cadena referida debe ser <carril_dirección>, <carril_velocidad mínima permitida>, <carril_velocidad máxima permitida>, <carril_altura máxima permitida>, <carril_altura máxima permitida>. <lane_direction> es una cadena de texto con los siguientes valores permitidos: `hacia adelante`. El carril se utiliza actualmente en la dirección "hacia adelante". hacia atrás". El carril se utiliza actualmente en la dirección "hacia atrás". El único parámetro obligatorio es `lane_direction`. Si no se especifica, se puede asumir que el resto de parámetros son iguales a los especificados a nivel de entidad.  . Model: [https://schema.org/Text](https://schema.org/Text)- `length[number]`: Longitud total de este segmento de carretera en kilómetros  . Model: [https://schema.org/length](https://schema.org/length)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maximumAllowedHeight[number]`: Altura máxima permitida para los vehículos que transitan por este tramo de carretera  . Model: [https://schema.org/height](https://schema.org/height)- `maximumAllowedSpeed[number]`: Velocidad máxima permitida en el segmento de carretera. Pueden aplicarse límites más restrictivos a determinados tipos de vehículos (camiones, caravanas, etc.)  . Model: [https://schema.org/Number](https://schema.org/Number)- `maximumAllowedWeight[number]`: Peso máximo permitido para los vehículos que transitan por este tramo de carretera  . Model: [https://schema.org/weight](https://schema.org/weight)- `maximumAllowedWidth[number]`: Anchura máxima permitida para los vehículos que utilizan la entidad correspondiente a esta observación.  - `medianHeight[number]`: Altura de la mediana o de la mediana de la carretera correspondiente a esta observación.  - `medianLength[number]`: Longitud de la mediana o de la mediana de la carretera correspondiente a esta observación.  - `medianWidth[number]`: Anchura de la mediana o de la mediana de la carretera correspondiente a esta observación.  - `minimumAllowedSpeed[number]`: Velocidad mínima permitida al transitar por este tramo de carretera  . Model: [https://schema.org/Number](https://schema.org/Number)- `municipalityInfo[object]`: Información del municipio correspondiente a esta observación.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pedestrianPathLeftHeight[number]`: Altura de la pasarela colocada en el borde izquierdo de la carretera correspondiente a esta observación.  - `pedestrianPathLeftWidth[number]`: Anchura de la pasarela colocada en el borde izquierdo de la carretera correspondiente a esta observación.  - `pedestrianPathMaterial[string]`: Material de construcción utilizado para la colocación de la pasarela / senda en los lados de la carretera correspondiente a esta observación.  - `pedestrianPathPlacement[string]`: Describe la presencia y la ubicación del peatón a lo largo del segmento de carretera correspondiente a esta observación. Enum:'DERECHA, IZQUIERDA, AMBAS, NOT_AVAILABLE'  - `pedestrianPathRightHeight[number]`: Altura de la pasarela colocada en el borde derecho de la carretera correspondiente a esta observación.  - `pedestrianPathRightWidth[number]`: Anchura de la pasarela colocada en el borde derecho de la carretera correspondiente a esta observación.  - `refRoad[*]`: Carretera a la que pertenece este segmento de carretera.  - `rightOfWayWidth[number]`: El derecho de paso (RoW) es la superficie total de terreno disponible para la carretera. Su anchura permite acoger el paso de carruajes + otras necesidades + la futura ampliación, a lo largo de la alineación de la carretera.  - `roadClass[string]`: El tipo de carretera correspondiente a esta observación. Enum: [OTRA_CARRETERA_PÚBLICA, CARRETERA_PRIVADA, CARRETERA_MENOR_CIUDAD, CARRETERA_MÁS_DISTRITAL, CARRETERA_NACIONAL, CARRETERA_DE_SERVICIO, CARRETERA_ESTATAL, OTRA CARRETERA_DISTRITAL, CARRETERA_PORTA].  - `roadDirection[string]`: Representa la dirección a la que se dirige la carretera. Enum:' ['N, S, E, W'. Los valores N,S,E,W representan el norte, el sur, el este y el oeste respectivamente.  - `roadId[string]`: Representación interna única de la carretera correspondiente a esta observación.  - `roadMaterial[string]`: El material de construcción utilizado para la colocación de la calzada correspondiente a esta observación. Por ejemplo, hormigón, tierra, alquitrán, etc.  - `roadName[string]`: El nombre de la carretera correspondiente a esta observación.  - `roadWork[string]`: Motivos de la obra en carretera en caso de intervención urgente. Una combinación de estos valores. Enum:'COLAPSO, DERRUMBO, INCENDIO, INUNDACIÓN, DERRUMBO DE GAS, DESLIZAMIENTO DE TIERRAS, OTROS, CORTE DE ENERGÍA, DESPLAZAMIENTO DE ROCA, AGUANTAMIENTO, DERRUMBO'.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startKilometer[number]`: El número de kilómetro (medido desde el punto de inicio de la carretera) donde comienza este segmento de carretera.  . Model: [https://schema.org/Number](https://schema.org/Number)- `startPoint[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `status[string]`: Condiciones específicas de conducción en el segmento de carretera. Utilice statusDescription para obtener información adicional. Enum: `abierto, cerrado, limitado`.  `abierto`: el segmento de carretera puede utilizarse en toda su capacidad prevista, `cerrado`: no es posible el tráfico, por ejemplo, debido a obras en la carretera, un puente o una esclusa abiertos, o cualquier otro evento que impida el tráfico. Limitado": el tráfico es posible, pero no en toda su capacidad.  - `statusDescription[string]`: Información adicional al atributo de estado.  - `totalCyclePathWidth[number]`: Anchura total del carril bici presente en la carretera correspondiente a esta observación.  - `totalLaneNumber[number]`: Número total de carriles que ofrece este segmento de carretera  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `totalPedestrianPathLength[number]`: Longitud total de la pasarela presente en la carretera correspondiente a esta observación.  - `totalPedestrianPathWidth[number]`: Anchura total de la pasarela presente en la carretera correspondiente a esta observación.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser RoadSegment  - `width[number]`: Anchura del segmento de la carretera.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Los segmentos de carretera pueden incluir varios carriles. Este modelo de datos permite transmitir segmentos de carretera formados por carriles heterogéneos (diferentes en su uso, velocidad, altura, etc.). Los carriles se identifican utilizando números enteros entre 1 y n, siendo el número 1 el carril de la derecha cuando se avanza. El sentido de avance es la dirección denotada por el vector que va desde el punto de inicio del segmento hasta el punto final del mismo. Se trata de la misma convención que utiliza OpenStreetMap. Esta entidad está asociada principalmente a los segmentos verticales de Automoción y Ciudades Inteligentes y a las aplicaciones IoT relacionadas. Este modelo de datos se ha desarrollado en colaboración con los operadores de telefonía móvil y la GSMA.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
    agency_name:    
      description: "The agency_name field contains the full name of the agency or organisation responsible for maintenance of the entity under consideration. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
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
    bridgeCount:    
      description: 'Number of bridges in the road segment corresponding to this observation. Takes 0 (zero) as the value when the road segment has no bridges.'    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayLength:    
      description: 'Total length of the carriage way of the road segment corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayWidth:    
      description: 'Total width of the carriage way of the road segment corresponding to this observation.'    
      type: number    
      x-ngsi:    
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
    culvertCount:    
      description: 'Number of culverts prevalent in the trace of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftHeight:    
      description: 'Height of the cycle track on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftWidth:    
      description: 'Width of the cycle track on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathMaterial:    
      description: 'Construction material used for laying the cycle path on the sides of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathPlacement:    
      description: 'Describes the placement of cycle track along the road segment corresponding to this observation. Enum:'' [''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      enum:    
        - BOTH    
        - LEFT    
        - NOT_AVAILABLE    
        - RIGHT    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathRightHeight:    
      description: 'Height of the cycle track on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathRightWidth:    
      description: 'Width of the cycle track on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    dataDescriptor:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'URI pointing to the data-descriptor entity'    
      x-ngsi:    
        type: Relationship    
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
    laneInfo:    
      description: 'Describes the aspects of lanes of the road corresponding to this observation.'    
      properties:    
        laneDirection:    
          description: 'Property. Describes the direction in which vehicles are plying on the lane corresponding to this observation. Enum:''FORWARD, BACKWARD, INBOUND, OUTBOUND, RIGHT, LEFT'''    
          enum:    
            - BACKWARD    
            - FORWARD    
            - INBOUND    
            - LEFT    
            - OUTBOUND    
            - RIGHT    
          laneLength:    
            description: 'Property. Length of the lane corresponding to this observation.'    
            type: number    
          laneWidth:    
            description: 'Property. Width of the lane corresponding to this observation.'    
            type: number    
          type: string    
        laneId:    
          description: 'Property. Unique identification number of the lane corresponding to this observation.'    
          type: number    
      type: object    
      x-ngsi:    
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
      description: 'Maximum allowed speed plying the road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
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
    maximumAllowedWidth:    
      description: 'Maximum allowed width for vehicles using the entity corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianHeight:    
      description: 'Height of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianLength:    
      description: 'Length of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    medianWidth:    
      description: 'Width of the median or central reservation in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        cityId:    
          description: 'Property. Model:''https://schema.org/Text''. City ID corresponding to this observation.'    
          type: string    
        cityName:    
          description: 'Property. Model:''https://schema.org/Text''. City name corresponding to this observation'    
          type: string    
        district:    
          description: 'Property. Model:''https://schema.org/Text''. District name corresponding to this observation.'    
          type: string    
        stateName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the state corresponding to this observation.'    
          type: string    
        ulbName:    
          description: 'Property. Model:''https://schema.org/Text''. Name of the Urban Local Body corresponding to this observation.'    
          type: string    
        wardId:    
          description: 'Property. Model:''https://schema.org/Text''. Ward ID corresponding to this observation.'    
          type: string    
        wardName:    
          description: 'Property. Model:''https://schema.org/Text''. Ward name corresponding to this observation.'    
          type: string    
        wardNum:    
          description: 'Property. Model:''https://schema.org/Number''. Ward number corresponding to this observation.'    
          type: number    
        zoneId:    
          description: 'Property. Model:''https://schema.org/Text''. Zone ID corresponding to this observation.'    
          type: string    
        zoneName:    
          description: 'Property. Model:''https://schema.org/Text''. Zone name corresponding to this observation.'    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    pedestrianPathLeftHeight:    
      description: 'Height of the walkway placed on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathLeftWidth:    
      description: 'Width of the walkway placed on the left edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathMaterial:    
      description: 'Construction material used for laying the walkway / footpath on the sides of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathPlacement:    
      description: 'Describes the presence and placement of pedestrian along the road segment corresponding to this observation. Enum:''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathRightHeight:    
      description: 'Height of the walkway placed on the right edge of the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathRightWidth:    
      description: 'Width of the walkway placed on the right edge of the road corresponding to this observation.'    
      type: number    
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
    rightOfWayWidth:    
      description: 'Right of Way (RoW) is the total land area available for the roadway. Its width accommodates for carriages way + other necessities + future extension, along the road''s alignment.'    
      type: number    
      x-ngsi:    
        type: Property    
    roadClass:    
      description: 'The type of road corresponding to this observation. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD].'    
      enum:    
        - MAJOR_DISTRICT_ROAD    
        - MAJOR_CITY_ROAD    
        - MINOR_CITY_ROAD    
        - NATIONAL_HIGHWAY    
        - OTHER_DISTRICT_ROAD    
        - OTHER_PUBLIC_ROAD    
        - PORT_ROAD    
        - PRIVATE_ROAD    
        - SERVICE_ROAD    
        - STATE_HIGHWAY    
      type: string    
      x-ngsi:    
        type: Property    
    roadDirection:    
      description: 'Represents the direction the road is heading to. Enum:'' [''N, S, E, W''. The values N,S,E,W represent North,South,East,West respectively.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadId:    
      description: 'Unique internal representation of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadMaterial:    
      description: 'The construction material used for laying the carriageway corresponding to this observation. For eg. concrete, earthen, tar etc.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadName:    
      description: 'The name of the road corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    roadWork:    
      description: 'Reasons for the road work in case of urgent intervention. A combination of these values. Enum:''COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK''.'    
      enum:    
        - COLLAPSE    
        - DERAILMENT    
        - FIRE    
        - FLOOD    
        - GASLEAK    
        - LANDSLIDE    
        - OTHER    
        - POWERCUT    
        - ROCKFALL    
        - SAGGING    
        - WATERLEAK    
      type: string    
      x-ngsi:    
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
    status:    
      description: 'Specific driving conditions on the roadsegment. Use statusDescription for additional information. Enum: ‘open, closed, limited’.  `open`: the roadsegment can be used in full intended capacity, `closed`: no traffic is possible, e.g. due to roadworks, an open bridge or lock, or any other event preventing traffic. `limited`: traffic is possible, but not in the full capacity.'    
      items:    
        enum:    
          - open    
          - closed    
          - limited    
        type: string    
      type: string    
      x-ngsi:    
        type: Property    
    statusDescription:    
      description: 'Additional information to the status attribute.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalCyclePathWidth:    
      description: 'Total width of the cycle track present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    totalPedestrianPathLength:    
      description: 'Total length of the walkway present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalPedestrianPathWidth:    
      description: 'Total width of the walkway present in the road corresponding to this observation.'    
      type: number    
      x-ngsi:    
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
  x-model-tags: IUDX    
  x-version: 0.4.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
Las propiedades `laneUsage` y las que transmiten los parámetros máximos permitidos pueden ser dinámicas, por ejemplo, se puede cambiar temporalmente la dirección de un carril para mejorar las condiciones del tráfico.  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### RoadSegment NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un RoadSegment en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": [  
    "oneway"  
  ],  
  "refRoad": "Spain-Road-A62",  
  "totalLaneNumber": 2,  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "startPoint": {  
    "type": "Point",  
    "coordinates": [  
      -4.7299180606009,  
      41.6844918725019  
    ]  
  },  
  "endPoint": {  
    "type": "Point",  
    "coordinates": [  
      -4.55167335377909,  
      41.8570461783071  
    ]  
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
  },  
  "laneUsage": [  
    "forward",  
    "forward"  
  ],  
  "source": "http://wwww.openstreetmap.org",  
  "status": "open",  
  "statusDescription": "Bridge state = DOWN",  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": 0.095454461114818,  
  "totalPedestrianPathWidth": 7,  
  "bridgeCount": 1,  
  "pedestrianPathLeftHeight": 2,  
  "maximumAllowedHeight": 72,  
  "totalPedestrianPathLength": 0.09,  
  "culvertCount": 0,  
  "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
  "roadClass": "OTHER_PUBLIC_ROAD",  
  "medianHeight": 3.6,  
  "roadWork": "OTHER",  
  "roadID": "5272",  
  "cyclePathRightWidth": 2.5,  
  "roadMaterial": "TAR",  
  "medianWidth": 1.5,  
  "carriagewayWidth": 3,  
  "cyclePathRightHeight": 1,  
  "roadDirection": "N",  
  "medianLength": 0.09,  
  "pedestrianPathMaterial": "PAVEMENT BLOCK",  
  "cyclePathLeftWidth": 2.5,  
  "maximumAllowedWidth": 74,  
  "rightOfWayWidth": 4,  
  "cyclePathLeftHeight": 1,  
  "maximumAllowedWeight": 109,  
  "pedestrianPathRightWidth": 3.5,  
  "pedestrianPathLeftWidth": 3.5,  
  "pedestrianPathPlacement": "NOT_AVAILABLE",  
  "pedestrianPathRightHeight": 2,  
  "cyclePathPlacement": "NOT_AVAILABLE",  
  "totalCyclePathWidth": 5,  
  "agency_name": "CORPORATION",  
  "municipalityInfo": {  
    "ulbName": "KANNUR MUNICIPAL CORPORATION"  
  }  
}  
```  
</details>  
#### RoadSegment NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un RoadSegment en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": [  
      "oneway"  
    ]  
  },  
  "endPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.55167335377909,  
        41.8570461783071  
      ]  
    }  
  },  
  "name": {  
    "value": "Valladolid-Dueñas"  
  },  
  "startPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.7299180606009,  
        41.6844918725019  
      ]  
    }  
  },  
  "allowedVehicleType": {  
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
    "value": [  
      "forward",  
      "forward"  
    ]  
  },  
  "status": {  
    "value": "open"  
  },  
  "statusDescription": {  
    "value": "Bridge state = DOWN"  
  },  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": {  
    "type": "number",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "number",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "number",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "number",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "number",  
    "value": 0  
  },  
  "roadName": {  
    "type": "string",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "string",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "number",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "string",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "string",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "string",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "number",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "number",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "string",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "string",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "number",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "number",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "number",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "number",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "string",  
    "value": "CORPORATION"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  }  
}  
```  
</details>  
#### RoadSegment NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un RoadSegment en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
    "type": "RoadSegment",  
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
    "status": "open",  
    "statusDescription": "Bridge state = DOWN",  
    "cyclePathMaterial": "ASPHALT",  
    "carriagewayLength": 0.095454461114818,  
    "totalPedestrianPathWidth": 7,  
    "bridgeCount": 1,  
    "pedestrianPathLeftHeight": 2,  
    "maximumAllowedHeight": 72,  
    "totalPedestrianPathLength": 0.09,  
    "culvertCount": 0,  
    "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
    "roadClass": "OTHER_PUBLIC_ROAD",  
    "medianHeight": 3.6,  
    "roadWork": "OTHER",  
    "roadID": "5272",  
    "cyclePathRightWidth": 2.5,  
    "roadMaterial": "TAR",  
    "medianWidth": 1.5,  
    "carriagewayWidth": 3,  
    "cyclePathRightHeight": 1,  
    "roadDirection": "N",  
    "medianLength": 0.09,  
    "pedestrianPathMaterial": "PAVEMENT BLOCK",  
    "cyclePathLeftWidth": 2.5,  
    "maximumAllowedWidth": 74,  
    "rightOfWayWidth": 4,  
    "cyclePathLeftHeight": 1,  
    "maximumAllowedWeight": 109,  
    "pedestrianPathRightWidth": 3.5,  
    "pedestrianPathLeftWidth": 3.5,  
    "pedestrianPathPlacement": "NOT_AVAILABLE",  
    "pedestrianPathRightHeight": 2,  
    "cyclePathPlacement": "NOT_AVAILABLE",  
    "totalCyclePathWidth": 5,  
    "agency_name": "CORPORATION",  
    "municipalityInfo": {  
        "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RoadSegment NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un RoadSegment en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
	"type": "RoadSegment",  
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
	"laneUsage": {  
		"type": "Property",  
		"value": [  
			"forward",  
			"forward"  
		]  
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
	"maximumAllowedSpeed": {  
		"type": "Property",  
		"value": 120  
	},  
	"minimumAllowedSpeed": {  
		"type": "Property",  
		"value": 60  
	},  
	"name": {  
		"type": "Property",  
		"value": "Valladolid-DueÃ±as"  
	},  
	"refRoad": {  
		"type": "Relationship",  
		"object": "urn:ngsi-ld:Road:Spain-Road-A62"  
	},  
	"source": {  
		"type": "Property",  
		"value": "http://wwww.openstreetmap.org"  
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
	"totalLaneNumber": {  
		"type": "Property",  
		"value": 2  
	},  
	"status": {  
		"type": "Property",  
		"value": "open"  
	},  
	"statusDescription": {  
		"type": "Property",  
		"value": "Bridge state = DOWN"  
	},  
	"carriagewayLength": {  
    "type": "Property",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "Property",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "Property",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "Property",  
    "value": 0  
  },  
  "roadName": {  
    "type": "Property",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "Property",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "Property",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "Property",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "Property",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "Property",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "Property",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "Property",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "Property",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "Property",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "Property",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "Property",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "Property",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "Property",  
    "value": "CORPORATION"  
  },  
 "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  },  
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
