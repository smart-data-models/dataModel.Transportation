Entité : BikeHireDockingStation  
===============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md)  
Description globale : **Station d'accueil pour la location de vélos**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `availableBikeNumber`: Le nombre de vélos disponibles dans la station d'accueil pour la location de vélos à louer par les utilisateurs  - `contactPoint`: Point de contact du service de location de vélos  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `freeSlotNumber`: Le nombre de places disponibles pour le retour et le stationnement des vélos. Il doit être inférieur ou égal à "totalSlotNumber".  - `id`: Identifiant unique de l'entité  - `location`:   - `name`: Le nom de cet article.  - `openingHours`: Heures d'ouverture de la station d'accueil  - `outOfServiceSlotNumber`: Le nombre de créneaux horaires qui sont hors service et qui ne peuvent pas être utilisés pour louer ou garer un vélo. Il doit être inférieur ou égal à "totalSlotNumber".  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `provider`: Prestataire de services de location de vélos  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `status`: Statut de la station d'accueil pour la location de vélos. Enum : "en fonctionnement, hors service, avec incidence, plein, presque plein, vide, presque vide". Ou toute autre application spécifique.  - `totalSlotNumber`: Le nombre total de places offertes par cette station d'accueil pour vélos  - `type`: Type d'entité NGSI. Il doit s'agir de BikeHireDockingStation    
Propriétés requises  
- `id`  - `type`    
De nombreuses villes proposent aux citoyens un système de location de vélos. Ceux-ci peuvent louer une base de vélos sur différents types d'abonnements. Une station de location de vélos où les utilisateurs abonnés peuvent louer et rendre un vélo. Elle fournit des données sur ses principales caractéristiques et sur la disponibilité des vélos et des emplacements libres.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BikeHireDockingStation:    
  description: 'Bike Hire Docking Station'    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    availableBikeNumber:    
      description: 'The number of bikes available in the bike hire docking station to be hired by users'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    contactPoint:    
      description: 'Bike hire service contact point'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/contactPoint    
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
      description: 'The number of slots available for returning and parking bikes. It must lower or equal than `totalSlotNumber`'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
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
    openingHours:    
      description: 'Opening hours of the docking station'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/openingHours.    
    outOfServiceSlotNumber:    
      description: 'The number of slots that are out of order and cannot be used to hire or park a bike. It must lower or equal than `totalSlotNumber`'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *bikehiredockingstation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    provider:    
      description: 'Bike hire service provider'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/provider.    
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
    status:    
      description: 'Status of the bike hire docking station. Enum:''working, outOfService, withIncidence, full, almostFull, empty, almostEmpty''. Or any other application specific.'    
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
        model: https://schema.org/Number    
    totalSlotNumber:    
      description: 'The total number of slots offered by this bike docking station'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number.    
    type:    
      description: 'NGSI Entity type. It has to be BikeHireDockingStation'    
      enum:    
        - BikeHireDockingStation    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### BikeHireDockingStation NGSI V2 Exemple de valeurs clés  
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
#### BikeHireDockingStation NGSI V2 normalisé Exemple  
Voici un exemple de BikeHireDockingStation au format JSON tel que normalisé. Elle est compatible avec NGSI V2 lorsqu'elle n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### BikeHireDockingStation NGSI-LD Exemple de valeurs clés  
Voici un exemple de BikeHireDockingStation au format JSON-LD comme valeurs clés. Elle est compatible avec le format NGSI-LD lorsqu'elle utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### BikeHireDockingStation NGSI-LD normalisé Exemple  
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
