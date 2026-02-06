from domain.report import Report
class ReportService:
    def create_report(self) -> Report:      #Factory method to be implemented by subclasses
        raise NotImplementedError("Subclasses must implement the create_report method.")
    def generate(self)-> str:
        report =self.create_report()
        return report.render()