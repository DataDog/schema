# semantic-core

Playground repo for the Semantic Core

## Setup

```
cd generation  
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Generate json schema

### Notes on schema generation and naming:

**General:**

- Run these commands from the generate directory

**Options:**

- Release/Draft (default: Draft): If this is a draft, the results are stored in schema/drafts, otherwise schema/releases
- Patch/Minor/Major (default Minor): What kind of update this is. This impacts which part of the version is updated
- Version: The version of the schema will be the latest version found in schema/releases modified by the type (patch/minor/major)

**Examples**

This will output a schema.json file in the ./schema/drafts directory:
```
# Creates a schema under 'schema/drafts/v{NEXT}'
./gen_semantic_defs.py generate
```

To create a new release version:
```
# Creates schema under 'schema/releases/v{NEXT}'
./gen_semantic_defs.py generate --release
```

To create a new major version:
```
./gen_semantic_defs.py generate --release-type major
``````

To create a new patch version:
```
python3 gen_semantic_defs.py --release-type patch
```