from urllib.parse import urljoin
from .session import DefectDojoSession


class Findings:
    def __init__(self, session: DefectDojoSession):
        self.session = session
        self.FINDINGS_API = '/api/v2/findings/'

    def get_all_findings(self, **kwargs):
        """
        Fetch all findings from DefectDojo.
        :param kwargs: Additional arguments that will be merged to the payload to DefectDojo
        :return: answer in json format
        """
        findings_url = urljoin(self.session.url, self.FINDINGS_API)
        if "params" in kwargs:
            params = kwargs.get("params")
        else:
            params = None
        response = self.session.get(findings_url, params=params)

        return response.json()
