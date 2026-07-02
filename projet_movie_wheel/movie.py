# module movie

from dataclasses import dataclass
from pydantic import BaseModel


class Mo_vie(BaseModel):
    """ Represents a movie with its title, release year and duration in minutes

    Example:

        m = Movie("La bataille de Gaulle: L'âge de fer", 2026, 160)
    """

    title: str
    year: int
    duration: int | None = None

    # implements builtin functions 

    def __str__(self) -> str:
        return f"{self.title} ({self.year}, {self.duration}mn)"
    
    def __len__(self) -> int:
        return self.duration if self.duration is not None else 0
    
    # surcharge d'opérateur

    # opérateur in
    def __contains__(self, item) -> bool:
            if isinstance(item, str):
                  return item.lower() in self.title.lower()
            else:
             return False
        
    def durationHourMinute(self) -> tuple[int, int] | None:
        if self.duration is not None:
            return divmod(self.duration, 60)
        # implicit return None