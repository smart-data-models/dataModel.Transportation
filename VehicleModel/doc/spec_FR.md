Entité : Modèle de véhicule  
===========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Transportation/blob/master/VehicleModel/LICENSE.md)  
Description globale : **Cette entité modélise un modèle de véhicule particulier, y compris toutes les propriétés qui sont communes à plusieurs instances de véhicules appartenant à ce modèle.  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `annotations`: Annotations sur le sujet  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `brandName`: Marque du véhicule  - `cargoVolume`: Le volume disponible pour le fret ou les bagages. Pour les automobiles, il s'agit généralement du volume du coffre. Si une seule valeur est fournie (tapez Numéro), elle fera référence au volume maximum.  - `color`: La couleur du produit  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `depth`: Profondeur du véhicule  - `description`: Une description de cet article  - `fuelConsumption`: La quantité de carburant consommée pour parcourir une distance ou une durée déterminée avec le véhicule donné (par exemple, litres aux 100 km)  - `fuelType`: Le type de carburant adapté au moteur ou aux moteurs du véhicule. Enum : "autogaz, biodiesel éthanol, cng, diesel, électrique, essence, hybride électrique/diesel, hybride électrique/essence, hydrogène, lpg, essence, essence (sans plomb), essence (avec plomb), autre".  - `height`: Hauteur du véhicule  - `id`: Identifiant unique de l'entité  - `image`: Une image de l'objet  - `location`:   - `manufacturerName`: Nom du constructeur du véhicule  - `modelName`: Nom du modèle du véhicule  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit s'agir d'un modèle de véhicule  - `url`: URL qui fournit une description de ce modèle de véhicule  - `vehicleEngine`: Informations sur le ou les moteurs du véhicule  - `vehicleModelDate`: La date de sortie d'un modèle de véhicule (souvent utilisée pour différencier les versions d'une même marque et d'un même modèle)  - `vehicleType`: Type de véhicule du point de vue de ses caractéristiques structurelles. Il est différent de la catégorie de véhicule . Enum :Véhicule agricole, tout véhicule, véhicule articulé, bicyclette, trolley, autobus, voiture, caravane, voiture ou véhicule léger, voiture avec caravane, voiture avec remorque, chariot de nettoyage, véhicule de construction ou d'entretien, véhicule à quatre roues motrices, véhicule surélevé, camion, minibus, cyclomoteur, moto, motocyclette avec side-car, scooter, balayeuse, camion-citerne, véhicule à trois roues, remorque, tramway, véhicule à deux roues, chariot, fourgon, véhicule sans catalyseur, véhicule avec caravane, véhicule avec remorque, avec plaques d'immatriculation à numéros pairs, avec plaques d'immatriculation à numéros impairs, autres". Les valeurs suivantes définies par _VehicleTypeEnum_ et _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  - `weight`: Poids du véhicule  - `width`: Largeur du véhicule    
Propriétés requises  
- `brandName`  - `id`  - `manufacturerName`  - `modelName`  - `name`  - `type`  - `vehicleType`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
VehicleModel:    
  description: 'This entity models a particular vehicle model, including all properties which are common to multiple vehicle instances belonging to such model.'    
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
    brandName:    
      description: 'Vehicle''s brand name'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/brand.    
    cargoVolume:    
      description: 'The available volume for cargo or luggage. For automobiles, this is usually the trunk volume. If only a single value is provided (type Number) it will refer to the maximum volume.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/cargoVolume    
        units: Liters    
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
    depth:    
      description: 'Vehicle''s depth'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth.    
    description:    
      description: 'A description of this item'    
      type: Property    
    fuelConsumption:    
      description: 'The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/fuelConsumption    
        units: 'liters per 100 kilometer'    
    fuelType:    
      description: 'The type of fuel suitable for the engine or engines of the vehicle. Enum:''autogas, biodiesel ethanol, cng, diesel, electric, gasoline, hybrid electric/diesel, hybrid electric/petrol, hydrogen, lpg, petrol, petrol(unleaded), petrol(leaded), other'''    
      enum:    
        - autogas    
        - biodiesel    
        - cng    
        - diesel    
        - electric    
        - ethanol    
        - gasoline    
        - 'hybrid electric/diesel'    
        - 'hybrid electric/petrol'    
        - hydrogen    
        - lpg    
        - petrol    
        - petrol(unleaded)    
        - petrol(leaded)    
        - other    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    height:    
      description: 'Vehicle''s height'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/height.    
    id:    
      anyOf: &vehiclemodel_-_properties_-_owner_-_items_-_anyof    
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
    manufacturerName:    
      description: 'Vehicle''s manufacturer name'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text.    
    modelName:    
      description: 'Vehicle''s model name'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/model.    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *vehiclemodel_-_properties_-_owner_-_items_-_anyof    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be VehicleModel'    
      enum:    
        - VehicleModel    
      type: Property    
    url:    
      description: 'URL which provides a description of this vehicle model'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL.    
    vehicleEngine:    
      description: 'Information about the engine or engines of the vehicle'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/vehicleEngine.    
    vehicleModelDate:    
      description: 'The release date of a vehicle model (often used to differentiate versions of the same make and model)'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/vehicleModelDate.    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . Enum:''agriculturalVehicle, anyVehicle, articulatedVehicle, bicycle, binTrolley, bus, car, caravan, carOrLightVehicle, carWithCaravan, carWithTrailer, cleaningTrolley, constructionOrMaintenanceVehicle, fourWheelDrive, highSidedVehicle, lorry, minibus, moped, motorcycle, motorcycleWithSideCar, motorscooter, sweepingMachine, tanker, threeWheeledVehicle, trailer, tram, twoWheeledVehicle, trolley, van, vehicleWithoutCatalyticConverter, vehicleWithCaravan, vehicleWithTrailer, withEvenNumberedRegistrationPlates, withOddNumberedRegistrationPlates, other''. The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)'    
      enum:    
        - agriculturalVehicle    
        - bicycle    
        - binTrolley    
        - bus    
        - car    
        - caravan    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - constructionOrMaintenanceVehicle    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - sweepingMachine    
        - tanker    
        - trailer    
        - tram    
        - van    
        - trolley    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    weight:    
      description: 'Vehicle''s weigth'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/weigth.    
    width:    
      description: 'Vehicle''s width'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width.    
  required:    
    - id    
    - name    
    - type    
    - vehicleType    
    - brandName    
    - modelName    
    - manufacturerName    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### VehicleModel NGSI V2 - Exemple de valeurs clés  
