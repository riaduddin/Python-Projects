from domain.report import Report
class PdfReport(Report):
    def render(self):
        return "PDF output"