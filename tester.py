from the4 import check_commands
from test_data import *

test_no = 1
error = 0
while test_no < 16:
    test_fs = "FS" + "%03d" % test_no
    test_c = "C" + "%03d" % test_no
    test_r = "R" + "%03d" % test_no
    if check_commands(vars()[test_fs], vars()[test_c]) != vars()[test_r]:
        print "-" * 30 + "%03d" % test_no + "-" * 30
        print test_fs + " >", vars()[test_fs]
        print test_c + " >", vars()[test_c][0]
        for x in vars()[test_c][1:]:
            print " " * 7 + x
        print "Result >", check_commands(vars()[test_fs], vars()[test_c])
        print "Ex.Result >", vars()[test_r]
        error += 1
    test_no += 1
print "-" * 63 + "\n" + "Test completed with", error, "errors."
