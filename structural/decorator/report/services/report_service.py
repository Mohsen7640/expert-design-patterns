from structural.decorator.report.contracts.report_generator import ReportGenerator


class ReportService(ReportGenerator):

    def generate(self):
        return "Report generated"
