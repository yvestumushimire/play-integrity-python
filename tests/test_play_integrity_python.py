from play_integrity_python import __version__
from play_integrity_python.play_integrity import Attestation


def test_version():
    assert __version__ == "0.1.0"


def test_attestation_init():
    attest = Attestation("integrity_token", "package_name")
    assert attest.integrity_token == "integrity_token"
    assert attest.package_name == "package_name"


def test_attestation_creds():
    attest = Attestation("integrity_token", "package_name")
    creds = attest._get_credentials()
    assert creds.valid == False
