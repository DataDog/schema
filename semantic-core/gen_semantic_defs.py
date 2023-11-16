import json
import os
from pydantic import BaseModel, Field

class Fields(BaseModel):
    hostname: str = Field(min_length=1)

def generate_schema(version):
    json_schema_str = json.dumps(Fields.model_json_schema(), indent=2)

    # Create the directory if it doesn't exist
    output_dir = os.path.join(os.getcwd(), version)
    os.makedirs(output_dir, exist_ok=True)

    # Write the schema to the specified file
    output_file = os.path.join(output_dir, "schema.json")
    with open(output_file, "w") as f:
        f.write(json_schema_str)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate schema JSON file.")
    parser.add_argument("version", type=str, help="Specify the version")

    args = parser.parse_args()
    generate_schema(version=args.version)
