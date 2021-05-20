Entität: Fahrzeug  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität modelliert ein bestimmtes Fahrzeugmodell, einschließlich aller Eigenschaften, die mehreren zu diesem Modell gehörenden Fahrzeuginstanzen gemeinsam sind.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `cargoWeight`: Aktuelles Gewicht der Ladung des Fahrzeugs  - `category`: Fahrzeugkategorie(n) aus externer Sicht. Diese unterscheidet sich vom Fahrzeugtyp (Pkw, Lkw usw.), der durch die Eigenschaft `vehicleType` dargestellt wird. Enum:'municipalServices, nonTracked, private, public, specialUsage, tracked'. Verfolgte Fahrzeuge sind solche Fahrzeuge, deren Position permanent von einem entfernten System verfolgt wird. Sie verfügen über einen GPS-Empfänger in Verbindung mit einer Netzwerkverbindung, um die gemeldete Position (Position, Geschwindigkeit, Richtung ...) regelmäßig zu aktualisieren.  - `color`: Farbe des Fahrzeugs  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateFirstUsed`: Zeitstempel, der angibt, wann das Fahrzeug zum ersten Mal benutzt wurde  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateVehicleFirstRegistered`: Das Datum der Erstzulassung des Fahrzeugs bei den jeweiligen Behörden  - `description`: Eine Beschreibung dieses Artikels  - `feature`: Vom Fahrzeug eingebaute Funktion(en). Enum:' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi'. Oder jedes andere, das von der Anwendung benötigt wird. Um mehrere Instanzen eines Features zu repräsentieren, kann die folgende Syntax verwendet werden: `<feature>,<occurences>`. Zum Beispiel wird ein Auto mit 4 Airbags durch `airbag,4` dargestellt.  - `fleetVehicleId`: Die Kennung des Fahrzeugs im Kontext der Fahrzeugflotte, zu der es gehört  - `heading`: Bezeichnet die Fahrtrichtung des Fahrzeugs und wird in Dezimalgraden angegeben, wobei 0 <= "Fahrtrichtung" < 360, im Uhrzeigersinn relativ zum wahren Norden gezählt wird. Wenn das Fahrzeug steht (d. h. der Wert des Attributs "speed" ist "0"), muss der Wert des Attributs "heading" gleich "-1" sein.  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `location`:   - `mileageFromOdometer`: Die vom Kilometerzähler abgelesene Gesamtkilometerzahl, die das betreffende Fahrzeug seit seiner Erstproduktion zurückgelegt hat  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `previousLocation`:   - `purchaseDate`: Das Datum, an dem das Objekt, z. B. das Fahrzeug, vom aktuellen Besitzer gekauft wurde  - `refVehicleModel`: Referenz auf ein VehicleModel  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `serviceProvided`: Dienst(e), den/die das Fahrzeug leisten kann oder dem/denen es zugeordnet ist. Enum:'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Oder jeder andere Wert, der von einer bestimmten Anwendung benötigt wird.  - `serviceStatus`: Fahrzeugstatus (aus Sicht des erbrachten Dienstes, kann also nicht für Privatfahrzeuge gelten). Geparkt": Das Fahrzeug ist geparkt und erbringt im Moment keinen Dienst. `onRoute` : Fahrzeug führt einen Einsatz durch. Ein kommagetrennter Modifikator kann hinzugefügt werden, um anzugeben, welche Mission das Fahrzeug gerade ausführt. Zum Beispiel kann `onRoute,garbageCollection` verwendet werden, um anzugeben, dass das Fahrzeug auf der Route und in einer Müllsammelmission ist. `broken` : Das Fahrzeug hat eine vorübergehende Panne. outOfService` : Fahrzeug ist auf der Straße, führt aber keine Mission aus, fährt wahrscheinlich zu seinem Parkplatz. Enum:'broken, onRoute, outOfService, parked'  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `speed`: Bezeichnet den Betrag der horizontalen Komponente der aktuellen Geschwindigkeit des Fahrzeugs und wird in Kilometern pro Stunde angegeben. Wenn angegeben, muss der Wert des Attributs "speed" eine nicht negative reelle Zahl sein. Der Wert "-1" KANN verwendet werden, wenn die Geschwindigkeit aus irgendeinem Grund vorübergehend nicht bekannt ist.  - `type`: NGSI Entity-Typ. Es muss Fahrzeug sein  - `vehicleConfiguration`: Ein kurzer Text, der die Konfiguration des Fahrzeugs angibt, z. B. '5dr Fließheck ST 2.5 MT 225 PS' oder 'limited edition'.  - `vehicleIdentificationNumber`: Die Fahrzeug-Identifikationsnummer (VIN) ist eine eindeutige Seriennummer, die von der Automobilindustrie verwendet wird, um einzelne Kraftfahrzeuge zu identifizieren  - `vehiclePlateIdentifier`:  Eine Kennung oder ein Code, die bzw. der auf einem am Fahrzeug angebrachten Kennzeichen zur amtlichen Identifizierung angezeigt wird. Die Zulassungskennung ist numerisch oder alphanumerisch und ist innerhalb der Region der ausstellenden Behörde eindeutig. Normative Verweise: DATEXII `vehicleRegistrationPlateIdentifier`  - `vehicleSpecialUsage`: Gibt an, ob das Fahrzeug für spezielle Zwecke verwendet wurde, wie z. B. für die gewerbliche Vermietung, Fahrschule oder als Taxi. Die Gesetzgebung in vielen Ländern schreibt vor, dass diese Information offengelegt werden muss, wenn ein Fahrzeug zum Verkauf angeboten wird. Enum:'Ambulanz, Feuerwehr, Militär, Polizei, SchulTransport, Taxi'  - `vehicleType`: Fahrzeugtyp unter dem Gesichtspunkt seiner strukturellen Eigenschaften. Dies ist etwas anderes als die Fahrzeugkategorie . Enum:'agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, carcaravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other'. Die folgenden durch _VehicleTypeEnum_ und _VehicleTypeEnum2_ definierten Werte, [DATEX 2 Version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)    
Erforderliche Eigenschaften  
- `category`  - `id`  - `location`  - `type`  - `vehicleType`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Vehicle:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      description: 'Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0 <= `heading` < 360, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`'    
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
            format: uri    
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
## Beispiel-Nutzlasten  
#### Fahrzeug NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Fahrzeug im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Fahrzeug NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Fahrzeug im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
#### Fahrzeug NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Fahrzeug im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Fahrzeug NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Fahrzeug im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "areaServed": "Centro",  
  "cargoWeight": 314,  
  "category": [  
    "municipalServices"  
  ],  
  "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "name": "C Recogida 1",  
  "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
  "serviceProvided": [  
    "gargabeCollection",  
    "wasteContainerCleaning"  
  ],  
  "serviceStatus": "onRoute",  
  "speed": 50,  
  "type": "Vehicle",  
  "vehiclePlateIdentifier": "3456ABC",  
  "vehicleType": "lorry"  
}  
```  
