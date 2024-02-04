# Project to practice Python / Kafka / Flink / ElasticSearch / Kibana

## Architecture

![Flink_Kibana_project drawio](https://github.com/skalskibukowa/Project-Kafka-Flink-ElastichSearch/assets/29678557/0ea9a89c-2895-4c37-b9bd-9837f9f936a5)

## Overview

**1. Introduction**

Real-time data processing application built with Flink that consumes transaction data from an e-commerce service processes it, and stores the results in both a PostgreSQL database and Elasticsearch for further analysis and visualization. The application is packaged and deployed using Docker containers for ease of use and scalability.

**2. System Architecture**

Data Source: An e-commerce service acts as the real-time data source, generating transaction data streamed to Kafka.
Data Processing: Flink reads the data stream from Kafka, transforms it, and aggregates sales data by category, day, and month.
Data Storage:
PostgreSQL: Processed data is stored in a PostgreSQL database for querying and analysis.
Elasticsearch: Aggregated sales data is stored in Elasticsearch for efficient search and visualization.
Visualization: Kibana provides a user-friendly interface to explore and visualize the data stored in Elasticsearch.
3. Integration with Ecommerce Service

The Flink application seamlessly integrates with your e-commerce service through Kafka. The e-commerce service publishes transaction data to a Kafka topic, which Flink subscribes to and consumes the data for processing. This ensures real-time processing of sales data as it occurs in your e-commerce platform.

**4. Key Features**

Real-time processing: Continuously processes transactions as they occur in your e-commerce service.
Data aggregation: Calculates sales totals by category, day, and month for valuable business insights.
Database storage: Stores detailed transaction data and aggregated sales data in PostgreSQL for querying and analysis.
Search and visualization: Enables efficient exploration and visualization of aggregated sales data using Kibana, providing insights into customer behaviour, product performance, and sales trends.
Containerized deployment: Simplifies deployment and management of the application across different environments.

**5. Deployment and Configuration**

The Dockerfile and docker-compose.yml files provided specify how to build and run the application using Docker containers. You will need to configure environment variables for the Kafka server, Zookeeper server, PostgreSQL database connection details, and the Kafka topic where your ecommerce service publishes transaction data.

## Instructions for building and running a flink application with Kafka, PostgreSQL, ElasticSearch, Kibana

1. Build the "Ecommerce service" Docker image:

cd kafka-producer && docker build -t kafka-producer .

2. Build the "Flink" Docker image:

cd flink-processor && mvn clean package
docker build -t flink-processor .

3. Start the Docker containers:

docker-compose up -d

4. Verify PostgreSQL connection:
docker exec -it postgres-flink psql -U postgres -d postgres
\dt
