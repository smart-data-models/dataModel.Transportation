Entité : TransportStation  
=========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Transportation/blob/master/TransportStation/LICENSE.md)  

## Liste des biens  

Propriétés requises  
- Aucune propriété requise  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
## Exemples de charges utiles  
#### TransportStation NGSI V2 - Exemple de valeurs clés  
Voici un exemple de TransportStation en format JSON comme valeurs clés. Il est compatible avec la version 2 du NGSI lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "Régie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gué / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ]  
}  
```  
#### TransportStation NGSI V2 normalisé Exemple  
Voici un exemple de TransportStation en format JSON normalisé. Ce format est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": "Tram"  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07.00",  
        "closes": "22.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08.00",  
        "closes": "23.00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8.30",  
        "closes": "21.00"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8.00",  
        "closes": "21.30"  
      }  
    ],  
    "validFrom": "-01-01",  
    "validThrough": "-31-12"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompany": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "www.lignesdazur.com"  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": "lateral"  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": {  
      "tram": {  
        "type": "Property",  
        "value": [  
          "Tram 2 - CADAM / Nikaia",  
          "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
        ]  
      },  
      "train": {  
        "type": "Property",  
        "value": [  
          "Gare SNCF Nice Saint Augustin (600m)"  
        ]  
      },  
      "bus": {  
        "type": "Property",  
        "value": [  
          "L20 - Giono / Les Pugets",  
          "L20 - Centre Commercial St Isidore",  
          "L21 - Le Gué / Polygone Riviera",  
          "L54 - Centre Commercial Cap 3000 - St Jeannet",  
          "L90 - La Bolline",  
          "91 Auron",  
          "L92 - Isola 2000"  
        ]  
      }  
    }  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architect": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  }  
}  
```  
#### TransportStation NGSI-LD valeurs clés Exemple  
Voici un exemple de TransportStation au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": "NCE-Tram-Station-L02-AP-T2",  
  "alternateName": "Nice - Tramway Station Description - L02-AP-T2",  
  "description": "Description and services provided in the station",  
  "seeAlso": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 2 - Door A2"  
  },  
  "areaServed": "Nice Airport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "stationType": [  
    "tram"  
  ],  
  "locationType": 1,  
  "levelId": 0,  
  "zoneId": "B",  
  "wheelChairAccessible": 1,  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "22:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:00:00",  
      "closes": "23:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "owner": [  
    "uri:ngsi:StreetRetail"  
  ],  
  "contractingAuthority": "MNCA - Metropole Nice Cote d'Azur",  
  "contractingCompagny": "Régie Ligne d'Azur",  
  "contactPoint": {  
    "url": "uri:ngsi:www.lignesdazur.com"  
  },  
  "webSite": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf",  
  "instalationMode": "ground",  
  "dimension": {  
    "length": 300,  
    "width": 25,  
    "thickness": 6.35  
  },  
  "inventory": {  
    "nbOfIOPoint": 2,  
    "nbOfLane": 1,  
    "nbOfPlatform": 1,  
    "PlatformType": [  
      "lateral"  
    ]  
  },  
  "stationConnected": [  
    {  
      "stationType": "tram",  
      "linesConnected": [  
        "Tram 2 - CADAM / Nikaia",  
        "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
      ]  
    },  
    {  
      "stationType": "train",  
      "linesConnected": [  
        "Gare SNCF Nice Saint Augustin (600m)"  
      ]  
    },  
    {  
      "stationType": "bus",  
      "linesConnected": [  
        "L20 - Giono / Les Pugets",  
        "L20 - Centre Commercial St Isidore",  
        "L21 - Le Gué / Polygone Riviera",  
        "L54 - Centre Commercial Cap 3000 - St Jeannet",  
        "L90 - La Bolline",  
        "91 Auron",  
        "L92 - Isola 2000"  
      ]  
    }  
  ],  
  "services": {  
    "purchaseDevice": true,  
    "interactiveDevice": true,  
    "timetableDevice": true,  
    "voiceDevice": true,  
    "informationBoardDevice": true,  
    "messageDevice": false,  
    "shelters": true,  
    "restBench": false,  
    "emergencyPhone": false,  
    "videoSurveillance": true,  
    "defibrillator": false,  
    "wheelChairAccessible": true  
  },  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR"  
  ],  
  "constructionDate": "2016-19-08",  
  "commissioningDate": "2018-09-15",  
  "architect": "Nice Architecture",  
  "featuredArtist ": [  
    "Leopold",  
    "De Renaiss"  
  ],  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### TransportStation NGSI-LD normalisé Exemple  
