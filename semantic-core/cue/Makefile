all: fmt vet schemas check-jsonschema
.PHONY: all

schemas: schemas/agent-payload schemas/span
.PHONY: schemas

schemas/agent-payload:
	@mkdir -p gen/schemas && cue export . -e AgentPayload -o gen/schemas/agent_payload.json -f
.PHONY: schemas/agent-payload

schemas/span:
	@mkdir -p gen/schemas && cue export . -e Span -o gen/schemas/span.json -f
.PHONY: schemas/span

fmt:
	@cue fmt ./...
.PHONY: fmt

vet:
	@cue vet ./... -c
.PHONY: vet

check-jsonschema:
	@check-jsonschema --check-metaschema ./gen/schemas/*.json
.PHONY: check-jsonschema

fields:
	@mkdir -p gen && cue export . -e Fields -o gen/fields.json -f
.PHONY: fields
