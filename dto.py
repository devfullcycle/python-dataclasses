from pydantic import BeforeValidator
from typing import Annotated
from pydantic.dataclasses import dataclass

StrNotEmpty = BeforeValidator(lambda v: None if v == '' else v)


@dataclass
class Input:
    name: Annotated[str, StrNotEmpty]