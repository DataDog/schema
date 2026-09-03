package schema

Fields: [string]: #Properties

Fields: Common: {
	"_dd.hostname": {
		title:       "Hostname"
		description: "Hostname of where the agent is running."
		type:        "string"
		default:     null
		examples: [
			"my-hostname",
		]
		minLength: 0
	}
	"span.kind": {
		title:       "Span Kind"
		description: "Span Kind"
		type:        "string"
		enum: ["client", "server", "producer", "consumer", "internal"]
	}
}
