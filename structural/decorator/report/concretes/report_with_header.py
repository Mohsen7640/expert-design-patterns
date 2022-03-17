from structural.decorator.report.contracts.report_generator import ReportGenerator
from structural.decorator.report.decorators.report_decorator import ReportDecorator


class ReportWithHeader(ReportDecorator):

    def __init__(self, report_generator: ReportGenerator):
        super().__init__(report_generator)

    def generate(self):
        return f"""
                Header Report
                {self.report_generator.generate()}
            """
