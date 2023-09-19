<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: CityWork  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/CityWork/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El Modelo de Datos es una descripción contextual de las obras urbanas realizadas sobre un eje viario y que pueden impactar sobre transportes individuales (Coches, motos, bicicletas, ....) o comunes (Tranvía, Autobús, metro). Contiene una representación geográfica que permite localizar las obras a partir de un objeto JSON específico y a un nivel más global (Segmento de carretera, Carretera, Distrito, ...) con el fin de evaluar los impactos potenciales sobre la circulación. Un objeto GeoJSON puede representar una región del espacio (una Geometría), una entidad delimitada espacialmente (una Característica) o una lista de características (una Colección de Características). consulte el documento [geojson](https://tools.ietf.org/pdf/draft-ietf-geojson-03.pdf) para obtener más información sobre el modelado y el valor posible.**  
versión: 0.4.1  
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
- `allowedVehicle[array]`: Tipo de vehículo autorizado a circular. Una combinación de estos valores. Enum:'todo Vehículo, bicicleta, autobús, coche, empresasCamiones, vehículo de emergencia, bomberos, camión, motocicleta, policía, metro, barredora, remolque, tranvía, camiones, furgoneta'  - `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `busImpacted[array]`: Líneas de autobús afectadas por las obras. Un valor estructurado de 0 a N ocurrencias con 2 subpropiedades por elemento. Primera subpropiedad, una de "lineId / lineName / lineLocation". Segunda subpropiedad, una de "segmentId / segmentName / segmentLocation".  - `contactPoint[object]`: Los datos de contacto del artículo  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: Área geográfica en la que se presta un servicio o se ofrece un artículo. Sustituye a serviceArea    
	- `availabilityRestriction[*]`: Esta propiedad vincula un punto de contacto con información sobre cuándo el punto de contacto no está disponible. Los detalles se proporcionan utilizando la clase Especificación de horarios de apertura  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Idioma que alguien puede utilizar con o en el artículo, servicio o lugar. Utilice uno de los códigos de idioma del estándar IETF BCP 47. Está implementada la opción Texto pero también podría ser Idioma  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Una opción disponible en este punto de contacto (por ejemplo, un número gratuito o asistencia para personas con problemas de audición)  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Tipo de contacto de este artículo    
	- `email[idn-email]`: Dirección de correo electrónico del propietario    
	- `faxNumber[string]`: El número de fax  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: El nombre de este artículo    
	- `productSupported[string]`: El producto o servicio con el que está relacionado este punto de contacto de asistencia (por ejemplo, asistencia para una línea de productos concreta). Puede tratarse de un producto o línea de productos específicos (por ejemplo, "iPhone") o de una categoría general de productos o servicios (por ejemplo, "smartphones").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Teléfono de este contacto    
- `contractingAuthority[string]`: Nombre del poder adjudicador  . Model: [https://schema.org/Text](https://schema.org/Text)- `countOfBusLineImpacted[number]`: Recuento de líneas de autobús afectadas por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfDerogation[number]`: Recuento de excepciones concedidas a la obra Número  . Model: [https://schema.org/number](https://schema.org/number)- `countOfEventImpacted[number]`: Recuento de eventos afectados por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfRailwayLineImpacted[number]`: Recuento de las líneas ferroviarias afectadas por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfRoadImpacted[number]`: Número de carreteras afectadas por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfSchoolBusLineImpacted[number]`: Recuento de las líneas de autobuses escolares afectadas por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfSchoolImpacted[number]`: Cuenta de la Universidad, Escuela u otro recurso educativo afectado por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfStationImpacted[number]`: Número de estaciones de ferrocarril afectadas por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfSubwayLineImpacted[number]`: Recuento de líneas de metro afectadas por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `countOfTramwayLineImpacted[number]`: Recuento de las líneas de tranvía afectadas por las obras  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateLastReported[date-time]`: Marca de tiempo que indica la última vez que el dispositivo notificó datos correctamente. La fecha y hora de esta observación en formato ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `decrees[array]`: Una lista de texto donde cada elemento es una cadena con la URL para descargar o el nombre del decreto  - `derogation[array]`: Excepción concedida para realizar trabajos en días y horas. Un valor estructurado de 0 a N ocurrencias en el que cada elemento tiene el siguiente formato `derogationType` : con subpropiedades "startDate, endDate, dayOfWeek, comment".  - `description[string]`: Descripción de este artículo  - `encroachment[array]`: Impacto de las obras en el espacio público y privado. Una combinación de estos valores. Enum:'otro, privado, público'  . Model: [https://schema.org/Text](https://schema.org/Text)- `endDate[date-time]`: Fecha y hora de finalización de los trabajos en formato ISO8601 UTC. El atributo puede utilizarse además del atributo `workDate` cuando corresponde a un intervalo de tiempo que debe resaltarse.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `eventsImpacted[array]`: Lista de texto libre o a la entidad [Eventos](https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/doc/spec.md) si existe  - `id[*]`: Identificador único de la entidad  - `infrastructureFunction[array]`:  Función de la infraestructura afectada por las obras. Enum:'recogida, distribución, otros, transporte'  . Model: [https://schema.org/Text](https://schema.org/Text)- `isMainRoadImpactedHTR[boolean]`: Valor que indica si la vía de circulación principal se ve afectada. Por defecto falso. https://schema.org/Boolean  - `isMobile[boolean]`: Característica sobre la movilidad de las obras : false para Fijo (por defecto) y true para Móvil  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `mainContractingCompany[string]`: La Empresa Contratista Principal responsable de las obras  . Model: [https://schema.org/Text](https://schema.org/Text)- `maxAuthorizedTonnage[array]`: Carreteras afectadas por las obras con tonelaje máximo autorizado. Un valor estructurado de 0 a N ocurrencias con 2 subpropiedades por elemento. Primera subpropiedad, una de las siguientes: "roadId / roadName / roadLocation". Segunda subpropiedad, "maxTonnage".  - `name[string]`: El nombre de este artículo  - `openingHoursSpecification[array]`: Valor estructurado que proporciona información sobre el horario de apertura de un lugar o de un determinado servicio dentro de un lugar.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `othersContractingCompany[array]`: Una Lista de Texto donde cada elemento es una cadena con el nombre de las Empresas contratantes bajo la responsabilidad de la Empresa contratante principal.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `railwayImpacted[array]`: Líneas ferroviarias afectadas por las obras. Un valor estructurado de 0 a N ocurrencias con 2 subpropiedades por elemento. Primera subpropiedad, una de "lineId / lineName / lineLocation". Segunda subpropiedad, una de "segmentId / segmentName / segmentLocation".  - `roadImpacted[array]`: Carreteras afectadas por las obras y detalles de las carreteras afectadas por las obras. Un valor estructurado de 0 a N ocurrencias en el que cada elemento es una cadena con el formato : 'roadImpact':[Lista de Segmento Impactado o Texto Libre o geo-propiedad, separados por una coma]. Si `isMainRoadImpactedHTR` = true, El primer elemento es este  - `roadImpactedMT[array]`: Una lista de carreteras definidas como Tráfico Mayor, impactadas por las obras. Los valores también se incluyen en el atributo roadImpacted  - `roadImpactedSA[array]`: Lista de carreteras definidas como zonas sensibles, impactadas por las obras. Los valores también se incluyen en el atributo roadImpacted  - `schoolBusImpacted[array]`: Líneas Scholl Bus afectadas por las obras. Un valor estructurado de 0 a N ocurrencias con 2 subpropiedades por elemento. Primera subpropiedad, una de "lineId / lineName / lineLocation". Segunda subpropiedad, una de "segmentId / segmentName / segmentLocation".  - `schoolImpacted[array]`: Lista de texto libre o una Referencia a una entidad [ESCUELA] si existe.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startDate[date-time]`: Fecha y hora de inicio de los trabajos en formato ISO8601 UTC. El atributo puede utilizarse además del atributo `workDate` cuando corresponde a un intervalo de tiempo que debe resaltarse.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `stationImpacted[array]`: Estación afectada por las obras. Valor estructurado de 0 a N ocurrencias con 2 subpropiedades por elemento. Primera subpropiedad, "stationType". Segunda subpropiedad, una de las siguientes: "stationId / stationName / stationLocation".  - `subwayImpacted[array]`: Líneas de metro afectadas por las obras. Un valor estructurado de 0 a N ocurrencias con 2 subpropiedades por elemento. Primera subpropiedad, una de "lineId / lineName / lineLocation". Segunda subpropiedad, una de "segmentId / segmentName / segmentLocation".  - `territorialArea[string]`: Área territorial. Nivel superior al atributo "areaServed". Una lista de texto libre  . Model: [https://schema.org/Text](https://schema.org/Text)- `tramwayImpacted[array]`: Línea de tranvía afectada por las obras. Valor estructurado de 0 a N ocurrencias con 2 subpropiedades por elemento. Primera subpropiedad, una de "lineId / lineName / lineLocation". Segunda subpropiedad, una de "segmentId / segmentName / segmentLocation".  - `type[string]`: Tipo de entidad NGSI. Tiene que ser CityWork  - `typeOfInterventionRequest[string]`: Tipo inicial de solicitud para realizar las obras. Enum:'solicitudAutorización, intervenciónNotificación, otro, urgenteTrabajos'  . Model: [https://schema.org/Text](https://schema.org/Text)- `workDate[string]`: Fecha y hora (Día o periodo) de las obras. Puede representarse mediante una cadena de tiempo específica  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `workDisposition[array]`: Normas específicas adoptadas para las obras. Un valor estructurado de 0 a N ocurrencias donde cada elemento tiene el siguiente formato: `Disposition`: con subpropiedades `startDate`, `endDate`, `dayOfWeek`, `comment`. Enum:'alternatingLights , bicyclePathClosure, bicyclePathDeviation, bicyclePathReduction, circulationManualControl, laneClosure, laneDeviation, laneReduction, noRestriction, parkingForbidden, parkingModification, sidewalkClosure, sidewalkClosureOrReduction, sidewalkReduction, speedReduction'  - `workLastDateUpdate[date-time]`: Fecha límite para actualizar un elemento contractual de la obra  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `workLevel[array]`: Posicionamiento de las obras en relación con un sistema de referencia terrestre. Una combinación de estos elementos. Enum:'aéreo, suelo, mixto, otro, cubierta, superficie, subterráneo, muro'.  - `workNature[array]`: Naturaleza de las obras. Una combinación de estos valores.Enum:'additionalInvestigations, brushCutting, cleaning, collection, connection, consolidation, construction, control, counting, craneLifting, creation, demolition, drivingSwitch, experimentation, extension, filmShooting, Installation-OR-layout, investigation, landFill, maintenance, manholeOpening, ManholeOpeningToRestoreService, miscellaneousInstallation, miscellaneousWorks, mowingDeburring, otros, overheadLinesWorksIntervention, poda, extracción, renovación, rehabilitación, refuerzo, renovación, reparación, sustitución, riprap, roadSign, safetyAndComplianceWork, safetyRailsInstallation, securingPerimeter, siteInstallation, staking, supportImplantation, surfaceOccupationAuthorization, survey, tarring, tonnageExemption, treeCutting, trenchOpening, upgrading".  - `workNumber[string]`: Número asignado a la obra  . Model: [https://schema.org/Text](https://schema.org/Text)- `workOtherImpact[array]`: Otro impacto. Una lista de valores libres  . Model: [https://schema.org/Text](https://schema.org/Text)- `workReason[array]`: Motivos de las obras en caso de intervención urgente. Una combinación de estos valores. Enum:'derrumbe, descarrilamiento, incendio, inundación, fuga de gas, corrimiento de tierras, otro, corte de energía, desprendimiento de rocas, hundimiento, fuga de agua'  - `workState[string]`: Número asignado a la obra. Enum:'all, approved, authorized, cancelled, completed, decreeToBeSigned, draft, editedDecrees, instructionInProgress, investigated, nonCompliantOccupation, open, pendingAuthorization, pendingCancellation, planningCompleted, pendingDocument, pendingExtension, pendingPlanning, planned, received, reject, supported, validatedInPlanning'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `workTarget[array]`: Categorías de obras relativas a las distintas profesiones. Una combinación de estos elementos. Enum:'carrilBici, pasilloAutobús, catainers, cityMotorBike, cityBike, cityCar, cityScooter, coldAndAirCon, coldGroup, copperCable, CoringPenetrometry, drinkingWater, electricityNetworks, exploratoryWork, bocas contraincendios, marcoTecho, redes de gas, generador, monumentos históricos, infraestructura, zona ajardinada, movingHoistNacelleTruck, redes, offStreetParking, opticalFibers, other, overheadLine, papersCollection, pavimento, alumbrado público decorativo, dominio público, transporte público, ferrocarril, aguas pluviales, escollera, rMTNetworks, carreteras, carreteras y dominio público, saneamiento, andamiaje, acera lateral, dispositivos de reducción de velocidad, aparcamiento en la calle, surfaceOccupation, supportStructures, tagsAndPosters, telecomNetworks, telecom-RMT-VideoNetworks, trafficSignalingRegulation, tramway, urbanFurniture, urbanHeating, variousWorks, videoNetworks, vrd".  - `workZone[array]`: Zona de Obras. Una combinación de estos valores. Enum:' aeropuerto, playa, carril bici, puente, corredor de autobuses, dársena, zona inundable, puerto, helipuerto, zona montañosa, fuera de la carretera, otros, aparcamiento, parques-jardines, camino, zona protegida, línea de ferrocarril, zona de riesgo, río, carretera, zona rocosa, zona seveso, paseo lateral, línea de metro, línea de tranvía, túnel'.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CityWork:    
  description: 'The Data Model is a contextual description of urban works carried out on a road axis and which can impact individual (Cars, motorcycle, bicycles, .…) or common transport (Tram, Bus, subway). It contains a geographic representation making it possible to locate its work from a specific JSON Object and at a more global level (Road segment, Road, District, ...) in order to assess the potential impacts on the circulation. A GeoJSON object may represent a region of space (a Geometry), a spatially-bounded entity (a Feature), or a list of features (a Feature Collection). refer to the document [geojson](https://tools.ietf.org/pdf/draft-ietf-geojson-03.pdf) for more information about the modeling and the possible value.'    
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
    allowedVehicle:    
      description: 'Type of vehicle authorized to circulate. A combination of these values. Enum:''all Vehicle, bicycle, bus, car, companiesTrucks,  emergencyVehicle, firefighters, lorry, motorcycle, police, subway, sweepingMachine, trailer, tramway, trucks, van'''    
      items:    
        enum:    
          - allVehicle    
          - bicycle    
          - bus    
          - car    
          - companiesTrucks    
          - emergencyVehicle    
          - firefighters    
          - lorry    
          - motorcycle    
          - police    
          - subway    
          - sweepingMachine    
          - trailer    
          - tramway    
          - trucks    
          - van    
        type: string    
      type: array    
      x-ngsi:    
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
    busImpacted:    
      description: 'Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
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
          lineLocation:    
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
          lineName:    
            type: string    
          segmentId:    
            items:    
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
            type: array    
          segmentLocation:    
            description: Geoproperty. Segment Location of the bus impacted    
            items:    
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
            type: array    
          segmentName:    
            description: Segment Name    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
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
    contractingAuthority:    
      description: Name of the contracting authority    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    countOfBusLineImpacted:    
      description: Count of Bus Lines impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfDerogation:    
      description: Count of derogations granted to the work Number    
      type: number    
      x-ngsi:    
        model: https://schema.org/number    
        type: Property    
    countOfEventImpacted:    
      description: Count of Events impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfRailwayLineImpacted:    
      description: Count of Railway Lines impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfRoadImpacted:    
      description: Count of roads impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSchoolBusLineImpacted:    
      description: Count of School Bus Lines impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSchoolImpacted:    
      description: 'Count of University, School, or other educational resource impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfStationImpacted:    
      description: Count of Railway stations impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSubwayLineImpacted:    
      description: Count of Subway Lines impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfTramwayLineImpacted:    
      description: Count of tramway lines impacted by the works    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    decrees:    
      description: A List of text where each element is a string with the URL to download or the name of the decree    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    derogation:    
      description: 'Derogation granted for carrying out work on days and times. A structured value from 0 to N occurrences where each items has the following format `derogationType` :  with sub properties ''startDate, endDate, dayOfWeek, comment'''    
      items:    
        properties:    
          comment:    
            type: string    
          dayOfWeek:    
            items:    
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
            type: array    
          derogationType:    
            type: string    
          endDate:    
            format: date-time    
            type: string    
          startDate:    
            format: date-time    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    encroachment:    
      description: 'Impact of the works on public, private area. A combination of these values. Enum:''other, private, public'''    
      items:    
        enum:    
          - other    
          - private    
          - public    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    endDate:    
      description: End date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    eventsImpacted:    
      description: 'List of free text or to the entity [Events](https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/doc/spec.md) if exist'    
      items:    
        type: string    
      type: array    
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
    infrastructureFunction:    
      description: ' Function of the infrastructure impacted by the works. Enum:''collection, distribution, other, transportation'''    
      items:    
        enum:    
          - collection    
          - distribution    
          - other    
          - transportation    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    isMainRoadImpactedHTR:    
      description: 'Value to indicate whether the main traffic road is impacted. Default false. https://schema.org/Boolean'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isMobile:    
      description: 'Characteristic on the mobility of the works : false for Fixed (default) and true for Mobile'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
    mainContractingCompany:    
      description: The Main Contracting Company responsible of the works    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    maxAuthorizedTonnage:    
      description: 'Roads impacted by the works with Maximum tonnage authorized. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''roadId / roadName / roadLocation''. Second subproperties, ''maxTonnage'''    
      items:    
        properties:    
          maxTonnage:    
            description: Maximum tonnage authorized for the road. The unit code (text) **TNE** which represents Tonne Metric    
            type: number    
            x-ngsi:    
              type: Property    
          roadId:    
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
          roadImpacted:    
            type: string    
          roadLocation:    
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
          roadName:    
            description: Road Name    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
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
    othersContractingCompany:    
      description: A List of Text where each element is a string with the name of the contracting Companies under the responsibility of the main Contracting Company    
      items:    
        type: string    
      type: array    
      x-ngsi:    
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
    railwayImpacted:    
      description: 'Rail lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
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
          lineLocation:    
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
          lineName:    
            type: string    
          segmentId:    
            items:    
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
            type: array    
          segmentLocation:    
            description: Geoproperty. Segment Location of the railwayImpacted    
            items:    
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
            type: array    
          segmentName:    
            description: Segment Name    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpacted:    
      description: 'Roads impacted by the works and the details of the roads concerned by the work. A structured value from 0 to N occurrences where each items is a string in the format : ''roadImpact'':[List of Segment Impacted or Free Text or geo-property, separated by a comma]. If `isMainRoadImpactedHTR` = true, The first item is this one'    
      items:    
        properties:    
          roadId:    
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
          roadLocation:    
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
          roadName:    
            description: Road Name    
            type: string    
            x-ngsi:    
              type: Property    
          segmentId:    
            items:    
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
            type: array    
          segmentLocation:    
            description: Geoproperty. Segment Location of the road impacted    
            items:    
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
            type: array    
          segmentName:    
            description: Segment Name    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpactedMT:    
      description: 'A list of roads defined as Major Traffic, impacted by the works. Values are also included in the roadImpacted attribute'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpactedSA:    
      description: 'A list of roads defined as sensitive areas, impacted by the works. Values are also included in the roadImpacted attribute'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    schoolBusImpacted:    
      description: 'Scholl Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
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
          lineLocation:    
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
          lineName:    
            type: string    
          segmentId:    
            items:    
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
            type: array    
          segmentLocation:    
            description: Geoproperty. Segment Location of the school Bus Impacted    
            items:    
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
            type: array    
          segmentName:    
            description: Segment Name    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    schoolImpacted:    
      description: 'List of free text or a Reference to an entity [SCHOOL] if exist. '    
      items:    
        type: string    
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
    startDate:    
      description: Start date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    stationImpacted:    
      description: 'Station Impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, ''stationType''. Second subproperties, one of ''stationId / stationName / stationLocation'''    
      items:    
        properties:    
          stationId:    
            description: 'List of free text or reference to the entity [TransportStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/TransportStation/doc/spec.md) if used'    
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
          stationLocation:    
            description: Geoproperty. Station Location of the stationImpacted    
            items:    
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
            type: array    
          stationName:    
            description: Station Name    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
          stationType:    
            description: "A unique value of free text or from the urban transport Mode GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, tram, trolleybus'"    
            enum:    
              - aerialLift    
              - bus    
              - cableTram    
              - ferry    
              - funicular    
              - monorail    
              - rail    
              - subway    
              - tram    
              - trolleybus    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    subwayImpacted:    
      description: 'Subway lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
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
          lineLocation:    
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
          lineName:    
            type: string    
          segmentId:    
            items:    
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
            type: array    
          segmentLocation:    
            description: Geoproperty. Segment Location of the subwayImpacted    
            items:    
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
            type: array    
          segmentName:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    territorialArea:    
      description: Territorial area. Level higher to the attribute 'areaServed'. A list of Free Text    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    tramwayImpacted:    
      description: 'Tramway Line impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
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
          lineLocation:    
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
          lineName:    
            description: Line Name    
            type: string    
            x-ngsi:    
              type: Property    
          segmentId:    
            items:    
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
            type: array    
          segmentLocation:    
            description: Geoproperty. Segment Location of the tramwayImpacted    
            items:    
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
            type: array    
          segmentName:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be CityWork    
      enum:    
        - CityWork    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfInterventionRequest:    
      description: 'Initial type of request to do the works. Enum:''authorizationRequest,  interventionNotice,  other,  urgentWorks'''    
      enum:    
        - authorizationRequest    
        - interventionNotice    
        - other    
        - urgentWorks    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workDate:    
      description: Date and time (Day or period) of the works. It can be represented by an specific time string    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    workDisposition:    
      description: 'Specific rules taken for the works. A structured value from 0 to N occurrences where each items has the following format : `Disposition`: with sub properties  `startDate`, `endDate`,  `dayOfWeek`, `comment`. Enum:''alternatingLights , bicyclePathClosure, bicyclePathDeviation, bicyclePathReduction, circulationManualControl, laneClosure, laneDeviation, laneReduction, noRestriction, parkingForbidden, parkingModification, sidewalkClosure, sidewalkClosureOrReduction, sidewalkReduction, speedReduction'''    
      items:    
        properties:    
          comment:    
            type: string    
          dayOfWeek:    
            items:    
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
            type: array    
          disposition:    
            enum:    
              - alternatingLights    
              - bicyclePathClosure    
              - bicyclePathDeviation    
              - bicyclePathReduction    
              - circulationManualControl    
              - laneClosure    
              - laneDeviation    
              - laneReduction    
              - noRestriction    
              - parkingForbidden    
              - parkingModification    
              - sidewalkClosure    
              - sidewalkClosureOrReduction    
              - sidewalkReduction    
              - speedReduction    
              - workOtherImpact    
            type: string    
          endDate:    
            format: date-time    
            type: string    
          startDate:    
            format: date-time    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    workLastDateUpdate:    
      description: Last date for updating a contractual element of the work    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    workLevel:    
      description: 'Positioning of the works in relation to a ground reference system. A combination of these elements. Enum:''aerial, ground, mixed, other, roofing, surface, underground, wall'''    
      items:    
        enum:    
          - aerial    
          - ground    
          - mixed    
          - other    
          - roofing    
          - surface    
          - underground    
          - wall    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workNature:    
      description: 'Nature of the works. A combination of these values.Enum:''additionalInvestigations, brushCutting, cleaning, collection, connection, consolidation, construction, control, counting, craneLifting, creation, demolition, drivingSwitch, experimentation, extension, filmShooting, Installation-OR-layout, investigation, landFill, maintenance, manholeOpening, ManholeOpeningToRestoreService, miscellaneousInstallation, miscellaneousWorks, mowingDeburring, other, overheadLinesWorksIntervention, pruning, pulling, refurbishment, rehabilitation, reinforcement, renewal, renovation, repair, replacement, riprap, roadSign, safetyAndComplianceWork, safetyRailsInstallation, securingPerimeter, siteInstallation, staking, supportImplantation, surfaceOccupationAuthorization, survey, tarring, tonnageExemption, treeCutting, trenchOpening, upgrading'''    
      items:    
        enum:    
          - additionalInvestigations    
          - brushCutting    
          - cleaning    
          - collection    
          - connection    
          - consolidation    
          - construction    
          - control    
          - counting    
          - craneLifting    
          - creation    
          - demolition    
          - drivingSwitch    
          - experimentation    
          - extension    
          - filmShooting    
          - Installation-OR-layout    
          - investigation    
          - landFill    
          - maintenance    
          - manholeOpening    
          - ManholeOpeningToRestoreService    
          - miscellaneousInstallation    
          - miscellaneousWorks    
          - mowingDeburring    
          - other    
          - overheadLinesWorksIntervention    
          - pruning    
          - pulling    
          - refurbishment    
          - rehabilitation    
          - reinforcement    
          - renewal    
          - renovation    
          - repair    
          - replacement    
          - riprap    
          - roadSign    
          - safetyAndComplianceWork    
          - safetyRailsInstallation    
          - securingPerimeter    
          - siteInstallation    
          - staking    
          - supportImplantation    
          - surfaceOccupationAuthorization    
          - survey    
          - tarring    
          - tonnageExemption    
          - treeCutting    
          - trenchOpening    
          - upgrading    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workNumber:    
      description: Number assigned to the work    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workOtherImpact:    
      description: Other impact. A list of free values    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workReason:    
      description: 'Reasons of the works in case of urgent intervention. A combination of these values. Enum:''collapse, derailment, fire, flood, gasLeak, landslide, other, powerCut, rockfall, sagging, waterLeak'''    
      items:    
        enum:    
          - collapse    
          - derailment    
          - fire    
          - flood    
          - gasLeak    
          - landslide    
          - other    
          - powerCut    
          - rockfall    
          - sagging    
          - waterLeak    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workState:    
      description: 'Number assigned to the work. Enum:''all, approved, authorized, canceled, completed, decreeToBeSigned, draft, editedDecrees, instructionInProgress, investigated, nonCompliantOccupation, open, pendingAuthorization, pendingCancellation, planningCompleted, pendingDocument, pendingExtension, pendingPlanning, planned, received, reject, supported, validatedInPlanning'''    
      enum:    
        - all    
        - approved    
        - authorized    
        - canceled    
        - completed    
        - decreeToBeSigned    
        - draft    
        - editedDecrees    
        - instructionInProgress    
        - investigated    
        - nonCompliantOccupation    
        - open    
        - other    
        - pendingAuthorization    
        - pendingCancellation    
        - planningCompleted    
        - pendingDocument    
        - pendingExtension    
        - pendingPlanning    
        - planned    
        - received    
        - reject    
        - supported    
        - validatedInPlanning    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workTarget:    
      description: 'Categories of works regarding the different profession. A combination of these elements. Enum:''bicyclePath, busCorridor, catainers, cityMotorBike, cityBike, cityCar, cityScooter, coldAndAirCon, coldGroup, copperCable, CoringPenetrometry, drinkingWater, electricityNetworks, exploratoryWork, fireHydrants, frameRoof, gasNetworks, generator, historicalMonuments, infrastructure, landscapedArea, movingHoistNacelleTruck, networks, offStreetParking, opticalFibers, other, overheadLine, papersCollection, pavement, publicDecorativeLighting, publicDomain, publicTransport, railway, rainyWaters, riprap, rMTNetworks, roads, roadsAndPublicDomain, sanitation, scaffolding, sideWalk, speedReductionDevices, streetParking, surfaceOccupation, supportStructures, tagsAndPosters, telecomNetworks, telecom-RMT-VideoNetworks, trafficSignalingRegulation, tramway, urbanFurniture, urbanHeating, variousWorks, videoNetworks, vrd'''    
      items:    
        enum:    
          - bicyclePath    
          - busCorridor    
          - catainers    
          - cityMotorBike    
          - cityBike    
          - cityCar    
          - cityScooter    
          - coldAndAirCon    
          - coldGroup    
          - copperCable    
          - CoringPenetrometry    
          - drinkingWater    
          - electricityNetworks    
          - exploratoryWork    
          - fireHydrants    
          - frameRoof    
          - gasNetworks    
          - generator    
          - historicalMonuments    
          - infrastructure    
          - landscapedArea    
          - movingHoistNacelleTruck    
          - networks    
          - offStreetParking    
          - opticalFibers    
          - other    
          - overheadLine    
          - papersCollection    
          - pavement    
          - publicDecorativeLighting    
          - publicDomain    
          - publicTransport    
          - railway    
          - rainyWaters    
          - riprap    
          - rMTNetworks    
          - roads    
          - roadsAndPublicDomain    
          - sanitation    
          - scaffolding    
          - sideWalk    
          - speedReductionDevices    
          - streetParking    
          - surfaceOccupation    
          - supportStructures    
          - tagsAndPosters    
          - telecomNetworks    
          - telecom-RMT-VideoNetworks    
          - trafficSignalingRegulation    
          - tramway    
          - urbanFurniture    
          - urbanHeating    
          - variousWorks    
          - videoNetworks    
          - vrd    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workZone:    
      description: 'Zone of Works. A combination of these values. Enum:'' airport, beach, bicyclePath, bridge, busCorridor, dock, floodArea, harbor, heliport, mountainousArea, offRoad, other, parking, parksGardens, path, protectArea, railwayLine, riskArea, river, road, rockyArea, sevesoArea, sideWalk, subwayLine, tramwayLine, tunnel'''    
      items:    
        enum:    
          - airport    
          - beach    
          - bicyclePath    
          - bridge    
          - busCorridor    
          - dock    
          - floodArea    
          - harbor    
          - heliport    
          - mountainousArea    
          - offRoad    
          - other    
          - parking    
          - parksGardens    
          - path    
          - protectArea    
          - railwayLine    
          - riskArea    
          - river    
          - road    
          - rockyArea    
          - sevesoArea    
          - sideWalk    
          - subwayLine    
          - tramwayLine    
          - tunnel    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/CityWork/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/CityWork/schema.json    
  x-model-tags: ""    
  x-version: 0.4.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### CityWork NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de CityWork en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": "Nice-Airport-CW2020Q2-006",  
  "alternateName": "AirPort global Observation",  
  "description": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        43.20315,  
        7.20186  
      ],  
      [  
        43.20384,  
        7.20372  
      ],  
      [  
        43.20388,  
        7.20493  
      ],  
      [  
        43.19938,  
        7.20312  
      ],  
      [  
        43.20045,  
        7.20152  
      ],  
      [  
        43.20315,  
        7.20186  
      ]  
    ]  
  },  
  "areaServed": "Nice Aeroport",  
  "territorialArea": "subwaypole Nice",  
  "dateLastReported": "2020-04-02T10:30:00Z",  
  "workNumber": "CW2020Q2-006",  
  "workState": "open",  
  "workDate": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
  "startDate": "2020-03-17T08:45:00Z",  
  "endDate": "2020-04-22T18:45:00Z",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:30:00",  
      "closes": "17:00:00"  
    }  
  ],  
  "contractingAuthority": "MNCA - subwaypole Nice Cote d'Azur",  
  "contactPoint": {  
    "name": "Service des AO"  
  },  
  "decrees": [  
    "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
    "CW-2020Q2-006",  
    "CW-2020Q2-006-Av-001",  
    "CW-2020Q2-006-Av-002"  
  ],  
  "workLastDateUpdate": "2020-03-17T08:45:00Z",  
  "mainContractingCompagny": "XRP - NICOLSPA",  
  "othersContractingCompagny": [  
    "VRD - Terrassement Nicois",  
    "ELEC - Electricite de Nice",  
    "NUM - Consortium operateur"  
  ],  
  "workLevel": [  
    "ground",  
    "underground"  
  ],  
  "workTarget": [  
    "roads",  
    "pavement",  
    "electricityNetworks",  
    "opticalFibers",  
    "videoNetworks",  
    "vrd"  
  ],  
  "workNature": [  
    "landFill",  
    "repair",  
    "tonnageExemption",  
    "securingPerimeter",  
    "trenchOpening",  
    "tarring"  
  ],  
  "infrastructureFunction": [  
    "distribution",  
    "collection"  
  ],  
  "encroachment": [  
    "public",  
    "private"  
  ],  
  "typeOfInterventionRequest": "authorizationRequest",  
  "workReason": [  
    "sagging",  
    "powerCut"  
  ],  
  "workZone": [  
    "road",  
    "sideWalk",  
    "busCorridor",  
    "tramwayLine"  
  ],  
  "workDisposition": [  
    {  
      "disposition": "laneReduction",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ],  
      "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
    },  
    {  
      "disposition": "sidewalkReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "endDate": "2020-05-14T24:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "alternatingLights",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "speedReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday",  
        "Saturday",  
        "Sunday"  
      ],  
      "comment": "Speed Switching from 2 lanes to 1 lane"  
    }  
  ],  
  "workOtherImpact": [  
    "layingCablesOnGround",  
    "shopsTerrace"  
  ],  
  "isMobile": false,  
  "countOfDerogation": 2,  
  "derogation": [  
    {  
      "derogationType": "Work Night during Workday",  
      "startDate": "2020-05-11T20:30:00Z",  
      "endDate": "2020-05-15T23:30:00",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "derogationType": "BRH",  
      "startDate": "2020-05-13T20:30:00Z",  
      "endDate": "2020-05-13T23:30:00Z",  
      "dayOfWeek": [  
        "Wednesday"  
      ]  
    }  
  ],  
  "isMainRoadImpactedHTR": true,  
  "countOfRoadImpacted": 3,  
  "roadImpacted": [  
    {  
      "roadId": "urn:ngsi-ld:Road:N202",  
      "segmentImpacted": [  
        "urn:ngsi-ld:RoadSegment:N202-12",  
        "urn:ngsi-ld:RoadSegment:N202-13"  
      ]  
    },  
    {  
      "roadId": "Road:D021",  
      "segmentImpacted": [  
        "12",  
        "13",  
        "14",  
        "15"  
      ]  
    },  
    {  
      "roadId": "urn:ngsi-ld:Road:D032",  
      "segmentArea": {  
        "type": "LineString",  
        "coordinates": [  
          [  
            102.0,  
            0.0  
          ],  
          [  
            103.0,  
            1.0  
          ],  
          [  
            104.0,  
            0.0  
          ],  
          [  
            105.0,  
            1.0  
          ]  
        ]  
      }  
    }  
  ],  
  "allowedVehicle": [  
    "firefighters",  
    "police",  
    "emergencyVehicle",  
    "companiesTrucks"  
  ],  
  "maxAuthorizedTonnage": [  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:N202",  
      "maxTonnage": 30  
    },  
    {  
      "roadImpacted": "Road:D021",  
      "maxTonnage": 20  
    },  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:D032",  
      "maxTonnage": 15.2  
    }  
  ],  
  "countOfBusLineImpacted": 1,  
  "busImpacted": [  
    {  
      "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
    }  
  ],  
  "countOfTramwayLineImpacted": 2,  
  "tramwayImpacted": [  
    {  
      "lineImpacted": "TramWayLine:L01",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L01-12",  
        "urn:ngsi-ld:TramWaySegment:L01-19"  
      ]  
    },  
    {  
      "lineImpacted": "TramWayLine:L03",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L03-19"  
      ]  
    }  
  ],  
  "countOfRailwayLineImpacted": 1,  
  "railwayImpacted": [  
    {  
      "lineImpacted": "Nice-Grasse",  
      "segmentImpact": [  
        "Nice Saint Augustin section"  
      ]  
    }  
  ],  
  "countOfSchoolImpacted": 2,  
  "schoolImpacted": [  
    "Lycée Massena",  
    "Université Campus Saint Jean"  
  ],  
  "countOfStationImpacted": 4,  
  "stationImpacted": [  
    {  
      "stationId": [  
        "urn:ngsi-ld:station:L205-S13",  
        "urn:ngsi-ld:station:L205-S14"  
      ]  
    },  
    {  
      "stationType": "tram",  
      "stationId": [  
        "L01-S12",  
        "L01-S19"  
      ]  
    }  
  ],  
  "countOfEventImpacted": 2,  
  "eventsImpact": [  
    "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
    "NiceMarathon"  
  ]  
}  
```  
</details>  
#### CityWork NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de CityWork en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": {  
    "type": "string",  
    "value": "Nice-Airport-CW2020Q2-006"  
  },  
  "alternateName": {  
    "type": "string",  
    "value": "AirPort global Observation"  
  },  
  "description": {  
    "type": "string",  
    "value": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          43.20315,  
          7.20186  
        ],  
        [  
          43.20384,  
          7.20372  
        ],  
        [  
          43.20388,  
          7.20493  
        ],  
        [  
          43.19938,  
          7.20312  
        ],  
        [  
          43.20045,  
          7.20152  
        ],  
        [  
          43.20315,  
          7.20186  
        ]  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "string",  
    "value": "Nice Aeroport"  
  },  
  "territorialArea": {  
    "type": "string",  
    "value": "subwaypole Nice"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-04-02T10:30:00Z"  
  },  
  "workNumber": {  
    "type": "string",  
    "value": "CW2020Q2-006"  
  },  
  "workState": {  
    "type": "string",  
    "value": "open"  
  },  
  "workDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-04-02T10:30:00Z"  
      }  
    }  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-02-01TT17:25:00Z"  
      }  
    }  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2020-04-22T18:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-04-02T10:30:00Z"  
      }  
    }  
  },  
  "openingHoursSpecification": {  
    "type": "array",  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Tuesday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Thursday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08:30:00",  
        "closes": "17:00:00"  
      }  
    ]  
  },  
  "contractingAuthority": {  
    "type": "string",  
    "value": "MNCA - subwaypole Nice Cote d'Azur"  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "name": {  
        "type": "string",  
        "value": "Service des AO"  
      }  
    }  
  },  
  "decrees": {  
    "type": "array",  
    "value": [  
      "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
      "CW-2020Q2-006",  
      "CW-2020Q2-006-Av-001",  
      "CW-2020Q2-006-Av-002"  
    ]  
  },  
  "workLastDateUpdate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
     "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-03-16T09:12:25Z"  
      }  
    }  
  },  
  "mainContractingCompany": {  
    "type": "string",  
    "value": "XRP - NICOLSPA"  
  },  
  "othersContractingCompagny": {  
    "type": "array",  
    "value": [  
      "VRD - Terrassement Nicois",  
      "ELEC - Electricite de Nice",  
      "NUM - Consortium operateur"  
    ]  
  },  
  "workLevel": {  
    "type": "array",  
    "value": [  
      "ground",  
      "underground"  
    ]  
  },  
  "workTarget": {  
    "type": "array",  
    "value": [  
      "electricityNetworks",  
      "opticalFibers",  
      "pavement",  
      "roads",  
      "videoNetworks",  
      "vrd"  
    ]  
  },  
  "workNature": {  
    "type": "array",  
    "value": [  
      "landFill",  
      "repair",  
      "securingPerimeter",  
      "tarring",  
      "tonnageExemption",  
      "trenchOpening"  
    ]  
  },  
  "infrastructureFunction": {  
    "type": "array",  
    "value": [  
      "collection",  
      "distribution"  
    ]  
  },  
  "encroachment": {  
    "type": "array",  
    "value": [  
      "public",  
      "private"  
    ]  
  },  
  "typeOfInterventionRequest": {  
    "type": "string",  
    "value": "authorizationRequest"  
  },  
  "workReason": {  
    "type": "array",  
    "value": [  
      "sagging",  
      "powerCut"  
    ]  
  },  
  "workZone": {  
    "type": "array",  
    "value": [  
      "busCorridor",  
      "road",  
      "sideWalk",  
      "tramwayLine"  
    ]  
  },  
  "workDisposition": {  
    "type": "array",  
    "value": [  
      {  
        "disposition": "laneReduction",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ],  
        "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
      },  
      {  
        "disposition": "sidewalkReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "endDate": "2020-05-14T24:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ]  
      },  
      {  
        "disposition": "alternatingLights",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "disposition": "speedReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ],  
        "comment": "Speed Switching from 2 lanes to 1 lane"  
      }  
    ]  
  },  
  "workOtherImpact": {  
    "type": "array",  
    "value": [  
      "layingCablesOnGround",  
      "shopsTerrace"  
    ]  
  },  
  "isMobile": {  
    "type": "Boolean",  
    "value": false  
  },  
  "countOfDerogation": {  
    "type": "number",  
    "value": 2  
  },  
  "derogation": {  
    "type": "array",  
    "value": [  
      {  
        "derogationType": "Work Night during Workday",  
        "startDate": "2020-05-11T20:30:00Z",  
        "endDate": "2020-05-15T23:30:00",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "derogationType": "BRH",  
        "startDate": "2020-05-13T20:30:00Z",  
        "endDate": "2020-05-13T23:30:00Z",  
        "dayOfWeek": [  
          "Wednesday"  
        ]  
      }  
    ]  
  },  
  "isMainRoadImpactedHTR": {  
    "type": "Boolean",  
    "value": true  
  },  
  "countOfRoadImpacted": {  
    "type": "number",  
    "value": 3  
  },  
  "roadImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "roadId": "urn:ngsi-ld:Road:N202",  
        "segmentImpacted": [  
          "urn:ngsi-ld:RoadSegment:N202-12",  
          "urn:ngsi-ld:RoadSegment:N202-13"  
        ]  
      },  
      {  
        "roadId": "Road:D021",  
        "segmentImpacted": [  
          "12",  
          "13",  
          "14",  
          "15"  
        ]  
      },  
      {  
        "roadId": "urn:ngsi-ld:Road:D032",  
        "segmentArea": {  
          "type": "LineString",  
          "coordinates": [  
            [  
              102.0,  
              0.0  
            ],  
            [  
              103.0,  
              1.0  
            ],  
            [  
              104.0,  
              0.0  
            ],  
            [  
              105.0,  
              1.0  
            ]  
          ]  
        }  
      }  
    ]  
  },  
  "allowedVehicle": {  
    "type": "array",  
    "value": [  
      "firefighters",  
      "police",  
      "emergencyVehicle",  
      "companiesTrucks"  
    ]  
  },  
  "maxAuthorizedTonnage": {  
    "type": "array",  
    "value": [  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:N202",  
        "maxTonnage": 30  
      },  
      {  
        "roadImpacted": "Road:D021",  
        "maxTonnage": 20  
      },  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:D032",  
        "maxTonnage": 15.2  
      }  
    ]  
  },  
  "countOfBusLineImpacted": {  
    "type": "number",  
    "value": 1  
  },  
  "busImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
      }  
    ]  
  },  
  "countOfTramwayLineImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "tramwayImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "TramWayLine:L01",  
        "segmentImpacted": [  
          "urn:ngsi-ld:TramWaySegment:L01-12",  
          "urn:ngsi-ld:TramWaySegment:L01-19"  
        ]  
      },  
      {  
        "lineImpacted": "TramWayLine:L03",  
        "segmentImpacted": [  
          "urn:ngsi-ld:TramWaySegment:L03-19"  
        ]  
      }  
    ]  
  },  
  "countOfRailwayLineImpacted": {  
    "type": "number",  
    "value": 1  
  },  
  "railwayImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "Nice-Grasse",  
        "segmentImpact": [  
          "Nice Saint Augustin section"  
        ]  
      }  
    ]  
  },  
  "countOfSchoolImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "schoolImpacted": {  
    "type": "array",  
    "value": [  
      "Lycée Massena",  
      "Université Campus Saint Jean"  
    ]  
  },  
  "countOfStationImpacted": {  
    "type": "number",  
    "value": 4  
  },  
  "stationImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "stationType": "bus",  
        "stationId": [  
          "urn:ngsi-ld:station:L205-S13",  
          "urn:ngsi-ld:station:L205-S14"  
        ]  
      },  
      {  
        "stationType": "tram",  
        "stationId": [  
          "L01-S12",  
          "L01-S19"  
        ]  
      }  
    ]  
  },  
  "countOfEventImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "eventsImpact": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
      "NiceMarathon"  
    ]  
  }  
}  
```  
</details>  
#### CityWork NGSI-LD key-values Ejemplo  
He aquí un ejemplo de CityWork en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
    "type": "CityWork",  
    "allowedVehicle": [  
        "firefighters",  
        "police",  
        "emergencyVehicle",  
        "companiesTrucks"  
    ],  
    "alternateName": "AirPort global Observation",  
    "areaServed": "Nice Aeroport",  
    "busImpacted": [  
        {  
            "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
        }  
    ],  
    "contactPoint": {  
        "name": "Service des AO"  
    },  
    "contractingAuthority": "MNCA - subwaypole Nice Cote d'Azur",  
    "countOfBusLineImpacted": 1,  
    "countOfDerogation": 2,  
    "countOfEventImpacted": 2,  
    "countOfRailwayLineImpacted": 1,  
    "countOfRoadImpacted": 3,  
    "countOfSchoolImpacted": 2,  
    "countOfStationImpacted": 4,  
    "countOfTramwayLineImpacted": 2,  
    "dateLastReported": "2020-04-02T10:30:00Z",  
    "decrees": [  
        "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
        "CW-2020Q2-006",  
        "CW-2020Q2-006-Av-001",  
        "CW-2020Q2-006-Av-002"  
    ],  
    "derogation": [  
        {  
            "derogationType": "Work Nigth during Workday",  
            "startDate": "2020-05-11T20:30:00Z",  
            "endDate": "2020-05-15T23:30:00",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ]  
        },  
        {  
            "derogationType": "BRH",  
            "startDate": "2020-05-13T20:30:00Z",  
            "endDate": "2020-05-13T23:30:00Z",  
            "dayOfWeek": [  
                "Wednesday"  
            ]  
        }  
    ],  
    "description": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals",  
    "encroachment": [  
        "public",  
        "private"  
    ],  
    "endDate": "2020-04-22T18:45:00Z",  
    "eventsImpact": [  
        "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
        "NiceMarathon"  
    ],  
    "infrastructureFunction": [  
        "distribution",  
        "collection"  
    ],  
    "isMainRoadImpactedHTR": true,  
    "isMobile": false,  
    "location": {  
        "type": "Polygon",  
        "coordinates": [  
            [  
                43.20315,  
                7.20186  
            ],  
            [  
                43.20384,  
                7.20372  
            ],  
            [  
                43.20388,  
                7.20493  
            ],  
            [  
                43.19938,  
                7.20312  
            ],  
            [  
                43.20045,  
                7.20152  
            ],  
            [  
                43.20315,  
                7.20186  
            ]  
        ]  
    },  
    "mainContractingCompagny": "XRP - NICOLSPA",  
    "maxAuthorizedTonnage": [  
        {  
            "roadImpacted": "urn:ngsi-ld:Road:N202",  
            "maxTonnage": 30  
        },  
        {  
            "roadImpacted": "Road:D021",  
            "maxTonnage": 20  
        },  
        {  
            "roadImpacted": "urn:ngsi-ld:Road:D032",  
            "maxTonnage": 15.2  
        }  
    ],  
    "name": "Nce-Airport-CW2020Q2-006",  
    "openingHoursSpecification": [  
        {  
            "dayOfWeek": "Monday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Tuesday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Wednesday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Thursday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Friday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Saturday",  
            "opens": "08:30:00",  
            "closes": "17:00:00"  
        }  
    ],  
    "othersContractingCompagny": [  
        "VRD - Terrassement Nicois",  
        "ELEC - Electricite de Nice",  
        "NUM - Consortium operateur"  
    ],  
    "railwayImpacted": [  
        {  
            "lineImpacted": "Nice-Grasse",  
            "segmentImpact": [  
                "Nice Saint Augustin section"  
            ]  
        }  
    ],  
    "roadImpacted": [  
        {  
            "roadId": "urn:ngsi-ld:Road:N202",  
            "segmentImpacted": [  
                "urn:ngsi-ld:RoadSegment:N202-12",  
                "urn:ngsi-ld:RoadSegment:N202-13"  
            ]  
        },  
        {  
            "roadId": "Road:D021",  
            "segmentImpacted": [  
                "12",  
                "13",  
                "14",  
                "15"  
            ]  
        },  
        {  
            "roadId": "urn:ngsi-ld:Road:D032",  
            "segmentArea": {  
                "type": "LineString",  
                "coordinates": [  
                    [  
                        102.0,  
                        0.0  
                    ],  
                    [  
                        103.0,  
                        1.0  
                    ],  
                    [  
                        104.0,  
                        0.0  
                    ],  
                    [  
                        105.0,  
                        1.0  
                    ]  
                ]  
            }  
        }  
    ],  
    "schoolImpacted": [  
        "Lyc\u00e9e Massena",  
        "Universit\u00e9 Campus Saint Jean"  
    ],  
    "startDate": "2020-03-17T08:45:00Z",  
    "stationImpacted": [  
        {  
            "stationType": "bus",  
            "stationId": [  
                "urn:ngsi-ld:station:L205-S13",  
                "urn:ngsi-ld:station:L205-S14"  
            ]  
        },  
        {  
            "stationType": "tram",  
            "stationId": [  
                "L01-S12",  
                "L01-S19"  
            ]  
        }  
    ],  
    "territorialArea": "subwaypole Nice",  
    "tramwayImpacted": [  
        {  
            "lineImpacted": "TramWayLine:L01",  
            "segmentImpacted": [  
                "urn:ngsi-ld:TramWaySegment:L01-12",  
                "urn:ngsi-ld:TramWaySegment:L01-19"  
            ]  
        },  
        {  
            "lineImpacted": "TramWayLine:L03",  
            "segmentImpacted": [  
                "urn:ngsi-ld:TramWaySegment:L03-19"  
            ]  
        }  
    ],  
    "typeOfInterventionRequest": "authorizationRequest",  
    "workDate": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
    "workDisposition": [  
        {  
            "disposition": "laneReduction",  
            "startDate": "2020-05-11T08:00:00Z",  
            "endDate": "2020-05-15T18:30:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ],  
            "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
        },  
        {  
            "disposition": "sidewalkReduction",  
            "startDate": "2020-05-12T00:00:00Z",  
            "endDate": "2020-05-14T24:00:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ]  
        },  
        {  
            "disposition": "alternatingLights",  
            "startDate": "2020-05-11T08:00:00Z",  
            "endDate": "2020-05-15T18:30:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ]  
        },  
        {  
            "disposition": "speedReduction",  
            "startDate": "2020-05-12T00:00:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday",  
                "Saturday",  
                "Sunday"  
            ],  
            "comment": "Speed Switching from 2 lanes to 1 lane"  
        }  
    ],  
    "workLastDateUpdate": "2020-03-17T08:45:00Z",  
    "workLevel": [  
        "ground",  
        "underground"  
    ],  
    "workNature": [  
        "landFill",  
        "repair",  
        "tonnageExemption",  
        "securingPerimeter",  
        "trenchOpening",  
        "tarring"  
    ],  
    "workNumber": "CW2020Q2-006",  
    "workOtherImpact": [  
        "layingCablesOnGround",  
        "shopsTerrace"  
    ],  
    "workReason": [  
        "sagging",  
        "powerCut"  
    ],  
    "workState": "open",  
    "workTarget": [  
        "roads",  
        "pavement",  
        "electricityNetworks",  
        "opticalFibers",  
        "videoNetworks",  
        "vrd"  
    ],  
    "workZone": [  
        "road",  
        "sideWalk",  
        "busCorridor",  
        "tramwayLine"  
    ],  
    "@context": [  
        "https://smartdatamodels.org/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### CityWork NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de CityWork en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort global Observation"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "Service des AO"  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - subwaypole Nice Cote d'Azur"  
  },  
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-04-02T10:30:00Z"  
    }  
  },  
  "decrees": {  
    "type": "Property",  
    "value": [  
      "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
      "CW-2020Q2-006",  
      "CW-2020Q2-006-Av-001",  
      "CW-2020Q2-006-Av-002"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals"  
  },  
  "encroachment": {  
    "type": "Property",  
    "value": [  
      "private",  
      "public"  
    ]  
  },  
  "endDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-04-22T18:45:00Z"  
    }  
  },  
  "infrastructureFunction": {  
    "type": "Property",  
    "value": [  
      "collection",  
      "distribution"  
    ]  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            43.20315,  
            7.20186  
          ],  
          [  
            43.20384,  
            7.20372  
          ],  
          [  
            43.20388,  
            7.20493  
          ],  
          [  
            43.19938,  
            7.20312  
          ],  
          [  
            43.20045,  
            7.20152  
          ],  
          [  
            43.20315,  
            7.20186  
          ]  
        ]  
      ]  
    }  
  },  
  "mainContractingCompany": {  
    "type": "Property",  
    "value": "XRP - NICOLSPA"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Nce-Airport-CW2020Q2-006"  
  },  
  "openingHoursSpecification": {  
    "type": "Property",  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Tuesday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Thursday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "Opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "Opens": "08.30",  
        "closes": "17.00"  
      }  
    ]  
  },  
  "othersContractingCompany": {  
    "type": "Property",  
    "value": [  
      "VRD - Terrassement Nicois",  
      "ELEC - Electricite de Nice",  
      "NUM - Consortium operateur"  
    ]  
  },  
  "startDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "territorialArea": {  
    "type": "Property",  
    "value": "subwaypole Nice"  
  },  
  "typeOfInterventionRequest": {  
    "type": "Property",  
    "value": "authorizationRequest"  
  },  
  "workDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "workDisposition": {  
    "type": "Property",  
    "value": [  
      {  
        "disposition": "laneReduction",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ],  
        "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
      },  
      {  
        "disposition": "sidewalkReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "endDate": "2020-05-14T24:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ]  
      },  
      {  
        "disposition": "alternatingLights",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "disposition": "speedReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ],  
        "comment": "Speed Switching from 2 lanes to 1 lane"  
      }  
    ],  
    "workOtherImpact": {  
      "type": "Property",  
      "value": [  
        "layingCablesOnGround",  
        "shopsTerrace"  
      ]  
    },  
    "isMobile": {  
      "type": "Property",  
      "value": false  
    },  
    "countOfDerogation": {  
      "type": "Property",  
      "value": 2  
    },  
    "derogation": {  
      "type": "Property",  
      "value": [  
        {  
          "derogationType": "Work Nigth during Workday",  
          "startDate": "2020-05-11T20:30:00Z",  
          "endDate": "2020-05-15T23:30:00",  
          "dayOfWeek": [  
            "Monday",  
            "Tuesday",  
            "Wednesday",  
            "Thursday",  
            "Friday",  
            "Saturday",  
            "Sunday"  
          ]  
        },  
        {  
          "derogationType": "BRH",  
          "startDate": "2020-05-13T20:30:00Z ",  
          "endDate": "2020-05-13T23:30:00Z",  
          "dayOfWeek": "Wednesday"  
        }  
      ]  
    },  
    "isMainRoadImpactedHTR": {  
      "type": "Property",  
      "value": true  
    },  
    "countOfRoadImpacted": {  
      "type": "Property",  
      "value": 3  
    },  
    "roadImpacted": {  
      "type": "Property",  
      "value": [  
        {  
          "roadId": "urn:ngsi-ld:Road:N202",  
          "segmentId": [  
            "urn:ngsi-ld:RoadSegment:N202-12",  
            "urn:ngsi-ld:RoadSegment:N202-13"  
          ]  
        },  
        {  
          "roadId": "Road:D021",  
          "segmentName": [  
            "N\u00ba 12",  
            "N\u00ba 13",  
            "N\u00ba 14"  
          ]  
        },  
        {  
          "roadId": "urn:ngsi-ld:Road:D032",  
          "segmentLocation": [  
            {  
              "type": "LineString",  
              "coordinates": [  
                [  
                  102.0,  
                  0.0  
                ],  
                [  
                  103.0,  
                  1.0  
                ],  
                [  
                  104.0,  
                  0.0  
                ],  
                [  
                  105.0,  
                  1.0  
                ]  
              ]  
            },  
            {  
              "type": "Point",  
              "coordinates": [  
                43.655675,  
                7.161232  
              ]  
            }  
          ]  
        },  
        {  
          "roadLocation": {  
            "type": "Point",  
            "coordinates": [  
              43.67428,  
              7.161589  
            ]  
          }  
        }  
      ]  
    },  
    "allowedVehicle": {  
      "type": "Property",  
      "value": [  
        "companiesTrucks",  
        "emergencyVehicle",  
        "firefighters",  
        "police"  
      ]  
    },  
    "maxAuthorizedTonnage": {  
      "type": "Property",  
      "value": [  
        {  
          "roadImpacted": "urn:ngsi-ld:Road:N202",  
          "maxTonnage": 30  
        },  
        {  
          "roadImpacted": "Road:D021",  
          "maxTonnage": 20  
        },  
        {  
          "roadImpacted": "urn:ngsi-ld:Road:D032",  
          "maxTonnage": 15.2  
        }  
      ]  
    },  
    "countOfBusLineImpacted": {  
      "type": "Property",  
      "value": 1  
    },  
    "busImpacted": {  
      "type": "Property",  
      "value": [  
        {  
          "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
        }  
      ]  
    },  
    "countOfTramwayLineImpacted": {  
      "type": "Property",  
      "value": 2  
    },  
    "tramwayImpacted": {  
      "type": "Property ",  
      "value": [  
        {  
          "lineImpacted": "TramWayLine:L01",  
          "segmentImpacted": [  
            "urn:ngsi-ld:TramWaySegment:L01-12",  
            "urn:ngsi-ld:TramWaySegment:L01-19"  
          ]  
        },  
        {  
          "lineImpacted": "TramWayLine:L03",  
          "segmentImpacted": [  
            "urn:ngsi-ld:TramWaySegment:L03-19"  
          ]  
        }  
      ]  
    },  
    "countOfRailwayLineImpacted": {  
      "type": "Property",  
      "value": 1  
    },  
    "railwayImpacted": {  
      "type": "Property ",  
      "value": [  
        {  
          "lineImpacted": "Nice-Grasse",  
          "segmentImpact": [  
            "Nice Saint Augustin section"  
          ]  
        }  
      ]  
    },  
    "countOfSchoolImpacted": {  
      "type": "Property",  
      "value": 2  
    },  
    "schoolImpacted": {  
      "type": "Property",  
      "value": [  
        "Lyc\u00e9e Massena",  
        "Universit\u00e9 Campus Saint Jean"  
      ]  
    },  
    "countOfStationImpacted": {  
      "type": "Property",  
      "value": 4  
    },  
    "stationImpacted": {  
      "type": "Property ",  
      "value": [  
        {  
          "stationType": "bus",  
          "stationId": [  
            "urn:ngsi-ld:station:L205-S13",  
            "urn:ngsi-ld:station:L205-S14"  
          ]  
        },  
        {  
          "stationType": "tram",  
          "stationId": [  
            "L01-S12",  
            "L01-S19"  
          ]  
        }  
      ]  
    },  
    "countOfEventImpacted": {  
      "type": "Property",  
      "value": 2  
    },  
    "eventsImpact": {  
      "type": "Property",  
      "value": [  
        "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
        "NiceMarathon"  
      ]  
    }  
  },  
  "workLastDateUpdate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "workLevel": {  
    "type": "Property",  
    "value": [  
      "ground",  
      "underGround"  
    ]  
  },  
  "workNature": {  
    "type": "Property",  
    "value": [  
      "landFill",  
      "repair",  
      "securingPerimeter",  
      "tarring",  
      "tonnageExemption",  
      "trenchOpening"  
    ]  
  },  
  "workNumber": {  
    "type": "Property",  
    "value": "CW2020Q2-006"  
  },  
  "workReason": {  
    "type": "Property",  
    "value": [  
      "powerCut",  
      "sagging"  
    ]  
  },  
  "workState": {  
    "type": "Property",  
    "value": "open"  
  },  
  "workTarget": {  
    "type": "Property",  
    "value": [  
      "electricityNetworks",  
      "opticalFibers",  
      "pavement",  
      "roads",  
      "videoNetworks",  
      "vrd"  
    ]  
  },  
  "workZone": {  
    "type": "Property",  
    "value": [  
      "busCorridor",  
      "road",  
      "sideWalk",  
      "tramwayLine"  
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
