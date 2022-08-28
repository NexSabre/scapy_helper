from typing import Any, Dict

import requests  # noqa


def local_version() -> str:
    with open("./VERSION") as vr:
        version = vr.read()
        return version.lstrip().rstrip()


def latest_version_on_pypi() -> str:
    pypi_info: Dict[str, Any] = requests.request(
        "get", "https://pypi.org/pypi/scapy-helper/json"
    ).json()
    return pypi_info.get("info").get("version")


if __name__ == "__main__":
    pypi_version = latest_version_on_pypi()
    local_version = local_version()
    assert pypi_version != local_version
