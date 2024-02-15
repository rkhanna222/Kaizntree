# Kaizntree

# Kaizntree Full-Stack Take Home Challenge

## Overview

The goal of this project is to develop a set of RESTful API endpoints using Django REST Framework to serve data to front-end dashboards, specifically modeled after the Kaizntree's item dashboard. The project also includes a front-end application developed with React to consume the API and display the data.

## Figma Design

The UI design for the dashboard is provided in the following Figma file:
[View Figma Design](https://www.figma.com/file/fjzPIi67Jk7WgW3gjeA0Tk/Kaizntree-Full-Stack-Interview-UI-Template?type=whiteboard&node-id=0%3A1&t=SKHJWhMLI4drSMio-1)

## Backend Setup

### Data Models

The backend is structured around the following Django models corresponding to the entities visible in the item dashboard:
- `Item`: Represents an item with attributes like SKU, name, category, tags, stock status, and available stock.

### Database Connection

The project uses SQLite for development due to its lightweight nature and ease of configuration. For production, a transition to PostgreSQL is recommended for its robustness and scalability.

### API Endpoints

#### Item Dashboard

- `GET /api/items/`: Retrieves a list of items with details such as SKU, name, category, tags, stock status, and available stock.

### Serialization

Django REST Framework serializers are utilized to convert model instances into JSON format.

### Query Parameters

The API supports filtering results via query parameters, such as `?stock_status=in_stock` or `?category=Electronics`.

## Frontend Setup

The front-end application is built with React and interacts with the Django backend to present the data in accordance with the Figma design.

## API Documentation

Each endpoint is documented with details on the expected request format and the structure of the response JSON.

## Authentication

The API uses token-based authentication to ensure that endpoints are securely accessed by authenticated users only.

## Testing

Unit tests are written for the API endpoints to validate their functionality.

## Bonus Features

### Caching

Caching is implemented to optimize the performance of the API, reducing load times for frequently requested data.

### Frontend Interface

A basic frontend interface is created using React, showcasing a user-friendly format for the data provided by the API.
