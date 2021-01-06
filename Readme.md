# Endocode Technical Challenge

## Usage

"make up" builds and runs the service on default Port 8080

Command line flags are redirected and saved to a log file

Ctrl + C stops the service


## Endpoint /helloworld

/helloworld returns 'Hello Stranger'
http://0.0.0.0:8080/helloworld

**Definition**

`GET /helloworld`

**Response**

- `200 OK` on success

```Hello Stranger```



## Endpoint /helloworld?name=

/helloworld?name=AlfredENeumann (any filtered value) returns 'Hello Alfred E Neumann'
http://0.0.0.0:8080/helloworld?name=AlfredENeumann

**Definition**

`GET /helloworld?name=AlfredENeumann`

**Arguments**

- `"?name=":string` a string to be split before their capital letters

**Response**

- `200 OK` on success

```Hello Alfred E Neumann```



## Endpoint /versionz

Returns a JSON with the project name as 'Endocode' and the latest git commit hash

http://0.0.0.0:8080/versionz

**Response**

- `200 OK` on success

```json
{
    "Endocode": "Latest git commit hash",
}
```
