package schema

// AgentPayload represents the JSON Schema to validate Agent payloads.
AgentPayload: #JSONSchema & {
	"title":     "AgentPayload"
	description: "Represents the generic semantics for the agent payload, structurally defined here: https://github.com/DataDog/datadog-agent/blob/main/pkg/proto/datadog/trace/agent_payload.proto"
	"type":      "object"
	properties: {
		hostName: Fields.Common["_dd.hostname"]
		"env": {
			"default":     null
			"description": "Specifies the 'env' set in the agent's configuration."
			"minLength":   1
			"title":       "Env"
			"type":        "string"
		}
		"tags": {
			"additionalProperties": {
				"type": "string"
			}
			"default":     null
			"description": "Tags specifies tags common in all `tracerPayloads`"
			"title":       "Tags"
			"type":        "object"
		}
		"agentVersion": {
			"description": "Specifies version of the agent"
			"minLength":   1
			"title":       "Agent Version"
			"type":        "string"
		}
		"targetTPS": {
			"description":      "Holds `TargetTPS` value in AgentConfig"
			"exclusiveMinimum": 0.0
			"title":            "Target TPS"
			"type":             "number"
		}
		"errorTPS": {
			"description":      "Holds `ErrorTPS` value in AgentConfig"
			"exclusiveMinimum": 0.0
			"title":            "Error TPS"
			"type":             "number"
		}
		"rareSamplerEnabled": {
			"default":     null
			"description": "Holds `RareSamplerEnabled` value in AgentConfig"
			"title":       "Rare Sampler Flag"
			"type":        "boolean"
		}
		tracerPayloads: {
			"title":       "Tracer Payloads"
			"description": "Specifies the list of the payloads received from tracers"
			"items": {
				"$ref": "#/$defs/TracerPayload"
			}
			"type": "array"
		}
	}
	"required": [
		"agentVersion",
		"targetTPS",
		"errorTPS",
		"tracerPayloads",
	]
	$defs: {
		"TracerPayload": TracerPayload
		"TraceChunk":    TraceChunk
		"Span":          Span
		Span.$defs
	}
}

TracerPayload: {
	"title":     "TracerPayload"
	description: "Tracer Payload"
	"type":      "object"
	"properties": {
		"containerID": {
			"default":     null
			"description": "Specifies the ID of the container where the tracer is running on"
			"title":       "Container ID"
			"type":        "string"
		}
		"languageName": {
			"description": "Specifies the language of the tracer"
			// "pattern":     "^(golang|python|php|ruby|jvm|dotnet|js)$"
			"title": "Language Name"
			"type":  "string"
			enum: ["go", "python", "php", "ruby", "jvm", "dotnet", "js"]
		}
		"languageVersion": {
			"description": "Specifies the language version of the tracer"
			"title":       "Language Version"
			"type":        "string"
		}
		"tracerVersion": {
			"description": "Specifies the version of the tracer"
			"title":       "Tracer Version"
			"type":        "string"
		}
		"runtimeID": {
			"default":     null
			"description": "Specifies V4 UUID representation of a tracer session"
			"title":       "Runtime ID"
			"type":        "string"
		}
		"chunks": {
			"description": "Specifies the list of containing trace chunks"
			"items": {
				"$ref": "#/$defs/TraceChunk"
			}
			"title": "Trace Chunks"
			"type":  "array"
		}
		"tags": {
			"additionalProperties": {
				"type": "string"
			}
			"default":     null
			"description": "Specifies the list of tags common in all Trace Chunks"
			"title":       "Trace Tags"
			"type":        "object"
		}
		"env": {
			"description": "Specifies the `env` tag that is set in the tracer configuration"
			"title":       "Env"
			"type":        "string"
		}
		"hostname": {
			"default":     null
			"description": "Specifies the hostname where the tracer is running"
			"title":       "Hostname"
			"type":        "string"
		}
		"appVersion": {
			"description": "Specifies the `version` tag that set in the tracer configuration"
			"title":       "App Version"
			"type":        "string"
		}
	}
	"required": [
		"languageName",
		"languageVersion",
		"tracerVersion",
		"chunks",
		"env",
		"appVersion",
	]
}

TraceChunk: {
	"title":     "TraceChunk"
	description: "Trace Chunk"
	"type":      "object"
	"properties": {
		"priority": {
			"description": "Specifies the sampling priority of the trace"
			"title":       "Priority"
			"type":        "integer"
		}
		"origin": {
			"default":     null
			"description": "Specifies the origin product (`lambda`, `rum`, etc.) of the trace"
			"title":       "Origin"
			"type":        "string"
		}
		"spans": {
			"description": "Specifies the list of containing spans"
			"items": {
				"$ref": "#/$defs/Span"
			}
			"title": "Spans"
			"type":  "array"
		}
		"tags": {
			"additionalProperties": {
				"type": "string"
			}
			"default":     null
			"description": "Specifies the list of tags common in all Spans"
			"title":       "Tags"
			"type":        "object"
		}
		"droppedTrace": {
			"default":     null
			"description": "Specifies whether the trace was dropped by samplers or not"
			"title":       "Dropped Trace"
			"type":        "boolean"
		}
	}
	"required": [
		"priority",
		"spans",
	]
}
