import google.auth
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import logging


log = logging.getLogger(__name__)


class Attestation:
    """
    Verify Play integrity data

    attributes:
        verify_online: decode integrity token using play integrity api,
            verify data and return verdict
    """

    def __init__(self, integrity_token: str, package_name: str) -> None:
        """
        Constructor for Attestation

        Args:
            integrity_token: a signed response token provided by play integrity API from android app/game
            package_name: Android app/game name
        """
        self.integrity_token = integrity_token
        self.package_name = package_name

    def _get_credentials(self) -> Credentials | None:
        try:
            credentials, _ = google.auth.default()
        except Exception as e:
            log.warning(e)
            return None
        return credentials

    def verify_online(self):
        """
        Get decrypted and verified integrity verdict on Google's servers
        check verdict if passed or not passed
        """
        pass
