<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: APDSObservación    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/APDSObservation/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Esta entidad modela una observación particular de un conjunto de cámaras ANPR. La observación puede realizarse con varias cámaras ANPR, pero se limita a la observación de UN vehículo. Implementa el modelo de datos APDS https://www.allianceforparkingdatastandards.org/**    
versión: 0.0.1    
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
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública      
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `creator[string]`: Id del conductor actual.  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `images[array]`: Array de enlaces a imágenes. El elemento de la matriz contiene las URL de las imágenes e información adicional. Como alternativa a la URL de las imágenes, la propia imagen puede incluirse en el atributo binaryContent.  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `observationDateTime[date-time]`: Fecha y hora en que se realizó la observación (UTC). Obligatorio si no se utilizan observationStartDateTime y observationEndDateTime.  - `observationEndDateTime[date-time]`: Fecha y hora en que finalizó el evento de observación (en UTC) (por ejemplo, se observó la salida de un coche de una zona de entrega a las 9:33 horas). Obligatorio si no se utiliza creationDateTime.  - `observationStartDateTime[date-time]`: Fecha y hora de inicio del evento de observación (en UTC) (por ejemplo, se observó la entrada de un coche en una zona de entrega a las 8:01 horas). Obligatorio si no se utiliza creationDateTime.  - `observedCredentialCharacterConfidence[array]`: La confianza del reconocimiento de caracteres individuales. Al igual que con observedCredentialConfidence, es específico del proveedor. Utilice los metadatos para indicar cómo pueden interpretarse las confidencias.  - `observedCredentialConfidence[number]`: La confianza general de la medición. Puede ser específico de un proveedor, pero siempre debe escalarse a un valor entre 0 y 1. Utilice los metadatos para indicar cómo debe interpretarse este número. Arvoo: rango [0,0, 1,0] (cuanto más alto, mejor).  - `observedCredentialCountry[string]`: Código de país según la norma ISO3166 de 2 caracteres (https://www.iban.com/country-codes). Obsérvese que no debe utilizarse el código internacional de matriculación de vehículos para evitar ambigüedades (https://en.wikipedia.org/wiki/International_vehicle_registration_code). Si no se ha podido determinar el código de país, indique "XX" para este atributo.  - `observedCredentialId[string]`: Identificador específico de la credencial observada a la que se hace referencia. La credencial se especifica mediante observedCredentialType y puede ser una etiqueta RFID, un número de ticket de un terminal de pago, un número de matrícula, etc. En el caso de una matrícula, sólo se permiten valores numéricos alfabéticos (sin espacios ni guiones). Opcionalmente, puede utilizarse un ":" para indicar la posición de, por ejemplo, el sello de la ciudad alemana (https://www.europeanplates.com/information/german-city-codes.html).  - `observedCredentialType[string]`: Tipo de credencial a la que se hace referencia en la observación. Los valores permitidos se especifican en APDS CredentialType. Enum:'barcode, bluetooth, eticket, hangtag, licensePlate, permit, qrCode, rfid, ticket, other'  - `observedHeading[*]`: Denota la dirección de desplazamiento del observador y se especifica en grados decimales, donde 0 <= "heading" < 360, contando en el sentido de las agujas del reloj respecto al norte verdadero.Si el vehículo está parado (es decir, el valor del atributo "speed" es "0"), el valor del atributo "heading" debe ser igual a "-1". (Código ONU DD)  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedLocation`:   	- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)    
	- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.      
- `observedLocationPDOP[number]`: Precisión de la posición GPS del vehículo observado. Se expresa como "dilución de precisión de la posición" (https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation)). (código ONU "MTR").  - `observedMethod[string]`: El método de observación registrado para este elemento de observación, tal como se define en APDS (ObservationType). Enum:'anpr, tiza, visual, escáner, rfTranspoder, otro'  - `observedSpeed[*]`: Denota la magnitud del componente horizontal de la velocidad actual del vehículo observado y se especifica en kilómetros por hora. Si se proporciona, el valor del atributo velocidad debe ser un número real no negativo. "-1" PUEDE utilizarse si la velocidad se desconoce transitoriamente por alguna razón. (Código ONU KMH).  . Model: [https://schema.org/Number](https://schema.org/Number)- `observedVehicleColour[string]`: El color del vehículo observado  - `observedVehicleMake[string]`: Marca del vehículo observado  - `observedVehicleType[string]`: Tipo de vehículo desde el punto de vista de sus características estructurales. Es diferente de la categoría de vehículo . Enum:vehículo agrícola, cualquier vehículo, vehículo articulado, bicicleta, carro de basura, autobús, coche, caravana, vehículo ligero, coche con caravana, coche con remolque, carro de limpieza, vehículo de construcción o mantenimiento, tracción a las cuatro ruedas, vehículo de gran altura, camión, minibús, ciclomotor, motocicleta, motocicleta con sidecar, motocarro, barredora, cisterna, vehículo de tres ruedas, remolque, tranvía, vehículo de dos ruedas, carro, furgoneta, vehículo sin convertidor catalítico, vehículo con caravana, vehículo con remolque, con matrícula par, con matrícula impar, otros". Los siguientes valores definidos por _VehicleTypeEnum_ y _VehicleTypeEnum2_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) y ampliados para otros usos  . Model: [https://schema.org/Text](https://schema.org/Text)- `observer[string]`: Nombre o identificación del sistema de escaneado que realiza la observación registrada en este elemento de observación.  - `observerCameras[array]`: La primera cámara de la lista tiene el mejor reconocimiento. Utilice las siguientes abreviaturas para indicar la posición de la cámara en un coche: RF(Delantera derecha), RM(Media derecha), RB(Trasera derecha), LF(Delantera izquierda), LM(Media izquierda), LB(Trasera izquierda).  - `observerDescription[string]`: Descripción de texto libre para detalles de la observación o del observador. Puede utilizarse, por ejemplo, como nombre descriptivo de un vehículo de exploración ANPR específico.  - `observerHeading[*]`: Denota la dirección de desplazamiento del observador y se especifica en grados decimales, donde 0 <= 'heading' < 360, contando en el sentido de las agujas del reloj respecto al norte verdadero. Si el vehículo está parado (es decir, el valor del atributo "velocidad" es "0"), el valor del atributo "rumbo" debe ser igual a "-1".  . Model: [https://schema.org/Number](https://schema.org/Number)- `observerLocation`:   	- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)    
	- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)    
	- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.      
