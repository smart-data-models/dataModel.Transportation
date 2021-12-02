Entité : TrafficFlowObserved  
============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/TrafficFlowObserved/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Observation des conditions de circulation à un endroit et à un moment donnés**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `averageGapDistance`: Distance moyenne entre deux véhicules consécutifs  - `averageHeadwayTime`: Temps de passage moyen. Le temps de passage est le temps écoulé entre deux véhicules consécutifs.  - `averageVehicleLength`: Longueur moyenne des véhicules transitant pendant  
    la période d'observation  - `averageVehicleSpeed`: Vitesse moyenne des véhicules transitant pendant la période d'observation  - `congested`:  Indique s'il y a eu une congestion du trafic pendant la période d'observation dans la voie concernée. L'absence de cet attribut signifie qu'il n'y a pas eu d'embouteillage.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `dateObserved`: La date et l'heure de cette observation au format ISO8601 UTC. Elle peut être représentée par un instant précis ou par un intervalle ISO8601. Pour pallier l'absence de prise en charge des intervalles de temps par Orion Context Broker, il est possible d'utiliser deux attributs distincts : `dateObservedFrom`, `dateObservedTo`. Il peut s'agir de [DateTime](https://schema.org/DateTime) ou d'un intervalle ISO8601 représenté par [Text](https://schema.org/Text).  - `dateObservedFrom`: Date et heure de début de la période d'observation. Voir `dateObserved`.  - `dateObservedTo`: Date et heure de fin de la période d'observation. Voir `dateObserved`.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `intensity`: Nombre total de véhicules détectés pendant cette période d'observation  - `laneDirection`: Sens habituel de déplacement dans la voie visée par cette observation. Cet attribut est utile lorsque l'observation ne fait référence à aucun segment de route, permettant de connaître le sens de déplacement du flux de trafic observé. Enum:forward, backward'. Voir RoadSegment pour une description de la sémantique de ces valeurs.  - `laneId`: Identification des voies. L'identification des voies est effectuée à l'aide des conventions définies par l'entité RoadSegment qui sont basées sur [OpenStreetMap] (http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `occupancy`: Fraction du temps d'observation où un véhicule a occupé la voie observée  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refRoadSegment`: Segment de route concerné sur lequel l'observation a été faite. Référence à une entité de type RoadSegment  - `reversedLane`: Indique si la circulation dans la voie a été inversée pendant la période d'observation. L'absence de cet attribut signifie qu'il n'y a pas eu d'inversion de la voie.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit s'agir de TrafficFlowObserved.  - `vehicleSubType`: Il permet de spécifier un sous-type de `vehicleType`, par exemple si le `vehicleType` est défini sur `Lorry`, le `vehicleSubType` peut être `OGV1` ou `OGV2` pour donner plus d'informations sur le type exact de véhicule.  - `vehicleType`: Type de véhicule du point de vue de ses caractéristiques structurelles. Enum : 'agriculturalVehicle, bicycle, bus, minibus, car, caravan, tram, tanker, carWithCaravan, carWithTrailer, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, trailer, van, constructionOrMaintenanceVehicle, trolley, binTrolley, sweepingMachine, cleaningTrolley'.    
Propriétés requises  
- `dateObserved`  - `id`  - `type`    
Cette entité est principalement associée aux segments verticaux de l'automobile et de la ville intelligente et aux applications IoT connexes.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TrafficFlowObserved:    
  description: 'An observation of traffic flow conditions at a certain place and time.'    
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
    averageGapDistance:    
      description: 'Average gap distance between consecutive vehicles'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'meter (m)'    
    averageHeadwayTime:    
      description: 'Average headway time. Headway time is the time ellapsed between two consecutive vehicles'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'second (s)'    
    averageVehicleLength:    
      description: |-    
        Average length of the vehicles transiting during    
            the observation period    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'meter (m)'    
    averageVehicleSpeed:    
      description: 'Average speed of the vehicles transiting during the observation period'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'Kilometer per hour (Km/h)'    
    congested:    
      description: ' Flags whether there was a traffic congestion during the observation period in the referred lane. The absence of this attribute means no traffic congestion'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean.    
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
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval. As a workaround for the lack of support of Orion Context Broker for datetime intervals, it can be used two separate attributes: `dateObservedFrom`, `dateObservedTo`. [DateTime](https://schema.org/DateTime) or an ISO8601 interval represented as [Text](https://schema.org/Text)'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime.    
    dateObservedFrom:    
      description: 'Observation period start date and time. See `dateObserved`'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Datetime.    
    dateObservedTo:    
      description: 'Observation period end date and time. See `dateObserved`'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Datetime.    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &trafficflowobserved_-_properties_-_owner_-_items_-_anyof    
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
    intensity:    
      description: 'Total number of vehicles detected during this observation period'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    laneDirection:    
      description: 'Usual direction of travel in the lane referred by this observation. This attribute is useful when the observation is not referencing any road segment, allowing to know the direction of travel of the traffic flow observed. Enum:forward, backward''. See RoadSegment for a description of the semantics of these values.'    
      enum:    
        - forward    
        - backward    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    laneId:    
      description: 'Lane identifier. Lane identification is done using the conventions defined by RoadSegment entity which are based on [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Forward_%26_backward,_left_%26_right).'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    occupancy:    
      description: 'Fraction of the observation time where a vehicle has been occupying the observed lane'    
      maximum: 1    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *trafficflowobserved_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refRoadSegment:    
      description: 'Concerned road segment on which the observation has been made. Reference to an entity of type RoadSegment'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    reversedLane:    
      description: 'Flags whether traffic in the lane was reversed during the observation period. The absence of this attribute means no lane reversion'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Boolean.    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be TrafficFlowObserved'    
      enum:    
        - TrafficFlowObserved    
      type: Property    
    vehicleSubType:    
      description: 'It allows to specify a sub type of `vehicleType`, eg if the `vehicleType` is set to `Lorry` the `vehicleSubType` may be `OGV1` or `OGV2` to convey more information about the exact type of vehicle.'    
      type: Property    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. Enum:''agriculturalVehicle, bicycle, bus, minibus, car, caravan, tram, tanker, carWithCaravan, carWithTrailer, lorry, moped, motorcycle, motorcycleWithSideCar, motorscooter, trailer, van, constructionOrMaintenanceVehicle, trolley, binTrolley, sweepingMachine, cleaningTrolley'''    
      enum:    
        - agriculturalVehicle    
        - bicycle    
        - bus    
        - minibus    
        - car    
        - caravan    
        - tram    
        - tanker    
        - carWithCaravan    
        - carWithTrailer    
        - lorry    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - trailer    
        - van    
        - constructionOrMaintenanceVehicle    
        - trolley    
        - binTrolley    
        - sweepingMachine    
        - cleaningTrolley    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
  required:    
    - id    
    - type    
    - dateObserved    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### TrafficFlowObserved Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'un TrafficFlowObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "laneId": 1,  
  "address": {  
    "streetAddress": "Avenida de Salamanca",  
    "addressLocality": "Valladolid",  
    "addressCountry": "ES"  
  },  
  "location": {  
    "type": "LineString",  
    "coordinates": [  
      [-4.73735395519672, 41.6538181849672],  
      [-4.73414858659993, 41.6600594193478],  
      [-4.73447575302641, 41.659585195093]  
    ]  
  },  
  "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",  
  "dateObservedFrom": "2016-12-07T11:10:00Z",  
  "dateObservedTo": "2016-12-07T11:15:00Z",  
  "averageHeadwayTime": 0.5,  
  "intensity": 197,  
  "occupancy": 0.76,  
  "averageVehicleSpeed": 52.6,  
  "averageVehicleLength": 9.87,  
  "reversedLane": false,  
  "laneDirection": "forward"  
}  
```  
#### TrafficFlowObserved Exemple normalisé NGSI-v2  
Voici un exemple d'un TrafficFlowObserved au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "dateObserved": {  
    "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
  },  
  "laneDirection": {  
    "value": "forward"  
  },  
  "dateObservedFrom": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:10:00Z"  
  },  
  "averageVehicleLength": {  
    "value": 9.87  
  },  
  "averageHeadwayTime": {  
    "value": 0.5  
  },  
  "occupancy": {  
    "value": 0.76  
  },  
  "reversedLane": {  
    "value": false  
  },  
  "dateObservedTo": {  
    "type": "DateTime",  
    "value": "2016-12-07T11:15:00Z"  
  },  
  "intensity": {  
    "value": 197  
  },  
  "laneId": {  
    "value": 1  
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
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES",  
      "streetAddress": "Avenida de Salamanca"  
    }  
  },  
  "averageVehicleSpeed": {  
    "value": 52.6  
  }  
}  
```  
#### TrafficFlowObserved Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un TrafficFlowObserved au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
  "type": "TrafficFlowObserved",  
  "dateObserved": {  
    "type": "Property",  
    "value": "2016-12-07T11:10:00/2016-12-07T11:15:00"  
  },  
  "laneDirection": {  
    "type": "Property",  
    "value": "forward"  
  },  
  "dateObservedFrom": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-07T11:10:00Z"  
    }  
  },  
  "averageVehicleLength": {  
    "type": "Property",  
    "value": 9.87  
  },  
  "averageHeadwayTime": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "occupancy": {  
    "type": "Property",  
    "value": 0.76  
  },  
  "reversedLane": {  
    "type": "Property",  
    "value": false  
  },  
  "dateObservedTo": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-12-07T11:15:00Z"  
    }  
  },  
  "intensity": {  
    "type": "Property",  
    "value": 197  
  },  
  "laneId": {  
    "type": "Property",  
    "value": 1  
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
  "address": {  
    "type": "Property",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "ES",  
      "streetAddress": "Avenida de Salamanca",  
      "type": "PostalAddress"  
    }  
  },  
  "averageVehicleSpeed": {  
    "type": "Property",  
    "value": 52.6  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### TrafficFlowObserved NGSI-LD normalisé Exemple  
Voici un exemple d'un TrafficFlowObserved au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Valladolid",  
    "streetAddress": "Avenida de Salamanca",  
    "type": "PostalAddress"  
  },  
  "averageHeadwayTime": 0.5,  
  "averageVehicleLength": 9.87,  
  "averageVehicleSpeed": 52.6,  
  "dateObserved": "2016-12-07T11:10:00/2016-12-07T11:15:00",  
  "dateObservedFrom": {  
    "@type": "DateTime",  
    "@value": "2016-12-07T11:10:00Z"  
  },  
  "dateObservedTo": {  
    "@type": "DateTime",  
    "@value": "2016-12-07T11:15:00Z"  
  },  
  "id": "urn:ngsi-ld:TrafficFlowObserved:TrafficFlowObserved-Valladolid-osm-60821110",  
  "intensity": 197,  
  "laneDirection": "forward",  
  "laneId": 1,  
  "location": {  
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
    ],  
    "type": "LineString"  
  },  
  "occupancy": 0.76,  
  "reversedLane": false,  
  "type": "TrafficFlowObserved"  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude