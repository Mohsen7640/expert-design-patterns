from structural.decorator.report.concretes.report_with_footer import ReportWithFooter
from structural.decorator.report.concretes.report_with_header import ReportWithHeader
from structural.decorator.report.services.report_service import ReportService


def run():
    report = ReportService()

    header = ReportWithHeader(report)

    footer = ReportWithFooter(report)

    print(report.generate())
    print(header.generate())
    print(footer.generate())

    print(ReportWithFooter(ReportWithHeader(report)).generate())


if __name__ == '__main__':
    run()