- `observerLocationPDOP[number]`: Precisión de la posición GPS del observador, expresada como "Dilución de la posición de precisión"(https: //en.wikipedia.org/wiki/Dilución_de_precisión_(navegación))  - `observerSpeed[*]`: Denota la magnitud del componente horizontal de la velocidad actual del observador y se especifica en kilómetros por hora. Si se proporciona, el valor del atributo velocidad debe ser un número real no negativo. Puede utilizarse "-1" si la velocidad se desconoce transitoriamente por algún motivo.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `towardsObserver[number]`: 1: El vehículo observado se desplaza en dirección a la cámara, 0: El vehículo observado se desplaza en dirección contraria a la cámara, -1: No se detecta la dirección del vehículo observado: No se detecta la dirección del vehículo observado.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser APDSObservation  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Este modelo captura el conjunto de datos de una observación de un Vehículo en un momento específico en un lugar concreto. Se deriva de la especificación APDS (Alliance for Parking DataStandard). El método de observación incluye el uso de cámaras ALPR, observación visual, escáner o cualquier otro medio de observación.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
APDSObservation:      
  description: 'This entity models a particular observation of a set of ANPR camera. The Observation might be done with several ANPR cameras, but is limited to the observation of ONE vehicle. It implements the APDS data model https://www.allianceforparkingdatastandards.org/'      
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
    creator:      
      description: Id of current driver.      
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
    images:      
      description: 'Array of links to images. The array element contain the URLs of the images and additional info. As an alternative to the images URL, the image itself can be included in the binaryContent attribute.'      
      items:      
        items:      
          description: Every element in the array of images      
          properties:      
            URL:      
              description: Uri of the image      
              format: uri      
              type: string      
              x-ngsi:      
                type: Property      
            binaryContent:      
              description: Binary format of the image content      
              format: uuencoded      
              type: string      
              x-ngsi:      
                type: Property      
            camId:      
              description: Identifier of the camera. It can be specified by the camera position (also used in the 'camera' attribute)      
              type: string      
              x-ngsi:      
                type: Property      
            distance:      
              description: The distance in meters from the observer      
              type: number      
              x-ngsi:      
                type: Property      
                units: meters      
            expiryDateTime:      
              description: Timestamp until which the URL is valid      
              format: date-time      
              type: string      
              x-ngsi:      
                type: Property      
            imageContent:      
              description: It specifies the content of the image      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
        type: array      
      type: array      
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
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: The timestamp the Observation was made (UTC). Mandatory if observationStartDateTime and observationEndDateTime are not used.      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    observationEndDateTime:      
      description: 'The date and time of the observation event ended(in UTC).(e.g.a car was observed to exit a delivery zone at 9: 33am). Mandatory if creationDateTime is not used.'      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    observationStartDateTime:      
      description: 'The date and time of the observation(in UTC)event started.(e.g.a car was observed to enter a delivery zone at 8: 01am). Mandatory if creationDateTime is not used.'      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    observedCredentialCharacterConfidence:      
      description: The confidence of individual character recognition. As with observedCredentialConfidence this is vendor specific. Use the metadata to indicate how the confidences can be interpreted.      
      items:      
        description: Every observation of the credential character confidence      
        maximum: 1      
        minimum: 0      
        type: number      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    observedCredentialConfidence:      
      description: 'The overall confidence of the measurement. This can be vendor specific, but should always be rescaled to value between 0 en 1. Use the metadata to indicate how this number should be interpreted. Arvoo: range[0.0, 1.0](higher is better).'      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    observedCredentialCountry:      
      description: 'Country Code following the 2 character ISO3166 standard (https://www.iban.com/country-codes). Note that the International vehicle registration code should not be used to avoid ambiguity (https://en.wikipedia.org/wiki/International_vehicle_registration_code). If the country-code could not be determined, set ''XX'' as for this attribute.'      
      type: string      
      x-ngsi:      
        type: Property      
    observedCredentialId:      
      description: 'Specific identifier to the referenced observed credential. The credential is specified by observedCredentialType and may be an RFID tag, ticket number from a paystation, license plate number, etc. In case of a licensePlate only alpha numerical values (no spaces or hyphens) are allowed. Optionally an '':'' can be used to indicate the position of e.g. the German City Seal (https://www.europeanplates.com/information/german-city-codes.html).'      
      type: string      
      x-ngsi:      
        type: Property      
    observedCredentialType:      
      description: 'Type of the credential referenced within  the observation. Allowed values are specified in the APDS CredentialType. Enum:''barcode, bluetooth, eticket, hangtag, licensePlate, permit, qrCode, rfid, ticket, other'''      
      enum:      
        - barcode      
        - bluetooth      
        - eticket      
        - hangtag      
        - licensePlate      
        - permit      
        - qrCode      
        - rfid      
        - ticket      
        - other      
      type: string      
      x-ngsi:      
        type: Property      
    observedHeading:      
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north.If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1''. (UN code DD)'      
      oneOf:      
        - exclusiveMaximum: 360      
          maximum: 360      
          minimum: 0      
          type: number      
        - enum:      
            - -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Degrees      
    observedLocation:      
      description: GPS position of the middle position of the scanned vehicle.      
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
        areaServed:      
          description: The geographic area where a service or offered item is provided      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        location:      
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
          oneOf:      
            - bbox:      
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
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type:      
                enum:      
                  - Polygon      
                type: string      
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 2      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiLineString      
                type: string      
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 4      
                    type: array      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiPolygon      
                type: string      
          x-ngsi:      
            type: GeoProperty      
      type: object      
      x-ngsi:      
        type: GeoProperty      
    observedLocationPDOP:      
      description: 'Accuracy of GPS position of the observed vehicle. This is expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation)). (UN code ''MTR''). '      
      type: number      
      x-ngsi:      
        type: Property      
        units: meters      
    observedMethod:      
      description: 'The method of observation recorded for this observation element as defined by APDS (ObservationType). Enum:''anpr, chalk, visual, scanner, rfTranspoder, other'''      
      enum:      
        - anpr      
        - chalk      
        - other      
        - rfTranspoder      
        - scanner      
        - visual      
      type: string      
      x-ngsi:      
        type: Property      
    observedSpeed:      
      description: 'Denotes the magnitude of the horizontal component of the observed vehicles current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number.''-1'' MAY be used if speed is transiently unknown for some reason. (UN Code KMH).'      
      oneOf:      
        - minimum: 0      
          type: number      
        - maximum: -1      
          minimum: -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: km/h      
    observedVehicleColour:      
      description: The colour of the observed vehicle      
      type: string      
      x-ngsi:      
        type: Property      
    observedVehicleMake:      
      description: The make of the observed vehicle      
      type: string      
      x-ngsi:      
        type: Property      
    observedVehicleType:      
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses'      
      enum:      
        - agriculturalVehicle      
        - ambulance      
        - anyVehicle      
        - articulatedVehicle      
        - autorickshaw      
        - bicycle      
        - binTrolley      
        - BRT mini busÂ·      
        - BRT bus      
        - bus      
        - car      
        - caravan      
        - carOrLightVehicle      
        - carWithCaravan      
        - carWithTrailer      
        - cleaningTrolley      
        - compactor      
        - constructionOrMaintenanceVehicle      
        - dumper      
        - e-moped      
        - e-scooter      
        - e-motorcycle      
        - fireTender      
        - fourWheelDrive      
        - highSidedVehicle      
        - hopper      
        - lorry      
        - minibus      
        - moped      
        - motorcycle      
        - motorcycleWithSideCar      
        - motorscooter      
        - policeVan      
        - publicMotor      
        - sweepingMachine      
        - tanker      
        - tempo      
        - threeWheeledVehicle      
        - tipper      
        - trailer      
        - tram      
        - trolley      
        - twoWheeledVehicle      
        - van      
        - vehicleWithoutCatalyticConverter      
        - vehicleWithCaravan      
        - vehicleWithTrailer      
        - withEvenNumberedRegistrationPlates      
        - withOddNumberedRegistrationPlates      
        - other      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    observer:      
      description: The name or identification of the scanning system making the observation recorded in this observation element.      
      type: string      
      x-ngsi:      
        type: Property      
    observerCameras:      
      description: 'Array of camera positions that detected the vehicle.The first camera in the list has the best recognition.Use the following abbreviations to indicate the camera positioning on a car: RF(Right Front), RM(Right Middle), RB(Right Back), LF(Left Front), LM(Left Middle), LB(Left Back).'      
      items:      
        description: Every camera position      
        type: string      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    observerDescription:      
      description: Free-text description for details of the observation or observer. Can e.g.be used as a friendly name of a specific ANPR scan car.      
      type: string      
      x-ngsi:      
        type: Property      
    observerHeading:      
      description: 'Denotes the direction of travel of the observer and is specified in decimal degrees, where 0 <= ''heading'' < 360, counting clockwise relative to the true north. If the vehicle is stationary(i.e. the value of the ''speed'' attribute is ''0''), then the value of the heading attribute must be equal to ''-1'''      
      oneOf:      
        - exclusiveMaximum: 360      
          maximum: 360      
          minimum: 0      
          type: number      
        - enum:      
            - -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Degree.      
    observerLocation:      
      description: GPS position of the person or car equipped with the Camera/s that produce the observation.      
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
        areaServed:      
          description: The geographic area where a service or offered item is provided      
          type: string      
          x-ngsi:      
            model: https://schema.org/Text      
            type: Property      
        location:      
          description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
          oneOf:      
            - bbox:      
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
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type:      
                enum:      
                  - Polygon      
                type: string      
            - bbox:      
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
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 2      
                    type: array      
                  minItems: 2      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiLineString      
                type: string      
            - bbox:      
                items:      
                  type: number      
                minItems: 4      
                type: array      
              coordinates:      
                items:      
                  items:      
                    items:      
                    minItems: 4      
                    type: array      
                  type: array      
                type: array      
              type:      
                enum:      
                  - MultiPolygon      
                type: string      
          x-ngsi:      
            type: GeoProperty      
      type: object      
      x-ngsi:      
        type: GeoProperty      
    observerLocationPDOP:      
      description: 'Accuracy of the GPS position of the observer, expressed as ''Position Dilution Of Precision''(https: //en.wikipedia.org/wiki/Dilution_of_precision_(navigation))'      
      type: number      
      x-ngsi:      
        type: Property      
        units: meters.      
    observerSpeed:      
      description: 'Denotes the magnitude of the horizontal component of the observer current velocity and is specified in kilometers per hour. If provided, the value of the speed attribute must be a non - negative real number. ''-1'' MAY be used if speed is transiently unknown for some reason'      
      oneOf:      
        - minimum: 0      
          type: number      
        - maximum: -1      
          minimum: -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: 'KMH '      
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
    towardsObserver:      
      description: '1: Observed vehicle moves in direction of camera, 0: Observed vehicle moves away direction of camera, -1: Observed vehicle direction not detected.'      
      enum:      
        - -1      
        - 0      
        - 1      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be APDSObservation      
      enum:      
        - APDSObservation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://www.allianceforparkingdatastandards.org/      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/APDSObservation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/APDSObservation/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### APDSObservation NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de una APDSObservation en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
  "type": "APDSObservation",  
  "creator": "25399",  
  "images": [  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "ANPR"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Overview"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Plate"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Panorama"  
      },  
      {  
        "distance": -5.22  
      }  
    ]  
  ],  
  "observationDateTime": "2020-09-11T10:45:00.00Z",  
  "observedCredentialCharacterConfidence": [  
    0.944,  
    0.851,  
    0.876,  
    0.95,  
    0.932,  
    0.936,  
    0.901  
  ],  
  "observedCredentialConfidence": 0.851,  
  "observedCredentialCountry": "BE",  
  "observedCredentialId": "1ENC003",  
  "observedCredentialType": "licensePlate",  
  "observedHeading": 175,  
  "observedLocation": {  
    "coordinates": [  
      4.00412077,  
      51.00216632  
    ],  
    "type": "Point"  
  },  
  "observedLocationPDOP": 0.2959945752,  
  "observedMethod": "anpr",  
  "observedSpeed": -1,  
  "observer": "Arvoo",  
  "observerCameras": [  
    "LF,LB"  
  ],  
  "observerDescription": "Scangenius Auto-26",  
  "observerHeading": 175,  
  "observerLocation": {  
    "coordinates": [  
      4.412077,  
      51.216632  
    ],  
    "type": "Point"  
  },  
  "observerLocationPDOP": 0.2959945752,  
  "observerSpeed": 26  
}  
```  
</details>    
#### APDSObservation NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de APDSObservation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Text",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Text",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Text",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Text",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Number",  
		"value": 0.851,  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo. Higher is better."  
			}  
		}  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "array",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		],  
		"metadata": {  
			"confidenceMethod": {  
				"type": "Text",  
				"value": "Arvoo"  
			}  
		}  
	},  
	"observer": {  
		"type": "Text",  
		"value": "Arvoo",  
		"metadata": {}  
	},  
	"observerDescription": {  
		"type": "Text",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Text",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Array",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "DateTime",  
		"value": "2020-09-11T10:45:00.00Z"  
	},  
	"observerLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observerHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Number",  
		"value": 26,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "KMH"  
			}  
		}  
	},  
	"observedLocation": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		},  
		"metadata": {  
			"timestamp": {  
				"type": "DateTime",  
				"value": "2020-09-11T10:45:00.00Z"  
			}  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Number",  
		"value": 0.2959945752,  
		"metadata": {  
			"UnitCode": {  
				"type": "Text",  
				"value": "MTR"  
			}  
		}  
	},  
	"observedHeading": {  
		"type": "Number",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Number",  
		"value": -1  
	},  
	"images": {  
		"type": "array",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	}  
}  
```  
</details>    
#### APDSObservation NGSI-LD key-values Ejemplo    
Aquí hay un ejemplo de una APDSObservation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
  "type": "APDSObservation",  
  "creator": "25399",  
  "images": [  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=anpr"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "ANPR"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=overview"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Overview"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=lf&amp;imgreqtype=plate"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Plate"  
      }  
    ],  
    [  
      {  
        "URL": "http://10.1.0.11:7400/getimage?sgid=8775639&amp;camid=plf&amp;distance=-5.22"  
      },  
      {  
        "camId": "LF"  
      },  
      {  
        "imageContent": "Panorama"  
      },  
      {  
        "distance": -5.22  
      }  
    ]  
  ],  
  "observationDateTime": "2020-09-11T10:45:00.00Z",  
  "observedCredentialCharacterConfidence": [  
    0.944,  
    0.851,  
    0.876,  
    0.95,  
    0.932,  
    0.936,  
    0.901  
  ],  
  "observedCredentialConfidence": 0.851,  
  "observedCredentialCountry": "BE",  
  "observedCredentialId": "1ENC003",  
  "observedCredentialType": "licensePlate",  
  "observedHeading": 175,  
  "observedLocation": {  
    "coordinates": [  
      4.00412077,  
      51.00216632  
    ],  
    "type": "Point"  
  },  
  "observedLocationPDOP": 0.2959945752,  
  "observedMethod": "anpr",  
  "observedSpeed": -1,  
  "observer": "Arvoo",  
  "observerCameras": [  
    "LF,LB"  
  ],  
  "observerDescription": "Scangenius Auto-26",  
  "observerHeading": 175,  
  "observerLocation": {  
    "coordinates": [  
      4.412077,  
      51.216632  
    ],  
    "type": "Point"  
  },  
  "observerLocationPDOP": 0.2959945752,  
  "observerSpeed": 26,  
  "@context": [  
    "https://raw.githubusercontent.com/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### APDSObservation NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de APDSObservation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
	"id": "uri:ngsi-ld:APDSObservation:Arvoo:ArvooSGIDxxxx",  
	"type": "APDSObservation",  
	"observedMethod": {  
		"type": "Property",  
		"value": "anpr"  
	},  
	"observedCredentialType": {  
		"type": "Property",  
		"value": "license plate"  
	},  
	"observedCredentialId": {  
		"type": "Property",  
		"value": "1ENC003"  
	},  
	"observedCredentialCountry": {  
		"type": "Property",  
		"value": "BE"  
	},  
	"observedCredentialConfidence": {  
		"type": "Property",  
		"value": 0.851  
	},  
	"observedCredentialCharacterConfidence": {  
		"type": "Property",  
		"value": [  
			0.944,  
			0.851,  
			0.876,  
			0.950,  
			0.932,  
			0.936,  
			0.901  
		]  
	},  
	"observer": {  
		"type": "Property",  
		"value": "Arvoo"  
	},  
	"observerDescription": {  
		"type": "Property",  
		"value": "Scangenius Auto-26"  
	},  
	"creator": {  
		"type": "Property",  
		"value": "25399"  
	},  
	"observerCameras": {  
		"type": "Property",  
		"value": [  
			"LF,LB"  
		]  
	},  
	"observationDateTime": {  
		"type": "Property",  
		"value": {  
			"@type": "DateTime",  
			"@value": "2020-09-11T10:45:00.00Z"  
		}  
	},  
	"observerLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.412077,  
				51.216632  
			]  
		}  
	},  
	"observerLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observerHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observerSpeed": {  
		"type": "Property",  
		"value": 26  
	},  
	"observedLocation": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				4.00412077,  
				51.00216632  
			]  
		}  
	},  
	"observedLocationPDOP": {  
		"type": "Property",  
		"value": 0.2959945752  
	},  
	"observedHeading": {  
		"type": "Property",  
		"value": 175  
	},  
	"observedSpeed": {  
		"type": "Property",  
		"value": -1  
	},  
	"images": {  
		"type": "Property",  
		"value": [  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=anpr",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "ANPR"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=overview",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Overview"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=lf&imgreqtype=plate",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Plate"  
			},  
			{  
			  "URL": "http://localhost:4000/getimage?sgid=984133&camid=plf&distance=-3.23",  
			  "expiryDateTime": "2023-11-25T11:13:42.133Z",  
			  "camId": "LF",  
			  "imageContent": "Panorama",  
			  "distance": -3.232  
			}  
		]  
	},  
	 "@context": [  
        ""  
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
