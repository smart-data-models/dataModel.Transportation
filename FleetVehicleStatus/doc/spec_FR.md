<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : État des véhicules de la flotte    
========================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicleStatus/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Cette entité contient une description harmonisée de l'état d'un véhicule de flotte générique. Cette entité est principalement associée au segment vertical du transport et de la logistique, mais peut également être utilisée dans de nombreuses autres applications IdO connexes**.    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `battery[number]`: Le pourcentage actuel de la batterie restante dans le cas d'un véhicule électrique ou d'un appareil connecté au véhicule.  - `bearing[number]`: Le relèvement actuel du véhicule de la flotte en degrés par rapport au nord. L'élément d'horodatage de l'attribut doit indiquer le moment où le relevé a été obtenu.  - `currentOperative[object]`: L'opérateur actuel (par exemple le conducteur) du véhicule décrit comme une personne Schema.org  . Model: [https://schema.org/Person](https://schema.org/Person)	- `givenName`:       
- `currentStatus[string]`: Description de l'état actuel du véhicule, par exemple Enum : "déployé, fini, terminé, entretien, démarrage".  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `fleetVehicle[*]`: Référence à l'entité FleetVehicle à laquelle se rapporte cette entité de statut  - `fleetVehicleOperation[*]`: Référence à l'entité FleetVehicleOperation à laquelle se rapporte cette entité de statut  - `id[*]`: Identifiant unique de l'entité  - `inRestrictedArea[boolean]`: Indique si le véhicule se trouve dans une zone réglementée au moment de la mise à jour de l'état.  - `lastFuellingAmount[number]`: Niveau de carburant ajouté au véhicule lors du dernier ravitaillement. L'élément d'horodatage de l'attribut doit indiquer le moment où le véhicule a été ravitaillé en carburant. Données à enregistrer en litres  - `lastKnownPosition[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `lastKnownPositionUpdatedAt[date-time]`: Horodatage de la dernière mise à jour de la position connue du véhicule de la flotte  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `mileageFromOdometer[number]`: Distance totale parcourue par le véhicule de la flotte selon l'odomètre embarqué, en kilomètres (unitCode KMT) ou en miles (unitCode SMI). Voir également Schema.org Vehicle/ mileageFromOdometer. L'élément timestamp (horodatage) enregistre le moment où le relevé du compteur kilométrique a été effectué  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `restFuelAmount[number]`: Niveau de carburant enregistré lorsque le véhicule était au repos pour la dernière fois (c'est-à-dire à l'arrêt). L'élément d'horodatage de l'attribut doit indiquer le moment où le véhicule était à l'arrêt pour la dernière fois. Données à enregistrer en litres  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `speed[number]`: La vitesse actuelle du véhicule de la flotte (km/h). L'élément d'horodatage de l'attribut doit indiquer le moment où le relevé a été effectué.  - `type[string]`: Identifiant de l'entité NGSI. Il doit s'agir de FleetVehicleStatus  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Ce modèle de données provient du projet original GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Il a fait l'objet de quelques adaptations mineures pour répondre aux exigences des modèles de données intelligents.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
FleetVehicleStatus:      
  description: This entity contains a harmonised description of the status of a generic fleet vehicle. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.      
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
    battery:      
      description: 'The current percentage of battery left in case of an electric vehicle, or a device connected to the vehicle'      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        type: Property      
    bearing:      
      description: The current bearing of the fleet vehicle in degrees relative to North. The timestamp element of the attribute should indicate when the reading was obtained      
      type: number      
      x-ngsi:      
        type: Property      
    currentOperative:      
      description: The current operative (e.g. driver) of the vehicle described as a Schema.org  person      
      properties:      
        givenName:      
          type: string      
        jobTitle:      
          type: string      
      type: object      
      x-ngsi:      
        model: https://schema.org/Person      
        type: Property      
    currentStatus:      
      description: 'A description of the current status of the vehicle e.g. Enum:''deployed, finished, terminated, servicing, starting'''      
      enum:      
        - deployed      
        - finished      
        - servicing      
        - starting      
        - terminated      
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
    fleetVehicle:      
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
      description: Reference to the FleetVehicle entity to which this status entity relates      
      x-ngsi:      
        type: Relationship      
    fleetVehicleOperation:      
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
      description: Reference to the FleetVehicleOperation entity to which this status entity relates      
      x-ngsi:      
        type: Relationship      
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
    inRestrictedArea:      
      description: Indicates if the vehicle is known to be in a restricted area at the time of the status update      
      type: boolean      
      x-ngsi:      
        type: Property      
    lastFuellingAmount:      
      description: The level of fuel added to the vehicle at the last fuelling. The timestamp element of the attribute should indicate when the vehicle was fuelled. Data to be recorded in Litres      
      type: number      
      x-ngsi:      
        type: Property      
        units: litres      
    lastKnownPosition:      
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
    lastKnownPositionUpdatedAt:      
      description: The timestamp of the last known position update for the fleet vehicle      
      format: date-time      
      type: string      
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
    mileageFromOdometer:      
      description: The total distance the fleet vehicle has travelled according to the on-board odometer in kilometres (unitCode KMT) or miles (unitCode SMI). See also Schema.org Vehicle/ mileageFromOdometer. The timestamp element records when the odometer reading was taken      
      type: number      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
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
    restFuelAmount:      
      description: The level of fuel recorded when the vehicle was last at rest (i.e. stopped). The timestamp element of the attribute should indicate when the vehicle was last at rest. Data to be recorded in Litres      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    speed:      
      description: The current speed of the fleet vehicle (km/h). The timestamp element of the attribute should indicate when the reading was obtained      
      type: number      
      x-ngsi:      
        type: Property      
        units: km/h      
    type:      
      description: NGSI Entity identifier. It has to be FleetVehicleStatus      
      enum:      
        - FleetVehicleStatus      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicleStatus/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleStatus/schema.json      
  x-model-tags: GSMA      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### FleetVehicleStatus Valeurs clés de l'INSIG-v2 Exemple    
Voici un exemple de FleetVehicleStatus au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
  "type": "FleetVehicleStatus",  
  "battery": 0.81,  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleOperation": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b",  
  "restFuelAmount": 28,  
  "lastFuellingAmount": 95,  
  "currentStatus": "finished",  
  "currentOperative": {  
    "givenName": "John Smith",  
    "jobTitle": "Ambulance Operator"  
  },  
  "speed": 60,  
  "unitCode": "KMH",  
  "bearing": 80,  
  "lastKnownPosition": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "lastKnownPositionUpdatedAt": "2016-08-28T10:18:16Z",  
  "inRestrictedArea": true,  
  "mileageFromOdometer": 18756  
}  
```  
</details>    
#### FleetVehicleStatus NGSI-v2 normalisé Exemple    
Voici un exemple de FleetVehicleStatus au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
  "type": "FleetVehicleStatus",  
  "battery": {  
    "type": "Number",  
    "value": 0.81  
  },  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleOperation": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b"  
  },  
  "restFuelAmount": {  
    "type": "Number",  
    "value": 28  
  },  
  "lastFuellingAmount": {  
    "type": "Number",  
    "value": 95  
  },  
  "currentStatus": {  
    "type": "Text",  
    "value": "finished"  
  },  
  "currentOperative": {  
    "type": "StructuredValue",  
    "value": {  
      "givenName": "John Smith",  
      "jobTitle": "Ambulance Operator"  
    }  
  },  
  "speed": {  
    "type": "Number",  
    "value": 60  
  },  
  "bearing": {  
    "type": "Number",  
    "value": 80  
  },  
  "lastKnownPosition": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "lastKnownPositionUpdatedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "inRestrictedArea": {  
    "type": "Boolean",  
    "value": true  
  },  
  "mileageFromOdometer": {  
    "type": "Number",  
    "value": 18756  
  }  
}  
```  
</details>    
#### FleetVehicleStatus Valeurs clés de l'INS-LD Exemple    
Voici un exemple de FleetVehicleStatus au format JSON-LD en tant que valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
  "type": "FleetVehicleStatus",  
  "battery": 0.81,  
  "bearing": 80,  
  "currentOperative": {  
    "givenName": "John Smith",  
    "jobTitle": "Ambulance Operator"  
  },  
  "currentStatus": "finished",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleOperation": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b",  
  "inRestrictedArea": true,  
  "lastFuellingAmount": 95,  
  "lastKnownPosition": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "lastKnownPositionUpdatedAt": "2016-08-28T10:18:16Z",  
  "mileageFromOdometer": 18756,  
  "restFuelAmount": 28,  
  "source": "https://source.example.com",  
  "speed": 60,  
  "unitCode": "KMH",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### FleetVehicleStatus NGSI-LD normalisé Exemple    
Voici un exemple de FleetVehicleStatus au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleStatus:16ea1c5c-5aa6-11e8-8144-4b82063ca31c",  
  "type": "FleetVehicleStatus",  
  "battery": {  
    "type": "Property",  
    "value": 0.81,  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "bearing": {  
    "type": "Property",  
    "value": 80,  
    "unitCode": "DD",  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "currentOperative": {  
    "type": "Property",  
    "value": {  
      "givenName": "John Smith",  
      "jobTitle": "Ambulance Operator"  
    }  
  },  
  "currentStatus": {  
    "type": "Property",  
    "value": "finished"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleOperation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicleOperation:a4f0a07a-5aa6-11e8-b70f-4b9d36e53d7b"  
  },  
  "inRestrictedArea": {  
    "type": "Property",  
    "value": true  
  },  
  "lastFuellingAmount": {  
    "type": "Property",  
    "value": 95,  
    "unitCode": "LTR",  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "lastKnownPosition": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "lastKnownPositionUpdatedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "mileageFromOdometer": {  
    "type": "Property",  
    "value": 18756,  
    "unitCode": "SMI",  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "restFuelAmount": {  
    "type": "Property",  
    "value": 28,  
    "unitCode": "LTR",  
    "observedAt": "2016-08-22T10:18:16Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "speed": {  
    "type": "Property",  
    "value": 60,  
    "unitCode": "KMH",  
    "observedAt": "2016-08-22T10:18:16Z"  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
