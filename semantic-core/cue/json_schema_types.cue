package schema

// #Property defines a property as defined in JSON Schema: https://json-schema.org/understanding-json-schema/reference/object#properties
#Property: {
	title:       string
	description: string
	examples?: [...]
	default?:          _
	exclusiveMinimum?: number
	minLength?:        number
	type:              #Type
	enum?: [...string]
	pattern?: string
	minimum?: number

	if type == "object" {
		additionalProperties: bool | {type: #Type}
	}

	if type == "array" {
		"items": {
			"$ref"?: string
			type?:   #Type
		}
	}

	// custom stuff
	is_sensitive: bool | *false
}

// #JSONSchema defines a schema from JSON Schema: https://json-schema.org/understanding-json-schema/reference
#JSONSchema: {
	title:       string
	description: string
	properties:  #Properties
	type?:       #Type
	required?: [...string]
	$defs?: [string]: #JSONSchema
	allOf?: [...]
}

// Properties defines a map of properties
#Properties: [string]: #Property

// Type represents all the available types in JSON Schema
#Type: "string" | "integer" | "number" | "object" | "boolean" | "array"
