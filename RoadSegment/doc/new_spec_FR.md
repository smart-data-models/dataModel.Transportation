Entité : RoadSegment  
====================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **Cette entité contient une description géographique et contextuelle harmonisée d'un segment de route. Une collection de segments de route est utilisée pour décrire une route. Les segments de route peuvent comprendre plusieurs voies. Ce modèle de données permet de transmettre des segments de route composés de voies hétérogènes (différentes par leur usage, leur vitesse, leur hauteur, etc.). Les voies sont identifiées en utilisant des nombres entiers entre 1 et n, le numéro 1 étant la voie de droite lorsque l'on avance. Le sens de marche avant est la direction indiquée par le vecteur qui va du point de départ du segment au point d'arrivée du segment. C'est la même convention que celle utilisée par OpenStreetMap. Cette entité est principalement associée aux segments verticaux Automotive et Smart City et aux applications IoT qui s'y rapportent. Ce modèle de données a été développé en coopération avec les opérateurs de téléphonie mobile et la GSMA.**  

## Liste des biens  

- `address`: L'adresse postale.  - `allowedVehicleType`:   - `alternateName`: Un autre nom pour cet article  - `annotations`:   - `areaServed`: La zone géographique où un service ou un article offert est fourni.  - `category`:   - `color`: La couleur du produit.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `endKilometer`:   - `endPoint`:   - `id`:   - `image`: Une image de l'objet.  - `laneUsage`:   - `length`:   - `location`:   - `maximumAllowedHeight`:   - `maximumAllowedSpeed`:   - `maximumAllowedWeight`:   - `minimumAllowedSpeed`:   - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refRoad`:   - `seeAlso`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `startKilometer`:   - `startPoint`:   - `totalLaneNumber`:   - `type`: NGSI Type d'entité  - `width`:   ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road. Road segments can include several lanes. This data model allows to convey road segments made up of heterogeneous lanes (different in their usage, speed, height, etc.). Lanes are identified by using integer numbers between 1 and n, being number 1 the lane to the right when going forwards. The forward direction is the direction denoted by the vector which goes from the segment"s start point to the segment"s end point. This is the same convention as the one used by OpenStreetMap. This entity is primarily associated with the Automotive and Smart City vertical segments and related IoT applications. This data model has been developed in cooperation with mobile operators and the GSMA.'    
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
    allowedVehicleType:    
      items:    
        enum:    
          - agriculturalVehicle    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - carWithCaravan    
          - carWithTrailer    
          - constructionOrMaintenanceVehicle    
          - lorry    
          - moped    
          - motorcycle    
          - motorcycleWithSideCar    
          - motorscooter    
          - tanker    
          - trailer    
          - van    
          - anyVehicle    
        type: string    
      type: array    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      items:    
        type: string    
      type: array    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    category:    
      enum:    
        - oneway    
        - toll    
        - link    
      type: string    
    color:    
      description: 'The color of the product.'    
      type: string    
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
    endKilometer:    
      minimum: 0    
      type: number    
    endPoint:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: &roadsegment_-_properties_-_location_-_oneof    
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
    id:    
      anyOf: &roadsegment_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      description: 'An image of the item.'    
      format: uri    
      type: string    
    laneUsage:    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: array    
    length:    
      minimum: 0    
      type: number    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    maximumAllowedHeight:    
      minimum: 0    
      type: number    
    maximumAllowedSpeed:    
      minimum: 0    
      type: number    
    maximumAllowedWeight:    
      minimum: 0    
      type: number    
    minimumAllowedSpeed:    
      minimum: 0    
      type: number    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    refRoad:    
      anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
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
    startKilometer:    
      minimum: 0    
      type: number    
    startPoint:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    totalLaneNumber:    
      minimum: 1    
      type: number    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - RoadSegment    
      type: string    
    width:    
      minimum: 0    
      type: number    
  required:    
    - id    
    - name    
    - type    
    - refRoad    
    - startPoint    
    - endPoint    
    - allowedVehicleType    
    - totalLaneNumber    
    - laneUsage    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### RoadSegment NGSI V2 valeurs clés Exemple  
Voici un exemple de RoadSegment en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": "oneway",  
  "refRoad": "Spain-Road-A62",  
  "totalLaneNumber": 2,  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "startPoint": {  
    "type": "Point",  
    "coordinates": [-4.7299180606009, 41.6844918725019]  
  },  
  "endPoint": {  
    "type": "Point",  
    "coordinates": [-4.55167335377909, 41.8570461783071]  
  },  
  "allowedVehicleType": [  
    "car",  
    "bus",  
    "lorry",  
    "trailer",  
    "tanker",  
    "van",  
    "caravan"  
  ],  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.7299180606009, 41.6844918725019],  
      [-4.72855890957602, 41.6860596957855],  
      [-4.5520357341647, 41.8569278186523],  
      [-4.55167335377909, 41.8570461783071]  
    ]  
  },  
  "laneUsage": ["forward", "forward"],  
  "source": "http://wwww.openstreetmap.org"  
}  
```  
#### RoadSegment NGSI V2 normalisé Exemple  
Voici un exemple de RoadSegment au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il utilise "options=valeurs clés" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": "oneway"  
  },  
  "endPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.55167335377909, 41.8570461783071]  
    }  
  },  
  "name": {  
    "value": "Valladolid-Due\u00f1as"  
  },  
  "startPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.7299180606009, 41.6844918725019]  
    }  
  },  
  "allowedVehicleType": {  
    "value": ["car", "bus", "lorry", "trailer", "tanker", "van", "caravan"]  
  },  
  "source": {  
    "value": "http://wwww.openstreetmap.org"  
  },  
  "totalLaneNumber": {  
    "value": 2  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "LineString",  
      "coordinates": [  
        [-4.7299180606009, 41.6844918725019],  
        [-4.72855890957602, 41.6860596957855],  
        [-4.5520357341647, 41.8569278186523],  
        [-4.55167335377909, 41.8570461783071]  
      ]  
    }  
  },  
  "minimumAllowedSpeed": {  
    "value": 60  
  },  
  "refRoad": {  
    "type": "Relationship",  
    "value": "Spain-Road-A62"  
  },  
  "maximumAllowedSpeed": {  
    "value": 120  
  },  
  "laneUsage": {  
    "value": ["forward", "forward"]  
  }  
}  
```  
#### RoadSegment NGSI-LD key-values Exemple  
Voici un exemple de RoadSegment en format JSON-LD comme valeurs clés. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "allowedVehicleType": ["car",  
                        "bus",  
                        "lorry",  
                        "trailer",  
                        "tanker",  
                        "van",  
                        "caravan"],  
 "category": "oneway",  
 "endPoint": {"coordinates": [-4.55167335377909, 41.8570461783071],  
              "type": "Point"},  
 "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
 "laneUsage": ["forward", "forward"],  
 "location": {"coordinates": [[-4.7299180606009, 41.6844918725019],  
                              [-4.72855890957602, 41.6860596957855],  
                              [-4.5520357341647, 41.8569278186523],  
                              [-4.55167335377909, 41.8570461783071]],  
              "type": "LineString"},  
 "maximumAllowedSpeed": 120,  
 "minimumAllowedSpeed": 60,  
 "name": "Valladolid-DueÃ±as",  
 "refRoad": "urn:ngsi-ld:Road:Spain-Road-A62",  
 "source": "http://wwww.openstreetmap.org",  
 "startPoint": {"coordinates": [-4.7299180606009, 41.6844918725019],  
                "type": "Point"},  
 "totalLaneNumber": 2,  
 "type": "RoadSegment"}  
```  
#### RoadSegment NGSI-LD normalisé Exemple  
Voici un exemple de RoadSegment au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
    "type": "RoadSegment",  
    "category": {  
        "type": "Property",  
        "value": "oneway"  
    },  
    "endPoint": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -4.55167335377909,  
                41.8570461783071  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "Valladolid-DueÃ±as"  
    },  
    "startPoint": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -4.7299180606009,  
                41.6844918725019  
            ]  
        }  
    },  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": [  
            "car",  
            "bus",  
            "lorry",  
            "trailer",  
            "tanker",  
            "van",  
            "caravan"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": "http://wwww.openstreetmap.org"  
    },  
    "totalLaneNumber": {  
        "type": "Property",  
        "value": 2  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "LineString",  
            "coordinates": [  
                [  
                    -4.7299180606009,  
                    41.6844918725019  
                ],  
                [  
                    -4.72855890957602,  
                    41.6860596957855  
                ],  
                [  
                    -4.5520357341647,  
                    41.8569278186523  
                ],  
                [  
                    -4.55167335377909,  
                    41.8570461783071  
                ]  
            ]  
        }  
    },  
    "minimumAllowedSpeed": {  
        "type": "Property",  
        "value": 60  
    },  
    "refRoad": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Road:Spain-Road-A62"  
    },  
    "maximumAllowedSpeed": {  
        "type": "Property",  
        "value": 120  
    },  
    "laneUsage": {  
        "type": "Property",  
        "value": [  
            "forward",  
            "forward"  
        ]  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
