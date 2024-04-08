from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

from Bio import pairwise2
from Bio.pairwise2 import format_alignment


def calculate_similarity(sequence1, sequence2):

    sequence1 = str(sequence1)
    sequence2 = str(sequence2)
    
    alignments = pairwise2.align.globalxx(sequence1, sequence2)

    # Extract the best alignment
    best_alignment = alignments[0]

    # Compute similarity score
    similarity_score = (best_alignment[2] / len(sequence1)) * 100  # Percentage similarity

    # Print alignment and similarity score
    #print(format_alignment(*best_alignment))
    print("Similarity Score:", similarity_score)

# Example usage


# Define your sequences
# sequence1 = "ACCGT"
# sequence2 = "ACGGG"

# Perform pairwise alignment
    # Perform BLAST search
    # result_handle = NCBIWWW.qblast("blastn", "nt", sequence1 + sequence2)

    # # Parse BLAST results
    # blast_records = NCBIXML.parse(result_handle)
    # for blast_record in blast_records:
    #     for alignment in blast_record.alignments:
    #         for hsp in alignment.hsps:
    #             # Calculate similarity score (percent identity)
    #             similarity_score = (hsp.identities / hsp.align_length) * 100
    #             return similarity_score
    #Bio.Align.PairwiseAligner



# this code is for adnan's reference -- nothing to do with this file

#     cur = mysql.connection.cursor()

# sql_get_sq = "SELECT Sequence FROM genome WHERE Accession = %s"

# cur.execute(sql_get_sq, ["AE002163"])
# data_first_seqn = cur.fetchall()
# sql_get_sq = "SELECT Sequence FROM genome WHERE Accession = %s"
# cur.execute(sql_get_sq, ["EF380032"])
# data_second_seqn  = cur.fetchall()

# # sql_host = "SELECT * FROM host WHERE Host = %s"
# # cur.execute(sql_host, [accession_id])
# # data_genome = cur.fetchall()
# # species = data_genome[0][1]
# # genome_length = data_genome[0][2]
# # modification_date = data_genome[0][3]

# cur.close()
# similarity = calculate_similarity(data_first_seqn, data_second_seqn)
# print(similarity)
