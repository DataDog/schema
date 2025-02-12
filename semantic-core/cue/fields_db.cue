package schema

Fields: DB: {
	"db.system": {
		"description": "An identifier for the database management system (DBMS) product being used."
		"examples": [
			"mysql",
			"postgresql",
		]
		"type": "string"
		// TODO: use enum feature instead of pattern.
		"enum": ["adabas", "buntdb", "cache"]
		// "pattern":      "^(adabas|buntdb|cache|cassandra|cloudscape|cockroachdb|coldfusion|consul|cosmosdb|couchbase|couchdb|db2|derby|dynamodb|edb|elasticsearch|eloquent|filemaker|firebird|firstsql|geode|h2|hanadb|hbase|hive|hsqldb|informix|ingres|instantdb|interbase|leveldb|mariadb|maxdb|memcached|mongodb|mssql|mysql|neo4j|netezza|opensearch|oracle|other_sql|pervasive|pointbase|postgresql|presto|progress|redis|redshift|snowflake|sqlite|sybase|teradata|vertica)$"
		"title": "DB System"
	}
	"db.connection_string": {
		"default":     null
		"description": "The connection string used to connect to the database."
		"examples": [
			"Server=(localdb)\u000b11.0;Integrated Security=true;",
			"postgresql://localhost:5432",
		]
		"is_sensitive": true
		"title":        "DB Connection String"
		"type":         "string"
	}
	"db.user": {
		"default":     null
		"description": "Username for accessing the database."
		"examples": [
			"widget_user",
		]
		"title": "DB User"
		"type":  "string"
	}
	"db.name": {
		"default":     null
		"description": "The name of the database being connected to."
		"examples": [
			"customers",
		]
		"title": "DB Name"
		"type":  "string"
	}
	"db.statement": {
		"default":     null
		"description": "The database statement being executed."
		"examples": [
			"SELECT * FROM wuser_table', 'SET mykey \"WuValue",
		]
		"is_sensitive": true
		"title":        "DB Statement"
		"type":         "string"
	}
	"db.operation": {
		"default":     null
		"description": "The name of the operation being executed, e.g. the MongoDB command name such as findAndModify, or the SQL keyword."
		"examples": [
			"findAndModify",
			"HMSET",
			"SELECT",
		]
		"title": "DB Operation"
		"type":  "string"
	}
	"db.sql.table": {
		"default":     null
		"description": "The name of the primary table that the operation is acting upon, including the database name (if applicable)."
		"examples": [
			"customers",
		]
		"title": "DB SQL Table"
		"type":  "string"
	}
	"db.row_count": {
		"default":     null
		"description": "\nThe number of rows/results from the query or operation. For caches and other datastores, i.e. Redis, this tag should only set for operations that retrieve stored data,\nsuch as GET operations and queries, excluding SET and other commands not returning data. "
		"examples": [
			"customers",
		]
		"minimum": 0
		"title":   "DB Row Count"
		"type":    "integer"
	}
}
