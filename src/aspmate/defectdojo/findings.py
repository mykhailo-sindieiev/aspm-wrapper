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
        :return: Answer in JSON format
        """
        findings_url = urljoin(self.session.url, self.FINDINGS_API)
        if "params" in kwargs:
            params = kwargs.get("params")
        else:
            params = None
        response = self.session.get(findings_url, params=params)

        return response.json()

    def close_finding(self, finding_id: int):
        """
        Close a finding by a given id

        :param finding_id: Finding id to close
        :return: Answer in JSON format
        """
        close_subpath = f"{self.FINDINGS_API}/{str(finding_id)}/close/"
        request_url = urljoin(self.session.url, close_subpath)
        response = self.session.post(request_url)

        return response.json()
