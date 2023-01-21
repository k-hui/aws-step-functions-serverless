# serverless-aws-step-functions

AWS Step Functions by Serverless Framework

## Setup (only the first time)

```bash
npm init
npm install -g serverless
npm install -D serverless-offline
npm install -D serverless-step-functions
```

### Setup Python Serverless Project

- https://www.serverless.com/framework/docs/getting-started
- https://www.serverless.com/plugins/serverless-offline
- https://www.serverless.com/plugins/serverless-step-functions

```bash
serverless # select Python Starter
```

- Then copy `handler.py` and `serverless.yml` to the root project
- Delete the temporary created serverless project

- append to `serverless.yml`

```yml
plugins:
  - serverless-offline
  - serverless-step-functions
```

## Getting Started

```bash
npm install
```

### Test offline

```bash
sls offline
sls invoke local -f hello && sls invoke local -f world
```

### Test on dev

```bash
sls invoke -f hello && sls invoke -f world
```

## Deployment

```bash
sls deploy -s dev
```

### Test Step Functions on dev

```bash
sls invoke stepf --name serverlessDemo
```
