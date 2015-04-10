import numpy as np


# Produces csv file with only results for my GOIs
def extract_genes_of_interest():

    selected_genes_results = []
    genes_of_interest = ["ITPKA","ITPKB","ITPKC","IPMK", "ITPK1", "IPPK", "IP6K1", "IP6K2", "IP6K3", "PPIP5K1", "PPIP5K2"]

    # .gct is a kind of tab-separated txt file, this one is 1.6GB
    with open("GTEx_Analysis_2014-01-17_RNA-seq_RNA-SeQCv1.1.8_gene_rpkm.gct", "r") as rna_seq_data:
        for line in rna_seq_data:
            temp = line.strip().split("\t")
            if temp[0] == "Name": # this is the header line, contains sample information
                selected_genes_results.append(temp)
            elif (len(temp)> 2) and (temp[1] in genes_of_interest): # these are results lines
                selected_genes_results.append(temp)
                print "GOI: %r" % temp

    with open("output_GOI_only.txt", "w") as goi:
        for i in selected_genes_results:
            goi.write(",".join(i))

    print "finished"

# Takes tissue information from Annotations file, adds it to the csv txt from extract_genes_of_interest
def add_tissue_type_to_columns():
    tissue_type_dict = {}

    with open("GTEx_Data_2014-01-17_Annotations_SampleAttributesDS.txt", "r") as SampleAttributes_file:
        for line in SampleAttributes_file:
            temp = line.strip().split("\t")
            if temp[0] != "SAMPID":
                try:
                    tissue_type_dict[temp[0]] = temp[5] + ": " + temp[6]
                    # do a tuple or list here if want to separate the tissues/subtissues after all
                except:
                    print "temp to dict failed, %r" % temp

    #print tissue_type_dict.keys()

    with open("output_GOI_only.txt", "r") as results_file, open("output_GOI_with_tissue_types.txt", "w") as output:
        sample_codes = results_file.readline().strip().split(",") # NB strip before split
        actual_results = results_file.read()
        #print actual_results

        tissues_in_order = []

        #print sample_codes
        for i in sample_codes:
            if i in tissue_type_dict.keys():
                #print "yes it's here %r" % i
                tissues_in_order.append(tissue_type_dict[i])
            else:
                print "no: %r" % i
                tissues_in_order.append("")

        output.write(",".join(sample_codes) + "\n")
        output.write(",".join(tissues_in_order) + "\n")
        output.write(actual_results)

# surely this doesn't really need to be a separate function. But how to get the list back out to upper scope?
def get_names_list():
    with open("output_GOI_with_tissue_types_test.csv", "r") as tt: # this test file is sorted by tissue too
        tt.readline()
        names_list = tt.readline().strip("\n").replace(" ","").replace("-", "").replace(":","").split(",") # Don't strip everything, those empty strings are important
        return names_list

# Tidies the results into an easy format for pasting into GraphPad Prism for pretty graphs
# maybe it would be worth using Pandas so I can have row/column names?

def get_mean_sd_n_for_gene_per_tissue_type():

    names_list = get_names_list()
    #print names_list
    test = np.genfromtxt("output_GOI_with_tissue_types_test.csv", delimiter=",", skip_header=2,  dtype=None, names=names_list)

    print "test %r" % test

    hippo_list = []
    for i in test.dtype.names:
        if "Hippo" in i:
            hippo_list.append(i)
    hippo_columns = test[hippo_list]
    print "hippos %r" % hippo_columns
    #print np.mean(hippo_columns)




#extract_genes_of_interest()
#add_tissue_type_to_columns()
get_mean_sd_n_for_gene_per_tissue_type()