from domain.report import Report 
class HtmlReport(Report):
    def render(self):
        return "HTML output"