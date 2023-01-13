import logging
from typing import Dict, Optional

import google.auth
from googleapiclient.discovery import build

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

    def _decrypt_integrity_token(self) -> Optional[Dict]:
        """
        Decrypt integrity token on google servers
        Args:
            - token: integrity token
        return:
            optional dict:

        """
        try:
            credentials, _ = google.auth.default()
            service = build(
                "playintegrity",
                "v1",
                credentials=credentials,
            )
            data = {
                "integrity_token": self.integrity_token
            }
            response = (
                service.v1()
                .decodeIntegrityToken(
                    packageName="com.truststamp.trustedcheckin.client.dev", body=data
                )
                .execute()
            )

        except Exception as e:
            log.warning(e)
            return None
        service.close()
        return response

    def verify_online(self, nonce: str) -> bool:
        """
        Get decrypted and verified integrity verdict on Google's servers
        check verdict if passed or not passed
        """
        data = self._decrypt_integrity_token()
        if not data:
            return False
        return True
