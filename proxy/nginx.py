import common.ip_updater.ip_address_lookup as ip_address_lookup

__author__ = 'cnishina'


def build_proxy_file(all_nodes, proxy_config):
    fo = open('proxy-nginx', 'w+')
    external_address = ip_address_lookup.get_wan_ip()

    # go through each host that matches the external port number
    # check ports from the hosts
    # for each port, go through proxy port array and see if it matches

    # go through each host
    for node in all_nodes:
        # select only matching external IP addresses
        if external_address == node.external_address:

            # get host ports and go through each
            try:
                if node.ports is not None:
                    write_ports(fo, node, proxy_config)
            except KeyError:
                pass


def write_ports(fo, node, proxy_config):
    # for all ports that the node services
    for port in node.ports:
        for proxy in proxy_config.proxies:
            # if the port
            if port in proxy.internal:
                fo.write('server {\n')
                fo.write('   listen   ' + str(proxy.external) + ';\n')
                fo.write('   server_name   ' + node.name + '.' + proxy_config.domain_name + ';\n')
                fo.write('   location / {\n')
                fo.write('      proxy_pass   http://' + node.local_address + ':' + str(port) + ';\n')
                fo.write('      proxy_redirect     default;\n')
                fo.write('      proxy_set_header   Host $host:$proxy_port;\n')
                fo.write('      proxy_set_header   X-Real-IP        $remote_addr;\n')
                fo.write('      proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;\n')
                fo.write('   }\n')
                fo.write('}\n')
                break
