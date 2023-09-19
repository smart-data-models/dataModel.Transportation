<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Station d'accueil pour vélos  
=====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Station d'accueil pour la location de vélos**  
version : 0.1.1  
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
- `agency_fare_url[string]`: URL d'une page web contenant les détails des tarifs et permettant d'acheter en ligne des billets pour cette agence. Idem : champ 'agency_fare_url' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `agency_name[string]`: Le champ agency_name contient le nom complet de l'agence de transport. Identique : Champ 'agency_name' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `agency_url[uri]`: Le champ agency_url contient l'URL de l'agence de transport. Identique : Champ 'agency_url' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableBikeNumber[number]`: Le nombre de vélos disponibles dans la station d'accueil des vélos à louer par les utilisateurs  . Model: [https://schema.org/Number](https://schema.org/Number)- `contactPoint[object]`: Les coordonnées à contacter avec l'article  . Model: [https://schema.org/ContactPoint](https://schema.org/ContactPoint)	- `areaServed[string]`: Zone géographique dans laquelle un service ou un article est proposé. Remplace serviceArea    
	- `availabilityRestriction[*]`: Cette propriété relie un point de contact à des informations sur les cas où le point de contact n'est pas disponible. Les détails sont fournis à l'aide de la classe de spécification des heures d'ouverture.  . Model: [http://schema.org/hoursAvailable](http://schema.org/hoursAvailable)  
	- `availableLanguage[*]`: Langue que quelqu'un peut utiliser avec ou dans l'article, le service ou le lieu. Veuillez utiliser l'un des codes de langue de la norme IETF BCP 47. L'option Texte est mise en œuvre, mais il peut s'agir également de l'option Langue.  . Model: [http://schema.org/availableLanguage](http://schema.org/availableLanguage)  
	- `contactOption[*]`: Une option disponible sur ce point de contact (par exemple, un numéro gratuit ou une assistance pour les malentendants).  . Model: [http://schema.org/contactOption](http://schema.org/contactOption)  
	- `contactType[string]`: Type de contact de cet article    
	- `email[idn-email]`: Adresse électronique du propriétaire    
	- `faxNumber[string]`: Le numéro de fax  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `name[string]`: Le nom de cet élément    
	- `productSupported[string]`: Le produit ou le service auquel se rapporte ce point de contact d'assistance (par exemple, l'assistance produit pour une ligne de produits particulière). Il peut s'agir d'un produit ou d'une ligne de produits spécifique (par exemple "iPhone") ou d'une catégorie générale de produits ou de services (par exemple "smartphones").  . Model: [http://schema.org/Text](http://schema.org/Text)  
	- `telephone[string]`: Téléphone de ce contact    
- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `freeSlotNumber[number]`: Le nombre d'emplacements disponibles pour la restitution et le stationnement des vélos. Il doit être inférieur ou égal à `totalSlotNumber`.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `mediaURL[uri]`: URL fournissant des informations complémentaires sur toute image ou média de la plainte ou du lieu  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Le nom de cet élément  - `observationDateTime[date-time]`: Dernière heure d'observation signalée  . Model: [https://schema.org/Text](https://schema.org/Text)- `openingHours[string]`: Heures d'ouverture de la station d'accueil  . Model: [http://schema.org/openingHours](http://schema.org/openingHours)- `outOfServiceSlotNumber[number]`: Le nombre d'emplacements qui sont hors service et qui ne peuvent pas être utilisés pour louer ou garer un vélo. Il doit être inférieur ou égal à `totalSlotNumber`.  . Model: [https://schema.org/Number](https://schema.org/Number)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `provider[string]`: Fournisseur de services de location de vélos  . Model: [https://schema.org/provider](https://schema.org/provider)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `stationCode[string]`: Le numéro ou le code de la station de location de vélos correspondant à l'observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `stationName[string]`: Le nom de la station de location de vélos correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)- `status[string]`: Statut de la station d'accueil pour vélos de location. Enum : "working, outOfService, withIncidence, full, almostFull, empty, almostEmpty". Ou toute autre application spécifique  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalSlotNumber[number]`: Le nombre total d'emplacements offerts par cette station d'accueil pour vélos  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Type d'entité NGSI. Il doit s'agir de BikeHireDockingStation  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
De nombreuses villes proposent un système de location de vélos pour les citoyens. Ceux-ci peuvent louer un vélo sur la base de différents types d'abonnements. Une station de location de vélos où les utilisateurs abonnés peuvent louer et rendre un vélo. Elle fournit des informations sur ses principales caractéristiques et sur la disponibilité des vélos et des emplacements libres.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BikeHireDockingStation:    
  description: Bike Hire Docking Station    
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
    agency_fare_url:    
      description: "URL of a web page that contains the details of the fares and also could allow to purchase tickets for that agency online. SameAs: 'agency_fare_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt) "    
      type: string    
      x-ngsi:    
        type: Property    
    agency_name:    
      description: "The agency_name field contains the full name of the transit agency. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    agency_url:    
      description: "The agency_url field contains the URL of the transit agency. SameAs: 'agency_url' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    availableBikeNumber:    
      description: The number of bikes available in the bike hire docking station to be hired by users    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    freeSlotNumber:    
      description: The number of slots available for returning and parking bikes. It must lower or equal than `totalSlotNumber`    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    mediaURL:    
      description: URL providing further information of any image(s) or media of the complaint or place    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: Last reported time of observation    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    openingHours:    
      description: Opening hours of the docking station    
      type: string    
      x-ngsi:    
        model: http://schema.org/openingHours    
        type: Property    
    outOfServiceSlotNumber:    
      description: The number of slots that are out of order and cannot be used to hire or park a bike. It must lower or equal than `totalSlotNumber`    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    provider:    
      description: Bike hire service provider    
      type: string    
      x-ngsi:    
        model: https://schema.org/provider    
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
    stationCode:    
      description: The station number or station code of the bike hire docking station corresponding to the observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    stationName:    
      description: The name of the bike hire docking station corresponding to this observation    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    status:    
      description: 'Status of the bike hire docking station. Enum:''working, outOfService, withIncidence, full, almostFull, empty, almostEmpty''. Or any other application specific'    
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
        model: https://schema.org/Number    
        type: Property    
    totalSlotNumber:    
      description: The total number of slots offered by this bike docking station    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be BikeHireDockingStation    
      enum:    
        - BikeHireDockingStation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/BikeHireDockingStation/schema.json    
  x-model-tags: ""    
  x-version: 0.1.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### BikeHireDockingStation Valeurs clés NGSI-v2 Exemple  
Voici un exemple d'une BikeHireDockingStation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "status": "working",  
    "provider": "University of Mumbay",  
    "contactPoint": {  
        "url": "uri:ngsi:www.lignesdazur.com"  
    },  
    "availableBikeNumber": 20,  
    "freeSlotNumber": 10,  
    "openingHours": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            2.180042,  
            41.397952  
        ]  
    },  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Barcelona",  
        "streetAddress": "Gran Via Corts Catalanes,760"  
    },  
    "totalSlotNumber": 100,  
    "outOfServiceSlotNumber": 21,  
    "stationName": "Pune",  
    "mediaURL": "http://pedalsaddle.in/",  
    "agency_url": "http://pedalsaddle.in/",  
    "agency_name": "PedalSaddle",  
    "stationCode": "2",  
    "observationDate": "2021-03-11T15:51:02+05:30",  
    "agency_fare_url": ""  
}  
```  
</details>  
#### BikeHireDockingStation NGSI-v2 normalisé Exemple  
Voici un exemple de BikeHireDockingStation au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
  "type": "BikeHireDockingStation",  
  "status": {  
    "type": "Text",  
    "value": "working"  
  },  
  "provider": {  
    "type": "Text",  
    "value": "University of Mumbay"  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "url": "uri:ngsi:www.lignesdazur.com"  
    }  
  },  
  "availableBikeNumber": {  
    "type": "Number",  
    "value": 20  
  },  
  "freeSlotNumber": {  
    "type": "Number",  
    "value": 10  
  },  
  "openingHours": {  
    "type": "Text",  
    "value": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        2.180042,  
        41.397952  
      ]  
    }  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressCountry": "ES",  
      "addressLocality": "Barcelona",  
      "streetAddress": "Gran Via Corts Catalanes,760"  
    }  
  },  
  "totalSlotNumber": {  
    "type": "Number",  
    "value": 100  
  },  
  "outOfServiceSlotNumber": {  
    "type": "Number",  
    "value": 21  
  },  
  "stationName": {  
    "type": "Text",  
    "value": "Pune"  
  },  
  "mediaURL": {  
    "type": "Text",  
    "value": "http://pedalsaddle.in/"  
  },  
  "agency_url": {  
    "type": "Text",  
    "value": "http://pedalsaddle.in/"  
  },  
  "agency_name": {  
    "type": "Text",  
    "value": "PedalSaddle"  
  },  
  "stationCode": {  
    "type": "Number",  
    "value": "2"  
  },  
  "observationDate": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "agency_fare_url": {  
    "type": "Text",  
    "value": ""  
  }  
}  
```  
</details>  
#### BikeHireDockingStation Valeurs clés NGSI-LD Exemple  
Voici un exemple de BikeHireDockingStation au format JSON-LD sous forme de valeurs-clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "address": {  
        "addressCountry": "ES",  
        "addressLocality": "Barcelona",  
        "streetAddress": "Gran Via Corts Catalanes,760"  
    },  
    "agency_fare_url": "",  
    "agency_name": "PedalSaddle",  
    "agency_url": "http://pedalsaddle.in/",  
    "availableBikeNumber": 20,  
    "contactPoint": {  
        "url": "uri:ngsi:www.lignesdazur.com"  
    },  
    "freeSlotNumber": 10,  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            2.180042,  
            41.397952  
        ]  
    },  
    "mediaURL": "http://pedalsaddle.in/",  
    "observationDate": "2021-03-11T15:51:02+05:30",  
    "openingHours": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00",  
    "outOfServiceSlotNumber": 21,  
    "provider": "University of Mumbay",  
    "stationCode": "2",  
    "stationName": "Pune",  
    "status": "working",  
    "totalSlotNumber": 100,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### BikeHireDockingStation NGSI-LD normalisé Exemple  
