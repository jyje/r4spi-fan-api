""" Fan Controller for Raspberry Pi"""
import uvicorn

from fastapi import FastAPI
from typer import Typer, Option
from typing_extensions import Annotated


typer = Typer(
    add_completion         = False,
    invoke_without_command = True,
    rich_markup_mode       = "rich"
)

api = FastAPI(

)

@typer.callback()
def main(
    host   : str = "0.0.0.0",
    port   : int = 8000,
    reload : Annotated[bool, Option("-r", "--reload")] = False
):

    """
    [blue]Fan Controller[/blue] for [red]Raspberry Pi[/red]
    """


    uvicorn.run(
        app   = "main:api",
        host  = host,
        port  = port,
        reload= reload
    )

if __name__ == "__main__":
    typer()
