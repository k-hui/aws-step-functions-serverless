# serverless-aws-step-functions

AWS Step Functions by Serverless Framework

- https://www.serverless.com/framework/docs/getting-started
- https://www.serverless.com/plugins/serverless-offline
- https://www.serverless.com/plugins/serverless-step-functions

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
npm run deploy
```

### Test Step Functions on dev

```bash
sls invoke stepf --name serverlessDemo
```
