"""Router for Fan"""

from fastapi import APIRouter
from fan.services.fan import service


router = APIRouter()

@router.get(
    path    = "/duty_cycle",
    summary = "Get a duty cycle of fan"
)
async def get_duty_cycle():
    """Get duty cycle of fan"""
    response = await service.get_duty_cycle()
    return response


@router.post(
    path    = "/enable",
    summary = "Run fan"
)
async def enable_fan():
    """Run fan"""
    response = await service.enable()
    return response


@router.post(
    path    = "/disable",
    summary = "Stop fan"
)
async def disable_fan():
    """Stop fan"""
    response = await service.disable()
    return response
