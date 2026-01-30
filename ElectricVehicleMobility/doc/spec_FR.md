<!-- 10-Header -->
  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

Entité: ElectricVehicleMobility  
===============================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Licence ouverte](https://github.com/smart-data-models//dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md)  

[document généré automatiquement](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Observation quotidienne des modèles de mobilité des véhicules électriques agrégés par emplacement, marque de véhicule et région géographique.**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## Liste de propriétés  


<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou des formats/motifs différents</sub></sup>  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse de rue, et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité, et qui est dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par les autorités locales.
	- `postOfficeBoxNumber[string]`: Le numéro de boîte postale pour les adresses de boîte postale. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique dans une rue publique
- `alternateName[string]`: Un nom alternatif pour cet élément
- `areaServed[string]`: Zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)
- `averageDistanceKm[number]`: Distance moyenne parcourue en kilomètres  . Model: [https://schema.org/Number](https://schema.org/Number)
- `dataProvider[string]`: Fournisseur de l'entité de données harmonisée  . Model: [https://schema.org/Text](https://schema.org/Text)
- `dateCreated[date-time]`: Horodatage de création de l'entité. Celui-ci sera généralement attribué par la plate-forme de stockage
- `dateModified[date-time]`: Heure de la dernière modification de l'entité. Ceci est généralement attribué par la plate-forme de stockage
- `dateObserved[date]`: Date de l'observation (YYYY-MM-DD)  . Model: [https://schema.org/Date](https://schema.org/Date)
- `description[string]`: Une description de cet article
- `deviceBrand[string]`: Marque ou fabricant du véhicule électrique  . Model: [https://schema.org/Text](https://schema.org/Text)
- `district[string]`: Lieu où l'observation a été faite  . Model: [https://schema.org/Text](https://schema.org/Text)
- `id[*]`: Identifiant unique de l'entité
- `location[*]`: Référence Geojson de l'élément. Il peut s'agir d'un Point, LineString, Polygon, MultiPoint, MultiLineString ou MultiPolygon
- `locationCode[string]`: Code officiel de la commune  . Model: [https://schema.org/Text](https://schema.org/Text)
- `municipality[string]`: Commune où l'observation a été faite  . Model: [https://schema.org/Text](https://schema.org/Text)
- `n[number]`: Nombre d'observations utilisées pour calculer la distance moyenne  . Model: [https://schema.org/Number](https://schema.org/Number)
- `name[string]`: Le nom de cet article
- `owner[array]`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux ID uniques du ou des propriétaires
- `region[string]`: Région où l'observation a été faite  . Model: [https://schema.org/Text](https://schema.org/Text)
- `seeAlso[*]`: liste d'URI pointant vers des ressources supplémentaires concernant l'élément
- `source[string]`: Source d'origine des données sous forme d'URL  . Model: [https://schema.org/Text](https://schema.org/Text)
- `type[string]`: Type d'entité NGSI. Il doit être ElectricVehicleMobility
- `vehicleType[string]`: Type de véhicule électrique  . Model: [https://schema.org/Text](https://schema.org/Text)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Propriétés requises  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-NotesYaml -->
  
<!-- /40-NotesYaml -->
  
<!-- 50-DataModelHeader -->
  

## Description du modèle de données des propriétés  

Trié par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>détails complets de yaml</strong></summary>    

```yaml  
ElectricVehicleMobility:    
  description: Daily observation of electric vehicle mobility patterns aggregated by location, vehicle brand, and geographic region.    
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
    averageDistanceKm:    
      description: Average distance traveled in kilometers    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilometers    
    dataProvider:    
      description: Provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: Date of the observation (YYYY-MM-DD)    
      format: date    
      type: string    
      x-ngsi:    
        model: https://schema.org/Date    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    deviceBrand:    
      description: Brand or manufacturer of the electric vehicle    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    district:    
      description: District where the observation was made    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    locationCode:    
      description: Official municipality code    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    municipality:    
      description: Municipality where the observation was made    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    n:    
      description: Number of observations used to calculate the average distance    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    region:    
      description: Region where the observation was made    
      enum:    
        - CONTINENTE    
        - AÇORES    
        - MADEIRA    
        - Outros - GDPR    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: Original source of the data as a URL    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI entity type. It has to be ElectricVehicleMobility    
      enum:    
        - ElectricVehicleMobility    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: Type of electric vehicle    
      enum:    
        - BEV    
        - PHEV    
        - HEV    
        - FCEV    
        - unknown    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms...    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/ElectricVehicleMobility/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/ElectricVehicleMobility/schema.json    
  x-model-tags: transportation,electricVehicle,mobility,statistics    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Exemples de charges utiles  

#### Exemple de valeurs clés NGSI-v2 de ElectricVehicleMobility  

Voici un exemple de ElectricVehicleMobility au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lors de l'utilisation de `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": "2025-12-15",  
  "region": "Outros - GDPR",  
  "district": "Outros - GDPR",  
  "municipality": "Outros - GDPR",  
  "locationCode": "Outros - GDPR",  
  "deviceBrand": "Outros - GDPR",  
  "averageDistanceKm": "",  
  "n": 26  
}  
```  
</details>  

#### Exemple normalisé ElectricVehicleMobility NGSI-v2  

Voici un exemple de ElectricVehicleMobility au format JSON-LD normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et retourne les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/cacher l'exemple</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": {  
    "type": "Date-Time",  
    "value": "2025-12-15"  
  },  
  "region": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "district": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "municipality": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "locationCode": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "deviceBrand": {  
    "type": "Text",  
    "value": "Outros - GDPR"  
  },  
  "averageDistanceKm": {  
    "type": "Text",  
    "value": ""  
  },  
  "n": {  
    "type": "Property",  
    "value": 26  
  }  
}  
```  
</details>  

#### Exemple de valeurs clés NGSI-LD pour la mobilité des véhicules électriques  

Voici un exemple de ElectricVehicleMobility au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lors de l'utilisation de `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
<details><summary><strong>afficher/masquer l'exemple</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": "2025-12-15",  
  "region": "Outros - GDPR",  
  "district": "Outros - GDPR",  
  "municipality": "Outros - GDPR",  
  "locationCode": "Outros - GDPR",  
  "deviceBrand": "Outros - GDPR",  
  "averageDistanceKm": "",  
  "n": 26,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details>  

#### Exemple normalisé ElectricVehicleMobility NGSI-LD  

Voici un exemple de ElectricVehicleMobility au format JSON-LD normalisé. Ceci est compatible avec NGSI-LD lorsqu'on n'utilise pas d'options et retourne les données de contexte d'une entité individuelle.  
<details><summary><strong>afficher/cacher l'exemple</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:ElectricVehicleMobility:PT:OUTROS-GDPR:OUTROS-GDPR:20251215",  
  "type": "ElectricVehicleMobility",  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "Date",  
      "@value": "2025-12-15"  
    }  
  },  
  "region": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "district": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "municipality": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "locationCode": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "deviceBrand": {  
    "type": "Property",  
    "value": "Outros - GDPR"  
  },  
  "averageDistanceKm": {  
    "type": "Property",  
    "value": ""  
  },  
  "n": {  
    "type": "Property",  
    "value": 26  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->
  
<!-- 90-FooterNotes -->
  
<!-- /90-FooterNotes -->
  
<!-- 95-Units -->
  

Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de gérer les unités de magnitude  
<!-- /95-Units -->
  
<!-- 97-LastFooter -->
  
---  

[Modèles de données intelligents](https://smartdatamodels.org) +++ [Manuel de contribution](https://bit.ly/contribution_manual)  
  
