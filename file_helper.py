import csv

class File:
    
    def __init__(self, name='broken_links.csv', oper_type='w', encoding='utf-8'):
        self.f = open(name, oper_type, encoding=encoding)
        self.writer = csv.writer(self.f)
    
    def write_to_file(self, data):
        self.writer.writerow(data)
    
    def close_file(self):
        self.f.close()