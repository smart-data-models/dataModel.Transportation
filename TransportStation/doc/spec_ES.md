<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: TransportStation  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TransportStation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El modelo de datos es una descripción general de las estaciones urbanas (Metro, Autobús, Tranvía, Helipuerto, ...) según la norma GFTS https://developers.google.com/transit/gtfs/reference/#stopstxt, así como la descripción detallada de las mismas (medios de acceso, andén, asistencia, ...).**.  
versión: 0.1.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `contactPoint[object]`: Los datos de contacto del artículo  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: Área geográfica en la que se presta un servicio o se ofrece un artículo. Sustituye a serviceArea    
	- `availabilityRestriction[*]`: Esta propiedad vincula un punto de contacto con información sobre cuándo el punto de contacto no está disponible. Los detalles se proporcionan utilizando la clase Especificación de horarios de apertura  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Idioma que alguien puede utilizar con o en el artículo, servicio o lugar. Utilice uno de los códigos de idioma del estándar IETF BCP 47. Está implementada la opción Texto pero también podría ser Idioma  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Una opción disponible en este punto de contacto (por ejemplo, un número gratuito o asistencia para personas con problemas de audición)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Tipo de contacto de este artículo    
	- `email[idn-email]`: Dirección de correo electrónico del propietario    
	- `faxNumber[string]`: El número de fax  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: El nombre de este artículo    
	- `productSupported[string]`: El producto o servicio con el que está relacionado este punto de contacto de asistencia (por ejemplo, asistencia para una línea de productos concreta). Puede tratarse de un producto o línea de productos específicos (por ejemplo, "iPhone") o de una categoría general de productos o servicios (por ejemplo, "smartphones").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Teléfono de este contacto    
