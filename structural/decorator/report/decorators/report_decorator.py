from structural.decorator.report.contracts.report_generator import ReportGenerator


class ReportDecorator(ReportGenerator):

    def __init__(self, report_generator: ReportGenerator):
        self.report_generator = report_generator

    def generate(self):
        return self.report_generator.generate()
