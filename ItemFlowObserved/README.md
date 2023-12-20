[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
# ItemFlowObserved
Version: 0.0.2

## Description 

The data model intended to measure an observation linked to the movement of an item at a certain location and over a given period. This Data Model proposes an evolution of two Data Model by merging them and integrating all the attributes of the initial version of [TrafficFlowObserved] and [CrowFlowObserved] and by extension any type of item that we want to analyze the movements. Attributes `vehicleType` and `vehicleSubType` are removed from the initial data Model in order to become generic `itemType` and `itemSubType` of possible values. (people, Type of vehicle, Type of boat, Type of plane, ...).
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Transportation/ItemFlowObserved/swagger.yaml)

Link to the [specification](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec.md)

Enlace a la [Especificación en español](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec_ES.md)

Lien vers le [spécification en français](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec_FR.md)

Link zur [deutschen Spezifikation](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec_DE.md)

Link alla [specifica](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec_IT.md)

[仕様へのリンク](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec_JA.md)

[链接到规范](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec_ZH.md)

[사양 링크](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/doc/spec_KO.md)
### Examples

Link to the [example](https://smart-data-models.github.io/dataModel.Transportation/ItemFlowObserved/examples/example.json) (keyvalues) for NGSI v2

Link to the [example](https://smart-data-models.github.io/dataModel.Transportation/ItemFlowObserved/examples/example.jsonld) (keyvalues) for NGSI-LD

Link to the [example](https://smart-data-models.github.io/dataModel.Transportation/ItemFlowObserved/examples/example-normalized.json) (normalized) for NGSI-V2

Link to the [example](https://smart-data-models.github.io/dataModel.Transportation/ItemFlowObserved/examples/example-normalized.jsonld) (normalized) for NGSI-LD

Link to the [example](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/examples/example.json.csv) (keyvalues) for NGSI v2 in CSV format

Link to the [example](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/examples/example.jsonld.csv) (keyvalues) for NGSI-LD in CSV format

Link to the [example](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/examples/example-normalized.json.csv) (normalized) for NGSI-V2 in CSV format

Link to the [example](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/examples/example-normalized.jsonld.csv) (normalized) for NGSI-LD in CSV format
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/ItemFlowObserved/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/ItemFlowObserved/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/geojson_features_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/ItemFlowObserved/schema.json&email=info@smartdatamodels.org) of geojson feature format payloads compliant with this data model. Refresh for new values
### PostgreSQL schema

Link to the [PostgreSQL schema](https://github.com/smart-data-models/dataModel.Transportation/blob/master/ItemFlowObserved/schema.sql) of this data model
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.Transportation/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.Transportation/pulls)

 If you wish to develop your own data model you can start from [contribution manual](https://bit.ly/contribution_manual). Several services have been developed to help with: 
 - [Test data model repository](https://smartdatamodels.org/index.php/data-models-contribution-api/) including the schema and example payloads, etc
 - [Generate PostgreSQL schema](https://smartdatamodels.org/index.php/sql-service/) to help create a table, create type, etc