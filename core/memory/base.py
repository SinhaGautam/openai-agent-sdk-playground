from abc import ABC, abstractmethod

class BaseMemory(ABC):
    @abstractmethod
    def add(self, role: str, content: str):
        pass

    @abstractmethod
    def get_context(self) -> str:
        pass