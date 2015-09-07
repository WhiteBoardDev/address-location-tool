__author__ = 'cnishina'

import requests
import json
import ip_address_lookup


def get_hosts(url):
    r = requests.get(url)
    json_data = json.loads(r.text)
    return json_data


def build_proxy_file(hosts_data, proxy_data):
    fo = open('proxy-nginx', 'w+')
    external_address = ip_address_lookup.get_wan_ip()

    # go through each host that matches the external port number
    # check ports from the hosts
    # for each port, go through proxy port array and see if it matches

    # go through each host
    for key in hosts_data.keys():

        # select only matching external IP addresses
        if external_address == hosts_data[key]['external_address']:

            # get host ports and go through each
            try:
                if hosts_data[key]['ports'] is not None:
                    host_ports = hosts_data[key]['ports']
                    local_address = hosts_data[key]['local_address']
                    write_ports(fo, key, local_address, host_ports, proxy_data)
            except KeyError:
                pass


def write_ports(fo, key, local_address, host_ports, proxy_data):
    domain_name = proxy_data['domain']

    for host_port in host_ports:
        for proxy in proxy_data['proxy']:
            if host_port in proxy['internal']:
                external = proxy['external']
                fo.write('server {\n')
                fo.write('   listen   ' + str(external) + ';\n')
                fo.write('   server_name   ' + key + '.' + domain_name + ';\n')
                fo.write('   location / {\n')
                fo.write('      proxy_pass   ' + local_address + ':' + str(host_port) + ';\n')
                fo.write('   }\n')
                fo.write('}\n')
                break
