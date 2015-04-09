from_samples_file = []
sample_dict = {}
raw_input_data = []

genes_of_interest = ["ITPKA","ITPKB","ITPKC","IPMK", "ITPK1", "IPPK", "IP6K1", "IP6K2", "IP6K3", "PPIP5K1", "PPIP5K2"]
selected_genes_results = []


with open("GTEx_Data_2014-01-17_Annotations_SampleAttributesDS.csv", "r") as SampleAttributes_file:
    for line in SampleAttributes_file:
        from_samples_file.append(line.split("\t")) #  each line is now a list, inside main list

from_samples_file.pop(0) # remove list item at index 0

for i in from_samples_file:
    sample_dict[i[0]] = i[5:7] # make key from 1st index of each inner list, with values as list containing 2 items
#print from_samples_file
#print sample_dict

# this file is 1.6 GB, be careful!
#with open("GTEx_Analysis_2014-01-17_RNA-seq_RNA-SeQCv1.1.8_gene_rpkm.gct", "r") as rna_seq_data:
    for line in rna_seq_data:
        raw_input_data.append(line.split("\t"))
        # this failed because MemoryError. how to process more efficiently - can whittle down before append?
        # lists aren't great memory-wise
        # maybe use CSV library?


#print raw_input_data
raw_input_data.pop(0)
raw_input_data.pop(0)
raw_input_data.pop(0) # remove first 3 rows

for i in raw_input_data:
    if i[1] in genes_of_interest:
        selected_genes_results.append(i)

#print selected_genes_results

with open("output.txt", "w") as translated_results:
    for i in selected_genes_results:
        try:
            tissue_plus = sample_dict[i]
            output = i + "\t" + tissue_plus[0] + "\t" + tissue_plus[1] + "\n"
            #print "output: %r" % output
            translated_results.write(output)
        except:
            #print "not in dict"
            pass
print "finished"