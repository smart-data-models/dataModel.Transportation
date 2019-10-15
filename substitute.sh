#!/bin/sh

find . -type f -name "*schema.json" -exec sed -i bak -e 's/dataModels/data-models/g' {} +
