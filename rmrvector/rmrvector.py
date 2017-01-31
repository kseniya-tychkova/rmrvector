# -*- coding: utf-8 -*-

"""Calculate scalar product"""

import argparse
from json import loads


class Vector:
    """Iterable compressed vector.

    :param data: A list of data.
    """
    def __init__(self, data):
        self.data = data
        self.pointer = 0
        self.counter = data[self.pointer + 1]

    def __iter__(self):
        return self

    def __next__(self):
        """ Gets next value from compressed vector.

        :return: next value
        """

        # pointer is the current value
        # counter is an item next to pointer
        # take value from pointer position and reduce
        # counter until counter is not 0
        # if counter == 0 move pointer to the next position
        # with value (stride=2)
        if self.counter <= 0:
            # move pointer to the next item
            self.pointer += 2
            try:
                # take counter
                self.counter = self.data[self.pointer + 1]
            except IndexError:
                raise StopIteration

        # take value from pointer position and reduce counter
        value = self.data[self.pointer]
        self.counter -= 1

        return value


def scalar_product(data_1, data_2):
    """Calculate scalar product

    :param data_1: first list with compressed vector
    :param data_2: second list with compressed vector
    :return: scalar product of decompressed vectors
    """
    # decompress and merge vectors
    merged_vector = zip(Vector(data_1), Vector(data_2))

    # math calculation of scalar product
    return sum([v1*v2 for v1, v2 in merged_vector])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input', type=argparse.FileType('r'),
                        required=True, help='Input file')
    args = parser.parse_args()

    try:
        # load data from input file
        vector_1 = loads(args.input.readline())
        vector_2 = loads(args.input.readline())
    except ValueError as exc:
        raise SystemExit("Error in input file:", exc)

    print("Scalar product = %d" % scalar_product(vector_1, vector_2))
