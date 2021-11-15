# SimpCity

## Development guide

During development, please create a new branch `feature-{featureName}-{version}` from the latest development branch. When the feature is finished developed, please submit a pull request before merging the feature branch to the development branch for code reviewing.

## Build Docker

### Run docker with -ti flag to run in interative mode

```bash
docker build -t simpcity .
docker run -ti simpcity
```
