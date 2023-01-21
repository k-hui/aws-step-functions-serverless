# serverless-aws-step-functions

AWS Step Functions by Serverless Framework

## Setup (only the first time)

```bash
npm init
npm install -D serverless
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

- append to `serverless.yml`

```yml
plugins:
  - serverless-offline
```

## Getting Started

```bash
npm install
```

### Test offline

```bash
npm start
npm test
```

### Test on dev

```bash
npm test:dev
```

## Deployment

```bash
npm run deploy
```

### Test Step Functions on dev

```bash
npm test:stepf
```
