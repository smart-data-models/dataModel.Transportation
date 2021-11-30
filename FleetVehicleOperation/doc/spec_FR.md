Entité : FleetVehicleOperation  
==============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/FleetVehicleOperation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'une opération générique de véhicule de flotte telle qu'une livraison, ou une collecte postale. Cette entité est principalement associée au segment vertical du transport et de la logistique, mais peut également être utilisée dans de nombreuses autres applications IdO connexes**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `endedAt`: La date et l'heure de fin de l'événement, lorsque l'événement ou l'opération est connu comme étant terminé/complété. Nul/omis si l'événement n'est pas encore terminé.  - `fleetVehicle`: Référence à l'entité FleetVehicle à laquelle cette opération se rapporte.  - `fleetVehicleOperation`: Référence à l'entité FleetVehicleOperation à laquelle se rapporte cette entité d'état.  - `id`: Identifiant unique de l'entité  - `initiatingLocation`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `operationType`: Le type de texte libre de l'événement ou de l'opération, par exemple : appel pour le transport d'un patient, collecte postale, livraison, proximité d'une zone interdite, survitesse.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `responseTime`: Indique le délai de réponse à un événement, en secondes. L'horodatage observéAt associé indique quand la dernière mise à jour a été enregistrée. Par exemple, enregistre le temps de réponse d'une ambulance pour atteindre un patient.  - `result`: Le résultat final de l'événement ou de l'opération.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startedAt`: La date et l'heure de début du déclenchement de l'événement ou de l'opération.  - `transportTime`: Indique le temps que le véhicule de la flotte a passé à transporter des personnes ou des fournitures pour l'opération en cours. Par exemple, indique le temps qu'une ambulance a passé à transporter un patient vers le service des urgences d'un hôpital.  - `type`: Identifiant de l'entité NGSI. Il doit être FleetVehicleOperation.    
Propriétés requises  
- `id`  - `type`    
Ce modèle de données est issu du projet original GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Il y a quelques adaptations mineures pour répondre aux exigences des modèles de données intelligents.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
FleetVehicleOperation:    
  description: 'This entity contains a harmonised description of a generic fleet vehicle operation such as a delivery, or a postal collection. This entity is primarily associated with the vertical segment of the transport and logistics but may also be used many other related IoT applications.'    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
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
    endedAt:    
      description: 'The end date and time of the event when the event or operation is known to be over/complete. Null/omitted if not yet ended.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    fleetVehicle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicle entity to which this operation relates.'    
      x-ngsi:    
        type: Relationship    
    fleetVehicleOperation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the FleetVehicleOperation entity to which this status entity relates.'    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &fleetvehicleoperation_-_properties_-_owner_-_items_-_anyof    
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
    initiatingLocation:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: &fleetvehicleoperation_-_properties_-_location_-_oneof    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf: *fleetvehicleoperation_-_properties_-_location_-_oneof    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'The free text type of the event or operation e.g. e.g. Call for a patient transportation, postal collection, delivery, close to a restricted area, overspeed.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *fleetvehicleoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    responseTime:    
      description: 'Indicates the time to respond to an event, in seconds. The associated observedAt timestamp indicates when the last update was recorded. E.g. records the response time for an ambulance to reach to a patient'    
      type: number    
      x-ngsi:    
        type: Property    
        units: seconds    
    result:    
      description: 'The final result of the event or operation.'    
      type: string    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startedAt:    
      description: 'The start date and time when the event or operation was triggered.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    transportTime:    
      description: 'Indicates the time that the fleet vehicle has spent transporting people or supplies for the current operation. E.g. indicates the time an ambulance spent transporting a patient to a hospital emergency department.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be FleetVehicleOperation'    
      enum:    
        - FleetVehicleOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/FleetVehicleOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### FleetVehicleOperation Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'une FleetVehicleOperation au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleStatus": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286",  
  "initiatingLocation": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "Patient transportation",  
  "description": "An emergency transportation of a 3 year old boy",  
  "result": "Completed",  
  "responseTime": 2500,  
  "transportTime": 1220  
}  
```  
#### FleetVehicleOperation NGSI-v2 normalisée Exemple  
Voici un exemple d'une FleetVehicleOperation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleStatus": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286"  
  },  
  "initiatingLocation": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "@value": "2016-08-28T10:18:16Z"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "Patient transportation"  
  },  
  "description": {  
    "type": "Text",  
    "value": "An emergency transportation of a 3 year old boy"  
  },  
  "result": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "responseTime": {  
    "type": "Number",  
    "value": 2500  
  },  
  "transportTime": {  
    "type": "Number",  
    "value": 1220  
  }  
}  
```  
#### FleetVehicleOperation Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'une FleetVehicleOperation au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "fleetVehicle": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f",  
  "fleetVehicleStatus": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286",  
  "initiatingLocation": {  
    "type": "Point",  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ]  
  },  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "Patient transportation",  
  "description": "An emergency transportation of a 3 year old boy",  
  "result": "Completed",  
  "responseTime": 2500,  
  "transportTime": 1220  
}  
```  
#### FleetVehicleOperation NGSI-LD normalisé Exemple  
Voici un exemple d'une FleetVehicleOperation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Transportation/FleetVehicleOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:FleetVehicleOperation:8e876a60-5aa3-11e8-b350-d7b51a09fb6c",  
  "type": "FleetVehicleOperation",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "fleetVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicle:84c6a3a8-5aa6-11e8-bedc-27e105edd16f"  
  },  
  "fleetVehicleStatus": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:FleetVehicleStatus:0284e0dc-5aa4-11e8-97e6-2351fc70c286"  
  },  
  "initiatingLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "startedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "endedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "operationType": {  
    "type": "Property",  
    "value": "Patient transportation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "An emergency transportation of a 3 year old boy"  
  },  
  "result": {  
    "type": "Property",  
    "value": "Completed"  
  },  
  "responseTime": {  
    "type": "Property",  
    "value": 2500,  
    "unitCode": "SEC",  
    "observedAt": "2016-08-28T10:18:16Z"  
  },  
  "transportTime": {  
    "type": "Property",  
    "value": 1220,  
    "unitCode": "SEC",  
    "observedAt": "2016-08-28T10:18:16Z"  
  }  
}  
```  
