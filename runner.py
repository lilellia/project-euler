import argparse
import datetime
import importlib
import sys


def run(problem: int):
    # import corresponding problem main function
    try:
        module = importlib.import_module(f'src.pe{problem:03}')
    except ModuleNotFoundError:
        sys.exit(f'Code for problem #{problem} could not be loaded.')

    # run the module's main method inside this timer
    start = datetime.datetime.now()
    answer = module.main()
    elapsed = (datetime.datetime.now() - start).total_seconds()

    return answer, elapsed


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('problem', type=int)
    args = parser.parse_args()

    answer, elapsed = run(args.problem)
    print(f' Answer: {answer}')
    print(f'Elapsed: {1000000 * elapsed:,.0f} us')
