Entité : Véhicule  
=================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité modélise un modèle de véhicule particulier, y compris toutes les propriétés qui sont communes à plusieurs instances de véhicules appartenant à ce modèle.**  
version : 0.0.3  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `annotations`: Annotations sur l'élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `bearing`: Donne l'angle GPS du véhicule, mesuré dans le sens des aiguilles d'une montre par rapport au nord vrai. Identique au champ "bearing" du message GTFS Realtime-Position (https://developers.google.com/transit/gtfs-realtime/reference#message-position).  - `cargoWeight`: Poids actuel du chargement du véhicule  - `category`: Catégorie(s) de véhicule(s) d'un point de vue externe. Elle est différente du type de véhicule (voiture, camion, etc.) représenté par la propriété `vehicleType`. Enum : 'municipalServices, nonTracked, private, public, specialUsage, tracked'. Les véhicules suivis sont les véhicules dont la position est suivie en permanence par un système distant. Ils intègrent un récepteur GPS ainsi qu'une connexion réseau pour mettre à jour périodiquement une position rapportée (localisation, vitesse, cap...).  - `color`: La couleur du produit  - `currentTripCount`: Le nombre actuel de trajets effectués par le véhicule correspondant à cette observation le jour d'exploitation donné.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateFirstUsed`: Horodatage qui indique la date de la première utilisation du véhicule.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateVehicleFirstRegistered`: La date de la première immatriculation du véhicule auprès des autorités publiques respectives.  - `description`: Une description de cet article  - `deviceBatteryStatus`: Donne l'état de charge de la batterie du dispositif de déclaration. Enum : 'connecté, déconnecté'.  - `deviceSimNumber`: Donne le numéro SIM de l'appareil dans le véhicule.  - `feature`: Fonction(s) incorporée(s) par le véhicule. Enum:' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi'. Ou tout autre élément nécessaire à l'application. Afin de représenter plusieurs instances d'une caractéristique, on peut utiliser la syntaxe suivante : `<fonctionnalité>,<occurrences>`. Par exemple, une voiture avec 4 airbags sera représentée par `airbag,4`.  - `fleetVehicleId`: L'identifiant du véhicule dans le contexte de la flotte de véhicules à laquelle il appartient.  - `fuelEfficiency`: La distance parcourue par unité de carburant utilisée, généralement en kilomètres par litre (km/L).  - `fuelFilled`: Quantité de carburant remplie en litres dans le véhicule correspondant à cette observation.  - `fuelType`: Le type de carburant adapté au moteur ou aux moteurs du véhicule correspondant à cette observation.  - `heading`: Indique le sens de déplacement du véhicule et est spécifié en degrés décimaux, où 0 <= `heading` < 360, en comptant dans le sens horaire par rapport au nord vrai. Si le véhicule est immobile (c'est-à-dire que la valeur de l'attribut `speed` est égale à `0`), la valeur de l'attribut heading doit être égale à `-1``.  - `id`: Identifiant unique de l'entité  - `ignitionStatus`: Indique l'état d'allumage du véhicule. Vrai signifie allumé  - `image`: Une image de l'article  - `license_plate`: Donne le numéro de la plaque d'immatriculation du véhicule. SameAs : license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)".  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `mileageFromOdometer`: La distance totale parcourue par le véhicule particulier depuis sa production initiale, telle que relevée sur son odomètre.  - `name`: Le nom de cet élément.  - `observationDateTime`: Dernière heure d'observation signalée  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `previousLocation`:   - `purchaseDate`: La date à laquelle l'article, par exemple le véhicule, a été acheté par le propriétaire actuel.  - `refVehicleModel`: Référence à un VehicleModel  - `reportId`: Id unique attribué au problème, au rapport, au feedback ou à la transaction correspondant à cette observation.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `serviceProvided`: Service(s) que le véhicule est capable de fournir ou auquel il est affecté. Enum : 'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Ou toute autre valeur requise par une application spécifique.  - `serviceStatus`: Statut du véhicule (du point de vue du service fourni, il ne pourrait donc pas s'appliquer aux véhicules privés). `parked` : le véhicule est garé et ne fournit aucun service pour le moment. `onRoute` : Le véhicule effectue une mission. Un ou plusieurs modificateurs séparés par des virgules peuvent être ajoutés pour indiquer quelle mission est en train de livrer le véhicule. Par exemple, `onRoute,garbageCollection` peut être utilisé pour indiquer que le véhicule est en route et en mission de collecte de déchets. broken (cassé) : Le véhicule souffre d'une panne temporaire. `outOfService` : Le véhicule est sur la route mais n'effectue aucune mission, il se rend probablement sur son aire de stationnement. Enum : 'broken, onRoute, outOfService, parked' (cassé, en route, hors service, garé)  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `speed`: Indique la magnitude de la composante horizontale de la vitesse actuelle du véhicule et est spécifiée en kilomètres par heure. Si elle est fournie, la valeur de l'attribut speed doit être un nombre réel non négatif. La valeur `-1` PEUT être utilisée si la vitesse est transitoirement inconnue pour une raison quelconque.  - `tripNetWeightCollected`: Le poids net collecté par le véhicule correspondant à cette observation à la fin du voyage.  - `type`: Type d'entité NGSI. Il doit s'agir d'un véhicule  - `vehicleAltitude`: Donne l'altitude actuelle du véhicule en utilisant le GPS  - `vehicleConfiguration`: Un texte court indiquant la configuration du véhicule, par exemple "5dr hatchback ST 2.5 MT 225 hp" ou "limited edition".  - `vehicleIdentificationNumber`: Le numéro d'identification du véhicule (NIV) est un numéro de série unique utilisé par l'industrie automobile pour identifier les véhicules à moteur individuels.  - `vehiclePlateIdentifier`:  Un identifiant ou un code affiché sur une plaque d'immatriculation fixée au véhicule, utilisé à des fins d'identification officielle. L'identifiant d'immatriculation est numérique ou alphanumérique et est unique dans la région de l'autorité qui le délivre. Références normatives : DATEXII `vehicleRegistrationPlateIdentifier` (Identificateur de plaque d'immatriculation de véhicule)  - `vehicleRunningStatus`: Donne l'état de charge de la batterie du dispositif de déclaration. Enum : 'en cours, en attente, arrêté'.  - `vehicleSpecialUsage`: Indique si le véhicule est utilisé à des fins particulières, comme la location commerciale, l'auto-école ou comme taxi. La législation de nombreux pays exige que cette information soit révélée lorsqu'une voiture est proposée à la vente. Enum : 'ambulance, pompiers, armée, police, transport scolaire, taxi, gestion des déchets'.  - `vehicleTrackerDevice`: État d'installation du dispositif GPS ou du dispositif de localisation installé sur le véhicule correspondant à cette observation.  - `vehicleType`: Type de véhicule du point de vue de ses caractéristiques structurelles. Il est différent de la catégorie de véhicule. Enum :'véhicule agricole, véhicule quelconque, véhicule articulé, bicyclette, chariot-benne, autobus, voiture, caravane, véhicule léger, voiture avec caravane, voiture avec remorque, chariot de nettoyage, véhicule de construction ou d'entretien, véhicule à quatre roues motrices, véhicule à flancs élevés, camion, minibus, cyclomoteur, moto, moto avec side-car, scooter, balayeuse, camion-citerne, véhicule à trois roues, remorque, tramway, véhicule à deux roues, chariot, camionnette, véhicule sans pot catalytique, véhicule avec caravane, véhicule avec remorque, avec plaques d'immatriculation paires, avec plaques d'immatriculation supplémentaires, autres". Les valeurs suivantes définies par _VehicleTypeEnum_ et _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) et étendues pour d'autres utilisations  - `wardId`: ID du quartier de l'entité correspondant à cette observation.  - `wardName`: Nom de l'entité correspondant à cette observation.  - `zoneName`: Nom de la zone de l'entité correspondant à cette observation    
Propriétés requises  
- `category`  - `id`  - `location`  - `type`  - `vehicleType`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Vehicle:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
  modelTags: IUDX    
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
    bearing:    
      description: "Gives the vehicle GPS angle measured in a clockwise direction from the True North. SameAs 'bearing' field from GTFS Realtime message-Position(https://developers.google.com/transit/gtfs-realtime/reference#message-position)"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cargoWeight:    
      description: 'Current weight of the vehicle''s cargo'    
      exclusiveMinimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
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
    currentTripCount:    
      description: 'The current count of trips made by the vehicle corresponding to this observation on the given day of operation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    dateFirstUsed:    
      description: 'Timestamp which denotes when the vehicle was first used'    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime.    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateVehicleFirstRegistered:    
      description: 'The date of the first registration of the vehicle with the respective public authorities'    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/dateVehicleFirstRegistered.    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBatteryStatus:    
      description: 'Gives the Battery charging status of the reporting device. Enum:''connected, disconnected''.'    
      enum:    
        - connected    
        - disconnected    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    deviceSimNumber:    
      description: 'Gives the SIM number of the device in the vehicle.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fleetVehicleId:    
      description: 'The identifier of the vehicle in the context of the fleet of vehicles to which it belongs'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text.    
        type: Property    
    fuelEfficiency:    
      description: 'The distance traveled per unit of fuel used, commonly in kilometers per liter (km/L).'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelFilled:    
      description: 'Amount of fuel filled in liters to the vehicle corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fuelType:    
      description: 'The type of fuel suitable for the engine or engines of the vehicle corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    heading:    
      description: 'Denotes the direction of travel of the vehicle and is specified in decimal degrees, where 0 <= `heading` < 360, counting clockwise relative to the true north. If the vehicle is stationary (i.e. the value of the `speed` attribute is `0`), then the value of the heading attribute must be equal to `-1`'    
      oneOf:    
        - maximum: 360    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Degree    
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
      x-ngsi:    
        type: Property    
    ignitionStatus:    
      description: 'Gives the ignition status of the vehicle. True means ignited'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    license_plate:    
      description: "Gives the License Plate number of the vehicle. SameAs: license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)'"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    mileageFromOdometer:    
      description: 'The total distance travelled by the particular vehicle since its initial production, as read from its odometer'    
      type: number    
      x-ngsi:    
        model: https://schema.org/mileageFromOdometer.    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vehicle_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    previousLocation:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
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
    purchaseDate:    
      description: 'The date the item e.g. vehicle was purchased by the current owner'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/purchaseDate.    
        type: Property    
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
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    reportId:    
      description: 'Unique Id assigned for the issue or report or feedback or transaction corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    serviceStatus:    
      description: 'Vehicle status (from the point of view of the service provided, so it could not apply to private vehicles). `parked` : Vehicle is parked and not providing any service at the moment. `onRoute` : Vehicle is performing a mission. A comma-separated modifier(s) can be added to indicate what mission is currently delivering the vehicle. For instance `onRoute,garbageCollection` can be used to denote that the vehicle is on route and in a garbage collection mission. ''broken'' : Vehicle is suffering a temporary breakdown. `outOfService` : Vehicle is on the road but not performing any mission, probably going to its parking area. Enum:''broken, onRoute, outOfService, parked'''    
      enum:    
        - broken    
        - onRoute    
        - outOfService    
        - parked    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    speed:    
      description: 'Denotes the magnitude of the horizontal component of the vehicle''s current velocity and is specified in Kilometers per Hour. If provided, the value of the speed attribute must be a non-negative real number. `-1` MAY be used if speed is transiently unknown for some reason'    
      oneOf:    
        - minimum: 0    
          type: number    
        - enum:    
            - -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Km/h    
    tripNetWeightCollected:    
      description: 'The net weight collected by the vehicle corresponding to this observation at the end of the trip.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Vehicle'    
      enum:    
        - Vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleAltitude:    
      description: 'Gives the current altitude of the vehicle using GPS'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleConfiguration:    
      description: 'A short text indicating the configuration of the vehicle, e.g. ''5dr hatchback ST 2.5 MT 225 hp'' or ''limited edition'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleConfiguration.    
        type: Property    
    vehicleIdentificationNumber:    
      description: 'The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles'    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleIdentificationNumber.    
        type: Property    
    vehiclePlateIdentifier:    
      description: ' An identifier or code displayed on a vehicle registration plate attached to the vehicle used for official identification purposes. The registration identifier is numeric or alphanumeric and is unique within the issuing authority''s region. Normative References: DATEXII `vehicleRegistrationPlateIdentifier`'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleRunningStatus:    
      description: 'Gives the Battery charging status of the reporting device. Enum:''running, waiting, stopped''.'    
      enum:    
        - running    
        - stopped    
        - waiting    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleSpecialUsage:    
      description: 'Indicates whether the vehicle is been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale. Enum:''ambulance, fireBrigade, military, police, schoolTransportation, taxi, trashManagement'''    
      enum:    
        - ambulance    
        - fireBrigade    
        - military    
        - police    
        - schoolTransportation    
        - taxi    
        - trashManagement    
      type: string    
      x-ngsi:    
        model: https://schema.org/vehicleSpecialUsage    
        type: Property    
    vehicleTrackerDevice:    
      description: 'Installation status of the GPS device or the tracking device fitted to the vehicle corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) and extended for other uses'    
      enum:    
        - agriculturalVehicle    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - 'BRT mini bus·'    
        - 'BRT bus'    
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
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
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
    wardId:    
      description: 'Ward ID of the entity corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    wardName:    
      description: 'Ward name of the entity corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    zoneName:    
      description: 'Zone name of the entity corresponding to this observation'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - vehicleType    
    - category    
    - location    
  type: object    
  version: 0.0.3    
```  
</details>    
## Exemples de charges utiles  
#### Véhicule NGSI-v2 valeurs-clés Exemple  
Voici un exemple de véhicule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Véhicule NGSI-v2 normalisé Exemple  
Voici un exemple d'un véhicule au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Véhicule NGSI-LD valeurs-clés Exemple  
Voici un exemple de véhicule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Véhicule NGSI-LD normalisé Exemple  
Voici un exemple de véhicule au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
