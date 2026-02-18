from application.html_report_service import HtmlReportService
from application.pdf_report_service import PdfReportService

def get_report_service(report_type: str):
    if report_type == "html":
        return HtmlReportService()
    elif report_type == "pdf":
        return PdfReportService()
    else:
        raise ValueError("Unsupported report type")