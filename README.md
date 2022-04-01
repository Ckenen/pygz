# Pigz wrapper

This repository is a wrapper for python to utilize pigz to compress or decompress data in parallel.

At first, you should add the path of this repository to your PYTHONPATH, or copy the pigz.py to your site-packages directory.

For reading:

    from pigz import PigzFile
    with PigzFile("input.gz") as f:
        for line in f:
            print(line)

For writing:

    from pigz import PigzFile
    threads = 4 # default
    with PigzFile("output.gz", "wt", threads) as fw:
        for line in lines:
            fw.write(line)

For testing:

    ./test_pigz.py

the output is as follows:

    ============================================================
    Read by gzip package:
    Number: 1, Time: 889.35 ms
    Number: 2, Time: 931.01 ms
    Number: 3, Time: 967.92 ms
    Number: 4, Time: 920.07 ms
    Number: 5, Time: 958.66 ms
    Average time: 933.40 ms
    ============================================================
    Read by pigz subprocess:
    Number: 1, Time: 483.14 ms
    Number: 2, Time: 414.45 ms
    Number: 3, Time: 413.28 ms
    Number: 4, Time: 460.89 ms
    Number: 5, Time: 468.44 ms
    Average time: 448.04 ms
    ============================================================
    Write by gzip package:
    Number: 1, Time: 66915.84 ms
    Number: 2, Time: 67248.85 ms
    Number: 3, Time: 65625.26 ms
    Number: 4, Time: 65328.97 ms
    Number: 5, Time: 65264.58 ms
    Average time: 66076.70 ms
    ============================================================
    Write by pigz subprocess:
    Number: 1, Time: 3522.61 ms
    Number: 2, Time: 3740.81 ms
    Number: 3, Time: 3542.37 ms
    Number: 4, Time: 3541.36 ms
    Number: 5, Time: 4064.07 ms
    Average time: 3682.24 ms