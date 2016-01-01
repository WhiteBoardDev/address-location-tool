import re
import sys
import common.ip_updater.ip_address_lookup as ip_address_lookup

# line space for address, ipv6 is 40 characters
line_space = 18


class LineItem:
    def __init__(self):
        self.ip_address = None
        self.name = None
        self.line = None

    def format_line(self):
        if self.name is not None:
            rem = line_space - self.ip_address.__len__()
            if rem < 0:
                rem = 5
            spaces = ''
            for i in range(rem):
                spaces += ' '
            return self.ip_address + spaces + self.name
        else:
            return self.line


class HostFile:
    def __init__(self, file_read, file_write):
        self.file_read = file_read
        self.file_write = file_write
        self.file_contents = None
        self.reg_alias = []
        self.alt_alias = []
        self.comment_start = '# Start ALT Host Records ------------------------------------------------------'
        self.comment_end = '# End ALT Host Records --------------------------------------------------------'

    # read in host file depending on platform
    def read_host_file(self):
        if 'darwin' in sys.platform:
            fi = open(self.file_read, 'r')
            self.file_contents = fi.read().strip()

    def build(self):
        alt_section = False
        lines = self.file_contents.split('\n')
        for line in lines:
            line_item = LineItem()

            if line.__len__() == 0 or line == ' ':
                if alt_section:
                    continue
                else:
                    line_item.line = line
                    self.reg_alias.append(line_item)
                    continue

            # alt section
            elif line == self.comment_start:
                alt_section = True
                continue
            elif line == self.comment_end:
                alt_section = False
                continue
            elif alt_section:
                # instead of updating alt nodes here...
                continue

            # regular comments
            elif line.startswith('#'):
                line_item.line = line
                self.reg_alias.append(line_item)
                continue

            # regular alias names
            else:
                line = re.sub('\\t+', ' ', line)
                line = re.sub(' +', ' ', line)
                line_item.line = line
                line_split = line.split(' ')
                line_item.ip_address = line_split[0]
                line_item.name = line_split[1]
                self.reg_alias.append(line_item)

    def update(self, all_nodes):
        external_address = ip_address_lookup.get_wan_ip()
        for node in all_nodes:
            if node.external_address == external_address:
                line_item = LineItem()
                line_item.name = node.name + '.local'
                line_item.ip_address = node.local_address
                self.alt_alias.append(line_item)

    def to_file(self):
        fo = open(self.file_write, 'w+')
        prev_line_empty = False
        for line_item in self.reg_alias:
            line = line_item.format_line() + '\n'
            if line is not '\n':
                prev_line_empty = False
            elif prev_line_empty:
                continue
            elif line == '\n':
                prev_line_empty = True
            fo.write(line)

        if not prev_line_empty:
            fo.write('\n')
        fo.write(self.comment_start + '\n')
        for line_item in self.alt_alias:
            fo.write(line_item.format_line() + '\n')
        fo.write(self.comment_end + '\n')

