# 公共静态配置

### FastAPI ###
DEBUG = True

### DATABASE ###
DATABASE_URL = 'mysql://root:root@127.0.0.1:3306/cooyun?charset=utf8mb4'

### 跨域请求 ###
allow_credentials = True
allow_origins = ['*']
allow_methods = ['*']
allow_headers = ['*']

### GZIP ###
open_minimum_size = 500

### Jinja2 Template ###
Jinja2directory = 'template'