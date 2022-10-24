<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Véhicule  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/Vehicle/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité modélise un modèle de véhicule particulier, y compris toutes les propriétés qui sont communes à plusieurs instances de véhicules appartenant à ce modèle.**  
version : 0.2.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `annotations[array]`: Annotations sur l'élément  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `bearing[number]`: Donne l'angle GPS du véhicule, mesuré dans le sens des aiguilles d'une montre par rapport au nord vrai. Identique au champ "bearing" du message GTFS Realtime-Position (https://developers.google.com/transit/gtfs-realtime/reference#message-position).  . Model: [https://schema.org/Number](https://schema.org/Number)- `cargoWeight[number]`: Poids actuel du chargement du véhicule  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Catégorie(s) de véhicule(s) d'un point de vue externe. Elle est différente du type de véhicule (voiture, camion, etc.) représenté par la propriété `vehicleType`. Enum : 'municipalServices, nonTracked, private, public, specialUsage, tracked'. Les véhicules suivis sont les véhicules dont la position est suivie en permanence par un système distant. Ils intègrent un récepteur GPS ainsi qu'une connexion réseau pour mettre à jour périodiquement une position rapportée (localisation, vitesse, cap...).  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: La couleur du produit  . Model: [https://schema.org/color](https://schema.org/color)- `currentTripCount[number]`: Le nombre actuel de trajets effectués par le véhicule correspondant à cette observation le jour d'exploitation donné.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateFirstUsed[string]`: Horodatage qui indique la date de la première utilisation du véhicule.  . Model: [https://schema.org/DateTime.](https://schema.org/DateTime.)- `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateVehicleFirstRegistered[string]`: La date de la première immatriculation du véhicule auprès des autorités publiques respectives.  . Model: [https://schema.org/dateVehicleFirstRegistered.](https://schema.org/dateVehicleFirstRegistered.)- `description[string]`: Une description de cet article  - `deviceBatteryStatus[string]`: Donne l'état de charge de la batterie du dispositif de déclaration. Enum : 'connecté, déconnecté'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceSimNumber[string]`: Donne le numéro SIM de l'appareil dans le véhicule.  . Model: [https://schema.org/Text](https://schema.org/Text)- `emergencyVehicleType[string]`: Type de véhicule d'urgence correspondant à cette observation. Enum:'policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulance, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck  . Model: [https://schema.org/Text](https://schema.org/Text)- `feature[array]`: Fonction(s) incorporée(s) par le véhicule. Enum:' abs, airbag, alarm, backCamera, disabledRamp, gps, internetConnection, overspeed, proximitySensor, wifi'. Ou tout autre élément nécessaire à l'application. Afin de représenter plusieurs instances d'une caractéristique, on peut utiliser la syntaxe suivante : `<fonctionnalité>,<occurrences>`. Par exemple, une voiture avec 4 airbags sera représentée par `airbag,4`.  . Model: [https://schema.org/Text](https://schema.org/Text)- `fleetVehicleId[string]`: L'identifiant du véhicule dans le contexte de la flotte de véhicules à laquelle il appartient.  . Model: [https://schema.org/Text.](https://schema.org/Text.)- `fuelEfficiency[number]`: La distance parcourue par unité de carburant utilisée, généralement en kilomètres par litre (km/L).  . Model: [https://schema.org/Number](https://schema.org/Number)- `fuelFilled[number]`: Quantité de carburant remplie en litres dans le véhicule correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `fuelType[string]`: Le type de carburant adapté au moteur ou aux moteurs du véhicule correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `heading[*]`: Indique le sens de déplacement du véhicule et est spécifié en degrés décimaux, où 0 <= `heading` < 360, en comptant dans le sens horaire par rapport au nord vrai. Si le véhicule est immobile (c'est-à-dire que la valeur de l'attribut `speed` est égale à `0`), la valeur de l'attribut heading doit être égale à `-1``.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `ignitionStatus[boolean]`: Indique l'état d'allumage du véhicule. Vrai signifie allumé  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `image[string]`: Une image de l'article  . Model: [https://schema.org/URL](https://schema.org/URL)- `license_plate[string]`: Donne le numéro de la plaque d'immatriculation du véhicule. SameAs : license_plate field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)".  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `mileageFromOdometer[number]`: La distance totale parcourue par le véhicule particulier depuis sa production initiale, telle que relevée sur son odomètre.  . Model: [https://schema.org/mileageFromOdometer.](https://schema.org/mileageFromOdometer.)- `municipalityInfo[object]`: Informations sur la municipalité correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Le nom de cet élément.  - `observationDateTime[string]`: Dernière heure d'observation signalée  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `previousLocation[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `purchaseDate[string]`: La date à laquelle l'article, par exemple le véhicule, a été acheté par le propriétaire actuel.  . Model: [https://schema.org/purchaseDate.](https://schema.org/purchaseDate.)- `refVehicleModel[*]`: Référence à un VehicleModel  . Model: [https://schema.org/URL](https://schema.org/URL)- `reportId[string]`: Id unique attribué au problème, au rapport, au retour d'information ou à la transaction correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `serviceOnDuty[string]`: Nature du service fourni par le véhicule d'urgence correspondant à cette observation. Vrai indique que le véhicule d'urgence correspondant à cette observation répond à un appel d'urgence et Faux dans le cas contraire.  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `serviceProvided[array]`: Service(s) que le véhicule est capable de fournir ou auquel il est affecté. Enum : 'auxiliaryServices, cargoTransport, construction, fairground, garbageCollection, goodsSelling, maintenance, parksAndGardens, roadSignalling, specialTransport, streetCleaning, streetLighting, urbanTransit, wasteContainerCleaning'. Ou toute autre valeur requise par une application spécifique.  . Model: [https://schema.org/Text](https://schema.org/Text)- `serviceStatus[string]`: Statut du véhicule (du point de vue du service fourni, il ne peut donc pas s'appliquer aux véhicules privés). `parked` : le véhicule est garé et ne fournit aucun service pour le moment. `onRoute` : Le véhicule effectue une mission. Un ou plusieurs modificateurs séparés par des virgules peuvent être ajoutés pour indiquer quelle mission est en train de livrer le véhicule. Par exemple, `onRoute,garbageCollection` peut être utilisé pour indiquer que le véhicule est en route et en mission de collecte de déchets. broken (cassé) : Le véhicule souffre d'une panne temporaire. `outOfService` : Le véhicule est sur la route mais n'effectue aucune mission, il se rend probablement sur son aire de stationnement. Enum : 'broken, onRoute, outOfService, parked' (cassé, en route, hors service, garé)  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `speed[*]`: Indique la magnitude de la composante horizontale de la vitesse actuelle du véhicule et est spécifiée en kilomètres par heure. Si elle est fournie, la valeur de l'attribut speed doit être un nombre réel non négatif. La valeur `-1` PEUT être utilisée si la vitesse est transitoirement inconnue pour une raison quelconque.  . Model: [https://schema.org/Number](https://schema.org/Number)- `tripNetWeightCollected[number]`: Le poids net collecté par le véhicule correspondant à cette observation à la fin du voyage.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type d'entité NGSI. Il doit s'agir d'un véhicule  - `vehicleAltitude[string]`: Donne l'altitude actuelle du véhicule en utilisant le GPS  . Model: [https://schema.org/Text](https://schema.org/Text)- `vehicleConfiguration[string]`: Un texte court indiquant la configuration du véhicule, par exemple "5dr hatchback ST 2.5 MT 225 hp" ou "limited edition".  . Model: [https://schema.org/vehicleConfiguration.](https://schema.org/vehicleConfiguration.)- `vehicleIdentificationNumber[string]`: Le numéro d'identification du véhicule (NIV) est un numéro de série unique utilisé par l'industrie automobile pour identifier les véhicules à moteur individuels.  . Model: [https://schema.org/vehicleIdentificationNumber.](https://schema.org/vehicleIdentificationNumber.)- `vehiclePlateIdentifier[string]`:  Un identifiant ou un code affiché sur une plaque d'immatriculation fixée au véhicule, utilisé à des fins d'identification officielle. L'identifiant d'immatriculation est numérique ou alphanumérique et est unique dans la région de l'autorité qui le délivre. Références normatives : DATEXII `vehicleRegistrationPlateIdentifier` (Identificateur de plaque d'immatriculation de véhicule)  . Model: [https://schema.org/Text](https://schema.org/Text)- `vehicleRunningStatus[string]`: Donne l'état de charge de la batterie du dispositif de déclaration. Enum : 'en cours, en attente, arrêté'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `vehicleSpecialUsage[string]`: Indique si le véhicule est utilisé à des fins particulières, comme la location commerciale, l'auto-école ou comme taxi. La législation de nombreux pays exige que cette information soit révélée lorsqu'une voiture est proposée à la vente. Enum : 'ambulance, pompiers, armée, police, transport scolaire, taxi, gestion des déchets'.  . Model: [https://schema.org/vehicleSpecialUsage](https://schema.org/vehicleSpecialUsage)- `vehicleTrackerDevice[string]`: État d'installation du dispositif GPS ou du dispositif de localisation installé sur le véhicule correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `vehicleType[string]`: Type de véhicule du point de vue de ses caractéristiques structurelles. Il est différent de la catégorie de véhicule. Enum :'véhicule agricole, véhicule quelconque, véhicule articulé, bicyclette, chariot-benne, autobus, voiture, caravane, véhicule léger, voiture avec caravane, voiture avec remorque, chariot de nettoyage, véhicule de construction ou d'entretien, véhicule à quatre roues motrices, véhicule à flancs élevés, camion, minibus, cyclomoteur, moto, moto avec side-car, scooter, balayeuse, camion-citerne, véhicule à trois roues, remorque, tramway, véhicule à deux roues, chariot, camionnette, véhicule sans pot catalytique, véhicule avec caravane, véhicule avec remorque, avec plaques d'immatriculation paires, avec plaques d'immatriculation supplémentaires, autres". Les valeurs suivantes définies par _VehicleTypeEnum_ et _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) et étendues pour d'autres utilisations  . Model: [https://schema.org/Text](https://schema.org/Text)- `wardId[string]`: ID du quartier de l'entité correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `wardName[string]`: Nom de l'entité correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `zoneName[string]`: Nom de la zone de l'entité correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `category`  - `id`  - `location`  - `type`  - `vehicleType`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
      exclusiveMinimum: true    
      minimum: 0    
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
    emergencyVehicleType:    
      description: 'Type of emergency vehicle corresponding to this observation. Enum:''policeCar, policeMotorcycle, policeVan, policeSWAT, fireEngine, waterTender, airAmbulance, ambulance, motorcycleAmbulance, rescueVehicle, hazardousMaterialsApparatus, towTruck'    
      enum:    
        - policeCar    
        - policeMotorcycle    
        - policeVan    
        - policeSWAT    
        - fireEngine    
        - waterTender    
        - airAmbulance    
        - ambulance    
        - motorcycleAmbulance    
        - rescueVehicle    
        - hazardousMaterialsApparatus    
        - towTruck    
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
        - exclusiveMaximum: true    
          maximum: 360    
          minimum: 0    
          type: number    
        - enum:    
            - -1    
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
      oneOf: &vehicle_-_properties_-_previouslocation_-_oneof    
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
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *vehicle_-_properties_-_previouslocation_-_oneof    
      x-ngsi:    
        type: Geoproperty    
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
    serviceOnDuty:    
      description: 'Nature of service provided by emergency vehicle corresponding to this observation. True indicates the emergency vehicle corresponding to this observation is attending to/ servicing to an emergency call of duty and is False otherwise.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Boolean    
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
        - maximum: -1    
          minimum: -1    
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
        - ambulance    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/Vehicle/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/Vehicle/schema.json    
  x-model-tags: IUDX    
  x-version: 0.2.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### Véhicule NGSI-v2 valeurs-clés Exemple  
Voici un exemple de véhicule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "vehicleType": "lorry",  
  "category": [  
    "municipalServices"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ]  
  },  
  "name": "C Recogida 1",  
  "speed": 50,  
  "cargoWeight": 314,  
  "serviceStatus": "onRoute",  
  "serviceProvided": [  
    "garbageCollection",  
    "wasteContainerCleaning"  
  ],  
  "areaServed": "Centro",  
  "refVehicleModel": "vehiclemodel:econic",  
  "vehiclePlateIdentifier": "3456ABC",  
  "bearing": 43,  
  "fuelEfficiency": 13,  
  "fuelType": "Petrol",  
  "fuelFilled": 6,  
  "tripNetWeightCollected": 12,  
  "vehicleTrackerDevice": "Installed",  
  "wardId": "4",  
  "license_plate": "KA052134",  
  "currentTripCount": 1,  
  "reportId": "21645",  
  "zoneName": "South Zone",  
  "vehicleAltitude": 600,  
  "deviceSimNumber": "9942142573",  
  "wardName": "Kempegowda Ward",  
  "deviceBatteryStatus": "Connected",  
  "ignitionStatus": true,  
  "vehicleRunningStatus": "running",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "serviceOnDuty": false,  
  "emergencyVehicleType": "ambulance",  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "wardId": "23",  
    "stateName": "Karnataka",  
    "cityName": "Bangalore",  
    "zoneName": "South",  
    "wardName": "Bangalore Urban",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
