from genome import Genome


# TODO: train "iseq" model
MODELS = ["novaseq", "miseq", "hiseq"]

# We're committed to uniform.
UNIFORM_ABUNDANCE = "uniform"

# 2x this for a pair
READ_SIZE = 150


TOP_6_ID_GENOMES = [
    Genome("bacteria", "klebsiella_pneumoniae_HS11286",
           [("subspecies", 1125630), ("species", 573), ("genus", 570), ("family", 543)],
           ["NC_016845.1"]),

    Genome("fungi", "aspergillus_fumigatus",
           [("subspecies", 330879), ("species", 746128), ("genus", 5052), ("family", 1131492)],
           ["NC_007194.1", "NC_007195.1", "NC_007196.1", "NC_007197.1", "NC_007198.1", "NC_007199.1",
            "NC_007200.1", "NC_007201.1"],
           "https://www.ncbi.nlm.nih.gov/genome/18?genome_assembly_id=22576"),

    Genome("viruses", "rhinovirus_c",
           [("subspecies", 0), ("species", 463676), ("genus", 12059), ("family", 12058)],
           ["MG148341.1"]),

    Genome("viruses", "chikungunya",
           [("subspecies", 0), ("species", 37124), ("genus", 11019), ("family", 11018)],
           ["MG049915.1"]),

    Genome("bacteria", "staphylococcus_aureus",
           [("subspecies", 93061), ("species", 1280), ("genus", 1279), ("family", 90964)],
           ["NC_007795.1"],
           "https://www.ncbi.nlm.nih.gov/genome/154?genome_assembly_id=299272"),

    Genome("protista", "plasmodium_falciuparum",
           [("subspecies", 36329), ("species", 5833), ("genus", 5820), ("family", 1639119)],
           ["NC_004325.2", "NC_037280.1", "NC_000521.4", "NC_004318.2", "NC_004326.2",
            "NC_004327.3", "NC_004328.3", "NC_004329.3", "NC_004330.2", "NC_037281.1",
            "NC_037282.1", "NC_037284.1", "NC_004331.3", "NC_037283.1", "NC_036769.1"],
           "https://www.ncbi.nlm.nih.gov/genome/33?genome_assembly_id=22642")
]
