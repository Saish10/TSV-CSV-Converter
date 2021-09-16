#Requirements: pip install argparse 
#To run the program - converter.py inputfile outputfile
import argparse

def convert(inputfile, outputfile, to=None):
    if to == 'csv':
        join_delimeter = ','
        split_delimeter = '\t'
    elif to == 'tsv':
        join_delimeter = '\t'
        split_delimeter = ','
    else:
        return

    with open(inputfile, encoding='utf-8') as ifile, open(outputfile, 'w') as ofile:
        rows = ifile.readlines()
        for row in rows:
            line = join_delimeter.join(row.split(split_delimeter))
            ofile.write(line)
        print("Converted to " + to)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', type=str, help='Input file')
    parser.add_argument('outputfile', type=str, help='Output file')
    args = parser.parse_args()

    if args.inputfile.endswith('.csv') & args.outputfile.endswith('.tsv'):
        convert(args.inputfile, args.outputfile, to='tsv')
    elif args.inputfile.endswith('.tsv') & args.outputfile.endswith('.csv'):
        convert(args.inputfile, args.outputfile, to='csv')
    else:
        print('Invalid conversion')
