import argparse


def greeting(name):
    print(name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("city")
    args = parser.parse_args()
    greeting(args.name)
    greeting(args.city)
    return 0


if __name__ == "__main__":
    main()

# tracemalloc
# pympler
# objgraph
# memray
# gc
