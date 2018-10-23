import os.path
import re
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Please supply a list of files on the command line.')
        
    filnamelist = sys.argv[1:]
    for filename in filnamelist:
        if not os.path.isfile(filename):
            sys.exit('Exiting because {} is not a file.'.format(filename))
            
    pattern = re.compile('blocked on .*@([a-f0-9]{8})')
    blocked_threads = dict()
    filenum = -1
    for filename in filnamelist:
        filenum += 1
        with open(filename,'r') as f:
            line = f.readline()
            while len(line) > 0:
                match = pattern.search(line)
                if match:
                    addr = match.group(1)
                    if addr not in blocked_threads:
                        entry = [ 0 for _ in filnamelist]
                        blocked_threads[addr] = entry
                    else:
                        entry = blocked_threads[addr]
                        
                    entry[filenum] += 1
                        
                line = f.readline()
                
    
    # now print the results
    output_formatter = '{} '
    for _ in filnamelist:
        output_formatter += '{:5,d} '
        
    for addr in sorted(blocked_threads.keys()):
        print(output_formatter.format(addr,*blocked_threads[addr]), file = sys.stdout)