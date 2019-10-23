# SSH Observatory

A server-less implementation of the ssh observatory

## Use-cases

- API for a Web Application
- API for a Mobile Application

## Setup

```bash
npm install -g serverless
```

## Deploy

In order to deploy the endpoint simply run

```bash
assume-role YOUR_ROLE && serverless deploy
```

The expected result should be similar to:

```bash
$ serverless deploy
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (4.18 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..........................
Serverless: Stack update finished...
Service Information
service: ssh-observatory
stage: dev
region: us-east-1
stack: ssh-observatory-dev
api keys:
  None
endpoints:
  POST - https://kz5f2ztw43.execute-api.us-east-1.amazonaws.com/dev/scans
  GET - https://kz5f2ztw43.execute-api.us-east-1.amazonaws.com/dev/scans
  GET - https://kz5f2ztw43.execute-api.us-east-1.amazonaws.com/dev/scans/{id}
functions:
  create: ssh-observatory-dev-create
  list: ssh-observatory-dev-list
  get: ssh-observatory-dev-get
```

## Usage

You can create, retrieve, update, or delete todos with the following commands:

### Create a scan

```bash
curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans --data '{ "target": "ssh.mozilla.com", "port": 22 }'
```

Example output:
```bash
{"port": 22, "updatedAt": 1536951946457, "id": "2f8f92ec-b851-11e8-8c13-ee273c03d56e", "createdAt": 1536951946457, "target": "ssh.mozilla.com"}
```

### List all scans

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans
```

Example output:
```bash
[{"port": 22, "id": "2f8f92ec-b851-11e8-8c13-ee273c03d56e", "target": "ssh.mozilla.com", "createdAt": 1536951946457, "updatedAt": 1536951946457}, {"port": 22, "id": "2e94de74-b851-11e8-8c13-ee273c03d56e", "target": "ssh.mozilla.com", "createdAt": 1536951944812, "updatedAt": 1536951944812}, {"port": 22, "id": "59d27142-b850-11e8-8c13-ee273c03d56e", "target": "ssh.mozilla.com", "createdAt": 1536951587861, "updatedAt": 1536951587861}]
```

### Get one scan

```bash
# Replace the <id> part with a real id from your todos table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/scans/<id>
```

Example Result:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa81-11e6-9ede-afdfa051af86","createdAt":1479138570824,"checked":false,"updatedAt":1479138570824}%
```

## Unit-testing

### Install dependencies for unit-tests

```bash
make dependencies
```

### Run unit-tests

```bash
make unit-tests
```
