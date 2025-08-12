from urllib.parse import urljoin
from .session import DefectDojoSession

class Scan:
    def __init__(self, session):
        self.session = session
        self.SCAN_API = '/api/v2/import-scan/'


    def upload_scan_id(self, engagement: int, scan_type: str):
        pass