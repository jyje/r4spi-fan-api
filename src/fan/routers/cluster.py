"""Router for Cluster"""

from fastapi import APIRouter
from fan.services.cluster import service

router = APIRouter()

@router.get(
    path    = "/temperture/max",
    summary = "Get maximum temperture of current cluster"
)
async def get_maximum_temperture():
    """Get maximum temperture of cluster"""
    response = await service.get_maximum_temperture()
    return response


@router.get(
    path    = "/temperture/target",
    summary = "Get target temperture of cluster"
)
async def get_target_temperture():
    """Get target temperture of cluster"""
    response = await service.get_target_temperture()
    return response


@router.post(
    path    = "/temperture/target/{value}",
    summary = "Set target temperture of cluster"
)
async def set_target_temperture(value: float):
    """Set target temperture of cluster"""
    response = await service.set_target_temperture(value)
    return response
