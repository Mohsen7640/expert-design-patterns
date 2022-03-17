from behavioral.template_method.reporter.exports.csv import ReportInCSV
from behavioral.template_method.reporter.exports.pdf import ReportInPDF
from behavioral.template_method.reporter.models.user import User


def run():
    u1 = User(pk=1, username="john")
    u2 = User(pk=2, username="anna")
    u3 = User(pk=3, username="mark")

    report_in_pdf = ReportInPDF(users=[u1, u2, u3])
    report_in_pdf.generate()

    report_in_csv = ReportInCSV(users=[u1, u2, u3])
    report_in_csv.generate()


if __name__ == '__main__':
    run()
