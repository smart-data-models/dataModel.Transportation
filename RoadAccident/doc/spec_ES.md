Entidad: RoadAccident  
=====================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadAccident/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Descripción de un accidente de tráfico con causas y secuelas. Primera versión desarrollada en el proyecto Synchronicity**.  

## Lista de propiedades  

- `accidentDate`: Fecha del accidente  - `accidentDescription`: Descripción sobre este Accidente de tráfico como combinación de la situación codificada enlistada. 0: Circunstancia no especificada; 1: Conductor procedió regularmente sin girar; 2: Conductor procedió con una conducción distraída o indecisa; 3: Conductor procedió sin mantener la distancia de seguridad; 4: Conductor procedió sin dar prioridad al vehículo que venía por la derecha; 5: Conductor procedió sin respetar el stop; 6: Conductor procedió sin respetar la señal de prioridad; 7: Conductor procedió contra el tráfico; 8: Conductor procedió sin respetar las señales del semáforo o agentes Conductor procedió en contra de la circulación; 8: Conductor procedió sin respetar las señales del semáforo o de los agentes; 10: Conductor procedió sin respetar las señales de prohibición de tránsito o acceso; 11: Conductor procedió con exceso de velocidad; 12: Conductor procedió sin respetar los límites de velocidad; 13: Conductor procedió con el deslumbramiento de las luces cruzando otros vehículos; 14: El conductor giró regularmente a la derecha; 15: Giró irregularmente a la derecha; 16: El conductor giró regularmente a la izquierda; 17: Giró irregularmente a la izquierda; 18: El conductor pasó en la intersección; 20: El conductor procedió regularmente; 21: El conductor procedió con una conducción distraída o indecisa; 22: El conductor procedió sin mantener la distancia de seguridad; 23: El conductor procedió con exceso de velocidad; 24. El conductor procedió sin respetar los límites de velocidad: Conductor procedió sin respetar los límites de velocidad; 25: Procedió sin acercarse al borde derecho de la calzada; 26: Conductor procedió en sentido contrario a la circulación; 27: Conductor procedió sin respetar las señales de prohibición de tránsito o acceso; 28: Conductor procedió con las luces deslumbrantes cruzando otros vehículos; 29: Conductor adelantó regularmente; 30: Adelantó irregularmente a la derecha; 31: El conductor adelantó en una curva, en una pendiente o con visibilidad insuficiente; 32: Adelantó a un vehículo que estaba adelantando a otro; 33: El conductor adelantó sin respetar la señal de prohibición correspondiente; 34: Maniobró en relegación o conversión; 35: El conductor maniobró para incorporarse al flujo de la circulación; 36: Maniobró para girar a la izquierda (paso privado, distribuidor); 37: El conductor maniobró regularmente para detenerse o parar; 38: El conductor maniobró irregularmente para detenerse o parar; 39: Se unió a otros vehículos irregulares de dos ruedas; 40: El conductor procedió regularmente; 41: El conductor procedió con exceso de velocidad; 42: El conductor procedió sin respetar los límites de velocidad; 43: El conductor procedió en contra del tráfico; 44: El conductor pasó el vehículo en marcha; 45: Maniobró; 46: Maniobró sin respetar las señales del semáforo o de los agentes; 47: El conductor salió de la calzada sin precaución; 48: El conductor se salió del carril y atropelló al peón; 49: No dio prioridad al peatón en los cruces correspondientes; 50: Adelantó a un vehículo detenido para permitir el cruce; 51: El conductor atropelló al peatón con la carga; 52: El conductor pasó a un tranvía de forma irregular en la parada El conductor procedía regularmente; 61: El conductor procedía con una conducción distraída o indecisa; 62: El conductor procedía sin mantener la distancia de seguridad; 63: El conductor procedía en contra de la circulación; 64: El conductor procedía con exceso de velocidad; 65: El conductor procedía sin respetar los límites de velocidad; 66: El conductor procedía sin respetar las señales de prohibición de tránsito o acceso; 67: Conductor procedía a adelantar a otro vehículo en marcha; 68: Conductor procedía a cruzar imprudentemente el paso a nivel; 70: Derrame con derrame para evitar el impacto; 71: Listado con derrame por conducción distraída; 72: Escucha con derrame por exceso de velocidad; 73: Frenada brusca del conductor con consecuencia para el transportado; 74: Caída de persona del vehículo por: apertura de puerta; 75: Caída de persona del vehículo por: descenso del vehículo en movimiento; 76: Caída de persona del vehículo por: aferramiento o colocación inadecuada; 80: Fallo o avería de los frenos; 81: Rotura o fallo de la dirección; 82: Reventón o desgaste excesivo de los neumáticos; 83: Falta o insuficiencia de los faros o de las luces de posición; 84: Falta o insuficiencia de las luces intermitentes o de las señales luminosas de parada; 85: Rotura de las piezas de acoplamiento del remolque; 86: Deficiencia del equipo de transporte de mercancías peligrosas; 87: Deficiencia de las adaptaciones prescritas a los vehículos de personas con discapacidad física; 88: Desprendimiento de ruedas; 89: Falta o insuficiencia de dispositivos visuales para bicicletas  - `accidentLocation`: Breve descripción si el accidente tuvo lugar en una zona urbana o extraurbana. 0: Regional dentro de la zona urbana 1: Carretera urbana dentro de la localidad 2: Carretera provincial dentro de la localidad 3: Carretera estatal dentro de la localidad 4: Carretera extraurbana 5: Provincial 6: Carretera estatal 7: Autopista 8: Otra vía 9: Carretera regional  - `accidentStatisticalDate`: la fecha aproximada del accidente (a menudo la fuente de datos de accidentes original sólo informa de atributos estadísticos como la estación, el día de la semana y la hora aproximada  - `accidentType`: Clasificación rápida este Accidente de tráfico. 1: Colisión frontal; 2: Colisión frontal-lateral; 3: Choque lateral; 4: Colisión; 5: Inversión de peatones; 6: Impacto con vehículo parado o detenido; 7: Impacto con vehículo estacionado; 8: Impacto con obstáculo; 9: Impacto con tren; 10: Derrame, deslizamiento; 11: Accidente por frenada brusca; 12: Accidente por caída de vehículo;.  - `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `localId`: Identificador único del conjunto de datos de origen  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `numPassengersDead`: Número de pasajeros del vehículo muertos a causa del accidente  - `numPassengersInjured`: Número de pasajeros del vehículo heridos a causa del accidente  - `numPedestrianDead`: Número de peatones muertos por el accidente  - `numPedestrianInjured`: Número de peatones heridos a causa del accidente  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pedestriansInvolved`: Booleano para determinar si hubo peatones en los accidentes  - `roadClass`:  La clasificación de la carretera donde tuvo lugar este accidente  - `roadIntersection`: Breve descripción del trozo de carretera donde se produjo el accidente.   1: Cruce; 2: Rotonda; 3: Intersección notificada; 4: Intersección con semáforo; 5: Intersección no notificada; 6: Cruce de vías; 7: Recta; 8: Curva; 9: Bache, cuello de botella; 10: Pendiente; 11: Galería iluminada; 12: Galería no iluminada;  - `roadPaving`: Pavimentación de la carretera. 1: Carretera pavimentada; 2: Carretera rugosa; 3: Carretera sin pavimentar;  - `roadSign`: Breve descripción de la señal de tráfico donde se produjo el accidente. 1: Ausente; 2: Vertical; 3: Horizontal; 4: Vertical y horizontal; 5: Temporal por obra;  - `roadSurface`: Breve descripción del estado de la carretera durante el accidente. 1: Seca; 2: Mojada; 3: Resbaladiza; 4: Congelada; 5: Con nieve;  - `roadTrunk`: Breve descripción del tipo de tronco de la carretera donde se produjo el accidente 1: Ramal de carretera; 2: Ramal secundario; 3: Ramal menor; 4: Ramal de empalme; 5: Empalme de carretera; 6: Carril izquierdo de autopista; 7: Derecha de autopista; 8: Entrada de empalme de autopista; 9: Empalme de salida de autopista; 10: Tronco de empalme de autopista; 11: Estación de autopista; 12: Otros casos; 15: Vía extraurbana.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `status`: Estado del accidente de tráfico. Enum:'archivado, en curso, resuelto'  - `totalDeadPeopleWithin24Hours`: Número de personas fallecidas directamente por el accidente  - `totalDeadPeopleWithin30Days`: Número de personas fallecidas a causa de las secuelas del accidente  - `totalInjured`: número total de personas heridas (no muertas) a causa del accidente  - `type`: Tipo de entidad NGSI. Tiene que ser RoadAccident  - `vehiclesInvolved`: Lista de los vehículos (y peatones) implicados en el accidente 0 : peatón 1 : bicicleta 2 : vehículo agrícola 3 : autobús 4 : minibús 5 : coche 6 : caravana 7 : tranvía 8 : camión cisterna 9 : cocheConCaravana 10 : cocheConRemolque 11 : camión 12 : ciclomotor 13 : camión cisterna 14 : motocicleta 15 : motocicletaConCocheLateral 16 : motocarro 17 : remolque 18 : furgoneta 19 : caravana 20 : vehículoDeConstrucciónOdeMantenimiento 21 : carro 22 : carro de basura 23 : máquina de barrer 24 : carro de limpieza  - `weakestSubject`: vehículo que representa el sujeto más débil implicado porque el accidente (generalmente peatón). 0 : peatón 1 : bicicleta 2 : vehículo agrícola 3 : autobús 4 : minibús 5 : coche 6 : caravana 7 : tranvía 8 : camión cisterna 9 : cocheConCaravana 10 : cocheConRemolque 11 : camión 12 : ciclomotor 13 : camión cisterna 14 : motocicleta 15 : motoConCarrera 16 : motocarro 17 : remolque 18 : furgoneta 19 : caravana 20 : vehículo de construcciónOrMantenimiento 21 : carro 22 : carro de basura 23 : máquina de barrer 24 : carro de limpieza  - `weatherConditions`: Breve descripción de las condiciones meteorológicas durante este accidente de tráfico. 0 : despejadoNoche 1 : soleadoDía 2 : ligeramenteNublado 3 : parcialmenteNublado 4 : bruma 5 : niebla 6 : nubesAltas 7 : nublado 8 : muyNublado 9 : nublado 10 : lluviaLigeraLluvia 11 : llovizna 12 : lluviaLigera 13 : lluvia fuerteDisparador 14 : lluvia fuerte 15 : aguanieveDisparador 16 : aguanieve 17 : granizoDisparador 18 : granizo 19 : lluvia 20 : nieve ligera 21 : nieve 22 : nieve fuerteDisparador 23 : nieve fuerte 24 : truenoDisparador 25 : trueno    
Propiedades requeridas  
- `id`  - `status`  - `type`    
Modelo de datos procedente del proyecto synchronicity  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadAccident:    
  description: 'A road accident description with causes and aftermath. First version developed in Synchronicity project'    
  properties:    
    accidentDate:    
      description: 'Datetime of the accident'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    accidentDescription:    
      description: 'Description about this Road Accident as a combination of codified situation enlisted. 0: Unspecified circumstance; 1: Driver proceeded regularly without turning; 2: Driver proceeded with a distracted driving or undecided course; 3: Driver proceeded without maintaining a safe distance; 4: Driver proceeded without giving priority to the vehicle coming from the right; 5: Driver proceeded without respecting the stop; 6: Driver proceeded without respecting the signal to give precedence; 7: Driver proceeded against traffic; 8: Driver proceeded without respecting the traffic light or agent signals; 10: Driver proceeded without respecting the signs of prohibition of transit or access; 11: Driver proceeded with speeding; 12: Driver proceeded without respecting the speed limits; 13: Driver proceeded with the dazzling lights crossing other vehicles; 14: Driver turned right regularly; 15: It turned irregularly to the right; 16: Driver turned left regularly; 17: It turned irregularly to the left; 18: Driver passed at the intersection; 20: Driver proceeded regularly; 21: Driver proceeded with a distracted driving or undecided course; 22: Driver proceeded without maintaining a safe distance; 23: Driver proceeded with speeding; 24: Driver proceeded without respecting the speed limits; 25: It proceeded not near the right edge of the roadway; 26: Driver proceeded against traffic; 27: Driver proceeded without respecting the signs of prohibition of transit or access; 28: Driver proceeded with the dazzling lights crossing other vehicles; 29: Driver passed regularly; 30: It passed irregularly to the right; 31: Driver overtook on a curve, on a hill or with insufficient visibility; 32: It overtook a vehicle that was overtaking another; 33: Driver passed without observing the appropriate prohibition sign; 34: Maneuvered in relegation or conversion; 35: Driver maneuvered to get into the flow of circulation; 36: Maneuvering To turn left (private passage, distributor); 37: Driver maneuvered regularly to stop or stop; 38: Driver maneuvered irregularly to stop or stop; 39: It was joined by other irregular two-wheeled vehicles; 40: Driver proceeded regularly; 41: Driver proceeded with speeding; 42: Driver proceeded without respecting the speed limits; 43: Driver proceeded against traffic; 44: Driver passed the vehicle in gear; 45: Maneuvered; 46: Maneuvered without respecting traffic light or agent signals; 47: Driver came out of the driveway without precaution; 48: Driver stepped out of the lane and hit the pawn; 49: It did not give priority to the pedestrian on the appropriate crossings; 50: It overtook a vehicle stopped to allow the crossing; 51: Driver hit the pedestrian with the load; 52: Driver was passing a tram unevenly at the stop; 60: Driver proceeded regularly; 61: Driver proceeded with a distracted driving or undecided course; 62: Driver proceeded without maintaining a safe distance; 63: Driver proceeded against traffic; 64: Driver proceeded with speeding; 65: Driver proceeded without respecting the speed limits; 66: Driver proceeded without respecting the signs of prohibition of transit or access; 67: Driver was passing another vehicle in gear; 68: Driver imprudently crossed the level crossing; 70: Spill with spillage to avoid impact; 71: Listening with spillage for distracted driving; 72: List with over-speed spill; 73: Driver suddenly braked with consequence to the transported; 74: Fall of person from vehicle for: door opening; 75: Fall of person from vehicle for: descent from vehicle in motion; 76: Fall of person from vehicle due to: clinging or improperly placed; 80: Brake failure or failure; 81: Breakage or steering failure; 82: Tire burst or excessive wear; 83: Lack or insufficiency of headlights or position lights; 84: Lack or insufficiency of flashing lights or stopping light signals; 85: Breaking of trailer coupling parts; 86: Deficiency of dangerous goods transport equipment; 87: Deficiency of the adaptations prescribed to vehicles of physically handicapped people; 88: Wheel detachment; 89: Lack or insufficiency    
        of visual devices for cycles'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
          - 25    
          - 26    
          - 27    
          - 28    
          - 29    
          - 30    
          - 31    
          - 32    
          - 33    
          - 34    
          - 35    
          - 36    
          - 37    
          - 38    
          - 39    
          - 40    
          - 41    
          - 42    
          - 43    
          - 44    
          - 45    
          - 46    
          - 47    
          - 48    
          - 49    
          - 50    
          - 51    
          - 52    
          - 53    
          - 54    
          - 55    
          - 56    
          - 57    
          - 58    
          - 59    
          - 60    
          - 61    
          - 62    
          - 63    
          - 64    
          - 65    
          - 66    
          - 67    
          - 68    
          - 69    
          - 70    
          - 71    
          - 72    
          - 73    
          - 74    
          - 75    
          - 76    
          - 77    
          - 78    
          - 79    
          - 80    
          - 81    
          - 82    
          - 83    
          - 84    
          - 85    
          - 86    
          - 87    
          - 88    
          - 89    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    accidentLocation:    
      description: 'Brief description if the accident took place in a urban or extra-urban area. 0: Regional within the urban area 1: Urban road in the town 2: Provincial road within the town 3: State road within the village 4: Extra-urban road 5: Provincial 6: State road 7: Highway 8: Another way 9: Regional road'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
      type: Property    
    accidentStatisticalDate:    
      description: 'approximate datetime of the accident (often original accident data source reports only statistical attributes such as season, weekday and approximate hour'    
      properties:    
        hour:    
          type: integer    
        quarter:    
          type: integer    
        weekday:    
          description: 'Week days'    
          enum:    
            - Monday    
            - Tuesday    
            - Wednesday    
            - Thursday    
            - Friday    
            - Saturday    
            - Sunday    
          type: string    
        year:    
          type: integer    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    accidentType:    
      description: 'Quick classification this Road Accident. 1: Frontal collision; 2: Frontal-lateral collision; 3: Side crash; 4: Collision; 5: Pedestrian investment; 6: Impact with vehicle stopped or stopped; 7: Impact with parked vehicle; 8: Impact with obstacle; 9: Impact with train; 10: Spill, slip; 11: Accident due to sudden braking; 12: Accident due to falling from a vehicle;. '    
      items:    
        enum:    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
        type: string    
      type: Property    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      anyOf: &roadaccident_-_properties_-_owner_-_items_-_anyof    
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
    localId:    
      description: 'Unique identifier from the source data set'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
    numPassengersDead:    
      description: 'Number of vehicle''s passengers dead because the accident'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    numPassengersInjured:    
      description: 'Number of vehicle''s passengers injured because the accident'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    numPedestrianDead:    
      description: 'Number of pedestrians dead because the accident'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    numPedestrianInjured:    
      description: 'Number of pedestrians injured because the accident'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadaccident_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pedestriansInvolved:    
      description: 'Boolean to determine if pedestrians were involved in the accidents'    
      type: Property    
    roadClass:    
      description: ' The classification of road where this accident took place'    
      type: Property    
      x-ngsi:    
        model: https://wiki.openstreetmap.org/wiki/Key:highway    
    roadIntersection:    
      description: 'Brief description of the piece of the road where the accident took place.   1: Crossroad; 2: Roundabout; 3: Reported intersection; 4: Intersection with traffic light; 5: Intersection not reported; 6: Rail crossing; 7: Straight; 8: Curve; 9: Bump, bottleneck; 10: Slope; 11: Illuminated gallery; 12: Unlit gallery;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
      type: Property    
    roadPaving:    
      description: 'Road paving. 1: Paved road; 2: Rough paved road; 3: Unpaved road;'    
      enum:    
        - 1    
        - 2    
        - 3    
      type: Property    
    roadSign:    
      description: 'Brief description of the road sign where the accident took place. 1: Absent; 2: Vertical; 3: Horizontal; 4: Vertical and horizontal; 5: Temporary by construction site;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
      type: Property    
    roadSurface:    
      description: 'Brief description of the condition of the road during the accident. 1: Dry; 2: Wet; 3: Slippery; 4: frozen; 5: Snowcapped;'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
      type: Property    
    roadTrunk:    
      description: 'Brief description of type of trunk of the road where the accident took place. 1: Road branch; 2: Secondary branch; 3: Minor branch; 4: Junction branch; 5: Road junction; 6: Motorway left lane; 7: Highway carriageway right; 8: Motorway junction entrance; 9: Highway exit junction; 10: Highway junction trunk; 11: Highway station; 12: Other cases; 15: Extra urban road.'    
      enum:    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 15    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    status:    
      description: 'Status of the Road Accident. Enum:''archived, onGoing, solved'''    
      enum:    
        - archived    
        - onGoing    
        - solved    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    totalDeadPeopleWithin24Hours:    
      description: 'Number of people dead directly because the accident'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    totalDeadPeopleWithin30Days:    
      description: 'Number of people dead because the aftermath of the accident'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    totalInjured:    
      description: 'total number of people injured (not dead) because the accident'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI Entity type. it has to be RoadAccident'    
      enum:    
        - RoadAccident    
      type: Property    
    vehiclesInvolved:    
      description: 'List of the vehicles (and pedestrians) involved because the accident 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
        type: string    
      type: Property    
    weakestSubject:    
      description: 'vehicle that represent the weakest subject involved because the accident (usually pedestrian). 0 : pedestrian 1 : bicycle 2 : agriculturalVehicle 3 : bus 4 : minibus 5 : car 6 : caravan 7 : tram 8 : tanker 9 : carWithCaravan 10 : carWithTrailer 11 : lorry 12 : moped 13 : tanker 14 : motorcycle 15 : motorcycleWithSideCar 16 : motorscooter 17 : trailer 18 : van 19 : caravan 20 : constructionOrMaintenanceVehicle 21 : trolley 22 : binTrolley 23 : sweepingMachine 24 : cleaningTrolley'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
        - 4    
        - 5    
        - 6    
        - 7    
        - 8    
        - 9    
        - 10    
        - 11    
        - 12    
        - 13    
        - 14    
        - 15    
        - 16    
        - 17    
        - 18    
        - 19    
        - 20    
        - 21    
        - 22    
        - 23    
        - 24    
      type: Property    
    weatherConditions:    
      description: 'Brief description of weather conditions during this Road Accident. 0 : clearNight 1 : sunnyDay 2 : slightlyCloudy 3 : partlyCloudy 4 : mist 5 : fog 6 : highClouds 7 : cloudy 8 : veryCloudy 9 : overcast 10 : lightRainShower 11 : drizzle 12 : lightRain 13 : heavyRainShower 14 : heavyRain 15 : sleetShower 16 : sleet 17 : hailShower 18 : hail 19 : shower 20 : lightSnow 21 : snow 22 : heavySnowShower 23 : heavySnow 24 : thunderShower 25 : thunder'    
      items:    
        enum:    
          - 0    
          - 1    
          - 2    
          - 3    
          - 4    
          - 5    
          - 6    
          - 7    
          - 8    
          - 9    
          - 10    
          - 11    
          - 12    
          - 13    
          - 14    
          - 15    
          - 16    
          - 17    
          - 18    
          - 19    
          - 20    
          - 21    
          - 22    
          - 23    
          - 24    
          - 25    
        type: string    
      type: Property    
  required:    
    - id    
    - type    
    - status    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### RoadAccident NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un RoadAccident en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "source": "To be defined",  
  "name": "Name of the element of the accident.",  
  "alternateName": "Other name.",  
  "description": "Clash in the middle of a traffic light",  
  "dataProvider": "Municipality.",  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "areaServed": "worldwide",  
  "localId": "20210312-A1.",  
  "status": "onGoing",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentStatisticalDate": {  
    "year": 2021,  
    "quarter": 1,  
    "weekday": "Friday",  
    "hour": 4  
  },  
  "accidentType": [  
    "10",  
    "6"  
  ],  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "roadSurface": "2",  
  "roadPaving": "2",  
  "accidentLocation": "5",  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadTrunk": "12",  
  "roadSign": "5",  
  "pedestriansInvolved":  
    true  
  ,  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "numPassengersInjured": 1,  
  "numPassengersDead": 1,  
  "numPedestrianInjured": 1,  
  "numPedestrianDead": 0,  
  "totalInjured": 2,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalDeadPeopleWithin24Hours": 0  
}  
```  
#### RoadAccident NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un RoadAccident en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-06-23T04:19:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-29T08:36:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "FranklinStrasse",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10387",  
      "postOfficeBoxNumber": "",  
      "areaServed": "worldwide."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentStatisticalDate": {  
    "type": "Property",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "Property",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": [  
      "true"  
    ]  
  },  
  "vehiclesInvolved": {  
    "type": "Property",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Property",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  }  
}  
```  
#### RoadAccident NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un RoadAccident en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-06-23T04:19:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-29T08:36:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "FranklinStrasse",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10387",  
      "postOfficeBoxNumber": "",  
      "areaServed": "worldwide."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentStatisticalDate": {  
    "type": "Property",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "Property",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": [  
      "true"  
    ]  
  },  
  "vehiclesInvolved": {  
    "type": "Property",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Property",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### RoadAccident NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un RoadAccident en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "source": "To be defined",  
  "name": "Name of the element of the accident.",  
  "alternateName": "Other name.",  
  "description": "Clash in the middle of a traffic light",  
  "dataProvider": "Municipality.",  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "areaServed": "worldwide",  
  "localId": "20210312-A1.",  
  "status": "onGoing",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentStatisticalDate": {  
    "year": 2021,  
    "quarter": 1,  
    "weekday": "Friday",  
    "hour": 4  
  },  
  "accidentType": [  
    "10",  
    "6"  
  ],  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "roadSurface": "2",  
  "roadPaving": "2",  
  "accidentLocation": "5",  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadTrunk": "12",  
  "roadSign": "5",  
  "pedestriansInvolved": [  
    "true"  
  ],  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "numPassengersInjured": 1,  
  "numPassengersDead": 1,  
  "numPedestrianInjured": 1,  
  "numPedestrianDead": 0,  
  "totalInjured": 2,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalDeadPeopleWithin24Hours": 0,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud