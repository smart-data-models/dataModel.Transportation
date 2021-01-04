Entidad: Vehículo  
=================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  
Descripción global: **Esta entidad modela un modelo de vehículo en particular, incluyendo todas las propiedades que son comunes a múltiples instancias de vehículos pertenecientes a dicho modelo.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `annotations`: Anotaciones sobre el artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `cargoWeight`: El peso actual de la carga del vehículo  - `category`: Categoría(s) de vehículo(s) desde un punto de vista externo. Es diferente del tipo de vehículo (coche, camión, etc.) representado por la propiedad "VehicleType". Enum:'municipalServicios, no rastreado, privado, público, uso especial, rastreado'. Los vehículos rastreados son aquellos cuya posición es rastreada permanentemente por un sistema remoto. O cualquier otro que necesite una aplicación Incorporan un receptor GPS junto con una conexión de red para actualizar periódicamente una posición reportada (ubicación, velocidad, rumbo...).  - `color`: El color del vehículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateFirstUsed`: La marca de tiempo que denota cuando el vehículo fue usado por primera vez  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `dateVehicleFirstRegistered`: La fecha de la primera matriculación del vehículo ante las respectivas autoridades públicas  - `description`: Una descripción de este artículo  - `feature`: Característica(s) incorporada(s) por el vehículo. Enum:' abs, airbag, alarma, cámara trasera, rampa de desactivación, gps, conexión a internet, sobrevelocidad, proximidadSensor, wifi'. O cualquier otro que necesite la aplicación. Para representar múltiples instancias de una característica se puede utilizar la siguiente sintaxis: `<característica>,<ocurrencias>`. Por ejemplo, un coche con 4 airbags será representado por "airbag,4".  - `fleetVehicleId`: El identificador del vehículo en el contexto de la flota de vehículos a la que pertenece  - `heading`: Denota la dirección de viaje del vehículo y se especifica en grados decimales, donde 0° ≤ "heading"< 360°, contando en el sentido de las agujas del reloj en relación con el verdadero norte. Si el vehículo está parado (es decir, el valor del atributo "velocidad" es "0"), entonces el valor del atributo "rumbo" debe ser igual a "1".  - `id`: Identificador único de la entidad  - `image`: Una imagen del artículo  - `location`:   - `mileageFromOdometer`: La distancia total recorrida por el vehículo en particular desde su producción inicial, según la lectura de su odómetro  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `previousLocation`:   - `purchaseDate`: La fecha en que el artículo, por ejemplo, el vehículo fue comprado por el actual propietario  - `refVehicleModel`: Referencia a un modelo de vehículo  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `serviceProvided`: Servicio(s) que el vehículo es capaz de proporcionar o al que está asignado. Enum:'auxiliarServicios, cargaTransporte, construcción, ferias, basuraRecogida, mercancíasVenta, mantenimiento, parques y jardines, señalización vial, transporte especial, limpieza de calles, alumbrado público, tránsito urbano, residuosLimpieza de contenedores'. O cualquier otro valor que requiera una aplicación específica.  - `serviceStatus`: Estado del vehículo (desde el punto de vista del servicio prestado, por lo que no podría aplicarse a los vehículos privados). "Estacionado": El vehículo está estacionado y no presta ningún servicio en este momento. "En ruta": El vehículo está realizando una misión. Se puede añadir un modificador(es) separado(s) por comas para indicar qué misión está actualmente entregando el vehículo. Por ejemplo, "en ruta, recolección de basura" puede usarse para indicar que el vehículo está en ruta y en una misión de recolección de basura. "averiado": El vehículo está sufriendo una avería temporal. "Fuera de servicio": El vehículo está en la carretera pero no está cumpliendo ninguna misión, probablemente va a su zona de aparcamiento. Enum:'roto, en ruta, fuera de servicio, aparcado'.  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `speed`: Denota la magnitud del componente horizontal de la velocidad actual del vehículo y se especifica en kilómetros por hora. Si se proporciona, el valor del atributo de velocidad debe ser un número real no negativo. `-1` PUEDE utilizarse si la velocidad es transitoriamente desconocida por alguna razón  - `type`: Tipo de entidad NGSI. Tiene que ser un vehículo  - `vehicleConfiguration`: Un texto corto que indique la configuración del vehículo, por ejemplo, "5dr hatchback ST 2.5 MT 225 hp" o "edición limitada".  - `vehicleIdentificationNumber`: El número de identificación del vehículo (VIN) es un número de serie único utilizado por la industria automotriz para identificar vehículos individuales.  - `vehiclePlateIdentifier`:  Un identificador o código que aparece en la placa de matrícula de un vehículo, fijado al mismo, que se utiliza para fines de identificación oficial. El identificador de la matrícula es numérico o alfanumérico y es único dentro de la región de la autoridad emisora. Referencias normativas: DATEXII "Identificador de la placa de matrícula del vehículo  - `vehicleSpecialUsage`: Indica si el vehículo se utiliza para fines especiales, como alquiler comercial, escuela de conducción o como taxi. La legislación de muchos países exige que se revele esta información cuando se ofrece un coche a la venta. Enum:'ambulancia, bomberosBrigada, militar, policía, escuelaTransporte, taxi'  - `vehicleType`: Tipo de vehículo desde el punto de vista de sus características estructurales. Esto es diferente a la categoría de vehículo . Enum:"Vehículo agrícola, cualquier vehículo, vehículo articulado, bicicleta, binTrolley, autobús, coche, caravana, coche ligero, coche con caravana, coche con remolque, limpieza, carrito, construcción o mantenimiento, vehículo, tracción a las cuatro ruedas, vehículo alto, camión, minibús, ciclomotor, motocicleta, Motocicleta con sidecar, motocarro, barredora, cisterna, vehículo de tres ruedas, remolque, tranvía, vehículo de dos ruedas, carro, furgoneta, vehículo sin convertidor catalítico, vehículo con caravana, vehículo con remolque, con placas de matrícula pares, con placas de matrícula impares, otros". Los siguientes valores definidos por _VehicleTypeEnum_ y _VehicleTypeEnum2_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)    
Propiedades requeridas  
- `category`  - `id`  - `location`  - `type`  - `vehicleType`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Vehicle:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
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
    cargoWeight:    
      description: 'Current weight of the vehicle''s cargo'    
      exclusiveMinimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: Kilograms    
    category:    
      description: 'Vehicle category(ies) from an external point of view. This is different than the vehicle type (car, lorry, etc.) represented by the `vehicleType` property. Enum:''municipalServices, nonTracked, private, public, specialUsage, tracked''. Tracked vehicles are those vehicles which position is permanently tracked by a remote system. Or any other needed by an application They incorporate a GPS receiver together with a network connection to periodically update a reported position (location, speed, heading ...).'    
      items:    
        enum:    
          - municipalServices    
          - nonTracked    
          - private    
          - public    
          - specialUsage    
          - tracked    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    color:    
      description: 'Vehicle''s color'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color.    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateFirstUsed:    
      description: 'Timestamp which denotes when the vehicle was first used'    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime.    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateVehicleFirstRegistered:    
      description: 'The date of the first registration of the vehicle with the respective public authorities'    
      format: date    
      type: Property    
      x-ngsi:    
        model: https://schema.org/dateVehicleFirstRegistered.    
    description:    
      description: 'A description of this item'    
      type: Property    
    feature:    
      description: 'Feature(s) incorporated by the vehicle. Enum:'' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi''. Or any other needed by the application. In order to represent multiple instances of a feature it can be used the following syntax: `<feature>,<occurences>`. For example, a car with 4 airbags will be represented by `airbag,4`.'    
      items:    
        enum:    
          - abs    
          - airbag    
          - alarm    
          - backCamera    
          - disabledRamp    
          - gps    
          - internetConnection    
          - overspeed    
          - proximitySensor    
          - wifi    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    fleetVehicleId:    
      description: 'The identifier of the vehicle in the context of the fleet of vehicles to which it belongs'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    heading:    
      description: 'Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0° ≤ `heading` < 360°, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`'    
      oneOf:    
        - maximum: 360    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    id:    
      anyOf: &vehicle_-_properties_-_owner_-_items_-_anyof    
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
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: &vehicle_-_properties_-_previouslocation_-_oneof    
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
    mileageFromOdometer:    
      description: 'The total distance travelled by the particular vehicle since its initial production, as read from its odometer'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/mileageFromOdometer.    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vehicle_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    previousLocation:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *vehicle_-_properties_-_previouslocation_-_oneof    
      title: 'GeoJSON Geometry'    
    purchaseDate:    
      description: 'The date the item e.g. vehicle was purchased by the current owner'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/purchaseDate.    
    refVehicleModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a VehicleModel'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
    serviceProvided:    
      description: 'Service(s) the vehicle is capable of providing or it is assigned to. Enum:''auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning''. Or any other value needed by an specific application.'    
      items:    
        enum:    
          - auxiliaryServices    
          - cargoTransport    
          - construction    
          - fairground    
          - garbageCollection    
          - goodsSelling    
          - maintenance    
          - parksAndGardens    
          - roadSignalling    
          - specialTransport    
          - streetCleaning    
          - streetLighting    
          - urbanTransit    
          - wasteContainerCleaning    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    serviceStatus:    
      description: 'Vehicle status (from the point of view of the service provided, so it could not apply to private vehicles). `parked` : Vehicle is parked and not providing any service at the moment. `onRoute` : Vehicle is performing a mission. A comma-separated modifier(s) can be added to indicate what mission is currently delivering the vehicle. For instance `onRoute,garbageCollection` can be used to denote that the vehicle is on route and in a garbage collection mission. `broken` : Vehicle is suffering a temporary breakdown. `outOfService` : Vehicle is on the road but not performing any mission, probably going to its parking area. Enum:''broken, onRoute, outOfService, parked'''    
      enum:    
        - broken    
        - onRoute    
        - outOfService    
        - parked    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    speed:    
      description: 'Denotes the magnitude of the horizontal component of the vehicle''s current velocity and is specified in Kilometers per Hour. If provided, the value of the speed attribute must be a non-negative real number. `-1` MAY be used if speed is transiently unknown for some reason'    
      oneOf:    
        - minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    type:    
      description: 'NGSI Entity type. It has to be Vehicle'    
      enum:    
        - Vehicle    
      type: Property    
    vehicleConfiguration:    
      description: 'A short text indicating the configuration of the vehicle, e.g. ''5dr hatchback ST 2.5 MT 225 hp'' or ''limited edition'''    
      type: Property    
      x-ngsi:    
        model: https://schema.org/vehicleConfiguration.    
    vehicleIdentificationNumber:    
      description: 'The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/vehicleIdentificationNumber.    
    vehiclePlateIdentifier:    
      description: ' An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes. The registration identifier is numeric or alphanumeric and is unique within the issuing authority''s region. Normative References: DATEXII `vehicleRegistrationPlateIdentifier`'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    vehicleSpecialUsage:    
      description: 'Indicates whether the vehicle is been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale. Enum:''ambulance, fireBrigade, military, police, schoolTransportation, taxi'''    
      enum:    
        - ambulance    
        - fireBrigade    
        - military    
        - police    
        - schoolTransportation    
        - taxi    
      type: Property    
      x-ngsi:    
        model: https://schema.org/vehicleSpecialUsage    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)'    
      enum:    
        - agriculturalVehicle    
        - anyVehicle    
        - articulatedVehicle    
        - bicycle    
        - binTrolley    
        - bus    
        - car    
        - caravan    
        - carOrLightVehicle    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - constructionOrMaintenanceVehicle    
        - fourWheelDrive    
        - highSidedVehicle    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - sweepingMachine    
        - tanker    
        - threeWheeledVehicle    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
  required:    
    - id    
    - type    
    - vehicleType    
    - category    
    - location    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### Vehículo NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de un vehículo en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
      "id": "vehicle:WasteManagement:1",  
      "type": "Vehicle",  
      "vehicleType": "lorry",  
      "category": ["municipalServices"],  
      "location": {  
         "type": "Point",  
         "coordinates": [ -3.164485591715449, 40.62785133667262 ]  
      },  
      "name": "C Recogida 1",  
      "speed": 50,  
      "cargoWeight": 314,  
      "serviceStatus": "onRoute",  
      "serviceProvided": ["garbageCollection", "wasteContainerCleaning"],  
      "areaServed": "Centro",  
      "refVehicleModel": "vehiclemodel:econic",  
      "vehiclePlateIdentifier": "3456ABC"  
}  
```  
#### Vehículo NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un vehículo en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "vehicle:WasteManagement:1",  
    "type": "Vehicle",   
    "category": {  
        "value": [  
            "municipalServices"  
        ]  
    },   
    "vehicleType": {  
        "value": "lorry"  
    },   
    "name": {  
        "value": "C Recogida 1"  
    },   
    "vehiclePlateIdentifier": {  
        "value": "3456ABC"  
    },   
    "refVehicleModel": {  
        "type": "Relationship",   
        "value": "vehiclemodel:econic"  
    },   
    "location": {  
        "type": "geo:json",   
        "value": {  
            "type": "Point",   
            "coordinates": [  
                -3.164485591715449,   
                40.62785133667262  
            ]  
        },  
        "metadata": {  
            "timestamp": {  
                "type": "DateTime",  
                "value": "2018-09-27T12:00:00"  
            }  
        }  
    },   
    "areaServed": {  
        "value": "Centro"  
    },   
    "serviceStatus": {  
        "value": "onRoute"  
    },   
    "cargoWeight": {  
        "value": 314  
    },   
    "speed": {  
        "value": 50,  
        "metadata": {  
            "timestamp": {  
                "type": "DateTime",  
                "value": "2018-09-27T12:00:00"  
            }  
        }  
    },    
    "serviceProvided": {  
        "value": [  
            "gargabeCollection",   
            "wasteContainerCleaning"  
        ]  
    }  
}  
```  
#### Vehículo NGSI-LD valores clave Ejemplo  
Aquí hay un ejemplo de un vehículo en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "areaServed": "Centro",  
 "cargoWeight": 314,  
 "category": ["municipalServices"],  
 "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
 "location": {"coordinates": [-3.164485591715449, 40.62785133667262],  
              "type": "Point"},  
 "name": "C Recogida 1",  
 "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
 "serviceProvided": ["gargabeCollection", "wasteContainerCleaning"],  
 "serviceStatus": "onRoute",  
 "speed": 50,  
 "type": "Vehicle",  
 "vehiclePlateIdentifier": "3456ABC",  
 "vehicleType": "lorry"}  
```  
#### Vehículo NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un vehículo en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
    "type": "Vehicle",  
    "category": {  
        "type": "Property",  
        "value": [  
            "municipalServices"  
        ]  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "lorry"  
    },  
    "name": {  
        "type": "Property",  
        "value": "C Recogida 1"  
    },  
    "vehiclePlateIdentifier": {  
        "type": "Property",  
        "value": "3456ABC"  
    },  
    "refVehicleModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.164485591715449,  
                40.62785133667262  
            ]  
        },  
        "observedAt": "2018-09-27T12:00:00Z"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Centro"  
    },  
    "serviceStatus": {  
        "type": "Property",  
        "value": "onRoute"  
    },  
    "cargoWeight": {  
        "type": "Property",  
        "value": 314  
    },  
    "speed": {  
        "type": "Property",  
        "value": 50,  
        "observedAt": "2018-09-27T12:00:00Z"  
    },  
    "serviceProvided": {  
        "type": "Property",  
        "value": [  
            "gargabeCollection",  
            "wasteContainerCleaning"  
        ]  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
