
from application.report_service import ReportService
from infrastructure.reports.pdf import PdfReport 
class PdfReportService(ReportService):
    def create_report(self):
        return PdfReport()


    