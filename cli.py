# Making whole suite work out of command line
import argparse
import loc_check
import t_time
from os import getcwd


def cli():
    cur_dir = getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("test", help="Run selected test",
                        type=str)
    args = parser.parse_args()

    # Missing localisation test
    if 'loc' in args.test:
        cur_dir = cur_dir + '/common/technologies'
        loc_check.print_output()

    # Count all tech time for each file
    if 'tech' in args.test:
        t_time.t_time()


if __name__ == '__main__':
    cli()
