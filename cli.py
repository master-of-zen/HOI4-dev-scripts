# Making whole suite work out of command line
import argparse
import loc_check
import t_time
import all_ic
from os import getcwd


def cli():
    cur_dir: str = getcwd()
    parser = argparse.ArgumentParser()
    parser.add_argument("test", help="Run selected test \n loc - localisation check\n tech - all tech time",
                        type=str)
    args = parser.parse_args()

    # Missing localisation test
    if 'loc' in args.test:
        cur_dir = cur_dir + '/common/technologies'
        loc_check.localisation_check(cur_dir)

    # Count all tech time for each file
    if 'tech' in args.test:
        t_time.t_time(cur_dir)

    # Get list of all equipment IC
    if 'ic' in args.test:
        all_ic.f_ic_cost(cur_dir)


if __name__ == '__main__':
    cli()
