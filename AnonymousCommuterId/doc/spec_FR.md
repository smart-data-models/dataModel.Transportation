<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : AnonymousCommuterId  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/AnonymousCommuterId/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Identifiant anonymisé pour le suivi des flux. Comprend une propriété d'origine et de destination pour cartographier son chemin.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `algorithm[string]`: Nom de l'algorithme utilisé pour anonymiser l'Id.  - `alternateName[string]`: Un nom alternatif pour cet élément  - `anonymizedId[string]`: Identifiant anonyme  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `date[string]`: Date de l'identifiant anonyme détecté.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `dest[string]`: Valeur en chaîne de l'identifiant de destination, entité réelle où l'identifiant anonyme a été détecté.  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `orig[string]`: Valeur en chaîne de l'id d'origine, dernière entité où l'id anonyme a été détecté.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Valeur en chaîne de la source de cet AnonymousCommuterId, par exemple (ALPR, surveillance des personnes, reconnaissance faciale, etc...)  - `type[string]`: Type d'entité NGSI. Il doit être AnonymousCommuterId.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `anonymizedId`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Ce modèle est destiné à être utilisé lorsqu'un certain suivi des IPI est nécessaire, et qu'il faut donc anonymiser les identifiants afin de fournir des informations utiles, mais en utilisant une fonction d'anonymisation (hachage) non réversible.  Comme c'est généralement le cas, des attributs normalisés sont prévus pour indiquer l'emplacement actuel et précédent de la détection. Ils sont destinés à contenir un autre ID d'entité, car le fait d'avoir les détecteurs également répliqués sous forme d'entités offre une bien meilleure expérience de modélisation des données. Enfin, un attribut d'algorithme a été ajouté afin de faciliter les différentes manières et méthodologies d'anonymisation des IPI.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AnonymousCommuterId:    
  description: 'Anonymized identifier for flow monitoring. Includes an origin and destiny property to map its path.'    
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
    algorithm:    
      description: 'Name of the algorithm used to anonymize the Id'    
      type: string    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    anonymizedId:    
      description: 'Anonymized identifier'    
      type: string    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    date:    
      description: 'Date of the detected anonymous identifier.'    
      format: date-time    
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
    dest:    
      description: 'String value of destination id, actual entity where the anonymous id was detected.'    
      type: string    
    id:    
      anyOf: &anonymouscommuterid_-_properties_-_owner_-_items_-_anyof    
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
    orig:    
      description: 'String value of origin id, last entity where the anonymous id was detected.'    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *anonymouscommuterid_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
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
    source:    
      description: 'String value of source of this AnonymousCommuterId, eg. (ALPR, People Monitoring, Face Recognition, etc...)'    
      type: string    
    type:    
      description: 'NGSI entity type. It has to be AnonymousCommuterId'    
      enum:    
        - AnonymousCommuterId    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - anonymizedId    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/AnonymousCommuterId/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/AnonymousCommuterId/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### AnonymousCommuterId Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'un AnonymousCommuterId au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ngsi-ld:HUES:001",  
    "anonymizedId": "D20220AC3478565F",  
    "type": "AnonymousCommuterId",  
    "date": "2022-09-05T08:25:35.00Z",  
    "orig": "City hall",  
    "dest": "Library",  
    "source": "People Monitoring",  
    "algorithm": "SHA1",  
    "dateCreated": "2022-09-05T09:25:35.00Z",  
    "dateModified": "2022-09-12T09:25:35.00Z",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.23161118206764,  
            -2.844695196525928  
        ]  
    }  
}  
```  
</details>  
#### AnonymousCommuterId NGSI-v2 normalisé Exemple  
Voici un exemple d'un AnonymousCommuterId au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
   "id": "ngsi-ld:HUES:001",  
    "anonymizedId": {  
        "type": "Text",  
        "value": "D20220AC3478565F"  
    },  
    "type": "AnonymousCommuterId",  
    "orig": {  
        "type": "Text",  
        "value": "City hall"  
    },  
    "dest": {  
        "type": "Text",  
        "value": "Library"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.23161118206764,  
                -2.844695196525928  
            ]  
        }  
    },  
    "date": {  
        "type": "DateTime",  
        "value": "2022-09-05T08:25:35.00Z"  
    },  
    "algorithm": {  
        "type": "Text",  
        "value": "SHA1"  
    },  
    "dateCreated": {  
        "type": "DateTime",  
        "value": "2022-09-05T09:25:35.00Z"  
    },  
    "dateModified": {  
        "type": "DateTime",  
        "value": "2022-09-12T09:25:35.00Z"  
    }  
}  
```  
</details>  
#### AnonymousCommuterId Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un AnonymousCommuterId au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ngsi-ld:HUES:001",  
    "anonymizedId": {  
        "type": "Text",  
        "value": "D20220AC3478565F"  
    },  
    "type": "AnonymousCommuterId",  
    "orig": {  
        "type": "Text",  
        "value": "City hall"  
    },  
    "dest": {  
        "type": "Text",  
        "value": "Library"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                43.23161118206764,  
                -2.844695196525928  
            ]  
        }  
    },  
    "date": {  
        "type": "DateTime",  
        "value": "2022-09-05T08:25:35.00Z"  
    },  
    "algorithm": {  
        "type": "Text",  
        "value": "SHA1"  
    },  
    "dateCreated": {  
        "type": "DateTime",  
        "value": "2022-09-05T09:25:35.00Z"  
    },  
    "dateModified": {  
        "type": "DateTime",  
        "value": "2022-09-12T09:25:35.00Z"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### AnonymousCommuterId NGSI-LD normalisé Exemple  
Voici un exemple d'un AnonymousCommuterId au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "ngsi-ld:HUES:001",  
    "anonymizedId": "D20220AC3478565F",  
    "type": "AnonymousCommuterId",  
    "date": "2022-09-05T08:25:35.00Z",  
    "orig": "City hall",  
    "dest": "Library",  
    "source": "People Monitoring",  
    "algorithm": "SHA1",  
    "dateCreated": "2022-09-05T09:25:35.00Z",  
    "dateModified": "2022-09-12T09:25:35.00Z",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.23161118206764,   
            -2.844695196525928  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
Ce modèle a été fourni par Purple Blob S.L., et adapté aux vues et aux besoins de notre produit METIS de flux de personnes anonymes. Nous sommes ouverts au développement d'un modèle de données interopérable AnonymousCommuterId à large usage, et donc, n'hésitez pas à contacter adelgado@purpleblob.net ou iruiz@purpleblob.net pour de plus amples discussions, ou encore mieux, à ouvrir un problème Github !  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
