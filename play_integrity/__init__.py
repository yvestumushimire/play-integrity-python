import logging

from play_integrity.integrity import Attestation

__version__ = "0.1.1"


__all__ = ["Attestation"]

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
