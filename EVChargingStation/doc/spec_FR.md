Entité : EVChargingStation  
==========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Transportation/blob/master/EVChargingStation/LICENSE.md)  
Description globale : **EV Station de recharge**  

## Liste des biens  

- `acceptedPaymentMethod`: Type(s) de charge lors de l'utilisation de cette station. Enumération : "ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm  - `address`: L'adresse postale.  - `allowedVehicleType`: Type(s) de véhicule(s) qui peuvent être facturés. Enum : "bicyclette, bus, voiture, caravane, moto, scooter, camion".  - `alternateName`: Un autre nom pour cet article  - `amperage`: L'ampérage total offert par la station de recharge.  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `availableCapacity`: Le nombre de véhicules qui peuvent actuellement être facturés. Il doit être inférieur ou égal à la "capacité".  - `capacity`: Le nombre total de véhicules qui peuvent être facturés en même temps. Le nombre total de prises peut être supérieur.  - `chargeType`: Type(s) de charge lors de l'utilisation de cette station. Enumération : "paiement annuel, forfaitaire, gratuit, paiement mensuel, autre".  - `contactPoint`: Point de contact de la station de recharge  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `network`: Le nom du réseau, avec lequel l'opérateur coopère.  - `openingHours`: Heures d'ouverture de la station de recharge.  - `operator`: Opérateur de la station de recharge.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `socketNumber`: Le nombre total de prises offertes par cette station de recharge  - `socketType`: Le type de prises offertes par cette station. Enum : "Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, Other, Tesla, Type2, Type3, Wall_Euro".  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `status`: Statut de la station de recharge. Enum : "presque vide, presque plein, vide, plein, hors service, avec incidence, en fonctionnement". Ou toute autre application spécifique.  - `type`: Type d'entité NGSI. Il doit s'agir de EVChargingStation  - `voltage`: La tension totale offerte par la station de recharge    
Propriétés requises  
- `allowedVehicleType`  - `capacity`  - `id`  - `name`  - `socketType`  - `type`    
Une station de recharge publique qui fournit de l'énergie aux véhicules électriques. Le temps de charge dépend de la puissance maximale de la station, du nombre de véhicules en cours de charge et du niveau actuel de la batterie.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EVChargingStation:    
  description: 'EV Charging Station'    
  properties:    
    acceptedPaymentMethod:    
      description: 'Type(s) of charge when using this station. Enum:''ByBankTransferInAdvance, ByInvoice, Cash, CheckInAdvance, COD, DirectDebit, GoogleCheckout, PayPal, PaySwarm'''    
      items:    
        enum:    
          - ByBankTransferInAdvance    
          - ByInvoice    
          - Cash    
          - CheckInAdvance    
          - COD    
          - DirectDebit    
          - GoogleCheckout    
          - PayPal    
          - PaySwarm    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Vehicle type(s) which can be charged. Enum:''bicycle, bus, car, caravan, motorcycle, motorscooter, truck'' '    
      items:    
        enum:    
          - bicycle    
          - bus    
          - car    
          - caravan    
          - motorcycle    
          - motorscooter    
          - truck    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    amperage:    
      description: 'The total amperage offered by the charging station.'    
      exclusiveMinimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Ampers (A)'    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    availableCapacity:    
      description: 'The number of vehicles which currently can be charged. It must lower or equal than `capacity`.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    capacity:    
      description: 'The total number of vehicles which can be charged at the same time. The total number of sockets can be higher. '    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    chargeType:    
      description: 'Type(s) of charge when using this station. Enum:''annualPayment, flat, free, monthlyPayment, other'''    
      items:    
        enum:    
          - annualPayment    
          - flat    
          - free    
          - monthlyPayment    
          - other    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: https://schema.org/Text    
    contactPoint:    
      description: 'Charging station contact point'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/contactPoint.    
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
      anyOf: &evchargingstation_-_properties_-_owner_-_items_-_anyof    
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
    network:    
      anyOf:    
        - format: uri    
          type: string    
        - type: string    
      description: 'The name of the Network, with that the operator cooperates. '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    openingHours:    
      description: 'Opening hours of the charging station. '    
      type: Property    
      x-ngsi:    
        model: http://schema.org/openingHours    
    operator:    
      anyOf:    
        - format: uri    
          type: string    
        - type: string    
      description: 'Charging station''s operator. '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *evchargingstation_-_properties_-_owner_-_items_-_anyof    
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
    socketNumber:    
      description: 'The total number of sockets offered by this charging station'    
      minimum: 1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number.    
    socketType:    
      description: 'The type of sockets offered by this station. Enum:''Caravan_Mains_Socket, CHAdeMO, CCS/SAE, Dual_CHAdeMO, Dual_J-1772, Dual_Mennekes, J-1772, Mennekes, Other, Tesla, Type2, Type3, Wall_Euro'''    
      items:    
        enum:    
          - Caravan_Mains_Socket    
          - CHAdeMO    
          - CCS/SAE    
          - Dual_CHAdeMO    
          - Dual_J-1772    
          - Dual_Mennekes    
          - J-1772    
          - Mennekes    
          - Other    
          - Tesla    
          - Type2    
          - Type3    
          - Wall_Euro    
        type: string    
      minItems: 1    
      type: Property    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/Text    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    status:    
      description: 'Status of the charging station. Enum:''almostEmpty, almostFull, empty, full, outOfService, withIncidence, working''. Or any other application-specific.'    
      enum:    
        - almostEmpty    
        - almostFull    
        - empty    
        - full    
        - outOfService    
        - withIncidence    
        - working    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    type:    
      description: 'NGSI Entity type. It has to be EVChargingStation'    
      enum:    
        - EVChargingStation    
      type: Property    
    voltage:    
      description: 'The total voltage offered by the charging station'    
      exclusiveMinimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Volts (V)'    
  required:    
    - id    
    - type    
    - name    
    - socketType    
    - capacity    
    - allowedVehicleType    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### EVChargingStation NGSI V2 Exemple de valeurs clés  
