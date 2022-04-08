#!/usr/bin/env python
import os
import time
import gzip
import unittest
from pygz import GzipFile, PigzFile


def read_by_gzip(path):
    with GzipFile(path, "rt") as f:
        lines = [line for line in f]
    return lines


def write_by_gzip(path, lines):
    with GzipFile(path, "wt") as fw:
        for line in lines:
            fw.write(line)


def read_by_pigz(path):
    with PigzFile(path, "rt") as f:
        lines = [line for line in f]
    return lines


def write_by_pigz(path, lines):
    with PigzFile(path, "wt") as fw:
        for line in lines:
            fw.write(line)


def read_by_gzip_pkg(path):
    with gzip.open(path, "rt") as f:
        lines = [line for line in f]
    return lines


def write_by_gzip_pkg(path, lines):
    with gzip.open(path, "wt") as fw:
        for line in lines:
            fw.write(line)


PATH1 = "tests/data/GRCh39.p13.chr1.1000000.fa.gz"
PATH2 = "tests/data/out.test.gz"
N = 5


class TestPygz(unittest.TestCase):

    def test_gzip(self):
        print()

        print("=" * 60)
        print("Read by gzip subprocess:")
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
        print("Write by gzip subprocess:")
        ts = []
        for i in range(N):
            t1 = time.time()
            write_by_gzip(PATH2, lines)
            t2 = time.time()
            t3 = (t2 - t1) * 1000
            ts.append(t3)
            print("Number: %d, Time: %.2f ms" % (i + 1, t3))
        print("Average time: %.2f ms" % (sum(ts) / N))

        if os.path.exists(PATH2):
            os.remove(PATH2)

        print()

    def test_pigz(self):
        print()

        print("=" * 60)
        print("Read by pigz subprocess (4 threads):")
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
        print("Write by pigz subprocess (4 threads):")
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

        print()

    def test_gzip_package(self):
        print()

        print("=" * 60)
        print("Read by gzip package:")
        ts = []
        for i in range(N):
            t1 = time.time()
            lines = read_by_gzip_pkg(PATH1)
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
            write_by_gzip_pkg(PATH2, lines)
            t2 = time.time()
            t3 = (t2 - t1) * 1000
            ts.append(t3)
            print("Number: %d, Time: %.2f ms" % (i + 1, t3))
        print("Average time: %.2f ms" % (sum(ts) / N))

        if os.path.exists(PATH2):
            os.remove(PATH2)

        print()


if __name__ == '__main__':
    unittest.main()
