<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : FareCollectionSystem  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/FareCollectionSystem/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Un système de collecte des tarifs de transport public Modèle de données**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `cardId[string]`: Id unique du ticket de la transaction ou Id de la carte à puce utilisée dans la transaction.  . Model: [https://schema.org/Text](https://schema.org/Text)- `currentTripCount[number]`: Le nombre actuel de trajets effectués par le véhicule correspondant à cette observation le jour d'exploitation donné.  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `destinationStopCategory[string]`: Type de l'arrêt de bus de destination correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationStopId[string]`: Identité unique de l'arrêt de bus où le passager débarque du bus correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `destinationStopName[string]`: Le nom de l'arrêt de bus de destination correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction_id[number]`: Indique la direction du déplacement du véhicule correspondant à cette observation, peut être référencé à partir du flux statique GTFS trips.txt. Identique à : Champ "direction_id" du GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Number](https://schema.org/Number)- `entryAreaCode[string]`: Code régional de l'arrêt d'embarquement du passager (utilisé par l'agence de perception des droits). Par exemple, si l'arrêt est un arrêt de service de bus de ville ou un arrêt de bus de banlieue ou un autre type d'arrêt de service, etc.  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentCompanyCode[string]`: Code de la société/de l'agence pour l'équipement de transaction (utilisé par l'agence de perception des tarifs). Par exemple, 103 - CBS (city bus service),102 - BRTS etc.  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentId[string]`: Id unique de l'équipement correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentSequenceNumber[number]`: Numéro de séquence pour l'équipement donné.  . Model: [https://schema.org/Number](https://schema.org/Number)- `equipmentStopId[string]`: Stop Id (BRTS) où est installé l'équipement correspondant à cette transaction.  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentType[string]`: Type d'équipement ou le nom de l'équipement correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `equipmentTypeCode[string]`: Code unique indiquant le type d'équipement utilisé dans la transaction (utilisé par l'agence de perception des tarifs). ENUM [1B, 42, 02, 08, 41] 1B - POS, 42 - HTT, 02- Mobile, 08- Porte tarifaire, 41- Valideur de poteau.  . Model: [https://schema.org/Text](https://schema.org/Text)- `exitAreaCode[string]`: Code régional de l'arrêt de descente du passager (utilisé par l'agence de perception des droits). Par exemple, si l'arrêt est un arrêt de service de bus de ville ou un arrêt BRTS ou un autre type d'arrêt de service, etc.  . Model: [https://schema.org/Text](https://schema.org/Text)- `fareForAdult[number]`: Le tarif pour un adulte dans le trajet correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `fareForChild[number]`: Le tarif pour un enfant dans le voyage correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `observationDateTime[string]`: Dernière heure d'observation signalée.  . Model: [https://schema.org/Text](https://schema.org/Text)- `occupancyLevel[string]`: Niveau d'occupation dans le bus de transport public correspondant à cette observation. Le "rouge" indique que le niveau d'encombrement dans le bus est ÉLEVÉ, le "jaune" indique que le niveau d'encombrement dans le bus est MODÉRÉ et le "vert" indique que le niveau d'encombrement dans le bus est FAIBLE.  . Model: [https://schema.org/Text](https://schema.org/Text)- `originDestinationCode[string]`: Le code des arrêts d'origine et de destination correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopCategory[string]`: Type de l'arrêt de bus d'origine correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopId[string]`: Id unique de l'arrêt de bus où le passager monte dans le bus correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `originStopName[string]`: Le nom de l'arrêt de bus d'origine correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `passengerCount[number]`: Nombre de passagers voyageant dans le bus de transport public correspondant à cette observation. Ce nombre est calculé sur la base des transactions de billetterie en temps réel dans le bus de transport public.  . Model: [https://schema.org/Number](https://schema.org/Number)- `route_id[string]`: Id de l'itinéraire attribué à l'itinéraire sur lequel le bus/véhicule correspondant au bus de cette observation circule actuellement. Identique à : Champ 'route_id' du GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `shiftOfOperation[string]`: Poste d'exploitation du véhicule de transport en commun exploité par l'organisme de perception des droits de douane/l'organisme de transport en commun ou l'employé correspondant à cette observation. Indiqué par "1" lorsque le véhicule est exploité en première équipe, "2" lorsque le véhicule est exploité en deuxième équipe et "3" lorsque le véhicule est exploité en troisième équipe.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `stage[number]`: Nombre total d'étapes entre l'arrêt de bus d'origine et l'arrêt de bus de destination.  . Model: [https://schema.org/Number](https://schema.org/Number)- `ticketTypeCode[string]`: Code unique du type de billet du voyage correspondant.  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionDateTime[string]`: Date-heure de la transaction correspondant à cette observation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionType[string]`: Type de transaction correspondant à cette observation. Par exemple : émission, réémission, entrée, sortie, etc.  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionTypeDescription[string]`: Description du type de transaction. Explication des différents codes transactionTypeId utilisés dans les données.  . Model: [https://schema.org/Text](https://schema.org/Text)- `transactionVehicleNum[number]`: Code utilisé par l'agence de perception des droits pour le numéro de véhicule correspondant à la transaction.  . Model: [https://schema.org/Number](https://schema.org/Number)- `travelDistance[number]`: La distance entre l'arrêt de bus d'origine et l'arrêt de bus de destination correspondant à cette observation.  . Model: [https://schema.org/Number](https://schema.org/Number)- `trip_id[string]`: Id/nom du trajet attribué au bus correspondant à cette observation, en tenant compte de l'heure de la journée et de la direction du trajet sur le routeId donné. SameAs : Champ 'trip_id' du GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir de FareCollectionSystem.  - `vehicle_label[string]`: Étiquette visible par l'utilisateur, c'est-à-dire quelque chose qui doit être montré au passager pour l'aider à identifier le bon véhicule. Idem : Champ "label" du message GTFS Realtime-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FareCollectionSystem:    
  description: 'A public transit fare collection system Data Model'    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    cardId:    
      description: 'Unique ticket Id of the transaction or Id of the smart card used in the transaction.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    destinationStopCategory:    
      description: 'Type of the destination bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopId:    
      description: 'Unique Id of the bus stop at which the passenger deboards from the bus corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    destinationStopName:    
      description: 'The name of the destination bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    direction_id:    
      description: "Indicates the direction of travel of the vehicle corresponding to this observation, can be referenced from the GTFS static feed trips.txt. SameAs: 'direction_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    entryAreaCode:    
      description: 'Area code of the passenger boarding stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or brts stop or other service type stop etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentCompanyCode:    
      description: 'Company/Agency code for the transaction equipment (used by fare collection agency). For example, 103 - CBS (city bus service),102 - BRTS etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentId:    
      description: 'Unique Id of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentSequenceNumber:    
      description: 'Sequence number for the given equipment.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    equipmentStopId:    
      description: 'Stop Id (BRTS) at which the equipment corresponding to this transaction is installed.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentType:    
      description: 'Type of equipment or the name of the equipment corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    equipmentTypeCode:    
      description: 'Unique code indicating the type of equipment used in the transaction (used by fare collection agency).ENUM [1B, 42, 02, 08, 41] 1B - POS, 42 - HTT, 02- Mobile, 08- Fare Gate, 41- Pole Validator'    
      enum:    
        - 1B    
        - 42    
        - 02    
        - 08    
        - 41    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    exitAreaCode:    
      description: 'Area code of the passenger alighting stop (used by the fare collection agency). For example, whether the stop is city-bus-service stop or BRTS stop or other service type stop etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    fareForAdult:    
      description: 'The fare for an adult in the journey corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    fareForChild:    
      description: 'The fare for a child in the journey corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &farecollectionsystem_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    occupancyLevel:    
      description: 'Occupancy level in the public transit bus corresponding to this observation. ''Red'' indicates the congestion level in the bus is HIGH, ''Yellow'' indicates the congestion level in the bus is MODERATE and ''Green'' indicates the congestion level in the bus is LOW.'    
      enum:    
        - Red    
        - Yellow    
        - Green    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originDestinationCode:    
      description: 'The code for the origin and destination stops corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopCategory:    
      description: 'Type of the origin bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopId:    
      description: 'Unique Id of the bus stop at which the passenger boards into the bus corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    originStopName:    
      description: 'The name of the origin bus stop corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *farecollectionsystem_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    passengerCount:    
      description: 'Number of passengers travelling in the public transit bus corresponding to this observation. This count is computed based on the realtime ticketing transactions in the public transit bus.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    route_id:    
      description: "Route Id assigned to the route on which the bus/vehicle corresponding to the bus in this observation is currently plying on. SameAs: 'route_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
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
    shiftOfOperation:    
      description: 'Shift of operation of the public transit vehicle operated by the fare collection agency/ public transit agency or the employee corresponding to this observation. Indicated as ''1'' when the vehicle operates in the first shift, ''2'' when the vehicle operates in the second shift and ''3'' when the vehicle operates in the third shift.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    stage:    
      description: 'Total number of stages from the origin bus stop to the destination bus stop.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    ticketTypeCode:    
      description: 'Unique ticket type code of the corresponding trip.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionDateTime:    
      description: 'Date-time of the transaction corresponding to this observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionType:    
      description: 'Type of the transaction corresponding to this observation. For Eg - Issue, ReIssue, Entry, Exit etc.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionTypeDescription:    
      description: 'Description of the transaction type. Explanation of various transactionTypeId codes used in the data.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    transactionVehicleNum:    
      description: 'Code used by fare collection agency for the vehicle number corresponding to the transaction.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    travelDistance:    
      description: 'The distance between the origin bus stop and the destination bus stop corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    trip_id:    
      description: "Trip Id/Trip name alloted to the bus corresponding to this observation, in consideration to the time of the day and the direction of the trip on the given routeId. SameAs: 'trip_id' field from GTFS Realtime message-TripDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-tripdescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be FareCollectionSystem'    
      enum:    
        - FareCollectionSystem    
      type: string    
      x-ngsi:    
        type: Property    
    vehicle_label:    
      description: "User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. SameAs: 'label' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FareCollectionSystem/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FareCollectionSystem/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### FareCollectionSystem Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de FareCollectionSystem au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "address": {  
    "addressCountry": "France",  
    "addressLocality": "Nice",  
    "addressRegion": "Provenza-Alpes-Costa Azul",  
    "postOfficeBoxNumber": "",  
    "postalCode": "06000",  
    "streetAddress": "Av. Nicolas II"  
  },  
  "alternateName": "",  
  "areaServed": "Nice",  
  "cardId": "987201910",  
  "currentTripCount": 12,  
  "dataProvider": "",  
  "dateCreated": "2020-11-02T06:16:42Z",  
  "dateModified": "2020-12-27T15:13:17Z",  
  "description": "Fare collection system Nize for regional routes",  
  "destinationStopCategory": "Airport",  
  "destinationStopId": "Nice-Airport",  
  "destinationStopName": "Hour risk somebody deal system discussion other plan. Stage the film occur.",  
  "direction_id": 1,  
  "entryAreaCode": "city-bus-service",  
  "equipmentCompanyCode": "103",  
  "equipmentId": "S23",  
  "equipmentSequenceNumber": 2,  
  "equipmentStopId": "BRTS-Sen-23",  
  "equipmentType": "Entry sensor",  
  "equipmentTypeCode": "42",  
  "exitAreaCode": "city-bus-service",  
  "fareForAdult": 4.5,  
  "fareForChild": 3.6,  
  "location": {  
    "coordinates": [  
      43.7034,  
      7.2663  
    ],  
    "type": "Point"  
  },  
  "name": "Fare collection system Nize",  
  "observationDateTime": "1988-12-24T07:06:19Z",  
  "occupancyLevel": "Green",  
  "originDestinationCode": "23",  
  "originStopCategory": "Bus stop",  
  "originStopId": "9",  
  "originStopName": "Vauban",  
  "owner": [  
    "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
    "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
  ],  
  "passengerCount": 6,  
  "route_id": "4",  
  "seeAlso": [  
    "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
    "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
  ],  
  "shiftOfOperation": "2",  
  "source": "",  
  "stage": 4,  
  "ticketTypeCode": "Normal",  
  "transactionDateTime": "2021-08-20T15:45:22Z",  
  "transactionType": "Issue",  
  "transactionTypeDescription": "Regular Fare.",  
  "transactionTypeId": "2401",  
  "transactionVehicleNum": 23,  
  "travelDistance": 7.5,  
  "trip_id": "4A",  
  "vehicle_label": "5821JZS"  
}  
```  
</details>  
#### FareCollectionSystem NGSI-v2 normalisé Exemple  
Voici un exemple de FareCollectionSystem au format JSON-LD tel que normalisé. Il est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
  "type": "FareCollectionSystem",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2020-11-02T06:16:42Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2020-12-27T15:13:17Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Fare collection system Nize"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": "Fare collection system Nize for regional routes"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
      "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
      "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.7034,  
        7.2663  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "streetAddress": "Av. Nicolas II",  
      "addressLocality": "Nice",  
      "addressRegion": "Provenza-Alpes-Costa Azul",  
      "addressCountry": "France",  
      "postalCode": "06000",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice"  
  },  
  "destinationStopName": {  
    "type": "Text",  
    "value": "Hour risk somebody deal system discussion other plan. Stage the film occur."  
  },  
  "occupancyLevel": {  
    "type": "Text",  
    "value": "Green"  
  },  
  "travelDistance": {  
    "type": "number",  
    "value": 7.5  
  },  
  "passengerCount": {  
    "type": "number",  
    "value": 6  
  },  
  "transactionType": {  
    "type": "Text",  
    "value": "Issue"  
  },  
  "ticketTypeCode": {  
    "type": "Text",  
    "value": "Normal"  
  },  
  "originStopName": {  
    "type": "Text",  
    "value": "Vauban"  
  },  
  "entryAreaCode": {  
    "type": "Text",  
    "value": "city-bus-service"  
  },  
  "cardId": {  
    "type": "Text",  
    "value": "987201910"  
  },  
  "transactionTypeId": {  
    "type": "Text",  
    "value": "2401"  
  },  
  "stage": {  
    "type": "number",  
    "value": 4  
  },  
  "equipmentId": {  
    "type": "Text",  
    "value": "S23"  
  },  
  "direction_id": {  
    "type": "number",  
    "value": 1  
  },  
  "equipmentSequenceNumber": {  
    "type": "number",  
    "value": 2  
  },  
  "shiftOfOperation": {  
    "type": "Text",  
    "value": "2"  
  },  
  "route_id": {  
    "type": "Text",  
    "value": "4"  
  },  
  "trip_id": {  
    "type": "Text",  
    "value": "4A"  
  },  
  "originStopCategory": {  
    "type": "Text",  
    "value": "Bus stop"  
  },  
  "vehicle_label": {  
    "type": "Text",  
    "value": "5821JZS"  
  },  
  "fareForChild": {  
    "type": "number",  
    "value": 3.6  
  },  
  "transactionDateTime": {  
    "type": "DateTime",  
    "value":  "2021-08-20T15:45:22Z"  
  },  
  "destinationStopId": {  
    "type": "Text",  
    "value": "Nice-Airport"  
  },  
  "originDestinationCode": {  
    "type": "Text",  
    "value": "23"  
  },  
  "currentTripCount": {  
    "type": "number",  
    "value": 12  
  },  
  "equipmentTypeCode": {  
    "type": "Text",  
    "value": "42"  
  },  
  "destinationStopCategory": {  
    "type": "Text",  
    "value": "Airport"  
  },  
  "transactionVehicleNum": {  
    "type": "number",  
    "value": 23  
  },  
  "fareForAdult": {  
    "type": "number",  
    "value": 4.5  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "1988-12-24T07:06:19Z"  
  },  
  "equipmentCompanyCode": {  
    "type": "Text",  
    "value": "103"  
  },  
  "transactionTypeDescription": {  
    "type": "Text",  
    "value": "Regular Fare."  
  },  
  "exitAreaCode": {  
    "type": "Text",  
    "value": "city-bus-service"  
  },  
  "equipmentType": {  
    "type": "Text",  
    "value": "Entry sensor"  
  },  
  "equipmentStopId": {  
    "type": "Text",  
    "value": "BRTS-Sen-23"  
  },  
  "originStopId": {  
    "type": "Text",  
    "value": "9"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
</details>  
#### FareCollectionSystem Valeurs-clés NGSI-LD Exemple  
Voici un exemple de FareCollectionSystem au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
    "type": "FareCollectionSystem",  
    "address": {  
        "addressCountry": "France",  
        "addressLocality": "Nice",  
        "addressRegion": "Provenza-Alpes-Costa Azul",  
        "postOfficeBoxNumber": "",  
        "postalCode": "06000",  
        "streetAddress": "Av. Nicolas II"  
    },  
    "alternateName": "",  
    "areaServed": "Nice",  
    "cardId": "987201910",  
    "currentTripCount": 12,  
    "dataProvider": "",  
    "dateCreated": "2020-11-02T06:16:42Z",  
    "dateModified": "2020-12-27T15:13:17Z",  
    "description": "Fare collection system Nize for regional routes",  
    "destinationStopCategory": "Airport",  
    "destinationStopId": "Nice-Airport",  
    "destinationStopName": "Hour risk somebody deal system discussion other plan. Stage the film occur.",  
    "direction_id": 1,  
    "entryAreaCode": "city-bus-service",  
    "equipmentCompanyCode": "103",  
    "equipmentId": "S23",  
    "equipmentSequenceNumber": 2,  
    "equipmentStopId": "BRTS-Sen-23",  
    "equipmentType": "Entry sensor",  
    "equipmentTypeCode": "42",  
    "exitAreaCode": "city-bus-service",  
    "fareForAdult": 4.5,  
    "fareForChild": 3.6,  
    "location": {  
        "coordinates": [  
            43.7034,  
            7.2663  
        ],  
        "type": "Point"  
    },  
    "name": "Fare collection system Nize",  
    "observationDateTime": "1988-12-24T07:06:19Z",  
    "occupancyLevel": "Green",  
    "originDestinationCode": "23",  
    "originStopCategory": "Bus stop",  
    "originStopId": "9",  
    "originStopName": "Vauban",  
    "owner": [  
        "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
        "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
    ],  
    "passengerCount": 6,  
    "route_id": "4",  
    "seeAlso": [  
        "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
        "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
    ],  
    "shiftOfOperation": "2",  
    "source": "",  
    "stage": 4,  
    "ticketTypeCode": "Normal",  
    "transactionDateTime": "2021-08-20T15:45:22Z",  
    "transactionType": "Issue",  
    "transactionTypeDescription": "Regular Fare.",  
    "transactionTypeId": "2401",  
    "transactionVehicleNum": 23,  
    "travelDistance": 7.5,  
    "trip_id": "4A",  
    "vehicle_label": "5821JZS",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### FareCollectionSystem NGSI-LD normalisé Exemple  
Voici un exemple de FareCollectionSystem au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:FareCollectionSystem:id:RJSB:34513580",  
    "type": "FareCollectionSystem",  
    "address": {  
        "type": "Property",  
        "value": {  
            "streetAddress": "Av. Nicolas II",  
            "addressLocality": "Nice",  
            "addressRegion": "Provenza-Alpes-Costa Azul",  
            "addressCountry": "France",  
            "postalCode": "06000",  
            "postOfficeBoxNumber": ""  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": ""  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice"  
    },  
    "cardId": {  
        "type": "Property",  
        "value": "987201910"  
    },  
    "currentTripCount": {  
        "type": "Property",  
        "value": 12  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": ""  
    },  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-11-02T06:16:42Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-12-27T15:13:17Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Fare collection system Nize for regional routes"  
    },  
    "destinationStopCategory": {  
        "type": "Property",  
        "value": "Airport"  
    },  
    "destinationStopId": {  
        "type": "Property",  
        "value": "Nice-Airport"  
    },  
    "destinationStopName": {  
        "type": "Property",  
        "value": "Hour risk somebody deal system discussion other plan. Stage the film occur."  
    },  
    "direction_id": {  
        "type": "Property",  
        "value": 1  
    },  
    "entryAreaCode": {  
        "type": "Property",  
        "value": "city-bus-service"  
    },  
    "equipmentCompanyCode": {  
        "type": "Property",  
        "value": "103"  
    },  
    "equipmentId": {  
        "type": "Property",  
        "value": "S23"  
    },  
    "equipmentSequenceNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "equipmentStopId": {  
        "type": "Property",  
        "value": "BRTS-Sen-23"  
    },  
    "equipmentType": {  
        "type": "Property",  
        "value": "Entry sensor"  
    },  
    "equipmentTypeCode": {  
        "type": "Property",  
        "value": "42"  
    },  
    "exitAreaCode": {  
        "type": "Property",  
        "value": "city-bus-service"  
    },  
    "fareForAdult": {  
        "type": "Property",  
        "value": 4.5  
    },  
    "fareForChild": {  
        "type": "Property",  
        "value": 3.6  
    },  
    "location": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.7034,  
                7.2663  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Fare collection system Nize"  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1988-12-24T07:06:19Z"  
        }  
    },  
    "occupancyLevel": {  
        "type": "Property",  
        "value": "Green"  
    },  
    "originDestinationCode": {  
        "type": "Property",  
        "value": "23"  
    },  
    "originStopCategory": {  
        "type": "Property",  
        "value": "Bus stop"  
    },  
    "originStopId": {  
        "type": "Property",  
        "value": "9"  
    },  
    "originStopName": {  
        "type": "Property",  
        "value": "Vauban"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:FareCollectionSystem:items:XMXR:79897582",  
            "urn:ngsi-ld:FareCollectionSystem:items:SKAX:98192518"  
        ]  
    },  
    "passengerCount": {  
        "type": "Property",  
        "value": 6  
    },  
    "route_id": {  
        "type": "Property",  
        "value": "4"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:FareCollectionSystem:items:VSVS:72352464",  
            "urn:ngsi-ld:FareCollectionSystem:items:VMFR:36424993"  
        ]  
    },  
    "shiftOfOperation": {  
        "type": "Property",  
        "value": "2"  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "stage": {  
        "type": "Property",  
        "value": 4  
    },  
    "ticketTypeCode": {  
        "type": "Property",  
        "value": "Normal"  
    },  
    "transactionDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-08-20T15:45:22Z"  
        }  
    },  
    "transactionType": {  
        "type": "Property",  
        "value": "Issue"  
    },  
    "transactionTypeDescription": {  
        "type": "Property",  
        "value": "Regular Fare."  
    },  
    "transactionTypeId": {  
        "type": "Property",  
        "value": "2401"  
    },  
    "transactionVehicleNum": {  
        "type": "Property",  
        "value": 23  
    },  
    "travelDistance": {  
        "type": "Property",  
        "value": 7.5  
    },  
    "trip_id": {  
        "type": "Property",  
        "value": "4A"  
    },  
    "vehicle_label": {  
        "type": "Property",  
        "value": "5821JZS"  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
