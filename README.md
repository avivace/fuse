# fuse

> A simple file uploading service in Vue.js and Flask


### Deploy:

```bash
# Install npm dependencies
npm install

# Install python3 dependencies
pip3 install -r requirements.txt

# Build the Vue application for production
npm run build

# Start Flask backend server
python3 app.py

# Application is online at localhost:5000
```

## Backend

Flask, sqlite3 as database.

## Frontend

Vue.js, the CSS framework is [bootstrap-vue](https://github.com/bootstrap-vue/bootstrap-vue) ([Bootstrap 4](https://github.com/twbs/bootstrap)). Requests are handled with [Axios](https://github.com/axios/axios).

### Build Setup

``` bash
# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```


## Documentation Resources

- [VueJS webpack template guide](http://vuejs-templates.github.io/webpack/)
- [docs for vue-loader](http://vuejs.github.io/vue-loader)
