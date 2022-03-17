from abc import ABC, abstractmethod


class TemplateEngineInterface(ABC):

    @abstractmethod
    def render(self, template, params):
        pass
