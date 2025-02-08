## Resource Service

**Description:** The Resource service is responsible for managing all resources, including creation, update, validation, search, and tagging.

**Diagram:**

![Resource Service Diagram](./resource-service-diagram.png)

**Database:**

* **Resources:**
    * id (bigint, PK)
    * title (varchar)
    * type (varchar)
    * link (varchar)
    * timestamp (timestamp)
    * created_at (timestamp)

**API:**

* **Create Resource:** Creates a new resource.
* **Update Resource:** Updates an existing resource.
* **Validate URLs:** Validates URLs associated with resources.
* **Search Resources:** Searches for resources based on specific criteria.
* **Tag Resources:** Tags resources with relevant keywords.

**Business Logic:**

* **Process:** Handles resource creation, update, and validation requests.
* **Publish:** Publishes events related to resource updates.
* **Validate URL:** Validates the URL of a resource using an external URL validator.

**Event Bus:**

* **Resource Updated:** Published when a resource is updated.
* **Resource Created:** Published when a new resource is created.

**External Services:**

* **URL Validator:** Validates URLs.
* **Project Service:** Handles resource linking to projects.

**Database Relationships:**

* **Resources** has many **Project Resources**.
* **Resources** has many **Project Resources** through **Project Resources**.

**Dependencies:**

* **Project Service:** Used for resource linking to projects.
* **URL Validator:** Validates URLs.

**Data Flow:**

* Client applications (web/mobile) send requests to the API Gateway.
* The API Gateway routes requests to the Resource Service.
* The Resource Service processes requests, interacts with the database, and publishes events.
* External services, such as the URL Validator and Project Service, are called to fulfill certain tasks.
* Event Publishing Service receives events and processes them.
* User and Project services are notified of resource-related events.

**Notes:**

* The Resource service uses a Redis cache to improve performance.
* The service employs robust validation logic to ensure the integrity of resources.
* The service adheres to secure coding practices to protect sensitive data.
