Entité : RoadSegment  
====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description géographique et contextuelle harmonisée d'un segment de route. Une collection de segments de route est utilisée pour décrire une route**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `allowedVehicleType`: Type(s) de véhicule(s) autorisé(s) à transiter par ce segment de route. Enum : 'agriculturalVehicle, bicycle, bus, car, caravan, carWithCaravan, carWithTrailer, constructionOrMaintenanceVehicle, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, tanker, trailer, van, anyVehicle'. Valeurs autorisées : Les valeurs suivantes définies par _VehicleTypeEnum_, [DATEX 2 version 2.3] (http://d2docs.ndwcloud.nu/) :  - `alternateName`: Un nom alternatif pour cet élément  - `annotations`: Annotations sur l'élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `category`: Permet de transmettre des caractéristiques supplémentaires d'un segment de route. Enum : 'oneway, toll, link'.  `oneway` : Indique si le segment de route ne peut être utilisé que dans une seule direction. S'il n'est pas présent, cela signifie que le segment de route peut être utilisé dans les deux sens (avant et arrière). Voir aussi [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Indique si le tronçon de route est soumis à un péage. `link` : Indique si ce segment de route est un segment de liaison auxiliaire pour sortir ou entrer dans une route. Voir [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Toute autre valeur significative pour une application.  - `color`: La couleur du produit  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `endKilometer`: Le numéro de kilomètre (mesuré à partir du point de départ de la route) où se termine ce segment de route.  - `endPoint`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `id`: Identifiant unique de l'entité  - `image`: Une image de l'article  - `laneUsage`: Cet attribut peut être utilisé pour transmettre des paramètres spécifiques décrivant chaque voie. Il doit contenir une chaîne de caractères par voie de segment de route. L'élément 0 du tableau doit contenir les informations de la voie 1, et ainsi de suite. Le format de la chaîne référencée doit être : <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> est une chaîne de texte dont les valeurs autorisées sont les suivantes : `forward`. La voie est actuellement utilisée dans la direction `forwards`. `backward`. Le couloir est actuellement utilisé dans le sens "arrière". Le seul paramètre obligatoire est `lane_direction`. S'il n'est pas spécifié, le reste des paramètres peut être supposé être égal à ceux spécifiés au niveau de l'entité.  - `length`: Longueur totale de ce segment de route en kilomètres  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `maximumAllowedHeight`: Hauteur maximale autorisée pour les véhicules transitant par ce segment de route  - `maximumAllowedSpeed`: Vitesse maximale autorisée lors du transit sur ce segment de route. Des limites plus restrictives peuvent être appliquées à certains types de véhicules (camions, caravanes, etc.).  - `maximumAllowedWeight`: Poids maximal autorisé pour les véhicules transitant par ce segment de route  - `minimumAllowedSpeed`: Vitesse minimale autorisée lors du passage sur ce segment de route  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refRoad`: Route à laquelle appartient ce segment de route.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startKilometer`: Le numéro de kilomètre (mesuré à partir du point de départ de la route) où commence ce segment de route.  - `startPoint`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `totalLaneNumber`: Nombre total de voies offertes par ce segment de route  - `type`: Type d'entité NGSI. Il doit s'agir de RoadSegment  - `width`: Largeur du segment de route.    
Propriétés requises  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`    
Les segments de route peuvent comprendre plusieurs voies. Ce modèle de données permet de transmettre des segments de route composés de voies hétérogènes (différentes dans leur utilisation, leur vitesse, leur hauteur, etc.) Les voies sont identifiées à l'aide de nombres entiers compris entre 1 et n, le numéro 1 étant la voie de droite en marche avant. La direction avant est la direction indiquée par le vecteur qui va du point de départ du segment au point d "arrivée du segment. Il s "agit de la même convention que celle utilisée par OpenStreetMap. Cette entité est principalement associée aux segments verticaux de l'automobile et des villes intelligentes, ainsi qu'aux applications IoT connexes. Ce modèle de données a été développé en coopération avec les opérateurs mobiles et la GSMA.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: 'This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.'    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application.'    
      items:    
        enum:    
          - oneway    
          - toll    
          - link    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
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
    endKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment ends. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    endPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &roadsegment_-_properties_-_location_-_oneof    
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
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level.'    
      items:    
        enum:    
          - forward    
          - backward    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    length:    
      description: 'Total length of this road segment in kilometers'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: 'Kilometer (Km)'    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    maximumAllowedHeight:    
      description: 'Maximum allowed height for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
        units: 'Meter (m)'    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed while transiting this road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    maximumAllowedWeight:    
      description: 'Maximum allowed weight for vehicles transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: 'Kilogram (Kg)'    
    minimumAllowedSpeed:    
      description: 'Minimum allowed speed while transiting this road segment'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Kilometer per hour (Km/h)'    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *roadsegment_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      description: 'Road to which this road segment belongs to.'    
      x-ngsi:    
        type: Relationship    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    startPoint:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *roadsegment_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    totalLaneNumber:    
      description: 'Total number of lanes offered by this road segment'    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RoadSegment'    
      enum:    
        - RoadSegment    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: 'Road''s segment width.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Meter (m)'    
  required:    
    - id    
    - name    
    - type    
    - refRoad    
    - startPoint    
    - endPoint    
    - allowedVehicleType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadSegment/schema.json    
  x-model-tags: ""    
  x-version: 0.2.0    
```  
</details>    
Les propriétés `laneUsage` et celles qui indiquent les paramètres maximums autorisés peuvent être dynamiques, par exemple, la direction d'une voie peut être temporairement modifiée pour améliorer les conditions de circulation.  
## Exemples de charges utiles  
#### RoadSegment Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de RoadSegment au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": ["oneway"],  
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
#### RoadSegment NGSI-v2 normalisé Exemple  
Voici un exemple de RoadSegment au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": ["oneway"]  
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
#### RoadSegment Valeurs clés NGSI-LD Exemple  
Voici un exemple de RoadSegment au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "type": "Property",  
    "value": [  
      "oneway"  
    ]  
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
    "value": "Valladolid-Due\u00f1as"  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### RoadSegment NGSI-LD normalisé Exemple  
Voici un exemple de RoadSegment au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "allowedVehicleType": [  
    "car",  
    "bus",  
    "lorry",  
    "trailer",  
    "tanker",  
    "van",  
    "caravan"  
  ],  
  "category": [  
    "oneway"  
  ],  
  "endPoint": {  
    "coordinates": [  
      -4.55167335377909,  
      41.8570461783071  
    ],  
    "type": "Point"  
  },  
  "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
  "laneUsage": [  
    "forward",  
    "forward"  
  ],  
  "location": {  
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
    ],  
    "type": "LineString"  
  },  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "name": "Valladolid-Due\u00f1as",  
  "refRoad": "urn:ngsi-ld:Road:Spain-Road-A62",  
  "source": "http://wwww.openstreetmap.org",  
  "startPoint": {  
    "coordinates": [  
      -4.7299180606009,  
      41.6844918725019  
    ],  
    "type": "Point"  
  },  
  "totalLaneNumber": 2,  
  "type": "RoadSegment"  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude