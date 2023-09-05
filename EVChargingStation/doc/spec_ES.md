<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: EVChargingStation  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/EVChargingStation/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Estación de recarga de vehículos eléctricos  
versión: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `acceptedPaymentMethod[array]`: Tipo(s) de cargo al utilizar esta estación. Enum:'Por transferencia bancaria por adelantado, Por factura, Efectivo, Cheque por adelantado, Contra reembolso, Débito directo, GoogleCheckout, PayPal, PaySwarm'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `allowedVehicleType[array]`: Tipo(s) de vehículo que se puede(n) facturar. Enum:'bicicleta, autobús, coche, caravana, motocicleta, motoneta, camión'  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: Un nombre alternativo para este artículo  - `amountCollected[number]`: Importe recaudado por el servicio correspondiente a esta observación  - `amperage[number]`: El amperaje total ofrecido por la estación de carga.  . Model: [http://schema.org/Number](http://schema.org/Number)- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableCapacity[number]`: El número de vehículos que se pueden cargar actualmente. Debe ser menor o igual que `capacidad`.  . Model: [http://schema.org/Number](http://schema.org/Number)- `capacity[number]`: El número total de vehículos que pueden cargarse al mismo tiempo. El número total de enchufes puede ser mayor.  . Model: [http://schema.org/Number](http://schema.org/Number)- `chargeType[array]`: Tipo(s) de cargo al utilizar esta estación. Enum:'pago anual, fijo, gratuito, pago mensual, otro'  . Model: [https://schema.org/Text](https://schema.org/Text)- `chargingUnitId[string]`: Id del punto de recarga de la estación de recarga de VE correspondiente a esta observación  - `contactPoint[object]`: Los datos de contacto del artículo  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: Área geográfica en la que se presta un servicio o se ofrece un artículo. Sustituye a serviceArea    
	- `availabilityRestriction[*]`: Esta propiedad vincula un punto de contacto con información sobre cuándo el punto de contacto no está disponible. Los detalles se proporcionan utilizando la clase Especificación de horarios de apertura  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Idioma que alguien puede utilizar con o en el artículo, servicio o lugar. Utilice uno de los códigos de idioma del estándar IETF BCP 47. Está implementada la opción Texto pero también podría ser Idioma  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Una opción disponible en este punto de contacto (por ejemplo, un número gratuito o asistencia para personas con problemas de audición)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Tipo de contacto de este artículo    
	- `email[idn-email]`: Dirección de correo electrónico del propietario    
	- `faxNumber[string]`: El número de fax  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: El nombre de este artículo    
	- `productSupported[string]`: El producto o servicio con el que está relacionado este punto de contacto de asistencia (por ejemplo, asistencia para una línea de productos concreta). Puede tratarse de un producto o línea de productos específicos (por ejemplo, "iPhone") o de una categoría general de productos o servicios (por ejemplo, "smartphones").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Teléfono de este contacto    
- `dataDescriptor[uri]`: URI que apunta a la entidad descriptora de datos  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `endDateTime[date-time]`: Hora final notificada correspondiente a esta observación  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `network[string]`: El nombre de la Red con la que colabora el operador.  . Model: [https://schema.org/Text](https://schema.org/Text)- `observationDateTime[date-time]`: Última hora de observación comunicada  - `openingHours[string]`: Horario de apertura de la estación de carga.  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `operator[string]`: Operador de la estación de carga.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `powerConsumption[number]`: Potencia consumida por la entidad correspondiente a esta observación  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `socketNumber[number]`: Número total de tomas que ofrece esta estación de recarga  . Model: [http://schema.org/Number](http://schema.org/Number)- `socketType[array]`: Tipo de enchufes que ofrece esta estación. Enum:'Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, Other, Tesla, Type2, Type3, Wall_Euro'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startDateTime[date-time]`: Hora de inicio comunicada correspondiente a esta observación  - `stationName[string]`: El nombre de la estación correspondiente a esta observación. Puede ser el nombre de estación de estacionamiento de bicicletas, estación de carga, etc.  - `status[string]`: Estado de la estación de carga. Enum:'almostEmpty, almostFull, empty, full, outOfService, withIncidence, working'. O cualquier otro específico de la aplicación  . Model: [http://schema.org/Text](http://schema.org/Text)- `taxAmountCollected[number]`: El importe de los impuestos que gravan los productos, las cosas y los servicios, que incluye el impuesto sobre las ventas, el impuesto sobre el valor añadido, el impuesto sobre los servicios, el impuesto sobre bienes y servicios, los derechos de aduana, etc.  - `transactionId[string]`: Id. único de transacción de la entidad correspondiente a esta observación  - `transactionType[string]`: Tipo de transacción basada en el modo de pago (por ejemplo, móvil/UPI, tarjeta, etc.) o el modo de servicio (por ejemplo, emisión, reemisión, entrada, salida, etc.) correspondiente a esta observación.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser EVChargingStation  - `vehicleType[string]`: Tipo de vehículo desde el punto de vista de sus características estructurales. Es diferente de la categoría de vehículo . Enum:vehículo agrícola, ambulancia, cualquier vehículo, vehículo articulado, autorickshaw, bicicleta, binTrolley, autobús BRT, minibús BRT, autobús, coche, caravana, coche o vehículo ligero, coche con caravana, coche con remolque, carro de limpieza, compactador, vehículo de construcción o mantenimiento, volquete, ciclomotor eléctrico, scooter eléctrico, motocicleta eléctrica, camión de bomberos, tracción a las cuatro ruedas, vehículo de gran altura, tolva, camión, minibús, ciclomotor, motocicleta, motocicleta con sidecar, motocarro, furgón policial, barredora, cisterna, tempo, vehículo de tres ruedas, volquete, remolque, tranvía, vehículo de dos ruedas, trolebús, furgoneta, vehículo sin convertidor catalítico, vehículo con caravana, vehículo con remolque, con matrícula par, con matrícula añadida, otros". Los siguientes valores definidos por _VehicleTypeEnum_ y _VehicleTypeEnum2_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `voltage[number]`: La tensión total ofrecida por la estación de carga  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `allowedVehicleType`  - `capacity`  - `id`  - `socketType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Estación pública de recarga que suministra energía a los vehículos eléctricos. El tiempo de carga depende de la potencia máxima de la estación, del número de vehículos que se estén cargando y del nivel actual de la batería.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EVChargingStation:    
  description: EV Charging Station    
  properties:    
    acceptedPaymentMethod:    
      description: 'Type(s) of charge when using this station. Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'''    
      items:    
        enum:    
          - ByBankTransferInAdvance    
          - ByInvoice    
          - Cash    
          - CheckInAdvance    
          - COD    
          - DirectDebit    
          - GoogleCheckout    
          - PayPal    
          - PaySwarm    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
    allowedVehicleType:    
      description: 'Vehicle type(s) which can be charged. Enum:''bicycle, bus, car, caravan, motorcycle, motorscooter, truck'' '    
      items:    
        enum:    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - motorcycle    
          - motorscooter    
          - truck    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    amountCollected:    
      description: Amount collected towards the service corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    amperage:    
      description: The total amperage offered by the charging station.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Ampers (A)    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableCapacity:    
      description: The number of vehicles which currently can be charged. It must lower or equal than `capacity`    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    capacity:    
      description: 'The total number of vehicles which can be charged at the same time. The total number of sockets can be higher. '    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    chargeType:    
      description: 'Type(s) of charge when using this station. Enum:''annualPayment, flat, free, monthlyPayment, other'''    
      items:    
        enum:    
          - annualPayment    
          - flat    
          - free    
          - monthlyPayment    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    chargingUnitId:    
      description: The Id of the charging point in the EV charging station corresponding to this observation    
      type: string    
      x-ngsi:    
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
    dataDescriptor:    
      description: URI pointing to the data-descriptor entity    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    endDateTime:    
      description: Reported end time corresponding to this observation    
      format: date-time    
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
    network:    
      description: 'The name of the Network, with that the operator cooperates. '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    openingHours:    
      description: 'Opening hours of the charging station. '    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
        type: Property    
    operator:    
      description: 'Charging station''s operator. '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    powerConsumption:    
      description: Power consumed by the entity corresponding to this observation    
      type: number    
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
    socketNumber:    
      description: The total number of sockets offered by this charging station    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    socketType:    
      description: 'The type of sockets offered by this station. Enum:''Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, Other, Tesla, Type2, Type3, Wall_Euro'''    
      items:    
        enum:    
          - Caravan_Mains_Socket    
          - CHAdeMO    
          - CCS/SAE    
          - Dual_CHAdeMO    
          - Dual_J-1772    
          - Dual_Mennekes    
          - J-1772    
          - Mennekes    
          - Other    
          - Tesla    
          - Type2    
          - Type3    
          - Wall_Euro    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    startDateTime:    
      description: Reported start time corresponding to this observation    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    stationName:    
      description: 'The name station corresponding to this observation. It can be the name of bike docking station, charging station, etc'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Status of the charging station. Enum:''almostEmpty, almostFull, empty, full, outOfService, withIncidence, working''. Or any other application-specific'    
      enum:    
        - almostEmpty    
        - almostFull    
        - empty    
        - full    
        - outOfService    
        - withIncidence    
        - working    
      type: string    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    taxAmountCollected:    
      description: 'The amount of tax levied on the products, things and services which includes sales tax, value-added tax, service tax, Good and Service tax, customs duty, etc'    
      type: number    
      x-ngsi:    
        type: Property    
    transactionId:    
      description: Unique transaction Id of the entity corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    transactionType:    
      description: 'Type of the transaction based on the mode of payment (For eg. mobile/UPI, card, etc) or mode of service (For eg. Issue, ReIssue, Entry, Exit etc.) corresponding to this observation'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be EVChargingStation    
      enum:    
        - EVChargingStation    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, ambulance, anyVehicle, articulatedVehicle, autorickshaw, bicycle, binTrolley, BRT bus, BRT minibus, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, compactor, constructionOrMaintenanceVehicle, dumper, e-moped, e-scooter, e-motorcycle,fire tender, fourWheelDrive, highSidedVehicle, hopper, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, police van, sweepingMachine, tanker, tempo, threeWheeledVehicle, tipper, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)'    
      enum:    
        - agriculturalVehicle    
        - ambulance    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - BRT bus    
        - BRT minibus    
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
        - fire tender    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - police van    
        - sweepingMachine    
        - tanker    
        - tempo    
        - threeWheeledVehicle    
        - tipper    
        - trailer    
        - tram    
        - twoWheeledVehicle    
        - trolley    
        - van    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    voltage:    
      description: The total voltage offered by the charging station    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Volts (V)    
  required:    
    - id    
    - type    
    - socketType    
    - capacity    
    - allowedVehicleType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/EVChargingStation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/EVChargingStation/schema.json    
  x-model-tags: IUDX    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### EVChargingStation NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una EVChargingStation en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "name": "Agencia de Innovación",  
  "location": {  
    "coordinates": [-4.747901, 41.618265],  
    "type": "Point"  
  },  
  "capacity": 2,  
  "socketType": ["Wall_Euro"],  
  "address": {  
    "streetAddress": "Paseo de Zorrilla, 191",  
    "addressLocality": "Valladolid",  
    "addressCountry": "España"  
  },  
  "contactPoint": {  
    "email": "vehiculoelectrico@ava.es"  
  },  
  "operator": "Iberdrola",  
  "allowedVehicleType": ["car"],  
  "chargeType": ["free"],  
  "source": "https://openchargemap.org/",  
   "powerConsumption": 10.0,  
  "chargingUnitId": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001",  
  "transactionId": "84068784",  
  "transactionType": "RFID",  
  "stationName": "SmartCityTvmGandhiParkOne",  
  "amountCollected": 0.08,  
  "taxAmountCollected": 0.0,  
  "endDateTime": "2022-06-28T20:28:41+05:30",  
  "startDateTime": "2022-06-28T20:27:27+05:30",  
  "vehicleType": "e-motorcycle",  
  "observationDateTime": "2022-06-28T20:27:29+05:30"  
}  
```  
</details>  
#### EVChargingStation NGSI-v2 normalizada Ejemplo  
He aquí un ejemplo de EVChargingStation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "socketType": {  
    "type": "array",  
    "value": [  
      "Wall_Euro"  
    ]  
  },  
  "capacity": {  
    "type": "Number",  
    "value": 2  
  },  
  "name": {  
    "type": "Text",  
    "value": "Agencia de Innovaci\u00f3n"  
  },  
  "allowedVehicleType": {  
    "type": "array",  
    "value": [  
      "car"  
    ]  
  },  
  "source": {  
    "type": "Text",  
    "value": "https://openchargemap.org/"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.747901,  
        41.618265  
      ]  
    }  
  },  
  "chargeType": {  
    "type": "array",  
    "value": [  
      "free"  
    ]  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "Espa\u00f1a",  
      "streetAddress": "Paseo de Zorrilla, 191"  
    }  
  },  
  "operator": {  
    "type": "Text",  
    "value": "Iberdrola"  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  },  
  "powerConsumption": {  
    "type": "number",  
    "value": 10.0  
  },  
  "chargingUnitId": {  
    "type": "string",  
    "value": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001"  
  },  
  "transactionId": {  
    "type": "string",  
    "value": "84068784"  
  },  
  "transactionType": {  
    "type": "string",  
    "value": "RFID"  
  },  
  "stationName": {  
    "type": "string",  
    "value": "SmartCityTvmGandhiParkOne"  
  },  
  "amountCollected": {  
    "type": "number",  
    "value": 0.08  
  },  
  "taxAmountCollected": {  
    "type": "Number",  
    "value": 0.0  
  },  
  "endDateTime": {  
    "format": "date-time",  
    "type": "string",  
    "value": "2022-06-28T20:28:41+05:30"  
  },  
  "startDateTime": {  
    "format": "date-time",  
    "type": "string",  
    "value": "2022-06-28T20:27:27+05:30"  
  },  
  "vehicleType": {  
    "type": "string",  
    "value": "e-motorcycle"  
  },  
  "observationDateTime": {  
    "format": "date-time",  
    "type": "string",  
    "value": "2022-06-28T20:27:29+05:30"  
  }  
}  
```  
</details>  
#### EVChargingStation NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una EVChargingStation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
    "type": "EVChargingStation",  
    "name": "Agencia de Innovaci\u00f3n",  
    "location": {  
        "coordinates": [  
            -4.747901,  
            41.618265  
        ],  
        "type": "Point"  
    },  
    "capacity": 2,  
    "socketType": [  
        "Wall_Euro"  
    ],  
    "address": {  
        "streetAddress": "Paseo de Zorrilla, 191",  
        "addressLocality": "Valladolid",  
        "addressCountry": "Espa\u00f1a"  
    },  
    "contactPoint": {  
        "email": "vehiculoelectrico@ava.es"  
    },  
    "operator": "Iberdrola",  
    "allowedVehicleType": [  
        "car"  
    ],  
    "chargeType": [  
        "free"  
    ],  
    "source": "https://openchargemap.org/",  
    "powerConsumption": 10.0,  
    "chargingUnitId": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001",  
    "transactionId": "84068784",  
    "transactionType": "RFID",  
    "stationName": "SmartCityTvmGandhiParkOne",  
    "amountCollected": 0.08,  
    "taxAmountCollected": 0.0,  
    "endDateTime": "2022-06-28T20:28:41+05:30",  
    "startDateTime": "2022-06-28T20:27:27+05:30",  
    "vehicleType": "e-motorcycle",  
    "observationDateTime": "2022-06-28T20:27:29+05:30",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld",  
        "iudx:EVChargingStation"  
    ]  
}  
```  
</details>  
#### EVChargingStation NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de EVChargingStation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "Espa\u00f1a",  
      "addressLocality": "Valladolid",  
      "streetAddress": "Paseo de Zorrilla, 191"  
    }  
  },  
  "allowedVehicleType": {  
    "type": "Property",  
    "value": [  
      "car"  
    ]  
  },  
  "capacity": {  
    "type": "Property",  
    "value": 2  
  },  
  "chargeType": {  
    "type": "Property",  
    "value": [  
      "free"  
    ]  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "coordinates": [  
        -4.747901,  
        41.618265  
      ],  
      "type": "Point"  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "Agencia de Innovaci\u00f3n"  
  },  
  "operator": {  
    "type": "Property",  
    "value": "Iberdrola"  
  },  
  "socketType": {  
    "type": "Property",  
    "value": [  
      "Wall_Euro"  
    ]  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://openchargemap.org/"  
  },  
  "powerConsumption": {  
    "type": "Property",  
    "value": 10.0  
  },  
  "chargingUnitId": {  
    "type": "Property",  
    "value": "PZEV01-DeltaBharatAC001-SCTLGandhiPark001"  
  },  
  "transactionId": {  
    "type": "Property",  
    "value": "84068784"  
  },  
  "transactionType": {  
    "type": "Property",  
    "value": "RFID"  
  },  
  "stationName": {  
    "type": "Property",  
    "value": "SmartCityTvmGandhiParkOne"  
  },  
  "amountCollected": {  
    "type": "Property",  
    "value": 0.08  
  },  
  "taxAmountCollected": {  
    "type": "Property",  
    "value": 0.0  
  },  
  "endDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-06-28T20:28:41+05:30"  
    }  
  },  
  "startDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-06-28T20:27:27+05:30"  
    }  
  },  
  "vehicleType": {  
    "type": "Property",  
    "value": "e-motorcycle"  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-06-28T20:27:29+05:30"  
    }  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
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
