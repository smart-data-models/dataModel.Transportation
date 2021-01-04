Entité : RoadSegment  
====================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
Description globale : **Cette entité contient une description géographique et contextuelle harmonisée d'un segment de route. Une collection de segments de route est utilisée pour décrire une route.**  

## Liste des biens  

- `address`: L'adresse postale.  - `allowedVehicleType`: Le(s) type(s) de véhicule(s) autorisé(s) à transiter par ce segment de route. Enum : "véhicule agricole, bicyclette, bus, voiture, caravane, voiture avec caravane, voiture avec remorque, véhicule de construction ou d'entretien, camion, cyclomoteur, moto, moto avec side-car, scooter, camion-citerne, remorque, fourgon, tout véhicule". Valeurs autorisées : Les valeurs suivantes définies par _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/) :  - `alternateName`: Un autre nom pour cet article  - `annotations`: Annotations sur le sujet  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `category`: Permet de transmettre les caractéristiques supplémentaires d'un segment de route. Enum : "oneway, toll, link".  "oneway" : Indique si le segment de route ne peut être utilisé que dans un seul sens. S'il n'est pas présent, cela signifie que le segment de route peut être utilisé dans les deux sens (vers l'avant et vers l'arrière). Voir aussi [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). péage" : Indique si le segment de route est soumis à un péage. "link" : indique si ce segment de route est un segment de liaison auxiliaire pour sortir ou entrer dans une route. Voir [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Toute autre valeur significative pour une application.  - `color`: La couleur du produit  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `endKilometer`: Le numéro du kilomètre (mesuré à partir du point de départ de la route) où ce segment de route se termine.  - `endPoint`:   - `id`: Identifiant unique de l'entité  - `image`: Une image de l'objet  - `laneUsage`: Cet attribut peut être utilisé pour transmettre des paramètres spécifiques décrivant chaque voie. Il doit contenir une chaîne par voie de segment de route. L'élément 0 du tableau doit contenir les informations de la voie 1, et ainsi de suite. Le format de la chaîne référencée doit être : <direction_voie>, <vitesse_minimale autorisée de la voie>, <vitesse_maximale autorisée de la voie>, <hauteur_maximale autorisée de la voie>, <poids_maximum autorisé de la voie>. <lane_direction> est une chaîne de texte avec les valeurs autorisées suivantes : `forward`. La voie est actuellement utilisée dans la direction `forward`. en arrière. La voie est actuellement utilisée dans la direction "arrière". Le seul paramètre obligatoire est `lane_direction`. S'il n'est pas spécifié, les autres paramètres peuvent être considérés comme étant égaux à ceux spécifiés au niveau de l'entité.  - `length`: Longueur totale de ce tronçon de route en kilomètres  - `location`:   - `maximumAllowedHeight`: Hauteur maximale autorisée pour les véhicules transitant sur ce segment de route  - `maximumAllowedSpeed`: Vitesse maximale autorisée lors de la traversée de ce segment de route. Des limites plus restrictives pourraient être appliquées à des types de véhicules spécifiques (camions, caravanes, etc.)  - `maximumAllowedWeight`: Poids maximum autorisé pour les véhicules transitant sur ce segment de route  - `minimumAllowedSpeed`: Vitesse minimale autorisée lors du passage sur ce tronçon de route  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refRoad`: Route à laquelle appartient ce tronçon de route.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `startKilometer`: Le numéro du kilomètre (mesuré à partir du point de départ de la route) où commence ce segment de route.  - `startPoint`:   - `totalLaneNumber`: Nombre total de voies offertes par ce segment de route  - `type`: Type d'entité NGSI. Il doit s'agir d'un RoadSegment  - `width`: La largeur du segment de route.    
Propriétés requises  
- `allowedVehicleType`  - `endPoint`  - `id`  - `laneUsage`  - `name`  - `refRoad`  - `startPoint`  - `totalLaneNumber`  - `type`    
Les segments de route peuvent comprendre plusieurs voies. Ce modèle de données permet de transmettre des segments de route composés de voies hétérogènes (différentes par leur utilisation, leur vitesse, leur hauteur, etc.) Les voies sont identifiées par des nombres entiers compris entre 1 et n, le numéro 1 étant la voie de droite lorsque l'on avance. Le sens de marche avant est la direction indiquée par le vecteur qui va du point de départ du segment au point d'arrivée du segment. C'est la même convention que celle utilisée par OpenStreetMap. Cette entité est principalement associée aux segments verticaux Automotive et Smart City et aux applications IoT qui s'y rapportent. Ce modèle de données a été développé en coopération avec les opérateurs de téléphonie mobile et la GSMA.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    allowedVehicleType:    
      description: 'Vehicle type(s) allowed to transit through this road segment. Enum:''agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle''. Allowed values: The following values defined by _VehicleTypeEnum_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/):'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application.'    
      items:    
        enum:    
          - oneway    
          - toll    
          - link    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
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
      description: 'The kilometer number (measured from the road''s start point) where this road segment ends. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      description: 'Unique identifier of the entity'    
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level.'    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    length:    
      description: 'Total length of this road segment in kilometers'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: 'Kilometer (Km)'    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles transiting this road segment'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/height    
        units: 'Meter (m)'    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed while transiting this road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    maximumAllowedWeight:    
      description: 'Maximum allowed weight for vehicles transiting this road segment'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/weight    
        units: 'Kilogram (Kg)'    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refRoad:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Road to which this road segment belongs to. '    
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
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    startPoint:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      title: 'GeoJSON Geometry'    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    type:    
      description: 'NGSI Entity type. It has to be RoadSegment'    
      enum:    
        - RoadSegment    
      type: Property    
    width:    
      description: 'Road''s segment width.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Meter (m)'    
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
Les propriétés "laneUsage" et celles qui transmettent les paramètres maximums autorisés peuvent être dynamiques, par exemple, la direction d'une voie peut être temporairement modifiée pour améliorer les conditions de circulation.  
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
Voici un exemple de RoadSegment au format JSON tel que normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple de RoadSegment en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
