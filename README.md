# serverless-deploy

Deploys python 3.8 Serverless applications

example usage
```
jobs:
  build_matrix:
    name: Generate region matrix
    runs-on: ubuntu-latest
    strategy:
      matrix:
        stage: [prod]
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - uses: actions/checkout@v2

      - name: set region matrix
        id: set-matrix
        run: echo "::set-output name=matrix::$(jq -Mcr .regions config/${{ matrix.stage }}.json)"
  deploy:
    needs: build_matrix
    name: deploy
    runs-on: ubuntu-latest
    strategy:
      matrix:
        stage: [prod]
        regions: ${{ fromJson(needs.build_matrix.outputs.matrix) }}
    steps:
      - uses: actions/checkout@v2

      - uses: ivliab/serverless-deploy@v1
        with:
          stage: ${{ matrix.stage }}
          region: ${{ matrix.regions }}
          workdir: serverless/application
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```
