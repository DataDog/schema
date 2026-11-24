# Datadog Agent configuration schemas

JSON Schemas for the configuration files of the [Datadog Agent](https://github.com/DataDog/datadog-agent):

- `datadog.schema.json` validates `datadog.yaml`.
- `system-probe.schema.json` validates `system-probe.yaml`.

They let your IDE autocomplete and validate the Agent configuration, and let CI tools check a configuration before it's deployed. They're generated from the Agent's own configuration schema ([`pkg/config/schema/yaml`](https://github.com/DataDog/datadog-agent/tree/main/pkg/config/schema/yaml)), the same one the Agent uses to validate its configuration at runtime.

## Versions

Each Agent release has its own copy of the schemas, matching the settings of that exact version. A copy of the latest release is also available at the root of this folder.

```
datadog-agent/
├── datadog.schema.json          latest release
├── system-probe.schema.json     latest release
└── v<version>/                  one folder per Agent release, e.g. v7.87.1
    ├── datadog.schema.json
    └── system-probe.schema.json
```

| Schema | Latest release | Specific Agent version |
| --- | --- | --- |
| `datadog.yaml` | `https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/datadog.schema.json` | `https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/v7.87.1/datadog.schema.json` |
| `system-probe.yaml` | `https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/system-probe.schema.json` | `https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/v7.87.1/system-probe.schema.json` |

Use the version of the Agent you run, so the schema matches its settings exactly: a newer schema may describe settings your Agent doesn't know yet.

## Usage

### VS Code

With the [YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml), add this line at the top of your `datadog.yaml`:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/v7.87.1/datadog.schema.json
```

Or map the schemas to the configuration files in your VS Code `settings.json`:

```json
"yaml.schemas": {
  "https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/datadog.schema.json": "datadog.yaml",
  "https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/system-probe.schema.json": "system-probe.yaml"
}
```

### Command line

For example with [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema):

```sh
check-jsonschema --schemafile https://raw.githubusercontent.com/DataDog/schema/main/datadog-agent/v7.87.1/datadog.schema.json /etc/datadog-agent/datadog.yaml
```

## What the schemas contain

- Every setting of the configuration file, with its type and the values it accepts.
- The schemas follow [JSON Schema draft 2020-12](https://json-schema.org/draft/2020-12) and work with any conforming library. Their only non-standard keyword is `patternErrorMessage`, the message VS Code shows when a duration or a URL is invalid; other tools ignore it.

## Publishing

The schemas are published by the Agent release pipeline, which opens a pull request to this repository for each Agent release. Don't edit them by hand: fix the Agent's configuration schema instead, and the next release publishes the change.