Voici un exemple d'une EVChargingStation au format JSON comme valeurs clés. Elle est compatible avec NGSI V2 lorsqu'elle utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "name": "Agencia de Innovación",  
  "location": {  
    "coordinates": [-4.747901, 41.618265],  
    "type": "Point"  
  },  
  "capacity": 2,  
  "socketType": ["Wall_Euro"],  
  "address": {  
    "streetAddress": "Paseo de Zorrilla, 191",  
    "addressLocality": "Valladolid",  
    "addressCountry": "España"  
  },  
  "contactPoint": {  
    "email": "vehiculoelectrico@ava.es"  
  },  
  "operator": "Iberdrola",  
  "allowedVehicleType": ["car"],  
  "chargeType": ["free"],  
  "source": "https://openchargemap.org/"  
}  
```  
#### EVChargingStation NGSI V2 normalisée Exemple  
Voici un exemple d'une EVChargingStation au format JSON normalisé. Elle est compatible avec NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
  "type": "EVChargingStation",  
  "socketType": {  
    "value": ["Wall_Euro"]  
  },  
  "capacity": {  
    "value": 2  
  },  
  "name": {  
    "value": "Agencia de Innovaci\u00f3n"  
  },  
  "allowedVehicleType": {  
    "value": ["car"]  
  },  
  "source": {  
    "value": "https://openchargemap.org/"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-4.747901, 41.618265]  
    }  
  },  
  "chargeType": {  
    "value": ["free"]  
  },  
  "address": {  
    "type": "PostalAddress",  
    "value": {  
      "addressLocality": "Valladolid",  
      "addressCountry": "Espa\u00f1a",  
      "streetAddress": "Paseo de Zorrilla, 191"  
    }  
  },  
  "operator": {  
    "value": "Iberdrola"  
  },  
  "contactPoint": {  
    "value": {  
      "email": "vehiculoelectrico@ava.es"  
    }  
  }  
}  
```  
#### EVChargingStation NGSI-LD Exemple de valeurs clés  
Voici un exemple d'une EVChargingStation au format JSON-LD comme valeurs clés. Elle est compatible avec le format NGSI-LD lorsqu'elle utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address": {"addressCountry": "España",  
             "addressLocality": "Valladolid",  
             "streetAddress": "Paseo de Zorrilla, 191",  
             "type": "PostalAddress"},  
 "allowedVehicleType": ["car"],  
 "capacity": 2,  
 "chargeType": ["free"],  
 "contactPoint": {"email": "vehiculoelectrico@ava.es"},  
 "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
 "location": {"coordinates": [-4.747901, 41.618265], "type": "Point"},  
 "name": "Agencia de Innovación",  
 "operator": "Iberdrola",  
 "socketType": ["Wall_Euro"],  
 "source": "https://openchargemap.org/",  
 "type": "EVChargingStation"}  
```  
#### EVChargingStation NGSI-LD normalisée Exemple  
Voici un exemple d'une EVChargingStation au format JSON-LD, telle que normalisée. Elle est compatible avec le format JSON-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:EVChargingStation:ValladolI+D_Covaresa",  
    "type": "EVChargingStation",  
    "socketType": {  
        "type": "Property",  
        "value": [  
            "Wall_Euro"  
        ]  
    },  
    "capacity": {  
        "type": "Property",  
        "value": 2  
    },  
    "name": {  
        "type": "Property",  
        "value": "Agencia de Innovación"  
    },  
    "allowedVehicleType": {  
        "type": "Property",  
        "value": [  
            "car"  
        ]  
    },  
    "source": {  
        "type": "Property",  
        "value": "https://openchargemap.org/"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -4.747901,  
                41.618265  
            ]  
        }  
    },  
    "chargeType": {  
        "type": "Property",  
        "value": [  
            "free"  
        ]  
    },  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "Valladolid",  
            "addressCountry": "España",  
            "streetAddress": "Paseo de Zorrilla, 191",  
            "type": "PostalAddress"  
        }  
    },  
    "operator": {  
        "type": "Property",  
        "value": "Iberdrola"  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": {  
            "email": "vehiculoelectrico@ava.es"  
        }  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
