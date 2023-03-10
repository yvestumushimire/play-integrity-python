from play_integrity import Attestation, __version__


def test_version():
    assert __version__ == "0.1.1"


def test_attestation_init():
    attest = Attestation("integrity_token", "package_name")
    assert attest.integrity_token == "integrity_token"
    assert attest.package_name == "package_name"


def test_attestation_validate_online():
    attest = Attestation("integrity_token", "package_name")
    passed = attest.verify_online("nonce")
    assert passed == False
