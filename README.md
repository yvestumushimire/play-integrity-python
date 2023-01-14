# Python Play Integrity Verify

a Python library that verify apps and games from potentially risky and fraudulent interactions. based on [Play Integrity API](https://developer.android.com/google/play/integrity)

> Works for Apps that are exclusively distributed outside Google Play

## Table of Contents

- [Python Play Integrity Verify](#python-play-integrity-verify)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)


## Getting Started

### Prerequisites

- [Google cloud project](https://console.cloud.google.com/)
- **Play Integrity API** enabled in **APIs and services**
- a **Service account**: Create a service account within the Google Cloud project that's linked to your app. and grant your service account the roles of **Service Account User** and **Service Usage Consumer**.

### Installation

```bash
pip install play-integrity
```

## Usage

Make sure that `GOOGLE_APPLICATION_CREDENTIALS` is set

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/config.json
```

eg:

```py
from play_integrity import Attestation

attest = Attestation("integrity_token", "package_name")
passed = attest.verify_online("nonce")
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
