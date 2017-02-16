import time
import hashlib
from sys import argv

def encrypt(hash_object, text):

    hash_object.update(text)

if __name__ == "__main__":

    if len(argv) != 3:

        print "Format: python ej5benchmark.py <filename> <iterations>"
        exit()

    else:

        filename = argv[1]
        iterations = int(argv[2])

    sha = hashlib.sha512()
    file_lines = []
    test_times = []

    print "This benchmark measures the performance of your processor by encrypting a text line by line as many times as you want."
    print "The test will be repeated thrice and the mean time will be the final result."

    with open(filename) as file:

        for line in file:

            file_lines.append(line)

    for repetition in xrange(3):

        before = time.clock()

        for i in xrange(iterations):

            for line in file_lines:

                encrypt(sha, line)

        after = time.clock()

        test_times.append(after-before)

    print "Time to complete the first run: %f seconds." % test_times[0]
    print "Time to complete the second run: %f seconds." % test_times[1]
    print "Time to complete the third run: %f seconds." % test_times[2]
    print "Mean: %f seconds." % (sum(test_times)/3.0)