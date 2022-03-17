from behavioral.template_method.reporter.contracts.report import UserReport


class ReportInCSV(UserReport):

    def export(self):
        """
        Export data in CSV Format
        :return:
        """
        data = self.data_to_export
        print(f"Export Report In CSV Format")