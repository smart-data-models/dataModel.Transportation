<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : AnprFlowObserved  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Le modèle de données représente une observation liée au passage d'un véhicule à un endroit et à un moment donnés. Ce modèle de données est basé sur le [dataModel.Transportation/ItemFlowObserved], complété par des propriétés spécifiques à l'ANPR et des liens vers les images d'observation**.  
version : 0.0.2  
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
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateObserved[date-time]`: Date de l'entité observée définie par l'utilisateur  - `dateReceived[date-time]`: Date à laquelle l'observation a été reçue par la plate-forme  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `laneId[string]`: Identificateur de couloir. Identification de la voie fournie par l'observateur  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `observedBy[*]`: L'entité ou le dispositif qui a signalé cette observation  - `observedVehicle[object]`: Informations sur le véhicule observé  	- `brand[object]`: Marque détectée du véhicule observé    
	- `color[object]`: Couleur détectée du véhicule observé    
	- `country[object]`: Pays détecté du véhicule observé    
	- `direction[string]`: Direction détectée du véhicule observé    
	- `licensePlate[object]`: Plaque d'immatriculation détectée du véhicule observé    
	- `model[object]`: Modèle de marque détecté du véhicule observé    
	- `speed[number]`: Vitesse détectée du véhicule observé    
- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `refImages[array]`: Tableau de plusieurs objets faisant référence à des images  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit s'agir de AnprFlowObserved  - `vehiclePlateNotRead[boolean]`: Indique si une licence n'a pas pu être lue  - `zonesServed[array]`: Réseau de zones capables de recevoir ou de lire les observations  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `dateObserved`  - `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Ce modèle de données décrit les principales entités impliquées dans les applications intelligentes qui traitent des questions de police. Cet ensemble d'entités est principalement associé aux segments verticaux de l'automobile et de la ville intelligente, ainsi qu'aux applications IoT connexes. Lorsque cela est possible, des références aux types d'entités et aux attributs schema.org existants sont incluses. Ce modèle a été conçu pour être aussi générique que possible, permettant ainsi d'être utilisé par différents départements de police et des zones telles que l'ANPR, le contrôle de la trajectoire et les véhicules de police.  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnprFlowObserved:    
  description: The data model represents an observation linked to the passing of a vehicle at a certain location and at a given time. This Data Model is based on the [dataModel.Transportation/ItemFlowObserved], extended with ANPR specific properties and links to the observation images.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    dateObserved:    
      description: Date of the observed entity defined by the user    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateReceived:    
      description: Timestamp when the observation has been received by the platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
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
        type: Relationship    
    laneId:    
      description: Lane identifier. Lane identification provided by the observer    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    observedBy:    
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
      description: The entity or device which has reported this observation    
      x-ngsi:    
        type: Relationship    
    observedVehicle:    
      description: Information about the observed vehicle    
      properties:    
        brand:    
          description: Detected brand of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Brand name identified    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        color:    
          description: Detected color of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Color name    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        country:    
          description: Detected country of the observed vehicle    
          properties:    
            code:    
              description: Country code according to ISO 3166-1 alpha-2    
              type: string    
              x-ngsi:    
                type: Property    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        direction:    
          description: Detected direction of the observed vehicle    
          enum:    
            - away    
            - towards    
          type: string    
          x-ngsi:    
            type: Property    
        licensePlate:    
          description: Detected license plate of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Sequence of position points describing this location, expressed in coordinate system    
              oneOf:    
                - description: Geojson reference to the item. Point    
                  properties:    
                    bbox:    
                      description: BBox of the  Point    
                      items:    
                        type: number    
                      minItems: 4    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    coordinates:    
                      description: Coordinates of the Point    
                      items:    
                        type: number    
                      minItems: 2    
                      type: array    
                      x-ngsi:    
                        type: Property    
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
                      description: BBox coordinates of the LineString    
                      items:    
                        type: number    
                      minItems: 4    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    coordinates:    
                      description: Coordinates of the LineString    
                      items:    
                        items:    
                          type: number    
                        minItems: 2    
                        type: array    
                      minItems: 2    
                      type: array    
                      x-ngsi:    
                        type: Property    
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
                      description: BBox coordinates of the Polygon    
                      items:    
                        type: number    
                      minItems: 4    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    coordinates:    
                      description: Coordinates of the Polygon    
                      items:    
                        items:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        minItems: 4    
                        type: array    
                      type: array    
                      x-ngsi:    
                        type: Property    
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
                      description: BBox coordinates of the LineString    
                      items:    
                        type: number    
                      minItems: 4    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    coordinates:    
                      description: Coordinates of the MulitPoint    
                      items:    
                        items:    
                          type: number    
                        minItems: 2    
                        type: array    
                      type: array    
                      x-ngsi:    
                        type: Property    
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
                      description: BBox coordinates of the LineString    
                      items:    
                        type: number    
                      minItems: 4    
                      type: array    
                      x-ngsi:    
                        type: Property    
                    coordinates:    
                      description: Coordinates of the MultiLineString    
                      items:    
                        items:    
                          items:    
                            type: number    
                          minItems: 2    
                          type: array    
                        minItems: 2    
                        type: array    
                      type: array    
                      x-ngsi:    
                        type: Property    
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
                      description: Coordinates of the MultiPolygon    
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
                      x-ngsi:    
                        type: Property    
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
                type: Property    
            identifier:    
              description: License plate identifier    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        model:    
          description: Detected brand model of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Model name    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        plateColor:    
          description: Detected plate color of the observed vehicle    
          properties:    
            confidence:    
              description: Confidence level of the detection    
              maximum: 1    
              minimum: 0    
              type: number    
              x-ngsi:    
                type: Property    
            name:    
              description: Color name    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        speed:    
          description: Detected speed of the observed vehicle    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    refImages:    
      description: Array of multiple objects that refer to images    
      items:    
        properties:    
          contentType:    
            description: Content type according to IANA Media Types    
            type: string    
            x-ngsi:    
              type: Property    
          imageType:    
            description: Type of image    
            enum:    
              - plate    
              - overview    
              - anpr    
            type: string    
            x-ngsi:    
              type: Property    
          url:    
            description: URL referencing to the image    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Relationship    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be AnprFlowObserved    
      enum:    
        - AnprFlowObserved    
      type: string    
      x-ngsi:    
        type: Property    
    vehiclePlateNotRead:    
      description: Indicates if a license could not be read    
      type: boolean    
      x-ngsi:    
        type: Property    
    zonesServed:    
      description: Array of zones that are able to receive or read the observations    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnprFlowObserved/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/AnprFlowObserved/schema.json    
  x-model-tags: ''    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### AnprFlowObserved Valeurs clés NGSI-v2 Exemple  
