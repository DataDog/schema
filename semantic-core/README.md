# semantic-core

Playground repo for the Semantic Core

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install pydantic
```

## Generate json schema

This will output a schema.json file in the [VERSION] directory:

```
python3 gen_semantic_defs.py [VERSION]
```

Example:

```
python3 gen_semantic_defs.py v1
```
creates the `v1` directory if necessary, and writes the schema.json file.
