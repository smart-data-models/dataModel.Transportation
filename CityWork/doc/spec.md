[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: CityWork  
================  
[Open License](https://github.com/smart-data-models//dataModel.Transportation/blob/master/CityWork/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **The Data Model is a contextual description of urban works carried out on a road axis and which can impact individual (Cars, motorcycle, bicycles, .…) or common transport (Tram, Bus, subway). It contains a geographic representation making it possible to locate its work from a specific JSON Object and at a more global level (Road segment, Road, District, ...) in order to assess the potential impacts on the circulation. A GeoJSON object may represent a region of space (a Geometry), a spatially-bounded entity (a Feature), or a list of features (a Feature Collection). refer to the document [geojson](https://tools.ietf.org/pdf/draft-ietf-geojson-03.pdf) for more information about the modeling and the possible value.**  
version: 0.3.0  

## List of properties  

- `allowedVehicle`: Type of vehicle authorized to circulate. A combination of these values. Enum:'all Vehicle, bicycle, bus, car, companiesTrucks,  emergencyVehicle, firefighters, lorry, motorcycle, police, subway, sweepingMachine, trailer, tramway, trucks, van'  - `alternateName`: An alternative name for this item  - `busImpacted`: Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of 'lineId / lineName / lineLocation'. Second subproperties, one of 'segmentId / segmentName / segmentLocation'  - `contactPoint`: The details to contact with the item.  - `contractingAuthority`: Name of the contracting authority  - `countOfBusLineImpacted`: Count of Bus Lines impacted by the works  - `countOfDerogation`: Count of derogations granted to the work Number  - `countOfEventImpacted`: Count of Events impacted by the works  - `countOfRailwayLineImpacted`: Count of Railway Lines impacted by the works  - `countOfRoadImpacted`: Count of roads impacted by the works  - `countOfSchoolBusLineImpacted`: Count of School Bus Lines impacted by the works  - `countOfSchoolImpacted`: Count of University, School, or other educational resource impacted by the works  - `countOfStationImpacted`: Count of Railway stations impacted by the works  - `countOfSubwayLineImpacted`: Count of Subway Lines impacted by the works  - `countOfTramwayLineImpacted`: Count of tramway lines impacted by the works  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateLastReported`: A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `decrees`: A List of text where each element is a string with the URL to download or the name of the decree.  - `derogation`: Derogation granted for carrying out work on days and times. A structured value from 0 to N occurrences where each items has the following format `derogationType` :  with sub properties 'startDate, endDate, dayOfWeek, comment'  - `description`: A description of this item  - `encroachment`: Impact of the works on public, private area. A combination of these values. Enum:'other, private, public'  - `endDate`: End date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted  - `eventsImpacted`: List of free text or to the entity [Events](https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/doc/spec.md) if exist.  - `id`: Unique identifier of the entity  - `infrastructureFunction`:  Function of the infrastructure impacted by the works. Enum:'collection, distribution, other, transportation'  - `isMainRoadImpactedHTR`: Value to indicate whether the main traffic road is impacted. Default false. https://schema.org/Boolean  - `isMobile`: Characteristic on the mobility of the works : false for Fixed (default) and true for Mobile  - `mainContractingCompany`: The Main Contracting Company responsible of the works  - `maxAuthorizedTonnage`: Roads impacted by the works with Maximum tonnage authorized. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of 'roadId / roadName / roadLocation'. Second subproperties, 'maxTonnage'  - `name`: The name of this item.  - `openingHoursSpecification`: A structured value providing information about the opening hours of a place or a certain service inside a place  - `othersContractingCompany`: A List of Text where each element is a string with the name of the contracting Companies under the responsibility of the main Contracting Company.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `railwayImpacted`: Rail lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of 'lineId / lineName / lineLocation'. Second subproperties, one of 'segmentId / segmentName / segmentLocation'  - `roadImpacted`: Roads impacted by the works and the details of the roads concerned by the work. A structured value from 0 to N occurrences where each items is a string in the format : 'roadImpact':[List of Segment Impacted or Free Text or geo-property, separated by a comma]. If `isMainRoadImpactedHTR` = true, The first item is this one.  - `roadImpactedMT`: A list of roads defined as Major Traffic, impacted by the works. Values are also included in the roadImpacted attribute.  - `roadImpactedSA`: A list of roads defined as sensitive areas, impacted by the works. Values are also included in the roadImpacted attribute.  - `schoolBusImpacted`: Scholl Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of 'lineId / lineName / lineLocation'. Second subproperties, one of 'segmentId / segmentName / segmentLocation'  - `schoolImpacted`: List of free text or [GeoProperty] or a Reference to an entity [SCHOOL] if exist.   - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `startDate`: Start date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted  - `stationImpacted`: Station Impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, 'stationType'. Second subproperties, one of 'stationId / stationName / stationLocation'  - `subwayImpacted`: Subway lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of 'lineId / lineName / lineLocation'. Second subproperties, one of 'segmentId / segmentName / segmentLocation'  - `territorialArea`: Territorial area. Level higher to the attribute 'areaServed'. A list of Free Text  - `tramwayImpacted`: Tramway Line impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of 'lineId / lineName / lineLocation'. Second subproperties, one of 'segmentId / segmentName / segmentLocation'  - `type`: NGSI Entity type. It has to be CityWork  - `typeOfInterventionRequest`: Initial type of request to do the works. Enum:'authorizationRequest,  interventionNotice,  other,  urgentWorks'  - `workDate`: Date and time (Day or period) of the works. It can be represented by an specific time string  - `workDisposition`: Specific rules taken for the works. A structured value from 0 to N occurrences where each items has the following format : `Disposition`: with sub properties  `startDate`, `endDate`,  `dayOfWeek`, `comment`. Enum:'alternatingLights , bicyclePathClosure, bicyclePathDeviation, bicyclePathReduction, circulationManualControl, laneClosure, laneDeviation, laneReduction, noRestriction, parkingForbidden, parkingModification, sidewalkClosure, sidewalkClosureOrReduction, sidewalkReduction, speedReduction'  - `workLastDateUpdate`: Last date for updating a contractual element of the work  - `workLevel`: Positioning of the works in relation to a ground reference system. A combination of these elements. Enum:'aerial, ground, mixed, other, roofing, surface, underground, wall'  - `workNature`: Nature of the works. A combination of these values.Enum:'additionalInvestigations, brushCutting, cleaning, collection, connection, consolidation, construction, control, counting, craneLifting, creation, demolition, drivingSwitch, experimentation, extension, filmShooting, Installation-OR-layout, investigation, landFill, maintenance, manholeOpening, ManholeOpeningToRestoreService, miscellaneousInstallation, miscellaneousWorks, mowingDeburring, other, overheadLinesWorksIntervention, pruning, pulling, refurbishment, rehabilitation, reinforcement, renewal, renovation, repair, replacement, riprap, roadSign, safetyAndComplianceWork, safetyRailsInstallation, securingPerimeter, siteInstallation, staking, supportImplantation, surfaceOccupationAuthorization, survey, tarring, tonnageExemption, treeCutting, trenchOpening, upgrading'  - `workNumber`: Number assigned to the work  - `workOtherImpact`: Other impact. A list of free values  - `workReason`: Reasons of the works in case of urgent intervention. A combination of these values. Enum:'collapse, derailment, fire, flood, gasLeak, landslide, other, powerCut, rockfall, sagging, waterLeak'  - `workState`: Number assigned to the work. Enum:'all, approved, authorized, canceled, completed, decreeToBeSigned, draft, editedDecrees, instructionInProgress, investigated, nonCompliantOccupation, open, pendingAuthorization, pendingCancellation, planningCompleted, pendingDocument, pendingExtension, pendingPlanning, planned, received, reject, supported, validatedInPlanning'  - `workTarget`: Categories of works regarding the different profession. A combination of these elements. Enum:'bicyclePath, busCorridor, catainers, cityMotorBike, cityBike, cityCar, cityScooter, coldAndAirCon, coldGroup, copperCable, CoringPenetrometry, drinkingWater, electricityNetworks, exploratoryWork, fireHydrants, frameRoof, gasNetworks, generator, historicalMonuments, infrastructure, landscapedArea, movingHoistNacelleTruck, networks, offStreetParking, opticalFibers, other, overheadLine, papersCollection, pavement, publicDecorativeLighting, publicDomain, publicTransport, railway, rainyWaters, riprap, rMTNetworks, roads, roadsAndPublicDomain, sanitation, scaffolding, sideWalk, speedReductionDevices, streetParking, surfaceOccupation, supportStructures, tagsAndPosters, telecomNetworks, telecom-RMT-VideoNetworks, trafficSignalingRegulation, tramway, urbanFurniture, urbanHeating, variousWorks, videoNetworks, vrd'  - `workZone`: Zone of Works. A combination of these values. Enum:' airport, beach, bicyclePath, bridge, busCorridor, dock, floodArea, harbor, heliport, mountainousArea, offRoad, other, parking, parksGardens, path, protectArea, railwayLine, riskArea, river, road, rockyArea, sevesoArea, sideWalk, subwayLine, tramwayLine, tunnel'    
Required properties  
- `id`  - `location`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CityWork:    
  description: 'The Data Model is a contextual description of urban works carried out on a road axis and which can impact individual (Cars, motorcycle, bicycles, .…) or common transport (Tram, Bus, subway). It contains a geographic representation making it possible to locate its work from a specific JSON Object and at a more global level (Road segment, Road, District, ...) in order to assess the potential impacts on the circulation. A GeoJSON object may represent a region of space (a Geometry), a spatially-bounded entity (a Feature), or a list of features (a Feature Collection). refer to the document [geojson](https://tools.ietf.org/pdf/draft-ietf-geojson-03.pdf) for more information about the modeling and the possible value.'    
  properties:    
    allowedVehicle:    
      description: 'Type of vehicle authorized to circulate. A combination of these values. Enum:''all Vehicle, bicycle, bus, car, companiesTrucks,  emergencyVehicle, firefighters, lorry, motorcycle, police, subway, sweepingMachine, trailer, tramway, trucks, van'''    
      items:    
        enum:    
          - allVehicle    
          - bicycle    
          - bus    
          - car    
          - companiesTrucks    
          - emergencyVehicle    
          - firefighters    
          - lorry    
          - motorcycle    
          - police    
          - subway    
          - sweepingMachine    
          - trailer    
          - tramway    
          - trucks    
          - van    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    busImpacted:    
      description: 'Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: &citywork_-_properties_-_id_-_anyof    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: &citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
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
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    contactPoint:    
      description: 'The details to contact with the item.'    
      properties:    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Supersedes serviceArea.'    
          type: string    
        availabilityRestriction:    
          anyOf:    
            - description: 'Property. Array of identifiers format of any NGSI entity.'    
              items:    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              type: array    
            - description: 'Property. Array of identifiers format of any NGSI entity.'    
              items:    
                format: uri    
                type: string    
              type: array    
          description: 'Relationship. Model:''http://schema.org/hoursAvailable''. This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class.'    
        availableLanguage:    
          anyOf:    
            - anyOf:    
                - type: string    
                - items:    
                    type: string    
                  type: array    
          description: 'Property. Model:''http://schema.org/availableLanguage''. A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
        contactOption:    
          anyOf:    
            - type: string    
            - items:    
                type: string    
              type: array    
          description: 'Property. Model:''http://schema.org/contactOption''. An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).'    
        contactType:    
          description: 'Property. Contact type of this item.'    
          type: string    
        email:    
          description: 'Property. Email address of owner.'    
          format: idn-email    
          type: string    
        faxNumber:    
          description: 'Property. Model:''http://schema.org/Text''. The fax number.'    
          type: string    
        name:    
          description: 'Property. The name of this item.'    
          type: string    
        productSupported:    
          description: 'Property. Model:''http://schema.org/Text''. The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").'    
          type: string    
        telephone:    
          description: 'Property. Telephone of this contact.'    
          type: string    
        url:    
          description: 'Property. URL which provides a description or further information about this item.'    
          format: uri    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/ContactPoint    
        type: Property    
    contractingAuthority:    
      description: 'Name of the contracting authority'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    countOfBusLineImpacted:    
      description: 'Count of Bus Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfDerogation:    
      description: 'Count of derogations granted to the work Number'    
      type: number    
      x-ngsi:    
        model: https://schema.org/number    
        type: Property    
    countOfEventImpacted:    
      description: 'Count of Events impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfRailwayLineImpacted:    
      description: 'Count of Railway Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfRoadImpacted:    
      description: 'Count of roads impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSchoolBusLineImpacted:    
      description: 'Count of School Bus Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSchoolImpacted:    
      description: 'Count of University, School, or other educational resource impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfStationImpacted:    
      description: 'Count of Railway stations impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfSubwayLineImpacted:    
      description: 'Count of Subway Lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    countOfTramwayLineImpacted:    
      description: 'Count of tramway lines impacted by the works'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    dateLastReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    decrees:    
      description: 'A List of text where each element is a string with the URL to download or the name of the decree.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    derogation:    
      description: 'Derogation granted for carrying out work on days and times. A structured value from 0 to N occurrences where each items has the following format `derogationType` :  with sub properties ''startDate, endDate, dayOfWeek, comment'''    
      items:    
        properties:    
          comment:    
            type: string    
          dayOfWeek:    
            items:    
              enum:    
                - Monday    
                - Tuesday    
                - Wednesday    
                - Thursday    
                - Friday    
                - Saturday    
                - Sunday    
                - PublicHolidays    
              type: string    
            type: array    
          derogationType:    
            type: string    
          endDate:    
            format: date-time    
            type: string    
          startDate:    
            format: date-time    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    encroachment:    
      description: 'Impact of the works on public, private area. A combination of these values. Enum:''other, private, public'''    
      items:    
        enum:    
          - other    
          - private    
          - public    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    endDate:    
      description: 'End date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    eventsImpacted:    
      description: 'List of free text or to the entity [Events](https://github.com/smart-data-models/dataModel.TourismDestinations/blob/master/Event/doc/spec.md) if exist.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: *citywork_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    infrastructureFunction:    
      description: ' Function of the infrastructure impacted by the works. Enum:''collection, distribution, other, transportation'''    
      items:    
        enum:    
          - collection    
          - distribution    
          - other    
          - transportation    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    isMainRoadImpactedHTR:    
      description: 'Value to indicate whether the main traffic road is impacted. Default false. https://schema.org/Boolean'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isMobile:    
      description: 'Characteristic on the mobility of the works : false for Fixed (default) and true for Mobile'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    mainContractingCompany:    
      description: 'The Main Contracting Company responsible of the works'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    maxAuthorizedTonnage:    
      description: 'Roads impacted by the works with Maximum tonnage authorized. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''roadId / roadName / roadLocation''. Second subproperties, ''maxTonnage'''    
      items:    
        properties:    
          maxTonnage:    
            description: 'Property. Maximum tonnage authorized for the road. The unit code (text) **TNE** which represents Tonne Metric.'    
            type: number    
          roadId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          roadImpacted:    
            type: string    
          roadLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          roadName:    
            description: 'Property. Road Name'    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          dayOfWeek:    
            anyOf:    
              - description: 'Property. Array of days of the week.'    
                enum:    
                  - Monday    
                  - Tuesday    
                  - Wednesday    
                  - Thursday    
                  - Friday    
                  - Saturday    
                  - Sunday    
                  - PublicHolidays    
                type: string    
              - description: 'Property. Array of days of the week.'    
                enum:    
                  - https://schema.org/Monday    
                  - https://schema.org/Tuesday    
                  - https://schema.org/Wednesday    
                  - https://schema.org/Thursday    
                  - https://schema.org/Friday    
                  - https://schema.org/Saturday    
                  - https://schema.org/Sunday    
                  - https://schema.org/PublicHolidays    
                type: string    
            description: 'Property. Model:''http://schema.org/dayOfWeek''. The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays).'    
            type: string    
          opens:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          validFrom:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
          validThrough:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
            type: string    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    othersContractingCompany:    
      description: 'A List of Text where each element is a string with the name of the contracting Companies under the responsibility of the main Contracting Company.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *citywork_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    railwayImpacted:    
      description: 'Rail lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpacted:    
      description: 'Roads impacted by the works and the details of the roads concerned by the work. A structured value from 0 to N occurrences where each items is a string in the format : ''roadImpact'':[List of Segment Impacted or Free Text or geo-property, separated by a comma]. If `isMainRoadImpactedHTR` = true, The first item is this one.'    
      items:    
        properties:    
          roadId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          roadLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          roadName:    
            description: 'Property. Road Name'    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpactedMT:    
      description: 'A list of roads defined as Major Traffic, impacted by the works. Values are also included in the roadImpacted attribute.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    roadImpactedSA:    
      description: 'A list of roads defined as sensitive areas, impacted by the works. Values are also included in the roadImpacted attribute.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    schoolBusImpacted:    
      description: 'Scholl Bus lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            description: 'Property. Segment Name.'    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    schoolImpacted:    
      description: 'List of free text or [GeoProperty] or a Reference to an entity [SCHOOL] if exist. '    
      items:    
        type: string    
      type: array    
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
    startDate:    
      description: 'Start date and time of the works in an ISO8601 UTC format. The attribute can be used in addition to the `workDate` attribute when it corresponds to a time interval to be highlighted'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    stationImpacted:    
      description: 'Station Impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, ''stationType''. Second subproperties, one of ''stationId / stationName / stationLocation'''    
      items:    
        properties:    
          stationId:    
            description: 'Property. List of free text or reference to the entity [TransportStation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/TransportStation/doc/spec.md) if used.'    
            items:    
              anyOf: *citywork_-_properties_-_id_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            type: array    
          stationLocation:    
            description: 'Property. Station Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          stationName:    
            description: 'Property. Station Name.'    
            items:    
              type: string    
            type: array    
          stationType:    
            description: "Property. A unique value of free text or from the urban transport Mode GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). Enum:'aerialLift, bus, cableTram, ferry, funicular, monorail, rail, subway, tram, trolleybus'"    
            enum:    
              - aerialLift    
              - bus    
              - cableTram    
              - ferry    
              - funicular    
              - monorail    
              - rail    
              - subway    
              - tram    
              - trolleybus    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    subwayImpacted:    
      description: 'Subway lines impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    territorialArea:    
      description: 'Territorial area. Level higher to the attribute ''areaServed''. A list of Free Text'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    tramwayImpacted:    
      description: 'Tramway Line impacted by the works. A structured value from 0 to N occurrences with 2 subproperties per item. First subproperties, one of ''lineId / lineName / lineLocation''. Second subproperties, one of ''segmentId / segmentName / segmentLocation'''    
      items:    
        properties:    
          lineId:    
            anyOf: *citywork_-_properties_-_id_-_anyof    
            description: 'Property. Unique identifier of the entity'    
          lineLocation:    
            description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
            oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
          lineName:    
            description: 'Property. Line Name.'    
            type: string    
          segmentId:    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentLocation:    
            description: 'Property. Segment Location. A GeoProperty.'    
            items:    
              description: 'Geoproperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
              oneOf: *citywork_-_properties_-_busimpacted_-_items_-_properties_-_segmentid_-_items_-_oneof    
            type: array    
          segmentName:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be CityWork'    
      enum:    
        - CityWork    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfInterventionRequest:    
      description: 'Initial type of request to do the works. Enum:''authorizationRequest,  interventionNotice,  other,  urgentWorks'''    
      enum:    
        - authorizationRequest    
        - interventionNotice    
        - other    
        - urgentWorks    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workDate:    
      description: 'Date and time (Day or period) of the works. It can be represented by an specific time string'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    workDisposition:    
      description: 'Specific rules taken for the works. A structured value from 0 to N occurrences where each items has the following format : `Disposition`: with sub properties  `startDate`, `endDate`,  `dayOfWeek`, `comment`. Enum:''alternatingLights , bicyclePathClosure, bicyclePathDeviation, bicyclePathReduction, circulationManualControl, laneClosure, laneDeviation, laneReduction, noRestriction, parkingForbidden, parkingModification, sidewalkClosure, sidewalkClosureOrReduction, sidewalkReduction, speedReduction'''    
      items:    
        properties:    
          comment:    
            type: string    
          dayOfWeek:    
            items:    
              enum:    
                - Monday    
                - Tuesday    
                - Wednesday    
                - Thursday    
                - Friday    
                - Saturday    
                - Sunday    
                - PublicHolidays    
              type: string    
            type: array    
          disposition:    
            enum:    
              - alternatingLights    
              - bicyclePathClosure    
              - bicyclePathDeviation    
              - bicyclePathReduction    
              - circulationManualControl    
              - laneClosure    
              - laneDeviation    
              - laneReduction    
              - noRestriction    
              - parkingForbidden    
              - parkingModification    
              - sidewalkClosure    
              - sidewalkClosureOrReduction    
              - sidewalkReduction    
              - speedReduction    
              - workOtherImpact    
            type: string    
          endDate:    
            format: date-time    
            type: string    
          startDate:    
            format: date-time    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    workLastDateUpdate:    
      description: 'Last date for updating a contractual element of the work'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    workLevel:    
      description: 'Positioning of the works in relation to a ground reference system. A combination of these elements. Enum:''aerial, ground, mixed, other, roofing, surface, underground, wall'''    
      items:    
        enum:    
          - aerial    
          - ground    
          - mixed    
          - other    
          - roofing    
          - surface    
          - underground    
          - wall    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workNature:    
      description: 'Nature of the works. A combination of these values.Enum:''additionalInvestigations, brushCutting, cleaning, collection, connection, consolidation, construction, control, counting, craneLifting, creation, demolition, drivingSwitch, experimentation, extension, filmShooting, Installation-OR-layout, investigation, landFill, maintenance, manholeOpening, ManholeOpeningToRestoreService, miscellaneousInstallation, miscellaneousWorks, mowingDeburring, other, overheadLinesWorksIntervention, pruning, pulling, refurbishment, rehabilitation, reinforcement, renewal, renovation, repair, replacement, riprap, roadSign, safetyAndComplianceWork, safetyRailsInstallation, securingPerimeter, siteInstallation, staking, supportImplantation, surfaceOccupationAuthorization, survey, tarring, tonnageExemption, treeCutting, trenchOpening, upgrading'''    
      items:    
        enum:    
          - additionalInvestigations    
          - brushCutting    
          - cleaning    
          - collection    
          - connection    
          - consolidation    
          - construction    
          - control    
          - counting    
          - craneLifting    
          - creation    
          - demolition    
          - drivingSwitch    
          - experimentation    
          - extension    
          - filmShooting    
          - Installation-OR-layout    
          - investigation    
          - landFill    
          - maintenance    
          - manholeOpening    
          - ManholeOpeningToRestoreService    
          - miscellaneousInstallation    
          - miscellaneousWorks    
          - mowingDeburring    
          - other    
          - overheadLinesWorksIntervention    
          - pruning    
          - pulling    
          - refurbishment    
          - rehabilitation    
          - reinforcement    
          - renewal    
          - renovation    
          - repair    
          - replacement    
          - riprap    
          - roadSign    
          - safetyAndComplianceWork    
          - safetyRailsInstallation    
          - securingPerimeter    
          - siteInstallation    
          - staking    
          - supportImplantation    
          - surfaceOccupationAuthorization    
          - survey    
          - tarring    
          - tonnageExemption    
          - treeCutting    
          - trenchOpening    
          - upgrading    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workNumber:    
      description: 'Number assigned to the work'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workOtherImpact:    
      description: 'Other impact. A list of free values'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workReason:    
      description: 'Reasons of the works in case of urgent intervention. A combination of these values. Enum:''collapse, derailment, fire, flood, gasLeak, landslide, other, powerCut, rockfall, sagging, waterLeak'''    
      items:    
        enum:    
          - collapse    
          - derailment    
          - fire    
          - flood    
          - gasLeak    
          - landslide    
          - other    
          - powerCut    
          - rockfall    
          - sagging    
          - waterLeak    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workState:    
      description: 'Number assigned to the work. Enum:''all, approved, authorized, canceled, completed, decreeToBeSigned, draft, editedDecrees, instructionInProgress, investigated, nonCompliantOccupation, open, pendingAuthorization, pendingCancellation, planningCompleted, pendingDocument, pendingExtension, pendingPlanning, planned, received, reject, supported, validatedInPlanning'''    
      enum:    
        - all    
        - approved    
        - authorized    
        - canceled    
        - completed    
        - decreeToBeSigned    
        - draft    
        - editedDecrees    
        - instructionInProgress    
        - investigated    
        - nonCompliantOccupation    
        - open    
        - other    
        - pendingAuthorization    
        - pendingCancellation    
        - planningCompleted    
        - pendingDocument    
        - pendingExtension    
        - pendingPlanning    
        - planned    
        - received    
        - reject    
        - supported    
        - validatedInPlanning    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    workTarget:    
      description: 'Categories of works regarding the different profession. A combination of these elements. Enum:''bicyclePath, busCorridor, catainers, cityMotorBike, cityBike, cityCar, cityScooter, coldAndAirCon, coldGroup, copperCable, CoringPenetrometry, drinkingWater, electricityNetworks, exploratoryWork, fireHydrants, frameRoof, gasNetworks, generator, historicalMonuments, infrastructure, landscapedArea, movingHoistNacelleTruck, networks, offStreetParking, opticalFibers, other, overheadLine, papersCollection, pavement, publicDecorativeLighting, publicDomain, publicTransport, railway, rainyWaters, riprap, rMTNetworks, roads, roadsAndPublicDomain, sanitation, scaffolding, sideWalk, speedReductionDevices, streetParking, surfaceOccupation, supportStructures, tagsAndPosters, telecomNetworks, telecom-RMT-VideoNetworks, trafficSignalingRegulation, tramway, urbanFurniture, urbanHeating, variousWorks, videoNetworks, vrd'''    
      items:    
        enum:    
          - bicyclePath    
          - busCorridor    
          - catainers    
          - cityMotorBike    
          - cityBike    
          - cityCar    
          - cityScooter    
          - coldAndAirCon    
          - coldGroup    
          - copperCable    
          - CoringPenetrometry    
          - drinkingWater    
          - electricityNetworks    
          - exploratoryWork    
          - fireHydrants    
          - frameRoof    
          - gasNetworks    
          - generator    
          - historicalMonuments    
          - infrastructure    
          - landscapedArea    
          - movingHoistNacelleTruck    
          - networks    
          - offStreetParking    
          - opticalFibers    
          - other    
          - overheadLine    
          - papersCollection    
          - pavement    
          - publicDecorativeLighting    
          - publicDomain    
          - publicTransport    
          - railway    
          - rainyWaters    
          - riprap    
          - rMTNetworks    
          - roads    
          - roadsAndPublicDomain    
          - sanitation    
          - scaffolding    
          - sideWalk    
          - speedReductionDevices    
          - streetParking    
          - surfaceOccupation    
          - supportStructures    
          - tagsAndPosters    
          - telecomNetworks    
          - telecom-RMT-VideoNetworks    
          - trafficSignalingRegulation    
          - tramway    
          - urbanFurniture    
          - urbanHeating    
          - variousWorks    
          - videoNetworks    
          - vrd    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    workZone:    
      description: 'Zone of Works. A combination of these values. Enum:'' airport, beach, bicyclePath, bridge, busCorridor, dock, floodArea, harbor, heliport, mountainousArea, offRoad, other, parking, parksGardens, path, protectArea, railwayLine, riskArea, river, road, rockyArea, sevesoArea, sideWalk, subwayLine, tramwayLine, tunnel'''    
      items:    
        enum:    
          - airport    
          - beach    
          - bicyclePath    
          - bridge    
          - busCorridor    
          - dock    
          - floodArea    
          - harbor    
          - heliport    
          - mountainousArea    
          - offRoad    
          - other    
          - parking    
          - parksGardens    
          - path    
          - protectArea    
          - railwayLine    
          - riskArea    
          - river    
          - road    
          - rockyArea    
          - sevesoArea    
          - sideWalk    
          - subwayLine    
          - tramwayLine    
          - tunnel    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Transportation/blob/master/CityWork/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Transportation/CityWork/schema.json    
  x-model-tags: ""    
  x-version: 0.3.0    
```  
</details>    
## Example payloads    
#### CityWork NGSI-v2 key-values Example    
Here is an example of a CityWork in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": "Nce-Airport-CW2020Q2-006",  
  "alternateName": "AirPort global Observation",  
  "description": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        43.20315,  
        7.20186  
      ],  
      [  
        43.20384,  
        7.20372  
      ],  
      [  
        43.20388,  
        7.20493  
      ],  
      [  
        43.19938,  
        7.20312  
      ],  
      [  
        43.20045,  
        7.20152  
      ],  
      [  
        43.20315,  
        7.20186  
      ]  
    ]  
  },  
  "areaServed": "Nice Aeroport",  
  "territorialArea": "subwaypole Nice",  
  "dateLastReported": "2020-04-02T10:30:00Z",  
  "workNumber": "CW2020Q2-006",  
  "workState": "open",  
  "workDate": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
  "startDate": "2020-03-17T08:45:00Z",  
  "endDate": "2020-04-22T18:45:00Z",  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "20:00:00"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:30:00",  
      "closes": "17:00:00"  
    }  
  ],  
  "contractingAuthority": "MNCA - subwaypole Nice Cote d'Azur",  
  "contactPoint": {  
    "name": "Service des AO"  
  },  
  "decrees": [  
    "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
    "CW-2020Q2-006",  
    "CW-2020Q2-006-Av-001",  
    "CW-2020Q2-006-Av-002"  
  ],  
  "workLastDateUpdate": "2020-03-17T08:45:00Z",  
  "mainContractingCompagny": "XRP - NICOLSPA",  
  "othersContractingCompagny": [  
    "VRD - Terrassement Nicois",  
    "ELEC - Electricite de Nice",  
    "NUM - Consortium operateur"  
  ],  
  "workLevel": [  
    "ground",  
    "underground"  
  ],  
  "workTarget": [  
    "roads",  
    "pavement",  
    "electricityNetworks",  
    "opticalFibers",  
    "videoNetworks",  
    "vrd"  
  ],  
  "workNature": [  
    "landFill",  
    "repair",  
    "tonnageExemption",  
    "securingPerimeter",  
    "trenchOpening",  
    "tarring"  
  ],  
  "infrastructureFunction": [  
    "distribution",  
    "collection"  
  ],  
  "encroachment": [  
    "public",  
    "private"  
  ],  
  "typeOfInteventionRequest": "authorizationRequest",  
  "workReason": [  
    "sagging",  
    "powerCut"  
  ],  
  "workZone": [  
    "road",  
    "sideWalk",  
    "busCorridor",  
    "tramwayLine"  
  ],  
  "workDisposition": [  
    {  
      "disposition": "laneReduction",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ],  
      "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
    },  
    {  
      "disposition": "sidewalkReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "endDate": "2020-05-14T24:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "alternatingLights",  
      "startDate": "2020-05-11T08:00:00Z",  
      "endDate": "2020-05-15T18:30:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "disposition": "speedReduction",  
      "startDate": "2020-05-12T00:00:00Z",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday",  
        "Saturday",  
        "Sunday"  
      ],  
      "comment": "Speed Switching from 2 lanes to 1 lane"  
    }  
  ],  
  "workOtherImpact": [  
    "layingCablesOnGround",  
    "shopsTerrace"  
  ],  
  "isMobile": false,  
  "countOfDerogation": 2,  
  "derogation": [  
    {  
      "derogationType": "Work Nigth during Workday",  
      "startDate": "2020-05-11T20:30:00Z",  
      "endDate": "2020-05-15T23:30:00",  
      "dayOfWeek": [  
        "Monday",  
        "Tuesday",  
        "Wednesday",  
        "Thursday",  
        "Friday"  
      ]  
    },  
    {  
      "derogationType": "BRH",  
      "startDate": "2020-05-13T20:30:00Z",  
      "endDate": "2020-05-13T23:30:00Z",  
      "dayOfWeek": [  
        "Wednesday"  
      ]  
    }  
  ],  
  "isMainRoadImpactedHTR": true,  
  "countOfRoadImpacted": 3,  
  "roadImpacted": [  
    {  
      "roadId": "urn:ngsi-ld:Road:N202",  
      "segmentImpacted": [  
        "urn:ngsi-ld:RoadSegment:N202-12",  
        "urn:ngsi-ld:RoadSegment:N202-13"  
      ]  
    },  
    {  
      "roadId": "Road:D021",  
      "segmentImpacted": [  
        "12",  
        "13",  
        "14",  
        "15"  
      ]  
    },  
    {  
      "roadId": "urn:ngsi-ld:Road:D032",  
      "segmentArea": {  
        "type": "LineString",  
        "coordinates": [  
          [  
            102.0,  
            0.0  
          ],  
          [  
            103.0,  
            1.0  
          ],  
          [  
            104.0,  
            0.0  
          ],  
          [  
            105.0,  
            1.0  
          ]  
        ]  
      }  
    }  
  ],  
  "allowedVehicle": [  
    "firefighters",  
    "police",  
    "emergencyVehicle",  
    "companiesTrucks"  
  ],  
  "maxAuthorizedTonnage": [  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:N202",  
      "maxTonnage": 30  
    },  
    {  
      "roadImpacted": "Road:D021",  
      "maxTonnage": 20  
    },  
    {  
      "roadImpacted": "urn:ngsi-ld:Road:D032",  
      "maxTonnage": 15.2  
    }  
  ],  
  "countOfBusLineImpacted": 1,  
  "busImpacted": [  
    {  
      "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
    }  
  ],  
  "countOfTramwayLineImpacted": 2,  
  "tramwayImpacted": [  
    {  
      "lineImpacted": "TramWayLine:L01",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L01-12",  
        "urn:ngsi-ld:TramWaySegment:L01-19"  
      ]  
    },  
    {  
      "lineImpacted": "TramWayLine:L03",  
      "segmentImpacted": [  
        "urn:ngsi-ld:TramWaySegment:L03-19"  
      ]  
    }  
  ],  
  "countOfRailwayLineImpacted": 1,  
  "railwayImpacted": [  
    {  
      "lineImpacted": "Nice-Grasse",  
      "segmentImpact": [  
        "Nice Saint Augustin section"  
      ]  
    }  
  ],  
  "countOfSchoolImpacted": 2,  
  "schoolImpacted": [  
    "Lycée Massena",  
    "Université Campus Saint Jean"  
  ],  
  "countOfStationImpacted": 4,  
  "stationImpacted": [  
    {  
      "stationId": [  
        "urn:ngsi-ld:station:L205-S13",  
        "urn:ngsi-ld:station:L205-S14"  
      ]  
    },  
    {  
      "stationType": "tram",  
      "stationId": [  
        "L01-S12",  
        "L01-S19"  
      ]  
    }  
  ],  
  "countOfEventImpacted": 2,  
  "eventsImpact": [  
    "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
    "NiceMarathon"  
  ]  
}  
```  
#### CityWork NGSI-v2 normalized Example    
Here is an example of a CityWork in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
  "type": "CityWork",  
  "name": {  
    "type": "string",  
    "value": "Nice-Airport-CW2020Q2-006"  
  },  
  "alternateName": {  
    "type": "string",  
    "value": "AirPort global Observation"  
  },  
  "description": {  
    "type": "string",  
    "value": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          43.20315,  
          7.20186  
        ],  
        [  
          43.20384,  
          7.20372  
        ],  
        [  
          43.20388,  
          7.20493  
        ],  
        [  
          43.19938,  
          7.20312  
        ],  
        [  
          43.20045,  
          7.20152  
        ],  
        [  
          43.20315,  
          7.20186  
        ]  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "string",  
    "value": "Nice Aeroport"  
  },  
  "territorialArea": {  
    "type": "string",  
    "value": "subwaypole Nice"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-04-02T10:30:00Z"  
  },  
  "workNumber": {  
    "type": "string",  
    "value": "CW2020Q2-006"  
  },  
  "workState": {  
    "type": "string",  
    "value": "open"  
  },  
  "workDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-04-02T10:30:00Z"  
      }  
    }  
  },  
  "startDate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-02-01TT17:25:00Z"  
      }  
    }  
  },  
  "endDate": {  
    "type": "DateTime",  
    "value": "2020-04-22T18:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-04-02T10:30:00Z"  
      }  
    }  
  },  
  "openingHoursSpecification": {  
    "type": "array",  
    "value": [  
      {  
        "dayOfWeek": "Monday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Tuesday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Wednesday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Thursday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Friday",  
        "opens": "07:00:00",  
        "closes": "20:00:00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08:30:00",  
        "closes": "17.00:00"  
      }  
    ]  
  },  
  "contractingAuthority": {  
    "type": "string",  
    "value": "MNCA - subwaypole Nice Cote d'Azur"  
  },  
  "contactPoint": {  
    "type": "string",  
    "value": "Service des AO"  
  },  
  "decrees": {  
    "type": "array",  
    "value": [  
      "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
      "CW-2020Q2-006",  
      "CW-2020Q2-006-Av-001",  
      "CW-2020Q2-006-Av-002"  
    ]  
  },  
  "workLastDateUpdate": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
     "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-03-16T09:12:25Z"  
      }  
    }  
  },  
  "mainContractingCompany": {  
    "type": "string",  
    "value": "XRP - NICOLSPA"  
  },  
  "othersContractingCompagny": {  
    "type": "array",  
    "value": [  
      "VRD - Terrassement Nicois",  
      "ELEC - Electricite de Nice",  
      "NUM - Consortium operateur"  
    ]  
  },  
  "workLevel": {  
    "type": "array",  
    "value": [  
      "ground",  
      "underground"  
    ]  
  },  
  "workTarget": {  
    "type": "array",  
    "value": [  
      "electricityNetworks",  
      "opticalFibers",  
      "pavement",  
      "roads",  
      "videoNetworks",  
      "vrd"  
    ]  
  },  
  "workNature": {  
    "type": "array",  
    "value": [  
      "landFill",  
      "repair",  
      "securingPerimeter",  
      "tarring",  
      "tonnageExemption",  
      "trenchOpening"  
    ]  
  },  
  "infrastructureFunction": {  
    "type": "array",  
    "value": [  
      "collection",  
      "distribution"  
    ]  
  },  
  "encroachment": {  
    "type": "array",  
    "value": [  
      "private",  
      "public"  
    ]  
  },  
  "typeOfInterventionRequest": {  
    "type": "string",  
    "value": "authorizationRequest"  
  },  
  "workReason": {  
    "type": "array",  
    "value": [  
      "sagging",  
      "powerCut"  
    ]  
  },  
  "workZone": {  
    "type": "array",  
    "value": [  
      "busCorridor",  
      "road",  
      "sideWalk",  
      "tramwayLine"  
    ]  
  },  
  "workDisposition": {  
    "type": "array",  
    "value": [  
      {  
        "disposition": "laneReduction",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ],  
        "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
      },  
      {  
        "disposition": "sidewalkReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "endDate": "2020-05-14T24:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ]  
      },  
      {  
        "disposition": "alternatingLights",  
        "startDate": "2020-05-11T08:00:00Z",  
        "endDate": "2020-05-15T18:30:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "disposition": "speedReduction",  
        "startDate": "2020-05-12T00:00:00Z",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday",  
          "Saturday",  
          "Sunday"  
        ],  
        "comment": "Speed Switching from 2 lanes to 1 lane"  
      }  
    ]  
  },  
  "workOtherImpact": {  
    "type": "array",  
    "value": [  
      "layingCablesOnGround",  
      "shopsTerrace"  
    ]  
  },  
  "isMobile": {  
    "type": "Boolean",  
    "value": false  
  },  
  "countOfDerogation": {  
    "type": "number",  
    "value": 2  
  },  
  "derogation": {  
    "type": "array",  
    "value": [  
      {  
        "derogationType": "Work Night during Workday",  
        "startDate": "2020-05-11T20:30:00Z",  
        "endDate": "2020-05-15T23:30:00",  
        "dayOfWeek": [  
          "Monday",  
          "Tuesday",  
          "Wednesday",  
          "Thursday",  
          "Friday"  
        ]  
      },  
      {  
        "derogationType": "BRH",  
        "startDate": "2020-05-13T20:30:00Z",  
        "endDate": "2020-05-13T23:30:00Z",  
        "dayOfWeek": [  
          "Wednesday"  
        ]  
      }  
    ]  
  },  
  "isMainRoadImpactedHTR": {  
    "type": "Boolean",  
    "value": true  
  },  
  "countOfRoadImpacted": {  
    "type": "number",  
    "value": 3  
  },  
  "roadImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:N202",  
        "segmentImpacted": [  
          "urn:ngsi-ld:RoadSegment:N202-12",  
          "urn:ngsi-ld:RoadSegment:N202-13"  
        ]  
      },  
      {  
        "roadImpacted": "Road:D021",  
        "segmentImpacted": [  
          "12",  
          "13",  
          "14",  
          "15"  
        ]  
      },  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:D032",  
        "segmentArea": {  
          "type": "LineString",  
          "coordinates": [  
            [  
              102.0,  
              0.0  
            ],  
            [  
              103.0,  
              1.0  
            ],  
            [  
              104.0,  
              0.0  
            ],  
            [  
              105.0,  
              1.0  
            ]  
          ]  
        }  
      }  
    ]  
  },  
  "allowedVehicle": {  
    "type": "array",  
    "value": [  
      "companiesTrucks",  
      "emergencyVehicle",  
      "firefighters",  
      "police"  
    ]  
  },  
  "maxAuthorizedTonnage": {  
    "type": "array",  
    "value": [  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:N202",  
        "maxTonnage": 30  
      },  
      {  
        "roadImpacted": "Road:D021",  
        "maxTonnage": 20  
      },  
      {  
        "roadImpacted": "urn:ngsi-ld:Road:D032",  
        "maxTonnage": 15.2  
      }  
    ]  
  },  
  "countOfBusLineImpacted": {  
    "type": "number",  
    "value": 1  
  },  
  "busImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
      }  
    ]  
  },  
  "countOfTramwayLineImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "tramwayImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "TramWayLine:L01",  
        "segmentImpacted": [  
          "urn:ngsi-ld:TramWaySegment:L01-12",  
          "urn:ngsi-ld:TramWaySegment:L01-19"  
        ]  
      },  
      {  
        "lineImpacted": "TramWayLine:L03",  
        "segmentImpacted": [  
          "urn:ngsi-ld:TramWaySegment:L03-19"  
        ]  
      }  
    ]  
  },  
  "countOfRailwayLineImpacted": {  
    "type": "number",  
    "value": 1  
  },  
  "railwayImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "lineImpacted": "Nice-Grasse",  
        "segmentImpact": [  
          "Nice Saint Augustin section"  
        ]  
      }  
    ]  
  },  
  "countOfSchoolImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "schoolImpacted": {  
    "type": "array",  
    "value": [  
      "Lycée Massena",  
      "Université Campus Saint Jean"  
    ]  
  },  
  "countOfStationImpacted": {  
    "type": "number",  
    "value": 4  
  },  
  "stationImpacted": {  
    "type": "array",  
    "value": [  
      {  
        "stationType": "bus",  
        "stationId": [  
          "urn:ngsi-ld:station:L205-S13",  
          "urn:ngsi-ld:station:L205-S14"  
        ]  
      },  
      {  
        "stationType": "tram",  
        "stationId": [  
          "L01-S12",  
          "L01-S19"  
        ]  
      }  
    ]  
  },  
  "countOfEventImpacted": {  
    "type": "number",  
    "value": 2  
  },  
  "eventsImpact": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
      "NiceMarathon"  
    ]  
  }  
}  
```  
#### CityWork NGSI-LD key-values Example    
Here is an example of a CityWork in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
    "type": "CityWork",  
    "allowedVehicle": [  
        "firefighters",  
        "police",  
        "emergencyVehicle",  
        "companiesTrucks"  
    ],  
    "alternateName": "AirPort global Observation",  
    "areaServed": "Nice Aeroport",  
    "busImpacted": [  
        {  
            "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
        }  
    ],  
    "contactPoint": {  
        "name": "Service des AO"  
    },  
    "contractingAuthority": "MNCA - subwaypole Nice Cote d'Azur",  
    "countOfBusLineImpacted": 1,  
    "countOfDerogation": 2,  
    "countOfEventImpacted": 2,  
    "countOfRailwayLineImpacted": 1,  
    "countOfRoadImpacted": 3,  
    "countOfSchoolImpacted": 2,  
    "countOfStationImpacted": 4,  
    "countOfTramwayLineImpacted": 2,  
    "dateLastReported": "2020-04-02T10:30:00Z",  
    "decrees": [  
        "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
        "CW-2020Q2-006",  
        "CW-2020Q2-006-Av-001",  
        "CW-2020Q2-006-Av-002"  
    ],  
    "derogation": [  
        {  
            "derogationType": "Work Nigth during Workday",  
            "startDate": "2020-05-11T20:30:00Z",  
            "endDate": "2020-05-15T23:30:00",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ]  
        },  
        {  
            "derogationType": "BRH",  
            "startDate": "2020-05-13T20:30:00Z",  
            "endDate": "2020-05-13T23:30:00Z",  
            "dayOfWeek": [  
                "Wednesday"  
            ]  
        }  
    ],  
    "description": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals",  
    "encroachment": [  
        "public",  
        "private"  
    ],  
    "endDate": "2020-04-22T18:45:00Z",  
    "eventsImpact": [  
        "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
        "NiceMarathon"  
    ],  
    "infrastructureFunction": [  
        "distribution",  
        "collection"  
    ],  
    "isMainRoadImpactedHTR": true,  
    "isMobile": false,  
    "location": {  
        "type": "Polygon",  
        "coordinates": [  
            [  
                43.20315,  
                7.20186  
            ],  
            [  
                43.20384,  
                7.20372  
            ],  
            [  
                43.20388,  
                7.20493  
            ],  
            [  
                43.19938,  
                7.20312  
            ],  
            [  
                43.20045,  
                7.20152  
            ],  
            [  
                43.20315,  
                7.20186  
            ]  
        ]  
    },  
    "mainContractingCompagny": "XRP - NICOLSPA",  
    "maxAuthorizedTonnage": [  
        {  
            "roadImpacted": "urn:ngsi-ld:Road:N202",  
            "maxTonnage": 30  
        },  
        {  
            "roadImpacted": "Road:D021",  
            "maxTonnage": 20  
        },  
        {  
            "roadImpacted": "urn:ngsi-ld:Road:D032",  
            "maxTonnage": 15.2  
        }  
    ],  
    "name": "Nce-Airport-CW2020Q2-006",  
    "openingHoursSpecification": [  
        {  
            "dayOfWeek": "Monday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Tuesday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Wednesday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Thursday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Friday",  
            "opens": "07:00:00",  
            "closes": "20:00:00"  
        },  
        {  
            "dayOfWeek": "Saturday",  
            "opens": "08:30:00",  
            "closes": "17:00:00"  
        }  
    ],  
    "othersContractingCompagny": [  
        "VRD - Terrassement Nicois",  
        "ELEC - Electricite de Nice",  
        "NUM - Consortium operateur"  
    ],  
    "railwayImpacted": [  
        {  
            "lineImpacted": "Nice-Grasse",  
            "segmentImpact": [  
                "Nice Saint Augustin section"  
            ]  
        }  
    ],  
    "roadImpacted": [  
        {  
            "roadId": "urn:ngsi-ld:Road:N202",  
            "segmentImpacted": [  
                "urn:ngsi-ld:RoadSegment:N202-12",  
                "urn:ngsi-ld:RoadSegment:N202-13"  
            ]  
        },  
        {  
            "roadId": "Road:D021",  
            "segmentImpacted": [  
                "12",  
                "13",  
                "14",  
                "15"  
            ]  
        },  
        {  
            "roadId": "urn:ngsi-ld:Road:D032",  
            "segmentArea": {  
                "type": "LineString",  
                "coordinates": [  
                    [  
                        102.0,  
                        0.0  
                    ],  
                    [  
                        103.0,  
                        1.0  
                    ],  
                    [  
                        104.0,  
                        0.0  
                    ],  
                    [  
                        105.0,  
                        1.0  
                    ]  
                ]  
            }  
        }  
    ],  
    "schoolImpacted": [  
        "Lyc\u00e9e Massena",  
        "Universit\u00e9 Campus Saint Jean"  
    ],  
    "startDate": "2020-03-17T08:45:00Z",  
    "stationImpacted": [  
        {  
            "stationType": "bus",  
            "stationId": [  
                "urn:ngsi-ld:station:L205-S13",  
                "urn:ngsi-ld:station:L205-S14"  
            ]  
        },  
        {  
            "stationType": "tram",  
            "stationId": [  
                "L01-S12",  
                "L01-S19"  
            ]  
        }  
    ],  
    "territorialArea": "subwaypole Nice",  
    "tramwayImpacted": [  
        {  
            "lineImpacted": "TramWayLine:L01",  
            "segmentImpacted": [  
                "urn:ngsi-ld:TramWaySegment:L01-12",  
                "urn:ngsi-ld:TramWaySegment:L01-19"  
            ]  
        },  
        {  
            "lineImpacted": "TramWayLine:L03",  
            "segmentImpacted": [  
                "urn:ngsi-ld:TramWaySegment:L03-19"  
            ]  
        }  
    ],  
    "typeOfInterventionRequest": "authorizationRequest",  
    "workDate": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z",  
    "workDisposition": [  
        {  
            "disposition": "laneReduction",  
            "startDate": "2020-05-11T08:00:00Z",  
            "endDate": "2020-05-15T18:30:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ],  
            "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
        },  
        {  
            "disposition": "sidewalkReduction",  
            "startDate": "2020-05-12T00:00:00Z",  
            "endDate": "2020-05-14T24:00:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ]  
        },  
        {  
            "disposition": "alternatingLights",  
            "startDate": "2020-05-11T08:00:00Z",  
            "endDate": "2020-05-15T18:30:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday"  
            ]  
        },  
        {  
            "disposition": "speedReduction",  
            "startDate": "2020-05-12T00:00:00Z",  
            "dayOfWeek": [  
                "Monday",  
                "Tuesday",  
                "Wednesday",  
                "Thursday",  
                "Friday",  
                "Saturday",  
                "Sunday"  
            ],  
            "comment": "Speed Switching from 2 lanes to 1 lane"  
        }  
    ],  
    "workLastDateUpdate": "2020-03-17T08:45:00Z",  
    "workLevel": [  
        "ground",  
        "underground"  
    ],  
    "workNature": [  
        "landFill",  
        "repair",  
        "tonnageExemption",  
        "securingPerimeter",  
        "trenchOpening",  
        "tarring"  
    ],  
    "workNumber": "CW2020Q2-006",  
    "workOtherImpact": [  
        "layingCablesOnGround",  
        "shopsTerrace"  
    ],  
    "workReason": [  
        "sagging",  
        "powerCut"  
    ],  
    "workState": "open",  
    "workTarget": [  
        "roads",  
        "pavement",  
        "electricityNetworks",  
        "opticalFibers",  
        "videoNetworks",  
        "vrd"  
    ],  
    "workZone": [  
        "road",  
        "sideWalk",  
        "busCorridor",  
        "tramwayLine"  
    ],  
    "@context": [  
        "https://smartdatamodels.org/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld"  
    ]  
}  
```  
#### CityWork NGSI-LD normalized Example    
Here is an example of a CityWork in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:CityWork:CityWork:MNCA-CW-2020Q2-006",  
    "type": "CityWork",  
    "alternateName": {  
        "type": "Property",  
        "value": "AirPort global Observation"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Aeroport"  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": "Service des AO"  
    },  
    "contractingAuthority": {  
        "type": "Property",  
        "value": "MNCA - subwaypole Nice Cote d'Azur"  
    },  
    "dateLastReported": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2020-04-02T10:30:00Z"  
        }  
    },  
    "decrees": {  
        "type": "Property",  
        "value": [  
            "https://MNCA/CityWork/Decree/CW-2020Q2-006",  
            "CW-2020Q2-006",  
            "CW-2020Q2-006-Av-001",  
            "CW-2020Q2-006-Av-002"  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "Widening work on access roads and installation of a new electrical and digital network for the connection of T1 & T2 terminals"  
    },  
    "encroachment": {  
        "type": "Property",  
        "value": [  
            "private",  
            "public"  
        ]  
    },  
    "endDate": {  
        "type": "DateTime",  
        "value": "2020-04-22T18:45:00Z"  
    },  
    "infrastructureFunction": {  
        "type": "Property",  
        "value": [  
            "collection",  
            "distribution"  
        ]  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Polygon",  
            "coordinates": [  
                [  
                    43.20315,  
                    7.20186  
                ],  
                [  
                    43.20384,  
                    7.20372  
                ],  
                [  
                    43.20388,  
                    7.20493  
                ],  
                [  
                    43.19938,  
                    7.20312  
                ],  
                [  
                    43.20045,  
                    7.20152  
                ],  
                [  
                    43.20315,  
                    7.20186  
                ]  
            ]  
        }  
    },  
    "mainContractingCompany": {  
        "type": "Property",  
        "value": "XRP - NICOLSPA"  
    },  
    "name": {  
        "type": "Property",  
        "value": "Nce-Airport-CW2020Q2-006"  
    },  
    "openingHoursSpecification": {  
        "type": "Property",  
        "value": [  
            {  
                "dayOfWeek": "Monday",  
                "Opens": "07.00",  
                "closes": "20.00"  
            },  
            {  
                "dayOfWeek": "Tuesday",  
                "Opens": "07.00",  
                "closes": "20.00"  
            },  
            {  
                "dayOfWeek": "Wednesday",  
                "Opens": "07.00",  
                "closes": "20.00"  
            },  
            {  
                "dayOfWeek": "Thursday",  
                "Opens": "07.00",  
                "closes": "20.00"  
            },  
            {  
                "dayOfWeek": "Friday",  
                "Opens": "07.00",  
                "closes": "20.00"  
            },  
            {  
                "dayOfWeek": "Saturday",  
                "Opens": "08.30",  
                "closes": "17.00"  
            }  
        ]  
    },  
    "othersContractingCompany": {  
        "type": "Property",  
        "value": [  
            "VRD - Terrassement Nicois",  
            "ELEC - Electricite de Nice",  
            "NUM - Consortium operateur"  
        ]  
    },  
    "startDate": {  
        "type": "DateTime",  
        "value": "2020-03-17T08:45:00Z"  
    },  
    "territorialArea": {  
        "type": "Property",  
        "value": "subwaypole Nice"  
    },  
    "typeOfInteventionRequest": {  
        "type": "Property",  
        "value": "authorizationRequest"  
    },  
    "workDate": {  
        "type": "DateTime",  
        "value": "2020-03-17T08:45:00Z/2020-04-22T18:45:00Z"  
    },  
    "workDisposition": {  
        "type": "Property",  
        "value": [  
            {  
                "disposition": "laneReduction",  
                "startDate": "2020-05-11T08:00:00Z",  
                "endDate": "2020-05-15T18:30:00Z",  
                "dayOfWeek": [  
                    "Monday",  
                    "Tuesday",  
                    "Wednesday",  
                    "Thursday",  
                    "Friday"  
                ],  
                "comment": "Switching from 2 lanes to 1 lane - BusCorridor not available"  
            },  
            {  
                "disposition": "sidewalkReduction",  
                "startDate": "2020-05-12T00:00:00Z",  
                "endDate": "2020-05-14T24:00:00Z",  
                "dayOfWeek": [  
                    "Monday",  
                    "Tuesday",  
                    "Wednesday",  
                    "Thursday",  
                    "Friday",  
                    "Saturday",  
                    "Sunday"  
                ]  
            },  
            {  
                "disposition": "alternatingLights",  
                "startDate": "2020-05-11T08:00:00Z",  
                "endDate": "2020-05-15T18:30:00Z",  
                "dayOfWeek": [  
                    "Monday",  
                    "Tuesday",  
                    "Wednesday",  
                    "Thursday",  
                    "Friday"  
                ]  
            },  
            {  
                "disposition": "speedReduction",  
                "startDate": "2020-05-12T00:00:00Z",  
                "dayOfWeek": [  
                    "Monday",  
                    "Tuesday",  
                    "Wednesday",  
                    "Thursday",  
                    "Friday",  
                    "Saturday",  
                    "Sunday"  
                ],  
                "comment": "Speed Switching from 2 lanes to 1 lane"  
            }  
        ],  
        "workOtherImpact": {  
            "type": "Property",  
            "value": [  
                "layingCablesOnGround",  
                "shopsTerrace"  
            ]  
        },  
        "isMobile": {  
            "type": "Property",  
            "value": false  
        },  
        "countOfDerogation": {  
            "type": "Property",  
            "value": 2  
        },  
        "derogation": {  
            "type": "Property",  
            "value": [  
                {  
                    "derogationType": "Work Nigth during Workday",  
                    "startDate": "2020-05-11T20:30:00Z",  
                    "endDate": "2020-05-15T23:30:00",  
                    "dayOfWeek": [  
                        "Monday",  
                        "Tuesday",  
                        "Wednesday",  
                        "Thursday",  
                        "Friday",  
                        "Saturday",  
                        "Sunday"  
                    ]  
                },  
                {  
                    "derogationType": "BRH",  
                    "startDate": "2020-05-13T20:30:00Z ",  
                    "endDate": "2020-05-13T23:30:00Z",  
                    "dayOfWeek": "Wednesday"  
                }  
            ]  
        },  
        "isMainRoadImpactedHTR": {  
            "type": "Property",  
            "value": true  
        },  
        "countOfRoadImpacted": {  
            "type": "Property",  
            "value": 3  
        },  
        "roadImpacted": {  
            "type": "Property",  
            "value": [  
                {  
                    "roadId": "urn:ngsi-ld:Road:N202",  
                    "segmentId": [  
                        "urn:ngsi-ld:RoadSegment:N202-12",  
                        "urn:ngsi-ld:RoadSegment:N202-13"  
                    ]  
                },  
                {  
                    "roadId": "Road:D021",  
                    "segmentName": [  
                        "N\u00ba 12",  
                        "N\u00ba 13",  
                        "N\u00ba 14"  
                    ]  
                },  
                {  
                    "roadId": "urn:ngsi-ld:Road:D032",  
                    "segmentLocation": [  
                        {  
                            "type": "LineString",  
                            "coordinates": [  
                                [  
                                    102.0,  
                                    0.0  
                                ],  
                                [  
                                    103.0,  
                                    1.0  
                                ],  
                                [  
                                    104.0,  
                                    0.0  
                                ],  
                                [  
                                    105.0,  
                                    1.0  
                                ]  
                            ]  
                        },  
                        {  
                            "type": "Point",  
                            "coordinates": [  
                                43.655675,  
                                7.161232  
                            ]  
                        }  
                    ]  
                },  
                {  
                    "roadLocation": {  
                        "type": "Point",  
                        "coordinates": [  
                            43.67428,  
                            7.161589  
                        ]  
                    }  
                }  
            ]  
        },  
        "allowedVehicle": {  
            "type": "Property",  
            "value": [  
                "companiesTrucks",  
                "emergencyVehicle",  
                "firefighters",  
                "police"  
            ]  
        },  
        "maxAuthorizedTonnage": {  
            "type": "Property",  
            "value": [  
                {  
                    "roadImpacted": "urn:ngsi-ld:Road:N202",  
                    "maxTonnage": 30  
                },  
                {  
                    "roadImpacted": "Road:D021",  
                    "maxTonnage": 20  
                },  
                {  
                    "roadImpacted": "urn:ngsi-ld:Road:D032",  
                    "maxTonnage": 15.2  
                }  
            ]  
        },  
        "countOfBusLineImpacted": {  
            "type": "Property",  
            "value": 1  
        },  
        "busImpacted": {  
            "type": "Property",  
            "value": [  
                {  
                    "lineImpacted": "urn:ngsi-ld:BusLine:L205"  
                }  
            ]  
        },  
        "countOfTramwayLineImpacted": {  
            "type": "Property",  
            "value": 2  
        },  
        "tramwayImpacted": {  
            "type": "Property ",  
            "value": [  
                {  
                    "lineImpacted": "TramWayLine:L01",  
                    "segmentImpacted": [  
                        "urn:ngsi-ld:TramWaySegment:L01-12",  
                        "urn:ngsi-ld:TramWaySegment:L01-19"  
                    ]  
                },  
                {  
                    "lineImpacted": "TramWayLine:L03",  
                    "segmentImpacted": [  
                        "urn:ngsi-ld:TramWaySegment:L03-19"  
                    ]  
                }  
            ]  
        },  
        "countOfRailwayLineImpacted": {  
            "type": "Property",  
            "value": 1  
        },  
        "railwayImpacted": {  
            "type": "Property ",  
            "value": [  
                {  
                    "lineImpacted": "Nice-Grasse",  
                    "segmentImpact": [  
                        "Nice Saint Augustin section"  
                    ]  
                }  
            ]  
        },  
        "countOfSchoolImpacted": {  
            "type": "Property",  
            "value": 2  
        },  
        "schoolImpacted": {  
            "type": "Property",  
            "value": [  
                "Lyc\u00e9e Massena",  
                "Universit\u00e9 Campus Saint Jean"  
            ]  
        },  
        "countOfStationImpacted": {  
            "type": "Property",  
            "value": 4  
        },  
        "stationImpacted": {  
            "type": "Property ",  
            "value": [  
                {  
                    "stationType": "bus",  
                    "stationId": [  
                        "urn:ngsi-ld:station:L205-S13",  
                        "urn:ngsi-ld:station:L205-S14"  
                    ]  
                },  
                {  
                    "stationType": "tram",  
                    "stationId": [  
                        "L01-S12",  
                        "L01-S19"  
                    ]  
                }  
            ]  
        },  
        "countOfEventImpacted": {  
            "type": "Property",  
            "value": 2  
        },  
        "eventsImpact": {  
            "type": "Property",  
            "value": [  
                "urn:ngsi-ld:events:MNCA-EV-JazzCimiez",  
                "NiceMarathon"  
            ]  
        },  
        "@context": [  
            "https://smartdatamodels.org/ld/context",  
            "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
        ]  
    },  
    "workLastDateUpdate": {  
        "type": "DateTime",  
        "value": "2020-03-17T08:45:00Z"  
    },  
    "workLevel": {  
        "type": "Property",  
        "value": [  
            "ground",  
            "underGround"  
        ]  
    },  
    "workNature": {  
        "type": "Property",  
        "value": [  
            "landFill",  
            "repair",  
            "securingPerimeter",  
            "tarring",  
            "tonnageExemption",  
            "trenchOpening"  
        ]  
    },  
    "workNumber": {  
        "type": "Property",  
        "value": "CW2020Q2-006"  
    },  
    "workReason": {  
        "type": "Property",  
        "value": [  
            "powerCut",  
            "sagging"  
        ]  
    },  
    "workState": {  
        "type": "Property",  
        "value": "open"  
    },  
    "workTarget": {  
        "type": "Property",  
        "value": [  
            "electricityNetworks",  
            "opticalFibers",  
            "pavement",  
            "roads",  
            "videoNetworks",  
            "vrd"  
        ]  
    },  
    "workZone": {  
        "type": "Property",  
        "value": [  
            "busCorridor",  
            "road",  
            "sideWalk",  
            "tramwayLine"  
        ]  
    }  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