- `contractingAuthority[string]`: Nombre del poder adjudicador  - `contractingCompany[string]`: Nombre de la empresa contratante responsable de la explotación de la estación  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateLastReported[date-time]`: Marca de tiempo que indica la última vez que el dispositivo notificó datos correctamente. Fecha y hora en formato ISO8601 UTC  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `dimension[object]`: Dimensión global. El formato está estructurado por una subpropiedad de 3 elementos. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Metros  	- `depth`:     
	- `height`:     
- `id[*]`: Identificador único de la entidad  - `installationMode[string]`: Ubicación relativa a la referencia terrestre. Enum:'aérea, terrestre, subterránea, submarina'  - `inventory[object]`: Asignación general de datos sólo para `locationType` = 0, 1, 3, 4. El formato está estructurado por una subpropiedad de 4 elementos  	- `PlatformType`:     
	- `nbOfIOPoint`:     
	- `nbOfLane`:     
- `levelId[number]`: Planta en la que se encuentra la ubicación. Índice numérico asociado a la planta. Indica la posición relativa de esta planta con respecto a las demás. El índice 0 indica la planta baja. Las plantas por encima del nivel del suelo se indican mediante índices positivos, y las etapas subterráneas mediante índices negativos  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `locationType[number]`: Enlace al repositorio estándar GTFS que describe las distintas ubicaciones [Tipo de ubicación]. 0 Parada o andén (lugar donde los usuarios suben o bajan en un vehículo de transporte público). 1 Estación (zona o estructura física que comprende uno o más andenes). 2 Entrada o salida (lugar donde los usuarios pueden entrar/salir de una estación desde la calle). 3 Intersección genérica (ubicación en una estación que no corresponde a ningún otro valor de `location_type`). 4 Zona de embarque de un lugar específico de un andén donde los usuarios pueden subir / bajar en un vehículo.  - `name[string]`: El nombre de este artículo  - `openingHoursSpecification[array]`: Valor estructurado que proporciona información sobre el horario de apertura de un lugar o de un determinado servicio dentro de un lugar.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `parentStation[*]`: Enlace al repositorio estándar GTFS que describe el diferente vínculo entre Estación y Andén [Parent STATION]. Caso '1' location_type = 0 (Parada / andén ), el campo parent_station contiene el ID de una estación. Caso "2" location_type = 1 (Estación), este campo debe estar vacío. Caso '3' location_type = 2 (Entrada / salida) o location_type = 3 (intersección genérica), el campo parent_station contiene el ID de una estación location_type = 1. Caso '4' location_type = 4 (zona de embarque), el campo parent_station contiene el ID de un andén  - `platformCode[number]`: Identificador de andén para una parada de tipo andén `location_type` = 0 cuando la parada está en una estación  - `refPointOfInterest[*]`: Referencia a un punto de interés asociado a esta observación  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `stationConnected[array]`: Conexiones posibles desde esta estación. Un valor estructurado de 0 a N ocurrencias donde cada elemento es una cadena en el formato `stationType` : [Lista de líneas conectadas, separadas por una coma]. Enum:'aerialLift, bus, cableTram, ferry, funicular, monorraíl, ferrocarril, metro, tren, tranvía, trolebús'  - `stationType[array]`: Tipo de estación de transporte. Enum:'ascensor aéreo, autobús, teleférico, transbordador, funicular, monorraíl, ferrocarril, metro, trolebús, tranvía'.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser TransportStation  - `webSite[string]`: Enlace a la web oficial para más información  - `wheelChairAccessible[number]`: Acceso posible para personas con movilidad reducida. Para las paradas sin padres 0 no se dispone de información sobre la accesibilidad de la parada. 1 algunos vehículos en esta parada pueden embarcar a un usuario PMR. 2 en esta parada no puede embarcar un usuario PMR. Para una parada que forma parte de una estación 0 la parada hereda el comportamiento wheelchair_boarding de la estación padre, si se rellena. 1 los carriles proporcionan acceso en silla de ruedas a la parada / andén desde el exterior de la estación. 2 ningún carril proporciona acceso en silla de ruedas a la parada / andén desde el exterior de la estación. Para entradas / salidas de estación 0 la entrada de la estación hereda el comportamiento wheelchair_boarding de la estación principal, si se ha especificado. 1 la entrada de la estación es accesible en silla de ruedas. 2 ninguna ruta accesible para sillas de ruedas conecta la entrada de la estación con las paradas / andenes.  - `zoneId[string]`: Zona tarifaria de la estación  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TransportStation:    
  description: "The data model is a general description of urban stations (Metro, Bus, Tram, Heliport, ...) according to the GFTS standard https://developers.google.com/transit/gtfs/reference/#stopstxt, as well the detailed description of these (means of access, platform, assistance, ...)."    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contactPoint:    
      description: The details to contact with the item    
      properties:    
        areaServed:    
          description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
          type: string    
          x-ngsi:    
            type: Property    
        availabilityRestriction:    
          anyOf:    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
            - description: Array of identifiers format of any NGSI entity    
              items:    
                format: uri    
                type: string    
              type: array    
              x-ngsi:    
                type: Property    
          description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
          x-ngsi:    
            model: http://schema.org/hoursAvailable    
            type: Relationship    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
          x-ngsi:    
            model: http://schema.org/availableLanguage    
            type: Property    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
          x-ngsi:    
            model: http://schema.org/contactOption    
            type: Property    
        contactType:    
          description: Contact type of this item    
          type: string    
          x-ngsi:    
            type: Property    
        email:    
          description: Email address of owner    
          format: idn-email    
          type: string    
          x-ngsi:    
            type: Property    
        faxNumber:    
          description: The fax number    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        name:    
          description: The name of this item    
          type: string    
          x-ngsi:    
            type: Property    
        productSupported:    
          description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
          type: string    
          x-ngsi:    
            model: http://schema.org/Text    
            type: Property    
        telephone:    
          description: Telephone of this contact    
          type: string    
          x-ngsi:    
            type: Property    
        url:    
          description: URL which provides a description or further information about this item    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    contractingAuthority:    
      description: Name of the contracting authority    
      type: string    
      x-ngsi:    
        type: Property    
    contractingCompany:    
      description: Name of the contracting company responsible for the exploitation of the station    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateLastReported:    
      description: A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dimension:    
      description: 'Global dimension. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meters'    
      properties:    
        depth:    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
        units: meters    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    installationMode:    
      description: 'Location  relative to the ground reference. Enum:''aerial, ground, underGround, underSea'''    
      enum:    
        - aerial    
        - ground    
        - underGround    
        - underSea    
      type: string    
      x-ngsi:    
        type: Property    
    inventory:    
      description: 'General data mapping only for `locationType` = 0, 1, 3, 4. The format is structured by a sub-property of 4 items'    
      properties:    
        PlatformType:    
          items:    
            enum:    
              - lateral    
              - central    
            type: string    
          type: array    
        nbOfIOPoint:    
          minimum: 0    
          type: number    
        nbOfLane:    
          minimum: 0    
          type: number    
        nbOfPlatform:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    levelId:    
      description: 'Floor on which the location is located. Numerical index associated with the floor. Indicates the relative position of this stage in relation to the others. The index 0 indicates the ground floor. The floors above ground level are indicated by positive indices, and the underground stages by negative indices'    
      type: number    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    locationType:    
      description: 'Link to the GTFS standard repository describing the different location [Location Type]. 0 Stop or platform (place where users get on or off in a public transport vehicle). 1 Station (area or physical structure comprising one or more platforms). 2 Entrance or Exit (place where users can enter / exit a station from the street). 3 Generic intersection (location in a station that doesn''t correspond to any other `location_type` value). 4 Boarding area of a specific location on a platform where users can get on / off in a vehicle'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: A structured value providing information about the opening hours of a place or a certain service inside a place    
      items:    
        properties:    
          closes:    
            description: ' 	The closing hour of the place or service on the given day(s) of the week'    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          dayOfWeek:    
            anyOf:    
              - description: Array of days of the week    
                enum:    
                  - Monday    
                  - Tuesday    
                  - Wednesday    
                  - Thursday    
                  - Friday    
                  - Saturday    
                  - Sunday    
                  - PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
              - description: Array of days of the week    
                enum:    
                  - https://schema.org/Monday    
                  - https://schema.org/Tuesday    
                  - https://schema.org/Wednesday    
                  - https://schema.org/Thursday    
                  - https://schema.org/Friday    
                  - https://schema.org/Saturday    
                  - https://schema.org/Sunday    
                  - https://schema.org/PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
            description: 'The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)'    
            type: string    
            x-ngsi:    
              model: http://schema.org/dayOfWeek    
              type: Property    
          opens:    
            description: The opening hour of the place or service on the given day(s) of the week    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          validFrom:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            x-ngsi:    
              type: Property    
          validThrough:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    parentStation:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'Link to the GTFS standard repository describing the different link between Station and Platform [Parent STATION]. Case ''1'' location_type = 0 (Stop / platform ), the parent_station field contains the ID of a station. Case ''2'' location_type = 1  (Station), this field must be empty. Case ''3'' location_type = 2 (Input / output) or location_type = 3 (generic intersection), the parent_station field contains the ID of a station location_type = 1. Case ''4'' location_type = 4 (boarding area), the parent_station field contains the ID of a platform'    
      x-ngsi:    
        type: Relationship    
    platformCode:    
      description: Platform identifier for a platform type stop `location_type` = 0 when the stop is in a station    
      type: number    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: A reference to a point of interest associated to this observation    
      x-ngsi:    
        type: Relationship    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    stationConnected:    
      architect:    
        type: string    
      commissioningDate:    
        format: date-time    
        type: string    
      constructionDate:    
        format: date-time    
        type: string    
      currencyAccepted:    
        items:    
          enum:    
            - EUR    
            - USD    
          type: string    
        type: array    
      description: 'Connections possible from this station. A structured value from 0 to N occurrences where each items is a string in the format `stationType` : [List of Lines connected, separated by a comma]. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, train, tram, trolleybus'''    
      featuredArtist:    
        items:    
          anyOf:    
            - anyOf:    
                - description: Property. Identifier format of any NGSI entity    
                  maxLength: 256    
                  minLength: 1    
                  pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                  type: string    
                - description: Property. Identifier format of any NGSI entity    
                  format: uri    
                  type: string    
              description: Property. Unique identifier of the entity    
            - type: string    
        type: array    
      items:    
        properties:    
          linesConnected:    
            items:    
              type: string    
            type: array    
          stationType:    
            enum:    
              - aerialLift    
              - bus    
              - cableTram    
              - ferry    
              - funicular    
              - monorail    
              - rail    
              - subway    
              - train    
              - tram    
              - trolleybus    
            type: string    
        type: object    
      paymentAccepted:    
        items:    
          enum:    
            - Cash    
            - CreditCard    
            - CryptoCurrency    
            - other    
          type: string    
        type: array    
      services:    
        properties:    
          defibrillator:    
            type: Boolean    
          emergencyPhone:    
            type: Boolean    
          informationBoardDevice:    
            type: Boolean    
          interactiveDevice:    
            type: Boolean    
          messageDevice:    
            type: Boolean    
          purchaseDevice:    
            type: Boolean    
          restBench:    
            type: Boolean    
          shelters:    
            type: Boolean    
          timetableDevice:    
            type: Boolean    
          voiceDevice:    
            type: Boolean    
          wheelChairAccessible:    
            type: Boolean    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    stationType:    
      description: 'Type of transport station. Enum:''aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, trolleybus, tram'''    
      items:    
        enum:    
          - aerialLift    
          - bus    
          - cableTram    
          - ferry    
          - funicular    
          - monorail    
          - rail    
          - subway    
          - trolleybus    
          - tram    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be TransportStation    
      enum:    
        - TransportStation    
      type: string    
      x-ngsi:    
        type: Property    
    webSite:    
      description: Link to the official website for more information    
      type: string    
      x-ngsi:    
        type: Property    
    wheelChairAccessible:    
      description: 'Access possible for Person with Reduced Mobility. For stops without parents 0 no information is available regarding the accessibility of the stop. 1 some vehicles at this stop can board a PMR user. 2 PRM user cannot board  at this stop. For a stop that is part of a station 0 the stop inherits the wheelchair_boarding behavior of the parent station, if it is filled in. 1 lanes provide wheelchair access to the stop / platform  from outside the station. 2 no lane provides wheelchair access to the stop / platform from outside the station. For station inputs / outputs 0 the station entry inherits the wheelchair_boarding behavior of the main station, if specified. 1 the station entrance is wheelchair accessible. 2 no wheelchair accessible route connects the station entrance to the stops / platforms'    
      enum:    
        - 0    
        - 1    
        - 2    
      type: number    
      x-ngsi:    
        type: Property    
    zoneId:    
      description: Pricing zone of the station    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/TransportStation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models/Transportation/TransportStation/schema.json    
  x-model-tags: ""    
  x-version: 0.1.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### TransportStation NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un TransportStation en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "Régie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gué / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ]  
}  
```  
</details>  
#### TransportStation NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de TransportStation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": ["tram"]  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07:00:00",  
        "closes": "22:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08:00:00",  
        "closes": "23:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8:00:30",  
        "closes": "21:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8:00:00",  
        "closes": "21:00:30",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      }  
    ]  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompany": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "url": "www.lignesdazur.com"  
    }  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": ["lateral"]  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": [  
      {  
        "stationType": "tram",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Tram 2 - CADAM / Nikaia",  
            "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
          ]  
        }  
      },  
      {  
        "stationType": "train",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Gare SNCF Nice Saint Augustin (600m)"  
          ]  
        }  
      },  
      {  
        "stationType": "bus",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "L20 - Giono / Les Pugets",  
            "L20 - Centre Commercial St Isidore",  
            "L21 - Le Gué / Polygone Riviera",  
            "L54 - Centre Commercial Cap 3000 - St Jeannet",  
            "L90 - La Bolline",  
            "91 Auron",  
            "L92 - Isola 2000"  
          ]  
        }  
      }  
    ]  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architect": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  }  
}  
```  
</details>  
#### TransportStation NGSI-LD key-values Ejemplo  
He aquí un ejemplo de TransportStation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "architect": "Nice Architecture",  
  "areaServed": "Nice Airport",  
  "commissioningDate": "2018-09-15",  
  "constructionDate": "2016-19-08",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "R\u00e9gie Ligne d'Azur",  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "description": "Description and services provided in the station",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ],  
  "instalationMode": "ground",  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "levelId": 0,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "locationType": 1,  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gu\u00e9 / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "stationType": [  
    "tram"  
  ],  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "wheelChairAccessible": 1,  
  "zoneId": "B",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TransportStation NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de TransportStation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "TransportStation",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": ["tram"]  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07:00:00",  
        "closes": "22:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08:00:00",  
        "closes": "23:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8:00:30",  
        "closes": "21:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8:00:00",  
        "closes": "21:00:30",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      }  
    ]  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompany": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "url": "www.lignesdazur.com"  
    }  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": ["lateral"]  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": [  
      {  
        "stationType": "tram",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Tram 2 - CADAM / Nikaia",  
            "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
          ]  
        }  
      },  
      {  
        "stationType": "train",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "Gare SNCF Nice Saint Augustin (600m)"  
          ]  
        }  
      },  
      {  
        "stationType": "bus",  
        "linesConnected": {  
          "type": "Property",  
          "value": [  
            "L20 - Giono / Les Pugets",  
            "L20 - Centre Commercial St Isidore",  
            "L21 - Le Gué / Polygone Riviera",  
            "L54 - Centre Commercial Cap 3000 - St Jeannet",  
            "L90 - La Bolline",  
            "91 Auron",  
            "L92 - Isola 2000"  
          ]  
        }  
      }  
    ]  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architect": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
