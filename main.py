import noddy4
import gc


class CollectOnDelete(object):

    def __del__(self):
        gc.collect()


def make_noddy():
    n = noddy4.Noddy()
    n.first = CollectOnDelete()


def main():
    for i in range(100):
        make_noddy()


if __name__ == '__main__':
    main()
