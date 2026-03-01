from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

def bio_pipeline(raw_dna):
    # 1. THE CLEANER 
    # Standardize and audit quality
    clean_dna = raw_dna.strip().upper().replace("N", "")
    n_count = raw_dna.strip().upper().count("N")
    
    # 2. THE ANALYZER 
    # Perform biological calculations
    my_seq = Seq(clean_dna)
    gc_val = gc_fraction(my_seq) * 100
    protein = my_seq.translate()
    
    # 3. THE MASTER REPORT
    # Make it look professional
    print(f"{'='*30}")
    print(f"BIO-INFORMATICS REPORT")
    print(f"{'='*30}")
    print(f"Quality Audit: {n_count} 'N' bases removed.")
    print(f"GC Stability: {gc_val:.2f}%")
    print(f"Protein Code: {protein}")
    print(f"{'='*30}")
    
    return protein

# --- RUNNING THE FINAL TEST ---
my_raw_data = "  atgNNNcccaaatttG  "
result = bio_pipeline(my_raw_data)
