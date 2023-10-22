"""Top Level Router"""

from fastapi import APIRouter
from fan.routers.cluster import router as cluster_router
from fan.routers.fan import router as fan_router


router = APIRouter()

router.include_router(
    router = cluster_router,
    prefix = "/cluster",
    tags   = ["Cluster"]
)

router.include_router(
    router = fan_router,
    prefix = "/fan",
    tags   = ["Fan"]
)
