
from application.report_service import ReportService
from infrastructure.reports.html import HtmlReport

class HtmlReportService(ReportService):
    def create_report(self):
        return HtmlReport()