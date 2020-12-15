Entité : CrowdFlowObserved  
==========================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **CrowdFlowObserved**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `averageCrowdSpeed`:   - `averageHeadwayTime`:   - `congested`:   - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateObserved`:   - `dateObservedFrom`:   - `dateObservedTo`:   - `description`: Une description de cet article  - `direction`:   - `id`:   - `location`:   - `name`: Le nom de cet article.  - `occupancy`:   - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `peopleCount`:   - `refRoadSegment`:   - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: NGSI Type d'entité  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CrowdFlowObserved:    
  description: CrowdFlowObserved    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    averageCrowdSpeed:    
      minimum: 0    
      type: number    
    averageHeadwayTime:    
      minimum: 0    
      type: number    
    congested:    
      type: boolean    
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
    dateObserved:    
      type: string    
    dateObservedFrom:    
      format: date-time    
      type: string    
    dateObservedTo:    
      format: date-time    
      type: string    
    description:    
      description: 'A description of this item'    
      type: Property    
    direction:    
      enum:    
        - inbound    
        - outbound    
      type: string    
    id:    
      anyOf: &crowdflowobserved_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
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
    occupancy:    
      maximum: 1    
      minimum: 0    
      type: number    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *crowdflowobserved_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    peopleCount:    
      minimum: 0    
      type: integer    
    refRoadSegment:    
      format: uri    
      type: string    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - CrowdFlowObserved    
      type: string    
  required:    
    - id    
    - type    
    - dateObserved    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### CrowdFlowObserved NGSI V2 key-values Exemple  
Voici un exemple de CrowdFlowObserved en format JSON comme valeurs clés. Il est compatible avec la version 2 du NGSI lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "dateObserved": "2018-08-07T11:10:00/2018-08-07T11:15:00",  
  "dateObservedFrom": "2018-08-07T11:10:00Z",  
  "dateObservedTo": "2018-08-07T11:15:00Z",  
  "peopleCount": 100,  
  "averageHeadwayTime": 5,  
  "congested": false,  
  "direction": "inbound",  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.73735395519672, 41.6538181849672],  
      [-4.73414858659993, 41.6600594193478],  
      [-4.73447575302641, 41.659585195093]  
    ]  
  }  
}  
```  
#### CrowdFlowObserved NGSI V2 normalisé Exemple  
Voici un exemple de CrowdFlowObserved au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
  "type": "CrowdFlowObserved",  
  "dateObserved": {  
    "value": "2018-08-07T11:10:00/2018-08-07T11:15:00"  
  },  
  "direction": {  
    "value": "inbound"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2018-08-07T11:10:00Z"  
  },  
  "peopleCount": {  
    "value": 100  
  },  
  "averageHeadwayTime": {  
    "value": 5  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2018-08-07T11:15:00Z"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [-4.73735395519672, 41.6538181849672],  
        [-4.73414858659993, 41.6600594193478],  
        [-4.73447575302641, 41.659585195093]  
      ]  
    }  
  },  
  "congested": {  
    "value": false  
  }  
}  
```  
#### CrowdFlowObserved NGSI-LD valeurs clés Exemple  
Voici un exemple de CrowdFlowObserved au format JSON-LD comme valeurs clés. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "averageHeadwayTime": 5,  
 "congested": False,  
 "dateObserved": "2018-08-07T11:10:00/2018-08-07T11:15:00",  
 "dateObservedFrom": {"@type": "DateTime", "@value": "2018-08-07T11:10:00Z"},  
 "dateObservedTo": {"@type": "DateTime", "@value": "2018-08-07T11:15:00Z"},  
 "direction": "inbound",  
 "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
 "location": {"coordinates": [[-4.73735395519672, 41.6538181849672],  
                              [-4.73414858659993, 41.6600594193478],  
                              [-4.73447575302641, 41.659585195093]],  
              "type": "LineString"},  
 "peopleCount": 100,  
 "type": "CrowdFlowObserved"}  
```  
#### CrowdFlowObserved NGSI-LD normalisé Exemple  
Voici un exemple de CrowdFlowObserved au format JSON-LD tel que normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:CrowdFlowObserved:Valladolid_1",  
    "type": "CrowdFlowObserved",  
    "dateObserved": {  
        "type": "Property",  
        "value": "2018-08-07T11:10:00/2018-08-07T11:15:00"  
    },  
    "direction": {  
        "type": "Property",  
        "value": "inbound"  
    },  
    "dateObservedFrom": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-08-07T11:10:00Z"  
        }  
    },  
    "peopleCount": {  
        "type": "Property",  
        "value": 100  
    },  
    "averageHeadwayTime": {  
        "type": "Property",  
        "value": 5  
    },  
    "dateObservedTo": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2018-08-07T11:15:00Z"  
        }  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "LineString",  
            "coordinates": [  
                [  
                    -4.73735395519672,  
                    41.6538181849672  
                ],  
                [  
                    -4.73414858659993,  
                    41.6600594193478  
                ],  
                [  
                    -4.73447575302641,  
                    41.659585195093  
                ]  
            ]  
        }  
    },  
    "congested": {  
        "type": "Property",  
        "value": false  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
