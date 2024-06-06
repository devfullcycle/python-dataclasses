from dataclasses import dataclass, field, InitVar, Field
from typing import Any, cast

@dataclass(slots=True, kw_only=True)
class Pagination:
    page: int = field(init=False, default=1)
    per_page: int = field(init=False, default=15)
    
    init_page: InitVar[int | None] = None
    init_per_page: InitVar[int | None] = None

    def __post_init__(self, init_page: int | None,
                      init_per_page: int | None):
        self._normalize_page(init_page)
        self._normalize_per_page(init_per_page)

    def _normalize_page(self, page: int | None):
        page = _int_or_none(page)
        if page <= 0:
            page = cast(int, self.get_field('page').default)
        self.page = page

    def _normalize_per_page(self, per_page: int | None):
        per_page = _int_or_none(per_page)
        if per_page < 1:
            per_page = cast(int, self.get_field('per_page').default)
        self.per_page = per_page
    
    # def __eq__(self, value: object) -> bool:
    #     return isinstance(value, Pagination) and self.page == value.page and self.per_page == value.per_page
    
    @classmethod
    def get_field(cls, entity_field: str) -> Field[Any]:
        return cls.__dataclass_fields__[entity_field]

def _int_or_none(value: Any, default: int = 0) -> int:
    try:
        return value if isinstance(value, int) else int(value)
    except (ValueError, TypeError):
        return default

pagination = Pagination(init_page=0, init_per_page=0)

print(pagination)

pagination = Pagination(init_page='2', init_per_page='2') # type: ignore
print(pagination)

pagination1 = Pagination(init_page=0, init_per_page=0)
pagination2 = Pagination(init_page=0, init_per_page=0)

print(pagination1 == pagination2)  # True