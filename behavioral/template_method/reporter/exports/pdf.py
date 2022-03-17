from behavioral.template_method.reporter.contracts.report import UserReport


class ReportInPDF(UserReport):

    def export(self):
        """
        Export data in PDF Format
        :return:
        """
        data = self.data_to_export
        print(f"Export Report In PDF Format")
