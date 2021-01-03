modified = ""

with open("../data/snp_result.txt", "r") as snp_file:
    modified = snp_file.read()

modified = modified.replace(",", "|")
modified = modified.replace("\t", ",")

with open("../data/snps.csv", "w") as snp_csv:
    snp_csv.write(modified)
