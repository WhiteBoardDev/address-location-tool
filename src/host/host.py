from host_file import HostFile
import common.data_access.dao as dao

__author__ = 'cnishina'


class Host:
    def __init__(self, db_conf, file_read, file_write):
        self.dao = dao.create(db_conf)
        self.host_file = HostFile(file_read, file_write)

    def update(self):
        all_nodes = self.dao.get_all_nodes()
        self.host_file.read_host_file()
        self.host_file.build()
        self.host_file.update(all_nodes)
        self.host_file.to_file()