Voici un exemple de TransportStation au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:Station:Station:MNCA-STram-L02-AP-T2",  
  "type": "Station",  
  "name": {  
    "type": "Property",  
    "value": "NCE-Tram-Station-L02-AP-T2"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Nice - Tramway Station Description - L02-AP-T2"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description and services provided in the station"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "http://tramway.nice.fr/wp-content/uploads/2019/10/BD_pocket_plan_MAJ03_2019_20082019.pdf"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "point",  
      "coordinates": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 2 - Door A2"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Airport"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "stationType": {  
    "type": "Property",  
    "value": "Tram"  
  },  
  "locationType": {  
    "type": "Property",  
    "value": 1  
  },  
  "levelId": {  
    "type": "Property",  
    "value": 0  
  },  
  "zoneId": {  
    "type": "Property",  
    "value": "B"  
  },  
  "wheelChairAccessible": {  
    "type": "Property",  
    "value": 1  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07.00",  
        "closes": "22.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08.00",  
        "closes": "23.00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8.30",  
        "closes": "21.00"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8.00",  
        "closes": "21.30"  
      }  
    ],  
    "validFrom": "-01-01",  
    "validThrough": "-31-12"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Street furniture Urbain & Retail"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "MNCA - Metropole Nice Cote d'Azur"  
  },  
  "contractingCompagny": {  
    "type": "Property",  
    "value": "Régie Ligne d'Azur"  
  },  
  "contactPoint": {  
    "type": "Property",  
    "value": "www.lignesdazur.com"  
  },  
  "webSite": {  
    "type": "Property",  
    "value": "https://tramway.nice.fr/Plan-Station-L02-AP-T2.pdf"  
  },  
  "instalationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 300,  
      "width": 25,  
      "thickness": 6.35  
    }  
  },  
  "inventory": {  
    "type": "Property",  
    "value": {  
      "nbOfIOPoint": 2,  
      "nbOfLane": 1,  
      "nbOfPlatform": 1,  
      "PlatformType": "lateral"  
    }  
  },  
  "stationConnected": {  
    "type": "Property",  
    "value": {  
      "tram": {  
        "type": "Property",  
        "value": [  
          "Tram 2 - CADAM / Nikaia",  
          "Tram 3 - Saint Isidore / Stade Allianz Riviera"  
        ]  
      },  
      "train": {  
        "type": "Property",  
        "value": [  
          "Gare SNCF Nice Saint Augustin (600m)"  
        ]  
      },  
      "bus": {  
        "type": "Property",  
        "value": [  
          "L20 - Giono / Les Pugets",  
          "L20 - Centre Commercial St Isidore",  
          "L21 - Le Gué / Polygone Riviera",  
          "L54 - Centre Commercial Cap 3000 - St Jeannet",  
          "L90 - La Bolline",  
          "91 Auron",  
          "L92 - Isola 2000"  
        ]  
      }  
    }  
  },  
  "services": {  
    "type": "Property",  
    "value": {  
      "purchaseDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "interactiveDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "timetableDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "voiceDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "informationBoardDevice": {  
        "type": "Property",  
        "value": true  
      },  
      "messageDevice": {  
        "type": "Property",  
        "value": false  
      },  
      "shelters": {  
        "type": "Property",  
        "value": true  
      },  
      "restBench": {  
        "type": "Property",  
        "value": false  
      },  
      "emergencyPhone": {  
        "type": "Property",  
        "value": false  
      },  
      "videoSurveillance": {  
        "type": "Property",  
        "value": true  
      },  
      "defibrillator": {  
        "type": "Property",  
        "value": false  
      },  
      "wheelChairAccessible": {  
        "type": "Property",  
        "value": true  
      }  
    }  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR"  
    ]  
  },  
  "constructionDate": {  
    "type": "DateTime",  
    "value": "2016-19-08"  
  },  
  "commissioningDate": {  
    "type": "DateTime",  
    "value": "2018-09-15"  
  },  
  "architecte": {  
    "type": "Property",  
    "value": "Nice Architecture"  
  },  
  "featuredArtist ": {  
    "type": "Property",  
    "value": [  
      "Leopold",  
      "De Renaiss"  
    ]  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
