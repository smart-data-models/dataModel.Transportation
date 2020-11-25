Entité : EVChargingStation  
==========================  
Cette spécification est une **version temporelle**. Elle est générée automatiquement à partir des propriétés documentées décrites dans le schema.json condensé dans le fichier `model.yaml`. Un fichier temporaire `nouveau_modèle.yaml` a été créé dans chaque modèle de données pour éviter d'avoir un impact sur les scripts existants. Ainsi, la spécification sera incomplète tant que le fichier schema.json n'est pas mis à jour au nouveau format (documentation des propriétés). Une fois mis à jour, le fichier `model.yaml` (`nouveau_model.yaml`) doit être mis à jour également (automatiquement) . Plus d'informations dans ce [lien](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Tant qu'il s'agit d'un format provisoire, tout [feedback est le bienvenu dans ce formulaire](https://smartdatamodels.org/index.php/submit-an-issue-2/) en choisissant l'option "Feedback sur la nouvelle spécification".  
Description globale : **EV Station de recharge**  

## Liste des biens  

- `acceptedPaymentMethod`:   - `address`: L'adresse postale.  - `allowedVehicleType`:   - `alternateName`: Un autre nom pour cet article  - `amperage`:   - `areaServed`:   - `availableCapacity`:   - `capacity`:   - `chargeType`:   - `contactPoint`:   - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `id`:   - `image`:   - `location`:   - `name`: Le nom de cet article.  - `network`:   - `openingHours`:   - `operator`:   - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`:   - `socketNumber`:   - `socketType`:   - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `status`:   - `type`: NGSI Type d'entité  - `voltage`:   ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EVChargingStation:    
  description: 'EV Charging Station'    
  properties:    
    acceptedPaymentMethod:    
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
      type: array    
      uniqueItems: true    
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
          - bicycle    
          - bus    
          - car    
          - caravan    
          - motorcycle    
          - motorscooter    
          - truck    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    amperage:    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
    areaServed:    
      type: string    
    availableCapacity:    
      minimum: 0    
      type: integer    
    capacity:    
      minimum: 1    
      type: integer    
    chargeType:    
      items:    
        enum:    
          - flat    
          - annualPayment    
          - monthlyPayment    
          - free    
          - other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
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
    image:    
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
    network:    
      anyOf:    
        - format: uri    
          type: string    
        - type: string    
    openingHours:    
      type: string    
    operator:    
      anyOf:    
        - format: uri    
          type: string    
        - type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *evchargingstation_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    socketNumber:    
      minimum: 1    
      type: integer    
    socketType:    
      items:    
        enum:    
          - Type2    
          - CHAdeMO    
          - CCS/SAE    
          - Type3    
          - Tesla    
          - J-1772    
          - Wall_Euro    
          - Caravan_Mains_Socket    
          - Dual_J-1772    
          - Dual_CHAdeMO    
          - Mennekes    
          - Dual_Mennekes    
          - Other    
        type: string    
      minItems: 1    
      type: array    
      uniqueItems: true    
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
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - EVChargingStation    
      type: string    
    voltage:    
      exclusiveMinimum: 0    
      minimum: 0    
      type: number    
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
Voici un exemple d'une EVChargingStation au format JSON normalisé. Elle est compatible avec NGSI V2 lorsqu'elle utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
Voici un exemple d'une EVChargingStation au format JSON-LD comme valeurs clés. Elle est compatible avec le format JSON-LD lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
