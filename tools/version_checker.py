from typing import Dict, Any

import requests  # noqa


def local_version():
    with open("./VERSION") as vr:
        version = vr.read()  # type: str
        return version.lstrip().rstrip()


def latest_version_on_pypi():
    pypi_info = requests.request("get", "https://pypi.org/pypi/scapy-helper/json").json()  # type: Dict[str, Any]
    return pypi_info.get("info").get("version")


if __name__ == "__main__":
    pypi_version = latest_version_on_pypi()
    local_version = local_version()
    assert pypi_version != local_version
