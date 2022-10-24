<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : EVChargingStation  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/EVChargingStation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Station de recharge pour véhicules électriques**  
version : 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `acceptedPaymentMethod[array]`: Type(s) de frais lors de l'utilisation de cette station. Enum : "ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm  . Model: [https://schema.org/Text](https://schema.org/Text)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `allowedVehicleType[array]`: Type(s) de véhicule(s) pouvant être chargé(s). Enum : 'vélo, bus, voiture, caravane, moto, scooter, camion'.  . Model: [http://schema.org/Text](http://schema.org/Text)- `alternateName[string]`: Un nom alternatif pour cet élément  - `amountCollected[number]`: Montant perçu pour le service correspondant à cette observation.  - `amperage[number]`: L'ampérage total offert par la station de charge.  . Model: [http://schema.org/Number](http://schema.org/Number)- `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableCapacity[integer]`: Le nombre de véhicules qui peuvent actuellement être chargés. Il doit être inférieur ou égal à `capacité`.  . Model: [http://schema.org/Number](http://schema.org/Number)- `capacity[integer]`: Le nombre total de véhicules qui peuvent être chargés en même temps. Le nombre total de prises de courant peut être plus élevé.  . Model: [http://schema.org/Number](http://schema.org/Number)- `chargeType[array]`: Type(s) de frais lors de l'utilisation de cette station. Enum : 'annualPayment, flat, free, monthlyPayment, other' (paiement annuel, forfaitaire, gratuit, paiement mensuel, autre)  . Model: [https://schema.org/Text](https://schema.org/Text)- `chargingUnitId[string]`: L'Id du point de charge dans la station de recharge EV correspondant à cette observation.  - `contactPoint[object]`: Les coordonnées à contacter avec l'article.  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)- `dataDescriptor[string]`: URI pointant vers l'entité data-descriptor  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `endDateTime[string]`: Heure de fin déclarée correspondant à cette observation.  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `network[string]`: Le nom du réseau, avec lequel l'opérateur coopère.  . Model: [https://schema.org/Text](https://schema.org/Text)- `observationDateTime[string]`: Dernière heure d'observation signalée.  - `openingHours[string]`: Heures d'ouverture de la station de recharge.  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `operator[string]`: L'opérateur de la station de charge.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `powerConsumption[number]`: Puissance consommée par l'entité correspondant à cette observation.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `socketNumber[integer]`: Le nombre total de prises offertes par cette station de recharge  . Model: [http://schema.org/Number.](http://schema.org/Number.)- `socketType[array]`: Le type de prises proposées par cette station. Enum:'Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, Other, Tesla, Type2, Type3, Wall_Euro'  . Model: [http://schema.org/Text](http://schema.org/Text)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startDateTime[string]`: Heure de début déclarée correspondant à cette observation.  - `stationName[string]`: Le nom de la station correspondant à cette observation. Il peut s'agir du nom de la station d'accueil des vélos, de la station de recharge, etc.  - `status[string]`: État de la station de recharge. Enum : "almostEmpty, almostFull, empty, full, outOfService, withIncidence, working". Ou toute autre application spécifique.  . Model: [http://schema.org/Text](http://schema.org/Text)- `taxAmountCollected[number]`: Le montant de l'impôt prélevé sur les produits, les choses et les services, qui comprend la taxe de vente, la taxe sur la valeur ajoutée, la taxe sur les services, la taxe sur les biens et services, les droits de douane, etc.  - `transactionId[string]`: Id de transaction unique de l'entité correspondant à cette observation.  - `transactionType[string]`: Type de transaction basé sur le mode de paiement (par exemple, mobile/UPI, carte, etc.) ou le mode de service (par exemple, émission, réémission, entrée, sortie, etc.) correspondant à cette observation.  - `type[string]`: Type d'entité NGSI. Il doit être EVChargingStation  - `vehicleType[string]`: Type de véhicule du point de vue de ses caractéristiques structurelles. Il est différent de la catégorie de véhicule. Enum :'véhicule agricole, ambulance, tout véhicule, véhicule articulé, pousse-pousse, bicyclette, chariot-benne, autobus BRT, minibus BRT, autobus, voiture, caravane, voiture ou véhicule léger, voiture avec caravane, voiture avec remorque, chariot de nettoyage, compacteur, véhicule de construction ou d'entretien, benne basculante, cyclomoteur électrique, scooter électrique, motocyclette électrique, camion à incendie, véhicule à quatre roues motrices, véhicule à flancs élevés, trémie, camion, minibus, cyclomoteur, motocyclette, motocyclette avec side-car, scooter, fourgon de police, balayeuse, citerne, tempo, véhicule à trois roues, benne, remorque, tramway, véhicule à deux roues, trolley, camionnette, véhicule sans convertisseur catalytique, véhicule avec caravane, véhicule avec remorque, avec plaques d'immatriculation paires, avec plaques d'immatriculation supplémentaires, autre". Les valeurs suivantes définies par _VehicleTypeEnum_ et _VehicleTypeEnum2_, [DATEX 2 version 2.3] (http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  . Model: [https://schema.org/Text](https://schema.org/Text)- `voltage[number]`: La tension totale offerte par la station de charge  . Model: [http://schema.org/Number](http://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `allowedVehicleType`  - `capacity`  - `id`  - `socketType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Une station de recharge publique fournissant de l'énergie aux véhicules électriques. Le temps de charge dépend de la puissance maximale de la station, du nombre de véhicules en cours de charge et du niveau actuel de la batterie.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EVChargingStation:    
  description: 'EV Charging Station'    
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
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    amountCollected:    
      description: 'Amount collected towards the service corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    amperage:    
      description: 'The total amperage offered by the charging station.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Ampers (A)'    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    availableCapacity:    
      description: 'The number of vehicles which currently can be charged. It must lower or equal than `capacity`.'    
      minimum: 0    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    capacity:    
      description: 'The total number of vehicles which can be charged at the same time. The total number of sockets can be higher. '    
      minimum: 1    
      type: integer    
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
      description: 'The Id of the charging point in the EV charging station corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    contactPoint:    
      description: 'The details to contact with the item.'    
      properties:    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Supersedes serviceArea.'    
          type: string    
        availabilityRestriction:    
          anyOf:    
            - description: 'Property. Array of identifiers format of any NGSI entity.'    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
            - description: 'Property. Array of identifiers format of any NGSI entity.'    
              items:    
                format: uri    
                type: string    
              type: array    
          description: 'Relationship. Model:''http://schema.org/hoursAvailable''. This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class.'    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'Property. Model:''http://schema.org/availableLanguage''. A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: 'Property. Model:''http://schema.org/contactOption''. An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).'    
        contactType:    
          description: 'Property. Contact type of this item.'    
          type: string    
        email:    
          description: 'Property. Email address of owner.'    
          format: idn-email    
          type: string    
        faxNumber:    
          description: 'Property. Model:''http://schema.org/Text''. The fax number.'    
          type: string    
        name:    
          description: 'Property. The name of this item.'    
          type: string    
        productSupported:    
          description: 'Property. Model:''http://schema.org/Text''. The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").'    
          type: string    
        telephone:    
          description: 'Property. Telephone of this contact.'    
          type: string    
        url:    
          description: 'Property. URL which provides a description or further information about this item.'    
          format: uri    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    dataDescriptor:    
      description: 'URI pointing to the data-descriptor entity'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    endDateTime:    
      description: 'Reported end time corresponding to this observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &evchargingstation_-_properties_-_owner_-_items_-_anyof    
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
    network:    
      description: 'The name of the Network, with that the operator cooperates. '    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
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
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *evchargingstation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    powerConsumption:    
      description: 'Power consumed by the entity corresponding to this observation.'    
      type: number    
      x-ngsi:    
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
    socketNumber:    
      description: 'The total number of sockets offered by this charging station'    
      minimum: 1    
      type: integer    
      x-ngsi:    
        model: http://schema.org/Number.    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startDateTime:    
      description: 'Reported start time corresponding to this observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    stationName:    
      description: 'The name station corresponding to this observation. It can be the name of bike docking station, charging station, etc.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Status of the charging station. Enum:''almostEmpty, almostFull, empty, full, outOfService, withIncidence, working''. Or any other application-specific.'    
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
      description: 'The amount of tax levied on the products, things and services which includes sales tax, value-added tax, service tax, Good and Service tax, customs duty, etc.'    
      type: number    
      x-ngsi:    
        type: Property    
    transactionId:    
      description: 'Unique transaction Id of the entity corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    transactionType:    
      description: 'Type of the transaction based on the mode of payment (For eg. mobile/UPI, card, etc) or mode of service (For eg. Issue, ReIssue, Entry, Exit etc.) corresponding to this observation.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be EVChargingStation'    
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
        - 'BRT bus'    
        - 'BRT minibus'    
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
        - 'fire tender'    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - 'police van'    
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
      description: 'The total voltage offered by the charging station'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'Volts (V)'    
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
## Exemples de charges utiles  
#### EVChargingStation NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'une EVChargingStation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### EVChargingStation NGSI-v2 normalisée Exemple  
Voici un exemple d'une EVChargingStation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### EVChargingStation NGSI-LD key-values Exemple  
Voici un exemple d'une EVChargingStation au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
        "iudx:EVChargingStation",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EVChargingStation NGSI-LD normalisé Exemple  
Voici un exemple d'une EVChargingStation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
        "type": "Geoproperty",  
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
        "type": "string",  
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
            "@type": "date-time",  
            "@value": "2022-06-28T20:28:41+05:30"  
        }  
    },  
    "startDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "date-time",  
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
            "@type": "date-time",  
            "@value": "2022-06-28T20:27:29+05:30"  
        }  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld",  
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
