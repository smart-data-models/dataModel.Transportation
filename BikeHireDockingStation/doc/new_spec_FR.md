Entité : BikeHireDockingStation  
===============================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Station d'accueil pour la location de vélos**  

## Liste des biens  

`address`: L'adresse postale.  `alternateName`: Un autre nom pour cet article  `areaServed`: La zone géographique où un service ou un article offert est fourni.  `availableBikeNumber`:   `contactPoint`:   `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  `description`: Une description de cet article  `freeSlotNumber`:   `id`:   `location`:   `name`: Le nom de cet article.  `openingHours`:   `outOfServiceSlotNumber`:   `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  `provider`:   `seeAlso`:   `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  `status`:   `totalSlotNumber`:   `type`: NGSI Type d'entité  ## Modèle de données description des biens  
Classement par ordre alphabétique  
```yaml  
BikeHireDockingStation:    
  description: 'Bike Hire Docking Station'    
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
    availableBikeNumber:    
      minimum: 0    
      type: integer    
    contactPoint:    
      type: object    
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
    freeSlotNumber:    
      minimum: 0    
      type: integer    
    id:    
      anyOf: &bikehiredockingstation_-_properties_-_owner_-_items_-_anyof    
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
    openingHours:    
      type: string    
    outOfServiceSlotNumber:    
      minimum: 0    
      type: integer    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *bikehiredockingstation_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    provider:    
      type: object    
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
    status:    
      enum:    
        - working    
        - outOfService    
        - withIncidence    
        - full    
        - almostFull    
        - empty    
        - almostEmpty    
      type: string    
    totalSlotNumber:    
      minimum: 1    
      type: integer    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - BikeHireDockingStation    
      type: string    
  required:    
    - id    
    - type    
  type: object    
```  
Voici un exemple de BikeHireDockingStation au format JSON comme valeurs clés. Elle est compatible avec NGSI V2 lorsqu'elle utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
        "id": "Bcn-BikeHireDockingStation-1",  
        "type": "BikeHireDockingStation",  
        "address": {  
            "addressCountry": "ES",  
            "addressLocality": "Barcelona",  
            "streetAddress": "Gran Via Corts Catalanes,760"  
        },  
        "availableBikeNumber": 20,  
        "freeSlotNumber": 10,  
        "location": {  
            "type": "Point",  
            "coordinates": [  
                2.180042,  
                41.397952  
            ]  
        },  
        "status": "working"  
}  
```  
Voici un exemple de BikeHireDockingStation au format JSON tel que normalisé. Elle est compatible avec NGSI V2 lorsqu'elle utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",   
    "status": {  
        "value": "working"  
    },   
    "availableBikeNumber": {  
        "value": 20,  
        "metadata": {  
            "timestamp": {  
                "type": "DateTime",  
                "value": "2018-09-25T12:00:00"  
            }  
        }  
    },   
    "freeSlotNumber": {  
        "value": 10  
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
    }  
}  
```  
Voici un exemple de BikeHireDockingStation au format JSON-LD comme valeurs clés. Elle est compatible avec le format NGSI-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "ES",  
             "addressLocality": "Barcelona",  
             "streetAddress": "Gran Via Corts Catalanes,760",  
             "type": "PostalAddress"},  
 "availableBikeNumber": 20,  
 "freeSlotNumber": 10,  
 "id": "urn:ngsi-ld:BikeHireDockingStation:Bcn-BikeHireDockingStation-1",  
 "location": {"coordinates": [2.180042, 41.397952], "type": "Point"},  
 "status": "working",  
 "type": "BikeHireDockingStation"}  
```  
Voici un exemple de BikeHireDockingStation au format JSON-LD tel que normalisé. Elle est compatible avec le format NGSI-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:BikeHireDockingStation:Bcn-BikeHireDockingStation-1",  
    "type": "BikeHireDockingStation",  
    "status": {  
        "type": "Property",  
        "value": "working"  
    },  
    "availableBikeNumber": {  
        "type": "Property",  
        "value": 20,  
        "observedAt": "2018-09-25T12:00:00Z"  
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
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "ES",  
            "addressLocality": "Barcelona",  
            "streetAddress": "Gran Via Corts Catalanes,760",  
            "type": "PostalAddress"  
        }  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
