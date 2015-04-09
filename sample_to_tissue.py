# Produces csv file with only results for my GOIs
def extract_genes_of_interest():

    selected_genes_results = []
    genes_of_interest = ["ITPKA","ITPKB","ITPKC","IPMK", "ITPK1", "IPPK", "IP6K1", "IP6K2", "IP6K3", "PPIP5K1", "PPIP5K2"]

    # this file is 1.6GB
    with open("GTEx_Analysis_2014-01-17_RNA-seq_RNA-SeQCv1.1.8_gene_rpkm.gct", "r") as rna_seq_data:
        for line in rna_seq_data:
            temp = line.split("\t")
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
    pass

from_samples_file = []
sample_dict = {}

with open("GTEx_Data_2014-01-17_Annotations_SampleAttributesDS.csv", "r") as SampleAttributes_file:
    for line in SampleAttributes_file:
        from_samples_file.append(line.split("\t")) #  each line is now a list, inside main list

from_samples_file.pop(0) # remove list item at index 0

for i in from_samples_file:
    sample_dict[i[0]] = i[5:7] # make key from 1st index of each inner list, with values as list containing 2 items


# with open("output_GOI_only.txt", "w") as translated_results:
#     for i in selected_genes_results:
#         try:
#             tissue_plus = sample_dict[i]
#             output = i + "\t" + tissue_plus[0] + "\t" + tissue_plus[1] + "\n"
#             print "output: %r" % output
#             translated_results.write(output)
#         except:
#             #print "not in dict"
#             pass


# Could combine this function with the one below
def aggregate_values_by_tissue_type():
    pass

# Tidies the results into an easy format for pasting into GraphPad Prism
# I doubt Python can make graphs as pretty as Prism's
def get_mean_sd_n_for_gene_per_tissue_type():
    pass



