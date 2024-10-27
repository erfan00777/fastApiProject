# FastAPI ClickHouse Project

## Overview
This project is a FastAPI application that interacts with a ClickHouse database to track user page views. It provides an API for recording page views and retrieving view counts for specific users within the last 24 hours.

## Features
- User page view tracking
- API for inserting page view data
- API for retrieving view counts
- Docker support for easy deployment

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/erfan00777/fastApiProject.git

2. Navigate to the project directory:
   ```bash
   cd fastApiProject
   
3. build image:
   ```bash
   sudo docker build -t "your_tag" .

4. run docker-compose:
   ```bash
   sudo docker-compose up -d 

### write   
### POST /api/traffic/{request_id}
Insert a page view record.

**Request Body:**

{
  "user_id": 10,
  "created_at": "2024-10-26T12:00:00",
  "page_url": "http://example.com/page1"
}

### update   
### POST /api/traffic/{request_id}
update a page view record.

**Request Body:**

{
  "user_id": 10,
  "created_at": "2024-10-26T12:00:00",
  "page_url": "http://example.com/page1"
}

### GET /api/traffic/report/{user_id}
Retrieve the page view counts for a specific user over the last 24 hours.

**Response Body:**
[
  {
    "url": "http://example.com/page1",
    "count": 5
  },
  {
    "url": "http://example.com/page2",
    "count": 3
  }
]
