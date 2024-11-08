from .single import SingletonMeta
import consul
from dns import resolver
from dns import rdatatype
from typing import List, Dict
import settings


class GrpcAddress:
    def __init__(self, host: str, port: int):
        self.count = 0
        self.host = host
        self.port = port

    def increment(self):
        self.count += 1

    def format(self):
        return f"{self.host}:{self.port}"


class GrpcLoadBalancer(metaclass=SingletonMeta):
    def __init__(self, consul_host: str):
        self.consul_host = consul_host
        self.consul_client = consul.Consul(host=consul_host, port=8500)
        self.service_addresses: Dict[str, List[GrpcAddress]] = {}
        self._fetch_addresses()

    def _fetch_addresses(self):
        reso = resolver.Resolver()
        reso.nameservers = [self.consul_host]
        reso.port = 8600

        for service_name in settings.GRPC_SERVICE_NAMES:
            dnsanswer = reso.resolve(f"{service_name}.service.consul", rdatatype.A)
            dnsanswer_srv = reso.resolve(f"{service_name}.service.consul", rdatatype.SRV)
            for index, srv in enumerate(dnsanswer_srv):
                if len(dnsanswer) == 1:
                    ip = dnsanswer[0].address
                else:
                    ip = dnsanswer[index].address
                self.service_addresses[service_name].append(GrpcAddress(ip, srv.port))

    def get_address(self, service_name: str):
        print(self.service_addresses)
        print(service_name)
        addresses = self.service_addresses[service_name]
        addresses.sort(key=lambda address: address.count)
        address = addresses[0]
        address.increment()
        return address.format()