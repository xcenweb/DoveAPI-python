import config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from fastapi.staticfiles import StaticFiles

def get_app() -> FastAPI:

    app = FastAPI(debug=config.DEBUG)

    # 静态文件目录
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # 开启跨源资源共享
    app.add_middleware(
        CORSMiddleware,
        allow_origins = config.allow_origins,
        allow_credentials = config.allow_credentials,
        allow_methods = config.allow_methods,
        allow_headers = config.allow_headers,
    )
    
    # 指定字节以上开启gzip
    app.add_middleware(
        GZipMiddleware,
        minimum_size = config.open_minimum_size
    )
    
    # 从 ./router 导入路由
    import router.base as base
    app.include_router(base.router)

    return app