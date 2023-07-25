# Schema (v2)
Service Definition Schema is a JSON Schema that can be used to define metadata about a service in Datadog's Service Catalog. The latest schema version is v2. The schema is often used to: 
* Communicate a set of accepted metadata fields for a service
* Provide client side validations against user defined metadata files
* Add auto completion and validation in popular IDEs for user defined metadata files

# What is the Service Catalog?
Service Catalog is a new Datadog product that allows you to easily manage service ownership at scale and identify dependencies in complex, microservice-based applications. Built on top of the unified Datadog observability platform, Service Catalog helps you:

* Streamline root-cause investigations via a unified observability tool that leverages built-in integrations for Slack, PagerDuty, and Source Code 
* Automatically discover hundreds of APM services and RUM applications to quickly find owners, on-call engineers, and critical resources with minimal engineering effort
* Shorten new hire onboarding time with out-of-the-box answers to questions about system architecture, ownership, and different types of telemetry 

![service-catalog](../images/service-catalog.jpg)

# Getting Started
Check out our [onboarding guide](https://docs.datadoghq.com/tracing/service_catalog/setup) on how to get started. 

![sc-getting-started](../images/sc-getting-started.png)

# Documentation 
* [Product Overview](https://docs.datadoghq.com/tracing/faq/service_catalog/)
* [Service Definition Structure](https://docs.datadoghq.com/tracing/service_catalog/service_metadata_structure)
* [Service Definition API](https://docs.datadoghq.com/api/latest/service-definition/)
* [Understanding Your Service Configuration](https://docs.datadoghq.com/tracing/service_catalog/guides/understanding-service-configuration/)
* [Troubleshooting Guide](https://docs.datadoghq.com/tracing/service_catalog/troubleshooting)
* [JSON Schema Store](https://raw.githubusercontent.com/DataDog/schema/main/service-catalog/version.schema.json)
