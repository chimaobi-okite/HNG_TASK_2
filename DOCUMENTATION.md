# FastAPI
## Version: 0.1.0

### /api

#### POST
##### Summary:

Create Person

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| name | query |  | No | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

#### GET
##### Summary:

Get Person

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| name | query |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### PUT
##### Summary:

Update Person

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| name | query |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

#### DELETE
##### Summary:

Delete Person

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| name | query |  | Yes | string |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Successful Response |
| 422 | Validation Error |

### /api/{user_id}

#### GET
##### Summary:

Get Person

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

#### PUT
##### Summary:

Update Person

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful Response |
| 422 | Validation Error |

#### DELETE
##### Summary:

Delete Person

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Successful Response |
| 422 | Validation Error |
