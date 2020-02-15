import re


class subckt():
    def __init__(self,name):
        self.name=subckt

class spi_file():
    def __init__(self,spi_file):
        self.spi_file=spi_file
        self.subckt_list = []
        self.lines = []
    def parse_file(self,spi_file=None):
        if not spi_file:
            spi_file = self.spi_file
        duplicated_flag = False
        with open(spi_file,'r') as fh:
            print("Start to parsing %s" % spi_file)
            for line in fh.readlines():
                #line = line.strip()
                if re.match('INCLUDE\s+(.*)',line):
                    self.parse_file(spi_file=re.match('INCLUDE\s+(.*)',line).groups(1)[0].strip())
                elif re.match('.subckt\s+(\S+)\s+(\S+)',line):
                    sname = re.match('.subckt\s+(\S+)\s+(\S+)',line).groups(1)[0]
                    if sname in self.subckt_list:
                        print("Waring: duplicated subckt : %s [file : %s]" % (sname, spi_file))
                        duplicated_flag = True
                    else:
                        print("get subckt: %s in file %s" % (sname, spi_file))
                        self.subckt_list.append(sname)
                    if duplicated_flag:
                        pass
                    else:
                        self.lines.append(line)
                elif re.match('.end',line):
                    if duplicated_flag:
                        duplicated_flag = False
                    else:
                        self.lines.append(line)
                else:
                    if duplicated_flag:
                        pass
                    else:
                        self.lines.append(line)
    def dump_spi(self,outfile=None):
        if not outfile:
            outfile = self.spi_file.replace('.spi','_new.spi')
        with open(outfile,'w') as fh:
            for l in self.lines:
                fh.write(l)

if __name__=='__main__':
    TopSpi = spi_file('./top.spi')
    TopSpi.parse_file()
    TopSpi.dump_spi(outfile='./top.flat.spi')