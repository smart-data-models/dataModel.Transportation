Entité : RoadAccident  
=====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadAccident/LICENSE.md)  
Description globale : **Description d'un accident de la route avec ses causes et ses conséquences. Première version développée dans le cadre du projet Synchronicité**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.    
Propriétés requises  
- `id`  - `status`  - `type`    
Modèle de données provenant du projet Synchronicity  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadAccident:    
  description: 'A road accident description with causes and aftermath. First version developed in Synchronicity project'    
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
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
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &roadaccident_-_properties_-_owner_-_items_-_anyof    
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
    location:    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadaccident_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
  required:    
    - id    
    - type    
    - status    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### RoadAccident NGSI V2 valeurs-clés Exemple  
Voici un exemple d'un RoadAccident au format JSON sous forme de valeurs-clés. Ceci est compatible avec NGSI V2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "source": "To be defined",  
  "name": "Name of the element of the accident.",  
  "alternateName": "Other name.",  
  "description": "Clash in the middle of a traffic light",  
  "dataProvider": "Municipality.",  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "areaServed": "worldwide",  
  "localId": "20210312-A1.",  
  "status": "onGoing",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentStatisticalDate": {  
    "year": 2021,  
    "quarter": 1,  
    "weekday": "Friday",  
    "hour": 4  
  },  
  "accidentType": [  
    "10",  
    "6"  
  ],  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "roadSurface": "2",  
  "roadPaving": "2",  
  "accidentLocation": "5",  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadTrunk": "12",  
  "roadSign": "5",  
  "pedestriansInvolved": [  
    "true"  
  ],  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "numPassengersInjured": 1,  
  "numPassengersDead": 1,  
  "numPedestrianInjured": 1,  
  "numPedestrianDead": 0,  
  "totalInjured": 2,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalDeadPeopleWithin24Hours": 0  
}  
```  
#### RoadAccident NGSI V2 normalisé Exemple  
Voici un exemple d'un RoadAccident au format JSON tel que normalisé. Ceci est compatible avec NGSI V2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-06-23T04:19:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-29T08:36:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "FranklinStrasse",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10387",  
      "postOfficeBoxNumber": "",  
      "areaServed": "worldwide."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentStatisticalDate": {  
    "type": "Property",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "Property",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": [  
      "true"  
    ]  
  },  
  "vehiclesInvolved": {  
    "type": "Property",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Property",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  }  
}  
```  
#### Accident de la route Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un RoadAccident au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "type": "RoadAccident",  
  "dateCreated": "2018-06-23T04:19:24Z",  
  "dateModified": "2020-10-29T08:36:40Z",  
  "source": "To be defined",  
  "name": "Name of the element of the accident.",  
  "alternateName": "Other name.",  
  "description": "Clash in the middle of a traffic light",  
  "dataProvider": "Municipality.",  
  "owner": [  
    "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
    "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
    "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -56.6404505,  
      168.370658  
    ]  
  },  
  "address": {  
    "streetAddress": "FranklinStrasse",  
    "addressLocality": "Berlin",  
    "addressRegion": "Berlin",  
    "addressCountry": "Germany",  
    "postalCode": "10387",  
    "postOfficeBoxNumber": "",  
    "areaServed": "worldwide."  
  },  
  "areaServed": "worldwide",  
  "localId": "20210312-A1.",  
  "status": "onGoing",  
  "accidentDate": "2021-03-12T13:59:36Z",  
  "accidentStatisticalDate": {  
    "year": 2021,  
    "quarter": 1,  
    "weekday": "Friday",  
    "hour": 4  
  },  
  "accidentType": [  
    "10",  
    "6"  
  ],  
  "accidentDescription": [  
    "23",  
    "46"  
  ],  
  "weatherConditions": [  
    "10",  
    "20"  
  ],  
  "roadSurface": "2",  
  "roadPaving": "2",  
  "accidentLocation": "5",  
  "roadClass": "Motorway.",  
  "roadIntersection": "8",  
  "roadTrunk": "12",  
  "roadSign": "5",  
  "pedestriansInvolved": [  
    "true"  
  ],  
  "vehiclesInvolved": [  
    "21",  
    "6"  
  ],  
  "weakestSubject": "20",  
  "numPassengersInjured": 1,  
  "numPassengersDead": 1,  
  "numPedestrianInjured": 1,  
  "numPedestrianDead": 0,  
  "totalInjured": 2,  
  "totalDeadPeopleWithin30Days": 0,  
  "totalDeadPeopleWithin24Hours": 0,  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
#### Accident de la route NGSI-LD normalisé Exemple  
Voici un exemple d'un RoadAccident au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:RoadAccident:id:ORHW:45620815",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-06-23T04:19:24Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-10-29T08:36:40Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": "To be defined"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Name of the element of the accident."  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Other name."  
  },  
  "description": {  
    "type": "Property",  
    "value": "Clash in the middle of a traffic light"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "Municipality."  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:SUUU:18395806",  
      "urn:ngsi-ld:RoadAccident:items:GVOF:30958855"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:RoadAccident:items:ESLS:37894243",  
      "urn:ngsi-ld:RoadAccident:items:ZNUH:87936284"  
    ]  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -56.6404505,  
        168.370658  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "FranklinStrasse",  
      "addressLocality": "Berlin",  
      "addressRegion": "Berlin",  
      "addressCountry": "Germany",  
      "postalCode": "10387",  
      "postOfficeBoxNumber": "",  
      "areaServed": "worldwide."  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "worldwide"  
  },  
  "type": "RoadAccident",  
  "localId": {  
    "type": "Property",  
    "value": "20210312-A1."  
  },  
  "status": {  
    "type": "Property",  
    "value": "onGoing"  
  },  
  "accidentDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-12T13:59:36Z"  
    }  
  },  
  "accidentStatisticalDate": {  
    "type": "Property",  
    "value": {  
      "year": 2021,  
      "quarter": 1,  
      "weekday": "Friday",  
      "hour": 4  
    }  
  },  
  "accidentType": {  
    "type": "Property",  
    "value": [  
      "10",  
      "6"  
    ]  
  },  
  "accidentDescription": {  
    "type": "Property",  
    "value": [  
      "23",  
      "46"  
    ]  
  },  
  "weatherConditions": {  
    "type": "Property",  
    "value": [  
      "10",  
      "20"  
    ]  
  },  
  "roadSurface": {  
    "type": "Property",  
    "value": "2"  
  },  
  "roadPaving": {  
    "type": "Property",  
    "value": "2"  
  },  
  "accidentLocation": {  
    "type": "Property",  
    "value": "5"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "Motorway."  
  },  
  "roadIntersection": {  
    "type": "Property",  
    "value": "8"  
  },  
  "roadTrunk": {  
    "type": "Property",  
    "value": "12"  
  },  
  "roadSign": {  
    "type": "Property",  
    "value": "5"  
  },  
  "pedestriansInvolved": {  
    "type": "Property",  
    "value": [  
      "true"  
    ]  
  },  
  "vehiclesInvolved": {  
    "type": "Property",  
    "value": [  
      "21",  
      "6"  
    ]  
  },  
  "weakestSubject": {  
    "type": "Property",  
    "value": "20"  
  },  
  "numPassengersInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPassengersDead": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianInjured": {  
    "type": "Property",  
    "value": 1  
  },  
  "numPedestrianDead": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalInjured": {  
    "type": "Property",  
    "value": 2  
  },  
  "totalDeadPeopleWithin30Days": {  
    "type": "Property",  
    "value": 0  
  },  
  "totalDeadPeopleWithin24Hours": {  
    "type": "Property",  
    "value": 0  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
