#!/usr/bin/env python
import os
import time
import gzip
from pigz import PigzFile


def read_by_gzip(path):
    with gzip.open(path, "rt") as f:
        lines = [line for line in f]
    return lines
        
def read_by_pigz(path):
    with PigzFile(path, "rt") as f:
        lines = [line for line in f]
    return lines

def write_by_gzip(path, lines):
    with gzip.open(path, "wt") as fw:
        for line in lines:
            fw.write(line)
            
def write_by_pigz(path, lines):
    with PigzFile(path, "wt") as fw:
        for line in lines:
            fw.write(line)
        
def main():
    PATH1 = "data/GRCh39.p13.chr1.1000000.fa.gz"
    PATH2 = "data/out.test.gz"
    N = 5

    print("=" * 60)
    print("Read by gzip package:")
    ts = []
    for i in range(N):
        t1 = time.time()
        lines = read_by_gzip(PATH1)
        t2 = time.time()
        t3 = (t2 - t1) * 1000
        ts.append(t3)
        print("Number: %d, Time: %.2f ms" % (i + 1, t3))
    print("Average time: %.2f ms" % (sum(ts) / N))
    
    print("=" * 60)
    print("Read by pigz subprocess:")
    ts = []
    for i in range(N):
        t1 = time.time()
        lines = read_by_pigz(PATH1)
        t2 = time.time()
        t3 = (t2 - t1) * 1000
        ts.append(t3)
        print("Number: %d, Time: %.2f ms" % (i + 1, t3))
    print("Average time: %.2f ms" % (sum(ts) / N))
        
    print("=" * 60)
    print("Write by gzip package:")
    ts = []
    for i in range(N):
        t1 = time.time()
        write_by_gzip(PATH2, lines)
        t2 = time.time()
        t3 = (t2 - t1) * 1000
        ts.append(t3)
        print("Number: %d, Time: %.2f ms" % (i + 1, t3))
    print("Average time: %.2f ms" % (sum(ts) / N))

    print("=" * 60)
    print("Write by pigz subprocess:")
    ts = []
    for i in range(N):
        t1 = time.time()
        write_by_pigz(PATH2, lines)
        t2 = time.time()
        t3 = (t2 - t1) * 1000
        ts.append(t3)
        print("Number: %d, Time: %.2f ms" % (i + 1, t3))
    print("Average time: %.2f ms" % (sum(ts) / N))
    
    if os.path.exists(PATH2):
        os.remove(PATH2)


if __name__ == '__main__':
    main()
    
