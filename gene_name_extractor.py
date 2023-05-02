import sys
import argparse
def main():
    import os
    # got rid of dest for argparse bc it wasn't working
    parser = argparse.ArgumentParser(description='Extract gene names from fasta file.')
    parser.add_argument("input",help="Input Fasta File",action="store")
    parser.add_argument("output",help="Output File",action="store")
    #parser.add_argument("-t",help="Number of Cores",action="store",dest="threads",type=int, default=-1, required=False)
    args = parser.parse_args()
    if not os.path.isfile(args.input):
        print (args.input, "is not a correct file path!")
        sys.exit()




    output_prefix = "_genenamesoutput"
    with open(args.input, "r") as inputf:
        gene_names_lst = []
        #loop over each line in the file
        for line in inputf:
            header_info = 'None'
            if line[0] == '>':
               header_info = line.split('gene=')
               genenameblock = header_info[1]
               genenameblock2 = genenameblock.split(';')
               gene_name = genenameblock2[0]
               gene_names_lst.append(gene_name)
               gene_names_str = ', '.join(gene_names_lst)

    num_genes = str(len(gene_names_lst))
    with open(args.output, "w") as outputf:
        outputf.write(gene_names_str)
        outputf.write("\n")
        outputf.write(num_genes)
main()
