Entité : BikeHireDockingStation  
===============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Transportation/blob/master/BikeHireDockingStation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Station d'accueil pour la location de vélos**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `availableBikeNumber`: Le nombre de vélos disponibles dans la station d'accueil pour être loués par les utilisateurs.  - `contactPoint`: Point de contact du service de location de vélos  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `freeSlotNumber`: Le nombre d'emplacements disponibles pour le retour et le stationnement des vélos. Il doit être inférieur ou égal à `totalSlotNumber`.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `openingHours`: Heures d'ouverture de la station d'accueil  - `outOfServiceSlotNumber`: Le nombre d'emplacements qui sont hors service et qui ne peuvent pas être utilisés pour louer ou garer un vélo. Il doit être inférieur ou égal à `totalSlotNumber`.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `provider`: Fournisseur de services de location de vélos  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `status`: Statut de la station d'accueil de location de vélos. Enum : "en service, hors service, avec incident, plein, presque plein, vide, presque vide". Ou toute autre application spécifique.  - `totalSlotNumber`: Le nombre total d'emplacements offerts par cette station d'accueil pour vélos.  - `type`: Type d'entité NGSI. Il doit s'agir de BikeHireDockingStation.    
Propriétés requises  
- `id`  - `type`    
De nombreuses villes proposent un système de location de vélos aux citoyens. Ceux-ci peuvent louer un vélo sur la base de différents types d'abonnements. Une station d'accueil où les utilisateurs abonnés peuvent louer et rendre un vélo. Elle fournit des données sur ses principales caractéristiques et sur la disponibilité des vélos et des créneaux libres.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BikeHireDockingStation:    
  description: 'Bike Hire Docking Station'    
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
#### BikeHireDockingStation Exemple de valeurs clés NGSI-v2  
Voici un exemple de BikeHireDockingStation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### BikeHireDockingStation NGSI-v2 normalisée Exemple  
Voici un exemple de BikeHireDockingStation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### BikeHireDockingStation Valeurs-clés NGSI-LD Exemple  
Voici un exemple de BikeHireDockingStation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BikeHireDockingStation NGSI-LD normalisé Exemple  
Voici un exemple de BikeHireDockingStation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address": {  
    "addressCountry": "ES",  
    "addressLocality": "Barcelona",  
    "streetAddress": "Gran Via Corts Catalanes,760",  
    "type": "PostalAddress"  
  },  
  "availableBikeNumber": 20,  
  "freeSlotNumber": 10,  
  "id": "urn:ngsi-ld:BikeHireDockingStation:Bcn-BikeHireDockingStation-1",  
  "location": {  
    "coordinates": [  
      2.180042,  
      41.397952  
    ],  
    "type": "Point"  
  },  
  "status": "working",  
  "type": "BikeHireDockingStation"  
}  
```  