Voici un exemple de BikeHireDockingStation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "Barcelona",  
            "streetAddress": "Gran Via Corts Catalanes,760"  
        }  
    },  
    "agency_fare_url": {  
        "type": "Property",  
        "value": ""  
    },  
    "agency_name": {  
        "type": "Property",  
        "value": "PedalSaddle"  
    },  
    "agency_url": {  
        "type": "Property",  
        "value": "http://pedalsaddle.in/"  
    },  
    "availableBikeNumber": {  
        "type": "Property",  
        "value": 20  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": {  
            "url": "uri:ngsi:www.lignesdazur.com"  
        }  
    },  
    "freeSlotNumber": {  
        "type": "Property",  
        "value": 10  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                2.180042,  
                41.397952  
            ]  
        }  
    },  
    "mediaURL": {  
        "type": "Property",  
        "value": "http://pedalsaddle.in/"  
    },  
    "observationDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "openingHours": {  
        "type": "Property",  
        "value": "Mo-Fr 10:00-19:00, Sa 10:00-22:00, Su 10:00-21:00"  
    },  
    "outOfServiceSlotNumber": {  
        "type": "Property",  
        "value": 21  
    },  
    "provider": {  
        "type": "Property",  
        "value": "University of Mumbay"  
    },  
    "stationCode": {  
        "type": "Property",  
        "value": "2"  
    },  
    "stationName": {  
        "type": "Property",  
        "value": "Pune"  
    },  
    "status": {  
        "type": "Property",  
        "value": "working"  
    },  
    "totalSlotNumber": {  
        "type": "Property",  
        "value": 100  
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
