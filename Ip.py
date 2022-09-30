#!/usr/bin/python

class IPV4():
    def __init__(self, ip) -> None:
        self.ip = ip
        first = str(bin(int(str(ip).split(".")[0])))[2:]
        if len(first)==8 and first[:3] == "110":
            self.classe = "A"
        elif len(first) == 8 and first[:2] == "10":
            self.classe = "B"
        else:
            self.classe = "C"

    def __repr__(self) -> str:
        return f"{self.ip} : {self.classe}"

if __name__ == "__main__":
    ip = IPV4("192.168.1.1")
    print(ip)