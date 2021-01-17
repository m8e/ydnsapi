import requests
import json
import base64

from requests.api import head


def getPublicIP() -> str:
    text = requests.get("http://ip.jsontest.com")
    data = json.loads(text.text)
    return data["ip"]


def queryIP(host: str) -> str:
    url = "https://ydns.io/api/v1/ip?host={}.ynds.eu"
    r = requests.get(url)
    return r.text


class YDNS:

    def __init__(self, username: str, password: str):
        loginInfo = "{}:{}".format(username, password)
        info_byte = loginInfo.encode("ascii")
        base64_byte = base64.b64encode(info_byte)
        self.token = base64_byte.decode("ascii")

    def updateIP(self, hostname: str, ip: str) -> bool:
        """
        This method allow user update the ip manally.
        """
        url = "https://ydns.io/api/v1/update/?host={}.ydns.eu&ip={}".format(
            hostname, ip)
        headers = {"Authorization": "Basic {}".format(self.token)}
        r = requests.get(url, headers=headers)
        if "ok" in r.text:
            return True
        return False

    def autoUpdateIP(self, hostname: str) -> bool:
        """
        This method auto-dectect the public ip of the machine and
        update to the YDNS.
        """
        ip = getPublicIP()
        state = self.updateIP(hostname, ip)
        return state
