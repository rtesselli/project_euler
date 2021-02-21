import pydoc
import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help="Problem ID")
    return parser.parse_args()


def main():
    args = parse_args()
    fn = pydoc.locate(f"solutions.problem{args.id}")
    start_time = time.time()
    result = fn()
    end_time = time.time() - start_time
    print(f"Result: {result}")
    print(f"Took: {end_time}")


if __name__ == '__main__':
    main()