Voici un exemple de modèle de véhicule au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
      "id": "vehiclemodel:econic",  
      "type": "VehicleModel",  
      "name": "MBenz-Econic2014",  
      "brandName": "Mercedes Benz",  
      "modelName": "Econic",  
      "manufacturerName": "Daimler",  
      "vehicleType": "lorry",  
      "cargoVolume": 1000,  
      "fuelType": "diesel"  
}  
```  
#### VehicleModel NGSI V2 normalisé Exemple  
Voici un exemple de modèle de véhicule au format JSON normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "vehiclemodel:econic",  
    "type": "VehicleModel",  
    "name": {  
        "value": "MBenz-Econic2014"  
    },  
    "cargoVolume": {  
        "value": 1000  
    },   
    "modelName": {  
        "value": "Econic"  
    },   
    "brandName": {  
        "value": "Mercedes Benz"  
    },  
    "manufacturerName": {  
        "value": "Daimler"  
    },   
    "fuelType": {  
        "value": "diesel"  
    },   
    "vehicleType": {  
        "value": "lorry"  
    }  
}  
```  
#### VehicleModel NGSI-LD key-values Example  
Voici un exemple de modèle de véhicule au format JSON-LD en tant que valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "Mercedes Benz",  
 "cargoVolume": 1000,  
 "fuelType": "diesel",  
 "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
 "manufacturerName": "Daimler",  
 "modelName": "Econic",  
 "name": "MBenz-Econic2014",  
 "type": "VehicleModel",  
 "vehicleType": "lorry"}  
```  
#### Modèle de véhicule NGSI-LD normalisé Exemple  
Voici un exemple de modèle de véhicule au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:VehicleModel:vehiclemodel:econic",  
    "type": "VehicleModel",  
    "name": {  
        "type": "Property",  
        "value": "MBenz-Econic2014"  
    },  
    "cargoVolume": {  
        "type": "Property",  
        "value": 1000  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "Econic"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "Mercedes Benz"  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "Daimler"  
    },  
    "fuelType": {  
        "type": "Property",  
        "value": "diesel"  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "lorry"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
