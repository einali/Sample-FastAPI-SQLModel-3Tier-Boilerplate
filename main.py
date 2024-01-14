from fastapi import FastAPI
from fastapi.routing import APIRoute
from package_name.controller.routers import api_router
from starlette.middleware.cors import CORSMiddleware
from package_name.utils.setting import project_setting
import uvicorn




def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=project_setting.PROJECT_NAME,
    openapi_url=f"/api/docs/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)

# Set all CORS enabled origins
if project_setting.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in project_setting.CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix="/api")



if __name__ == "__main__":
    import logging

    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
    uvicorn.run(app, host="0.0.0.0", port=8000)