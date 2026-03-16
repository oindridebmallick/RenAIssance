import Levenshtein

def calculate_cer(reference, hypothesis):
    """
    Calculate Character Error Rate (CER).
    """
    if len(reference) == 0:
        return 1.0 if len(hypothesis) > 0 else 0.0
    
    dist = Levenshtein.distance(reference, hypothesis)
    return dist / len(reference)

def calculate_wer(reference, hypothesis):
    """
    Calculate Word Error Rate (WER).
    """
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    if len(ref_words) == 0:
        return 1.0 if len(hyp_words) > 0 else 0.0
    
    # Use Levenshtein distance on words
    dist = Levenshtein.distance(ref_words, hyp_words)
    return dist / len(ref_words)

if __name__ == "__main__":
    ref = "en el principio era el verbo"
    hyp = "en el principio era el vurbo"
    print(f"CER: {calculate_cer(ref, hyp):.4f}")
    print(f"WER: {calculate_wer(ref, hyp):.4f}")