</details>  
#### Véhicule NGSI-v2 normalisé Exemple  
Voici un exemple d'un véhicule au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "vehicle:WasteManagement:1",  
  "type": "Vehicle",  
  "category": {  
    "type": "array",  
    "value": [  
      "municipalServices"  
    ]  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "lorry"  
  },  
  "name": {  
    "type": "Text",  
    "value": "C Recogida 1"  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Text",  
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
    "type": "Text",  
    "value": "Centro"  
  },  
  "serviceStatus": {  
    "type": "Text",  
    "value": "onRoute"  
  },  
  "cargoWeight": {  
    "type": "Number",  
    "value": 314  
  },  
  "speed": {  
    "type": "Number",  
    "value": 50,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2018-09-27T12:00:00"  
      }  
    }  
  },  
  "serviceProvided": {  
    "type": "array",  
    "value": [  
      "gargabeCollection",  
      "wasteContainerCleaning"  
    ]  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 43  
  },  
  "fuelEfficiency": {  
    "type": "Number",  
    "value": 13  
  },  
  "fuelType": {  
    "type": "Text",  
    "value": "Petrol"  
  },  
  "fuelFilled": {  
    "type": "Number",  
    "value": 6  
  },  
  "tripNetWeightCollected": {  
    "type": "Number",  
    "value": 12  
  },  
  "vehicleTrackerDevice": {  
    "type": "Text",  
    "value": "Installed"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": "4"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "KA052134"  
  },  
  "currentTripCount": {  
    "type": "Number",  
    "value": 1  
  },  
  "reportId": {  
    "type": "Text",  
    "value": "21645"  
  },  
  "zoneName": {  
    "type": "Text",  
    "value": "South Zone"  
  },  
  "vehicleAltitude": {  
    "type": "Number",  
    "value": 600  
  },  
  "deviceSimNumber": {  
    "type": "Text",  
    "value": "9942142573"  
  },  
  "wardName": {  
    "type": "Text",  
    "value": "Kempegowda Ward"  
  },  
  "deviceBatteryStatus": {  
    "type": "Text",  
    "value": "Connected"  
  },  
  "ignitionStatus": {  
    "type": "Boolean",  
    "value": true  
  },  
  "vehicleRunningStatus": {  
    "type": "Text",  
    "value": "running"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "serviceOnDuty": {  
    "type": "Boolean",  
    "value": false  
  },  
  "emergencyVehicleType": {  
    "type": "Text",  
    "value": "ambulance"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "wardId": "23",  
      "stateName": "Karnataka",  
      "cityName": "Bangalore",  
      "zoneName": "South",  
      "wardName": "Bangalore Urban",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
</details>  
#### Véhicule NGSI-LD valeurs-clés Exemple  
Voici un exemple de véhicule au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
    "type": "Vehicle",  
    "areaServed": "Centro",  
    "bearing": 43,  
    "cargoWeight": 314,  
    "category": [  
        "municipalServices"  
    ],  
    "currentTripCount": 1,  
    "deviceBatteryStatus": "Connected",  
    "deviceSimNumber": "9942142573",  
    "emergencyVehicleType": "ambulance",  
    "fuelEfficiency": 13,  
    "fuelFilled": 6,  
    "fuelType": "Petrol",  
    "ignitionStatus": true,  
    "license_plate": "KA052134",  
    "location": {  
        "coordinates": [  
            -3.164485591715449,  
            40.62785133667262  
        ],  
        "type": "Point"  
    },  
    "municipalityInfo": {  
        "district": "Bangalore Urban",  
        "ulbName": "BMC",  
        "cityId": "23",  
        "wardId": "23",  
        "stateName": "Karnataka",  
        "cityName": "Bangalore",  
        "zoneName": "South",  
        "wardName": "Bangalore Urban",  
        "zoneId": "2",  
        "wardNum": 4  
    },  
    "name": "C Recogida 1",  
    "observationDateTime": "2021-03-11T15:51:02+05:30",  
    "refVehicleModel": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
    "reportId": "21645",  
    "serviceOnDuty": false,  
    "serviceProvided": [  
        "gargabeCollection",  
        "wasteContainerCleaning"  
    ],  
    "serviceStatus": "onRoute",  
    "speed": 50,  
    "tripNetWeightCollected": 12,  
    "vehicleAltitude": 600,  
    "vehiclePlateIdentifier": "3456ABC",  
    "vehicleRunningStatus": "running",  
    "vehicleTrackerDevice": "Installed",  
    "vehicleType": "lorry",  
    "wardId": "4",  
    "wardName": "Kempegowda Ward",  
    "zoneName": "South Zone",  
    "@context": [  
        "iudx:EmergencyVehicle",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Véhicule NGSI-LD normalisé Exemple  
Voici un exemple de véhicule au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Vehicle:vehicle:WasteManagement:1",  
    "type": "Vehicle",  
    "areaServed": {  
        "type": "Property",  
        "value": "Centro"  
    },  
    "bearing": {  
        "type": "Property",  
        "value": 43  
    },  
    "cargoWeight": {  
        "type": "Property",  
        "value": 314  
    },  
    "category": {  
        "type": "Property",  
        "value": [  
            "municipalServices"  
        ]  
    },  
    "currentTripCount": {  
        "type": "Property",  
        "value": 1  
    },  
    "deviceBatteryStatus": {  
        "type": "Property",  
        "value": "Connected"  
    },  
    "deviceSimNumber": {  
        "type": "Property",  
        "value": "9942142573"  
    },  
    "emergencyVehicleType": {  
        "type": "Property",  
        "value": "ambulance"  
    },  
    "fuelEfficiency": {  
        "type": "Property",  
        "value": 13  
    },  
    "fuelFilled": {  
        "type": "Property",  
        "value": 6  
    },  
    "fuelType": {  
        "type": "Property",  
        "value": "Petrol"  
    },  
    "ignitionStatus": {  
        "type": "Property",  
        "value": true  
    },  
    "license_plate": {  
        "type": "Property",  
        "value": "KA052134"  
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
    "municipalityInfo": {  
        "type": "Property",  
        "value": {  
            "district": "Bangalore Urban",  
            "ulbName": "BMC",  
            "cityId": "23",  
            "wardId": "23",  
            "stateName": "Karnataka",  
            "cityName": "Bangalore",  
            "zoneName": "South",  
            "wardName": "Bangalore Urban",  
            "zoneId": "2",  
            "wardNum": 4  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "C Recogida 1"  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "refVehicleModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic"  
    },  
    "reportId": {  
        "type": "Property",  
        "value": "21645"  
    },  
    "serviceOnDuty": {  
        "type": "Property",  
        "value": false  
    },  
    "serviceProvided": {  
        "type": "Property",  
        "value": [  
            "gargabeCollection",  
            "wasteContainerCleaning"  
        ]  
    },  
    "serviceStatus": {  
        "type": "Property",  
        "value": "onRoute"  
    },  
    "speed": {  
        "type": "Property",  
        "value": 50,  
        "observedAt": "2018-09-27T12:00:00Z"  
    },  
    "tripNetWeightCollected": {  
        "type": "Property",  
        "value": 12  
    },  
    "vehicleAltitude": {  
        "type": "Property",  
        "value": 600  
    },  
    "vehiclePlateIdentifier": {  
        "type": "Property",  
        "value": "3456ABC"  
    },  
    "vehicleRunningStatus": {  
        "type": "Property",  
        "value": "running"  
    },  
    "vehicleTrackerDevice": {  
        "type": "Property",  
        "value": "Installed"  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "lorry"  
    },  
    "wardId": {  
        "type": "Property",  
        "value": "4"  
    },  
    "wardName": {  
        "type": "Property",  
        "value": "Kempegowda Ward"  
    },  
    "zoneName": {  
        "type": "Property",  
        "value": "South Zone"  
    },  
    "@context": [  
        "iudx:EmergencyVehicle",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
