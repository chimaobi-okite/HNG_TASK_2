# FastAPI Documentation

Version: 0.1.0

## Endpoints

### `/api`

#### POST: Create Person

- **Summary:** Create Person

- **Parameters:**
  - Name (query, optional, type: string)

- **Request Body:** JSON
  - Name (required)

- **Responses:**
  - 201: Successful Response
  - 422: Validation Error

#### GET: Get Person

- **Summary:** Get Person

- **Parameters:**
  - Name (query, required, type: string)

- **Responses:**
  - 200: Successful Response
  - 422: Validation Error

#### PUT: Update Person

- **Summary:** Update Person

- **Parameters:**
  - Name (query, required, type: string)

- **Request Body:** JSON
  - Name (required)

- **Responses:**
  - 201: Successful Response
  - 422: Validation Error

#### DELETE: Delete Person

- **Summary:** Delete Person

- **Parameters:**
  - Name (query, required, type: string)

- **Responses:**
  - 204: Successful Response
  - 422: Validation Error

### `/api/{user_id}`

#### GET: Get Person

- **Summary:** Get Person

- **Parameters:**
  - user_id (path, required, type: integer)

- **Responses:**
  - 200: Successful Response
  - 422: Validation Error

#### PUT: Update Person

- **Summary:** Update Person

- **Parameters:**
  - user_id (path, required, type: integer)

- **Request Body:** JSON
  - Name (required)

- **Responses:**
  - 201: Successful Response
  - 422: Validation Error

#### DELETE: Delete Person

- **Summary:** Delete Person

- **Parameters:**
  - user_id (path, required, type: integer)

- **Responses:**
  - 204: Successful Response
  - 422: Validation Error

## Schemas

### HTTPValidationError

- **Properties:**
  - detail (array)

### Person

- **Properties:**
  - name (string, required)

### PersonOut

- **Properties:**
  - name (string, required)
  - user_id (integer, required)

### ValidationError

- **Properties:**
  - loc (array)
  - msg (string, required)
  - type (string, required)
