package schema

Span: {
	"title":     "Span"
	description: "Span"
	"type":      "object"
	"properties": {
		"service": {
			"description": "The name of the service with which this span is associated"
			"title":       "Service"
			"type":        "string"
		}
		"name": {
			"description": "The operation name of this span"
			"title":       "Name"
			"type":        "string"
		}
		"resource": {
			"description": "The resource name of this span, also sometimes called the endpoint (for web spans)"
			"title":       "Resource"
			"type":        "string"
		}
		"traceID": {
			"description": "The ID of the trace to which this span belongs"
			"title":       "Trace ID"
			// "type":        "integer"
			"type": "string"
		}
		"spanID": {
			"description": "The ID of this span"
			"title":       "Span ID"
			// "type":        "integer"
			"type": "string"
		}
		"parentID": {
			"default":     null
			"description": "The ID of this span's parent, or zero if this span has no parent"
			"title":       "Parent ID"
			// "type":        "integer"
			"type": "string"
		}
		"start": {
			"description": "The number of nanoseconds between the Unix epoch and the beginning of this span"
			"title":       "Start"
			// "type":        "integer"
			"type": "string"
		}
		"duration": {
			"description": "The time length of this span in nanoseconds"
			"title":       "Duration"
			// "type":        "integer"
			"type": "string"
		}
		"error": {
			"default":     null
			"description": "Error is 1 if there is an error associated with this span, or 0 if there is not"
			"title":       "Error"
			"type":        "integer"
		}
		"meta": {
			"additionalProperties": {
				"type": "string"
			}
			"default":     null
			"description": "Meta is a mapping from tag name to tag value for string-valued tags"
			"title":       "Meta"
			"type":        "object"
		}
		"metrics": {
			"additionalProperties": {
				"type": "number"
			}
			"default":     null
			"description": "Metrics is a mapping from tag name to tag value for numeric-valued tags"
			"title":       "Metrics"
			"type":        "object"
		}
		"type": {
			"default":     null
			"description": "Represents the type of the service with which this span is associated. Example values: `web`, `db`, `lambda`"
			"title":       "Type"
			"type":        "string"
		}
		"meta_struct": {
			"additionalProperties": {
				"type": "integer"
			}
			"default":     null
			"description": "Represents a registry of structured \"other\" data used by, e.g., AppSec"
			"title":       "Meta Struct"
			"type":        "object"
		}
	}
	"required": [
		"service",
		"name",
		"resource",
		"traceID",
		"spanID",
		"start",
		"duration",
	]
	"allOf": [
		{
			if: not: properties: type: enum: ["web", "db"]
			then: properties: meta: $ref: "#/$defs/BaseTags"
		},
		{
			if: {
				properties: type: const: "web"
				required: ["type"]
			}
			then: properties: meta: $ref: "#/$defs/HTTPTags"
		},
		{
			if: {
				properties: type: const: "db"
				required: ["type"]
			}
			then: properties: meta: $ref: "#/$defs/DBTags"
		},
	]
	$defs: {
		"BaseTags": BaseTags
		"HTTPTags": HTTPTags
		"DBTags":   DBTags
	}
}

BaseTags: {
	title:       "Base Tags"
	description: "Base Tags"
	properties: {
		Fields.Common
	}
	required: [
		// "_dd.hostname",
		"span.kind",
	]
}

HTTPTags: {
	title:       "HTTP Meta Tags"
	description: "HTTP Meta Tags"
	properties: {
		Fields.Common
		Fields.HTTP
	}
	required: BaseTags.required + [
		"http.status_code",
		"http.url",
		"http.method",
		// "http.version",
	]
}

DBTags: {
	title:       "HTTP DB Tags"
	description: "HTTP DB Tags"
	properties: {
		Fields.Common
		Fields.DB
	}
	required: BaseTags.required + [
		"db.system",
	]
}
