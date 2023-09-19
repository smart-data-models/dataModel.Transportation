<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : RoadSegment  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/RoadSegment/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité contient une description géographique et contextuelle harmonisée d'un segment de route. Un ensemble de segments de route est utilisé pour décrire une route**.  
version : 0.4.1  
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
- `agency_name[string]`: Le champ agency_name contient le nom complet de l'agence ou de l'organisation responsable de la maintenance de l'entité considérée. Identique : champ 'agency_name' de GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)  - `allowedVehicleType[array]`: Type(s) de véhicule(s) autorisé(s) à transiter par ce segment de route. Enum : "véhicule agricole, bicyclette, bus, voiture, caravane, voiture avec caravane, voiture avec remorque, véhicule de construction ou de maintenance, camion, cyclomoteur, motocyclette, motocyclette avec side-car, scooter, camion-citerne, remorque, camionnette, tout véhicule". Valeurs autorisées : Les valeurs suivantes définies par _VehicleTypeEnum_, [DATEX 2 version 2.3] (http://d2docs.ndwcloud.nu/) :  . Model: [https://schema.org/Text](https://schema.org/Text)- `alternateName[string]`: Un nom alternatif pour ce poste  - `annotations[array]`: Annotations sur l'article  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `bridgeCount[number]`: Nombre de ponts dans le segment de route correspondant à cette observation. Prend 0 (zéro) comme valeur lorsque le segment de route n'a pas de ponts.  - `carriagewayLength[number]`: Longueur totale de la chaussée du segment de route correspondant à cette observation  - `carriagewayWidth[number]`: Largeur totale de la chaussée du segment de route correspondant à cette observation  - `category[array]`: Permet de transmettre des caractéristiques supplémentaires d'un segment de route. Enum : "oneway, toll, link".  `oneway` : Indique si le segment de route ne peut être utilisé que dans une seule direction. S'il n'est pas présent, cela signifie que le segment de route peut être utilisé dans les deux sens (vers l'avant et vers l'arrière). Voir aussi [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Indique si le segment de route est soumis à des droits de péage. `link` : Indique si ce segment de route est un segment de liaison auxiliaire pour sortir ou entrer dans une route. Voir [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Toute autre valeur significative pour une application  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: La couleur du produit  . Model: [https://schema.org/color](https://schema.org/color)- `culvertCount[number]`: Nombre de ponceaux présents dans le tracé de la route correspondant à cette observation  - `cyclePathLeftHeight[number]`: Hauteur de la piste cyclable sur le bord gauche de la route correspondant à cette observation  - `cyclePathLeftWidth[number]`: Largeur de la piste cyclable sur le bord gauche de la route correspondant à cette observation  - `cyclePathMaterial[string]`: Matériaux de construction utilisés pour la mise en place de la piste cyclable sur les côtés de la route correspondant à cette observation  - `cyclePathPlacement[string]`: Décrit l'emplacement de la piste cyclable le long du segment de route correspondant à cette observation. Enum:' ['DROITE, GAUCHE, LES DEUX, NOT_AVAILABLE'  - `cyclePathRightHeight[number]`: Hauteur de la piste cyclable sur le bord droit de la route correspondant à cette observation  - `cyclePathRightWidth[number]`: Largeur de la piste cyclable sur le bord droit de la route correspondant à cette observation  - `dataDescriptor[*]`: URI pointant vers l'entité descripteur de données  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `endKilometer[number]`: Le numéro de kilomètre (mesuré à partir du point de départ de la route) où ce segment de route se termine.  . Model: [https://schema.org/Number](https://schema.org/Number)- `endPoint[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `id[*]`: Identifiant unique de l'entité  - `image[uri]`: Une image de l'objet  . Model: [https://schema.org/URL](https://schema.org/URL)- `laneInfo[object]`: Décrit les aspects des voies de la route correspondant à cette observation  	- `laneDirection[string]`: Décrit la direction dans laquelle les véhicules circulent sur la voie correspondant à cette observation. Enum : "AVANT, ARRIÈRE, ENTRANT, SORTIE, DROITE, GAUCHE".    
- `laneUsage[array]`: Cet attribut peut être utilisé pour transmettre des paramètres spécifiques décrivant chaque voie. Il doit contenir une chaîne de caractères par segment de route. L'élément 0 du tableau doit contenir les informations relatives à la voie 1, et ainsi de suite. Le format de la chaîne référencée doit être le suivant : <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> est une chaîne de texte dont les valeurs autorisées sont les suivantes : `forward`. La voie est actuellement utilisée dans le sens "vers l'avant". `backward`. Le couloir est actuellement utilisé dans le sens `backward`. Le seul paramètre obligatoire est `lane_direction`. S'il n'est pas spécifié, les autres paramètres peuvent être considérés comme égaux à ceux spécifiés au niveau de l'entité.  . Model: [https://schema.org/Text](https://schema.org/Text)- `length[number]`: Longueur totale de ce segment de route en kilomètres  . Model: [https://schema.org/length](https://schema.org/length)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `maximumAllowedHeight[number]`: Hauteur maximale autorisée pour les véhicules transitant par ce segment de route  . Model: [https://schema.org/height](https://schema.org/height)- `maximumAllowedSpeed[number]`: Vitesse maximale autorisée sur le segment de route. Des limites plus restrictives peuvent être appliquées à certains types de véhicules (camions, caravanes, etc.).  . Model: [https://schema.org/Number](https://schema.org/Number)- `maximumAllowedWeight[number]`: Poids maximal autorisé pour les véhicules transitant par ce segment de route  . Model: [https://schema.org/weight](https://schema.org/weight)- `maximumAllowedWidth[number]`: Largeur maximale autorisée pour les véhicules utilisant l'entité correspondant à cette observation  - `medianHeight[number]`: Hauteur du terre-plein ou du terre-plein central de la route correspondant à cette observation  - `medianLength[number]`: Longueur du terre-plein ou du terre-plein central de la route correspondant à cette observation  - `medianWidth[number]`: Largeur du terre-plein ou du terre-plein central de la route correspondant à cette observation  - `minimumAllowedSpeed[number]`: Vitesse minimale autorisée en traversant ce segment de route  . Model: [https://schema.org/Number](https://schema.org/Number)- `municipalityInfo[object]`: Informations sur la municipalité correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)	- `cityId[string]`: ID de la ville correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `cityName[string]`: Nom de la ville correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `district[string]`: Nom du district correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `stateName[string]`: Nom de l'État correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `ulbName[string]`: Nom de la collectivité locale urbaine correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardId[string]`: ID de l'unité correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardName[string]`: Nom du service correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
	- `wardNum[number]`: Numéro du service correspondant à cette observation  . Model: [https://schema.org/Number](https://schema.org/Number)  
	- `zoneId[string]`: ID de la zone correspondant à cette observation  . Model: [https://schema.org/Text](https://schema.org/Text)  
- `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `pedestrianPathLeftHeight[number]`: Hauteur de la passerelle placée sur le bord gauche de la route correspondant à cette observation  - `pedestrianPathLeftWidth[number]`: Largeur de la passerelle placée sur le bord gauche de la route correspondant à cette observation  - `pedestrianPathMaterial[string]`: Matériau de construction utilisé pour la mise en place de la passerelle / du sentier sur les côtés de la route correspondant à cette observation  - `pedestrianPathPlacement[string]`: Décrit la présence et l'emplacement du piéton le long du segment de route correspondant à cette observation. Enum : "DROITE, GAUCHE, LES DEUX, NOT_AVAILABLE  - `pedestrianPathRightHeight[number]`: Hauteur de la passerelle placée sur le bord droit de la route correspondant à cette observation  - `pedestrianPathRightWidth[number]`: Largeur de la passerelle placée sur le bord droit de la route correspondant à cette observation  - `refRoad[*]`: Route à laquelle appartient ce segment de route  - `rightOfWayWidth[number]`: L'emprise est la surface totale disponible pour la route. Sa largeur permet d'accueillir le passage des voitures + d'autres nécessités + une extension future, le long du tracé de la route.  - `roadClass[string]`: Type de route correspondant à cette observation. Enum : [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD]  - `roadDirection[string]`: Représente la direction vers laquelle la route se dirige. Enum:' ['N, S, E, W'. Les valeurs N, S, E, W représentent respectivement le nord, le sud, l'est et l'ouest.  - `roadId[string]`: Représentation interne unique de la route correspondant à cette observation  - `roadMaterial[string]`: Le matériau de construction utilisé pour la pose de la chaussée correspondant à cette observation. Par exemple, béton, terre, goudron, etc.  - `roadName[string]`: Le nom de la route correspondant à cette observation  - `roadWork[string]`: Raisons des travaux routiers en cas d'intervention urgente. Une combinaison de ces valeurs. Enum : 'COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK' (effondrement, déraillement, incendie, inondation, fuite de gaz, glissement de terrain, autre)  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `startKilometer[number]`: Le numéro de kilomètre (mesuré à partir du point de départ de la route) où commence ce segment de route.  . Model: [https://schema.org/Number](https://schema.org/Number)- `startPoint[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `status[string]`: Conditions de conduite spécifiques sur le segment de route. Utilisez statusDescription pour obtenir des informations supplémentaires. Enum : "open, closed, limited".  `open` : le segment de route peut être utilisé dans sa pleine capacité prévue, `closed` : aucune circulation n'est possible, par exemple en raison de travaux routiers, d'un pont ou d'une écluse ouverts, ou de tout autre événement empêchant la circulation. `limité` : le trafic est possible, mais pas dans toute sa capacité.  - `statusDescription[string]`: Informations complémentaires à l'attribut status  - `totalCyclePathWidth[number]`: Largeur totale de la piste cyclable présente dans la route correspondant à cette observation  - `totalLaneNumber[number]`: Nombre total de voies offertes par ce segment de route  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalPedestrianPathLength[number]`: Longueur totale de la passerelle présente dans la route correspondant à cette observation  - `totalPedestrianPathWidth[number]`: Largeur totale de la passerelle présente dans la route correspondant à cette observation  - `type[string]`: Type d'entité NGSI. Il doit s'agir de RoadSegment  - `width[number]`: Largeur du segment de route.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `allowedVehicleType`  - `endPoint`  - `id`  - `name`  - `refRoad`  - `startPoint`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Les segments de route peuvent comprendre plusieurs voies. Ce modèle de données permet de transmettre des segments de route composés de voies hétérogènes (différentes en termes d'utilisation, de vitesse, de hauteur, etc.) Les voies sont identifiées par des nombres entiers compris entre 1 et n, le numéro 1 étant la voie de droite en marche avant. La direction vers l'avant est la direction indiquée par le vecteur qui va du point de départ du segment au point d'arrivée du segment. Il s'agit de la même convention que celle utilisée par OpenStreetMap. Cette entité est principalement associée aux segments verticaux de l'automobile et de la ville intelligente et aux applications IdO connexes. Ce modèle de données a été développé en coopération avec les opérateurs de téléphonie mobile et la GSMA.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoadSegment:    
  description: This entity contains a harmonised geographic and contextual description of a road segment. A collection of road segments are used to describe a Road.    
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
    agency_name:    
      description: "The agency_name field contains the full name of the agency or organisation responsible for maintenance of the entity under consideration. SameAs: 'agency_name' field from GTFS Static Field Definition - agency.txt (https://developers.google.com/transit/gtfs/reference#agencytxt)"    
      type: string    
      x-ngsi:    
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
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: Annotations about the item    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bridgeCount:    
      description: Number of bridges in the road segment corresponding to this observation. Takes 0 (zero) as the value when the road segment has no bridges    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayLength:    
      description: Total length of the carriage way of the road segment corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    carriagewayWidth:    
      description: Total width of the carriage way of the road segment corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    category:    
      description: 'Allows to convey extra characteristics of a road segment. Enum:''oneway, toll, link''.  `oneway`: Flags whether the road segment can only be used in one direction. If not present it means road segment can be used in both directions (forwards and backwards). See also [http://wiki.openstreetmap.org/wiki/Key:oneway](http://wiki.openstreetmap.org/wiki/Key:oneway). `toll` : Flags whether the road segment is under toll fees. `link` : Flags whether this road segment is an auxiliary link segment for exiting or entering a road. See [https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_link). Any other value meaningful to an application'    
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
      description: The color of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    culvertCount:    
      description: Number of culverts prevalent in the trace of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftHeight:    
      description: Height of the cycle track on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathLeftWidth:    
      description: Width of the cycle track on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathMaterial:    
      description: Construction material used for laying the cycle path on the sides of the road corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathPlacement:    
      description: 'Describes the placement of cycle track along the road segment corresponding to this observation. Enum:'' [''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      enum:    
        - BOTH    
        - LEFT    
        - NOT_AVAILABLE    
        - RIGHT    
      type: string    
      x-ngsi:    
        type: Property    
    cyclePathRightHeight:    
      description: Height of the cycle track on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    cyclePathRightWidth:    
      description: Width of the cycle track on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    dataDescriptor:    
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
      description: URI pointing to the data-descriptor entity    
      x-ngsi:    
        type: Relationship    
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
    endKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment ends. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    endPoint:    
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
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    laneInfo:    
      description: Describes the aspects of lanes of the road corresponding to this observation    
      properties:    
        laneDirection:    
          description: 'Describes the direction in which vehicles are plying on the lane corresponding to this observation. Enum:''FORWARD, BACKWARD, INBOUND, OUTBOUND, RIGHT, LEFT'''    
          enum:    
            - BACKWARD    
            - FORWARD    
            - INBOUND    
            - LEFT    
            - OUTBOUND    
            - RIGHT    
          laneLength:    
            description: Length of the lane corresponding to this observation    
            type: number    
            x-ngsi:    
              type: Property    
          laneWidth:    
            description: Width of the lane corresponding to this observation    
            type: number    
            x-ngsi:    
              type: Property    
          type: string    
          x-ngsi:    
            type: Property    
        laneId:    
          description: Unique identification number of the lane corresponding to this observation    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    laneUsage:    
      description: 'This attribute can be used to convey specific parameters describing each lane. It must contain a string per road segment lane. The element 0 of the array must contain the information of lane 1, and so on. Format of the referred string must be: <lane_direction>, <lane_minimumAllowedSpeed>, <lane_maximumAllowedSpeed>, <lane_maximumAllowedHeight>, <lane_maximumAllowedWeight>. <lane_direction> is a text string with the following allowed values: `forward`. The lane is currently used in the `forwards` direction. `backward`. The lane is currently used in the `backwards` direction. The only mandatory parameter is `lane_direction`. If not specified, the rest of parameters can be assumed to be equal to those specified at entity level'    
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
      description: Total length of this road segment in kilometers    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: Kilometer (Km)    
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
    maximumAllowedHeight:    
      description: Maximum allowed height for vehicles transiting this road segment    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/height    
        type: Property    
        units: Meter (m)    
    maximumAllowedSpeed:    
      description: 'Maximum allowed speed plying the road segment. More restrictive limits might be applied to specific vehicle types (trucks, caravans, etc.)'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilometer per hour (Km/h)    
    maximumAllowedWeight:    
      description: Maximum allowed weight for vehicles transiting this road segment    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weight    
        type: Property    
        units: Kilogram (Kg)    
    maximumAllowedWidth:    
      description: Maximum allowed width for vehicles using the entity corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    medianHeight:    
      description: Height of the median or central reservation in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    medianLength:    
      description: Length of the median or central reservation in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    medianWidth:    
      description: Width of the median or central reservation in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    minimumAllowedSpeed:    
      description: Minimum allowed speed while transiting this road segment    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilometer per hour (Km/h)    
    municipalityInfo:    
      description: Municipality information corresponding to this observation    
      properties:    
        cityId:    
          description: City ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        cityName:    
          description: City name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        district:    
          description: District name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        stateName:    
          description: Name of the state corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        ulbName:    
          description: Name of the Urban Local Body corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardId:    
          description: Ward ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardName:    
          description: Ward name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        wardNum:    
          description: Ward number corresponding to this observation    
          type: number    
          x-ngsi:    
            model: https://schema.org/Number    
            type: Property    
        zoneId:    
          description: Zone ID corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
        zoneName:    
          description: Zone name corresponding to this observation    
          type: string    
          x-ngsi:    
            model: https://schema.org/Text    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    pedestrianPathLeftHeight:    
      description: Height of the walkway placed on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathLeftWidth:    
      description: Width of the walkway placed on the left edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathMaterial:    
      description: Construction material used for laying the walkway / footpath on the sides of the road corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathPlacement:    
      description: 'Describes the presence and placement of pedestrian along the road segment corresponding to this observation. Enum:''RIGHT, LEFT, BOTH, NOT_AVAILABLE'''    
      type: string    
      x-ngsi:    
        type: Property    
    pedestrianPathRightHeight:    
      description: Height of the walkway placed on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    pedestrianPathRightWidth:    
      description: Width of the walkway placed on the right edge of the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    refRoad:    
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
      description: Road to which this road segment belongs to    
      x-ngsi:    
        type: Relationship    
    rightOfWayWidth:    
      description: 'Right of Way (RoW) is the total land area available for the roadway. Its width accommodates for carriages way + other necessities + future extension, along the road''s alignment'    
      type: number    
      x-ngsi:    
        type: Property    
    roadClass:    
      description: 'The type of road corresponding to this observation. Enum: [OTHER_PUBLIC_ROAD, PRIVATE_ROAD, MINOR_CITY_ROAD, MAJOR_DISTRICT_ROAD, MAJOR_CITY_ROAD, NATIONAL_HIGHWAY, SERVICE_ROAD, STATE_HIGHWAY, OTHER_DISTRICT_ROAD, PORT_ROAD]'    
      enum:    
        - MAJOR_DISTRICT_ROAD    
        - MAJOR_CITY_ROAD    
        - MINOR_CITY_ROAD    
        - NATIONAL_HIGHWAY    
        - OTHER_DISTRICT_ROAD    
        - OTHER_PUBLIC_ROAD    
        - PORT_ROAD    
        - PRIVATE_ROAD    
        - SERVICE_ROAD    
        - STATE_HIGHWAY    
      type: string    
      x-ngsi:    
        type: Property    
    roadDirection:    
      description: 'Represents the direction the road is heading to. Enum:'' [''N, S, E, W''. The values N,S,E,W represent North,South,East,West respectively'    
      type: string    
      x-ngsi:    
        type: Property    
    roadId:    
      description: Unique internal representation of the road corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    roadMaterial:    
      description: 'The construction material used for laying the carriageway corresponding to this observation. For eg. concrete, earthen, tar etc'    
      type: string    
      x-ngsi:    
        type: Property    
    roadName:    
      description: The name of the road corresponding to this observation    
      type: string    
      x-ngsi:    
        type: Property    
    roadWork:    
      description: 'Reasons for the road work in case of urgent intervention. A combination of these values. Enum:''COLLAPSE, DERAILMENT, FIRE, FLOOD, GASLEAK, LANDSLIDE, OTHER, POWERCUT, ROCKFALL, SAGGING, WATERLEAK'''    
      enum:    
        - COLLAPSE    
        - DERAILMENT    
        - FIRE    
        - FLOOD    
        - GASLEAK    
        - LANDSLIDE    
        - OTHER    
        - POWERCUT    
        - ROCKFALL    
        - SAGGING    
        - WATERLEAK    
      type: string    
      x-ngsi:    
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
    startKilometer:    
      description: 'The kilometer number (measured from the road''s start point) where this road segment starts. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    startPoint:    
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
    status:    
      description: 'Specific driving conditions on the roadsegment. Use statusDescription for additional information. Enum: ‘open, closed, limited’.  `open`: the roadsegment can be used in full intended capacity, `closed`: no traffic is possible, e.g. due to roadworks, an open bridge or lock, or any other event preventing traffic. `limited`: traffic is possible, but not in the full capacity'    
      items:    
        enum:    
          - open    
          - closed    
          - limited    
        type: string    
      type: string    
      x-ngsi:    
        type: Property    
    statusDescription:    
      description: Additional information to the status attribute    
      type: string    
      x-ngsi:    
        type: Property    
    totalCyclePathWidth:    
      description: Total width of the cycle track present in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    totalLaneNumber:    
      description: Total number of lanes offered by this road segment    
      minimum: 1    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    totalPedestrianPathLength:    
      description: Total length of the walkway present in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    totalPedestrianPathWidth:    
      description: Total width of the walkway present in the road corresponding to this observation    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be RoadSegment    
      enum:    
        - RoadSegment    
      type: string    
      x-ngsi:    
        type: Property    
    width:    
      description: Road's segment width.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Meter (m)    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/RoadSegment/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/RoadSegment/schema.json    
  x-model-tags: IUDX    
  x-version: 0.4.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
Les propriétés `laneUsage` et celles qui véhiculent les paramètres maximums autorisés peuvent être dynamiques, par exemple, la direction d'une voie peut être temporairement modifiée pour améliorer les conditions de circulation.  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### RoadSegment Valeurs clés NGSI-v2 Exemple  
Voici un exemple de RoadSegment au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "name": "Valladolid-Dueñas",  
  "category": [  
    "oneway"  
  ],  
  "refRoad": "Spain-Road-A62",  
  "totalLaneNumber": 2,  
  "maximumAllowedSpeed": 120,  
  "minimumAllowedSpeed": 60,  
  "startPoint": {  
    "type": "Point",  
    "coordinates": [  
      -4.7299180606009,  
      41.6844918725019  
    ]  
  },  
  "endPoint": {  
    "type": "Point",  
    "coordinates": [  
      -4.55167335377909,  
      41.8570461783071  
    ]  
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
  },  
  "laneUsage": [  
    "forward",  
    "forward"  
  ],  
  "source": "http://wwww.openstreetmap.org",  
  "status": "open",  
  "statusDescription": "Bridge state = DOWN",  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": 0.095454461114818,  
  "totalPedestrianPathWidth": 7,  
  "bridgeCount": 1,  
  "pedestrianPathLeftHeight": 2,  
  "maximumAllowedHeight": 72,  
  "totalPedestrianPathLength": 0.09,  
  "culvertCount": 0,  
  "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
  "roadClass": "OTHER_PUBLIC_ROAD",  
  "medianHeight": 3.6,  
  "roadWork": "OTHER",  
  "roadID": "5272",  
  "cyclePathRightWidth": 2.5,  
  "roadMaterial": "TAR",  
  "medianWidth": 1.5,  
  "carriagewayWidth": 3,  
  "cyclePathRightHeight": 1,  
  "roadDirection": "N",  
  "medianLength": 0.09,  
  "pedestrianPathMaterial": "PAVEMENT BLOCK",  
  "cyclePathLeftWidth": 2.5,  
  "maximumAllowedWidth": 74,  
  "rightOfWayWidth": 4,  
  "cyclePathLeftHeight": 1,  
  "maximumAllowedWeight": 109,  
  "pedestrianPathRightWidth": 3.5,  
  "pedestrianPathLeftWidth": 3.5,  
  "pedestrianPathPlacement": "NOT_AVAILABLE",  
  "pedestrianPathRightHeight": 2,  
  "cyclePathPlacement": "NOT_AVAILABLE",  
  "totalCyclePathWidth": 5,  
  "agency_name": "CORPORATION",  
  "municipalityInfo": {  
    "ulbName": "KANNUR MUNICIPAL CORPORATION"  
  }  
}  
```  
</details>  
#### RoadSegment NGSI-v2 normalisé Exemple  
Voici un exemple de RoadSegment au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Spain-RoadSegment-A62-osm-24702186",  
  "type": "RoadSegment",  
  "category": {  
    "value": [  
      "oneway"  
    ]  
  },  
  "endPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.55167335377909,  
        41.8570461783071  
      ]  
    }  
  },  
  "name": {  
    "value": "Valladolid-Dueñas"  
  },  
  "startPoint": {  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -4.7299180606009,  
        41.6844918725019  
      ]  
    }  
  },  
  "allowedVehicleType": {  
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
    "value": [  
      "forward",  
      "forward"  
    ]  
  },  
  "status": {  
    "value": "open"  
  },  
  "statusDescription": {  
    "value": "Bridge state = DOWN"  
  },  
  "cyclePathMaterial": "ASPHALT",  
  "carriagewayLength": {  
    "type": "number",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "number",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "number",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "number",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "number",  
    "value": 0  
  },  
  "roadName": {  
    "type": "string",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "string",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "number",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "string",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "string",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "string",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "number",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "number",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "string",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "number",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "string",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "number",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "number",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "number",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "number",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "number",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "number",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "number",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "string",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "number",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "string",  
    "value": "CORPORATION"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  }  
}  
```  
</details>  
#### RoadSegment Valeurs clés NGSI-LD Exemple  
Voici un exemple de RoadSegment au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
    "type": "RoadSegment",  
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
    "status": "open",  
    "statusDescription": "Bridge state = DOWN",  
    "cyclePathMaterial": "ASPHALT",  
    "carriagewayLength": 0.095454461114818,  
    "totalPedestrianPathWidth": 7,  
    "bridgeCount": 1,  
    "pedestrianPathLeftHeight": 2,  
    "maximumAllowedHeight": 72,  
    "totalPedestrianPathLength": 0.09,  
    "culvertCount": 0,  
    "roadName": "GREEN VILLA ROAD TO CHAITHRAM HOUSE",  
    "roadClass": "OTHER_PUBLIC_ROAD",  
    "medianHeight": 3.6,  
    "roadWork": "OTHER",  
    "roadID": "5272",  
    "cyclePathRightWidth": 2.5,  
    "roadMaterial": "TAR",  
    "medianWidth": 1.5,  
    "carriagewayWidth": 3,  
    "cyclePathRightHeight": 1,  
    "roadDirection": "N",  
    "medianLength": 0.09,  
    "pedestrianPathMaterial": "PAVEMENT BLOCK",  
    "cyclePathLeftWidth": 2.5,  
    "maximumAllowedWidth": 74,  
    "rightOfWayWidth": 4,  
    "cyclePathLeftHeight": 1,  
    "maximumAllowedWeight": 109,  
    "pedestrianPathRightWidth": 3.5,  
    "pedestrianPathLeftWidth": 3.5,  
    "pedestrianPathPlacement": "NOT_AVAILABLE",  
    "pedestrianPathRightHeight": 2,  
    "cyclePathPlacement": "NOT_AVAILABLE",  
    "totalCyclePathWidth": 5,  
    "agency_name": "CORPORATION",  
    "municipalityInfo": {  
        "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RoadSegment NGSI-LD normalisé Exemple  
Voici un exemple d'un RoadSegment au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "urn:ngsi-ld:RoadSegment:Spain-RoadSegment-A62-osm-24702186",  
	"type": "RoadSegment",  
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
	"laneUsage": {  
		"type": "Property",  
		"value": [  
			"forward",  
			"forward"  
		]  
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
	"maximumAllowedSpeed": {  
		"type": "Property",  
		"value": 120  
	},  
	"minimumAllowedSpeed": {  
		"type": "Property",  
		"value": 60  
	},  
	"name": {  
		"type": "Property",  
		"value": "Valladolid-DueÃ±as"  
	},  
	"refRoad": {  
		"type": "Relationship",  
		"object": "urn:ngsi-ld:Road:Spain-Road-A62"  
	},  
	"source": {  
		"type": "Property",  
		"value": "http://wwww.openstreetmap.org"  
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
	"totalLaneNumber": {  
		"type": "Property",  
		"value": 2  
	},  
	"status": {  
		"type": "Property",  
		"value": "open"  
	},  
	"statusDescription": {  
		"type": "Property",  
		"value": "Bridge state = DOWN"  
	},  
	"carriagewayLength": {  
    "type": "Property",  
    "value": 0.095454461114818  
  },  
  "totalPedestrianPathWidth": {  
    "type": "Property",  
    "value": 7  
  },  
  "bridgeCount": {  
    "type": "Property",  
    "value": 1  
  },  
  "pedestrianPathLeftHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "maximumAllowedHeight": {  
    "type": "Property",  
    "value": 72  
  },  
  "totalPedestrianPathLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "culvertCount": {  
    "type": "Property",  
    "value": 0  
  },  
  "roadName": {  
    "type": "Property",  
    "value": "GREEN VILLA ROAD TO CHAITHRAM HOUSE"  
  },  
  "roadClass": {  
    "type": "Property",  
    "value": "OTHER_PUBLIC_ROAD"  
  },  
  "medianHeight": {  
    "type": "Property",  
    "value": 3.6  
  },  
  "roadWork": {  
    "type": "Property",  
    "value": "OTHER"  
  },  
  "roadID": {  
    "type": "Property",  
    "value": "5272"  
  },  
  "cyclePathRightWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "roadMaterial": {  
    "type": "Property",  
    "value": "TAR"  
  },  
  "medianWidth": {  
    "type": "Property",  
    "value": 1.5  
  },  
  "carriagewayWidth": {  
    "type": "Property",  
    "value": 3  
  },  
  "cyclePathRightHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "roadDirection": {  
    "type": "Property",  
    "value": "N"  
  },  
  "medianLength": {  
    "type": "Property",  
    "value": 0.09  
  },  
  "pedestrianPathMaterial": {  
    "type": "Property",  
    "value": "PAVEMENT BLOCK"  
  },  
  "cyclePathLeftWidth": {  
    "type": "Property",  
    "value": 2.5  
  },  
  "maximumAllowedWidth": {  
    "type": "Property",  
    "value": 74  
  },  
  "rightOfWayWidth": {  
    "type": "Property",  
    "value": 4  
  },  
  "cyclePathLeftHeight": {  
    "type": "Property",  
    "value": 1  
  },  
  "maximumAllowedWeight": {  
    "type": "Property",  
    "value": 109  
  },  
  "pedestrianPathRightWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathLeftWidth": {  
    "type": "Property",  
    "value": 3.5  
  },  
  "pedestrianPathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "pedestrianPathRightHeight": {  
    "type": "Property",  
    "value": 2  
  },  
  "cyclePathPlacement": {  
    "type": "Property",  
    "value": "NOT_AVAILABLE"  
  },  
  "totalCyclePathWidth": {  
    "type": "Property",  
    "value": 5  
  },  
  "agency_name": {  
    "type": "Property",  
    "value": "CORPORATION"  
  },  
 "municipalityInfo": {  
    "type": "Property",  
    "value": {  
      "ulbName": "KANNUR MUNICIPAL CORPORATION"  
    }  
  },  
	"@context": [  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
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