Voici un exemple d'AnprFlowObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed": "Antwerp",  
  "zonesServed": [  
    "Antwerp"  
  ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand": {  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model": {  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color": {  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country": {  
      "code": "BE",  
      "confidence": 0.95  
    },  
    "licensePlate": {  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    },  
    "plateColor": {  
      "name": "white",  
      "confidence": 0.95  
    }  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages": [  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-v2 normalisé Exemple  
Voici un exemple d'AnprFlowObserved au format JSON-LD tel que normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2022-09-01T16:30:00Z"  
  },  
  "laneId": {  
    "type": "Text",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "StructuredValue",  
    "value": [  
      "Antwerp"  
    ]  
  },  
  "vehiclePlateNotRead": {  
    "type": "Boolean",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "StructuredValue",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": {  
        "name": "Audi",  
        "confidence": 0.97  
      },  
      "model": {  
        "name": "A3",  
        "confidence": 0.98  
      },  
      "color": {  
        "name": "black",  
        "confidence": 0.95  
      },  
      "country": {  
        "code": "BE",  
        "confidence": 0.95  
      },  
      "licensePlate": {  
        "identifier": "1-ABC-123",  
        "confidence": 0.96  
      },  
      "plateColor": {  
      "name": "white",  
      "confidence": 0.95  
      }  
    }  
  },  
  "refImages": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "url": "s3://bucket/object-xxx-plate",  
        "contentType": "image/jpg",  
        "imageType": "anpr"  
      }  
    ]  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ],  
      "type": "Point"  
    }  
  }  
}  
```  
</details>  
#### Valeurs clés NGSI-LD observées AnprFlowObserved Exemple  
Voici un exemple d'AnprFlowObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "addressCountry": "BE",  
    "addressLocality": "Antwerp",  
    "streetAddress": "Noorderlaan"  
  },  
  "dateObserved": "2022-09-01T16:30:00Z",  
  "dateReceived": "2022-09-01T16:35:00Z",  
  "observedBy": "ANPR1_Noorderlaan",  
  "laneId": "ABC123",  
  "areaServed": "Antwerp",  
  "zonesServed": [  
    "Antwerp"  
  ],  
  "vehiclePlateNotRead": false,  
  "observedVehicle": {  
    "direction": "towards",  
    "speed": 50,  
    "brand": {  
      "name": "Audi",  
      "confidence": 0.97  
    },  
    "model": {  
      "name": "A3",  
      "confidence": 0.98  
    },  
    "color": {  
      "name": "black",  
      "confidence": 0.95  
    },  
    "country": {  
      "code": "BE",  
      "confidence": 0.95  
    },  
    "licensePlate": {  
      "identifier": "1-ABC-123",  
      "confidence": 0.96  
    },  
    "plateColor": {  
      "name": "white",  
      "confidence": 0.95  
    }  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "refImages": [  
    {  
      "contentType": "image/jpg",  
      "imageType": "anpr",  
      "url": "urn:ngsi-ld:ANPR:items:123"  
    }  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AnprFlowObserved NGSI-LD normalisé Exemple  
Voici un exemple d'AnprFlowObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "anprFlowObserved:LEZ-Noorderlaan",  
  "type": "AnprFlowObserved",  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "BE",  
      "addressLocality": "Antwerp",  
      "streetAddress": "Noorderlaan"  
    }  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-09-01T16:30:00Z"  
    }  
  },  
  "laneId": {  
    "type": "Property",  
    "value": "ABC123"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Antwerp"  
  },  
  "zonesServed": {  
    "type": "Property",  
    "value": {  
      "type": "string",  
      "coordinates": [  
        "Antwerp"  
      ]  
    }  
  },  
  "vehiclePlateNotRead": {  
    "type": "Property",  
    "value": false  
  },  
  "observedVehicle": {  
    "type": "Property",  
    "value": {  
      "direction": "towards",  
      "speed": 50,  
      "brand": "Audi",  
      "model": "A3",  
      "color": "black",  
      "country": "BE",  
      "licensePlate": "1-ABC-123",  
      "plateColor": "white"  
    }  
  },  
  "refImages": {  
    "type": "Property",  
    "value": [  
      {  
        "type": "s3://bucket/object-xxx-plate",  
        "contentType": "image/jpg",  
        "imageType": "anpr"  
      }  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
