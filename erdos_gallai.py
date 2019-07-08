import argparse
import logging as log

def erdos_gallai(degrees, verbose = False):

    degree_sum = sum(degrees)
    if  degree_sum % 2 != 0:
        log.info(f'Degree sum = {degree_sum} : not even')
        return False
    
    degrees = sorted(degrees, reverse = True)
    n = len(degrees)
    for k in range(1, n + 1):
        lhs = sum(degrees[i] for i in range(k));
        rhs1 = k*(k - 1)
        rhs2 = sum(min(k, degrees[i]) for i in range(k, n))
        res = lhs <= rhs1 + rhs2
        
        log.info(f'{lhs} <= {rhs1} + {rhs2} : {res}')

        if not res:
            return False
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check if degree sequence valid')
    parser.add_argument('-d', '--degrees', type=int, nargs='+',
                        help="Degrees of the graph")
    parser.add_argument('-v', '--verbose', action="count", 
                        help="Print result of intermediate steps")
    
    args = parser.parse_args()
    if args.verbose:
        log.basicConfig(format = "%(message)s", level=log.DEBUG)

    print(erdos_gallai(args.degrees, verbose = True))

