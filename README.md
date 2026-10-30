# Codon Table Generator

## 1. Project overview
The Codon Table Generator is a Python program that displays the standard genetic code and translates a DNA or RNA sequence into amino-acid names. It is a beginner-level bioinformatics project for practising dictionaries, loops, conditionals, string handling, and input validation.

## 2. Objectives
- Store all 64 codons and their corresponding amino-acid meanings in a Python dictionary.
- Accept a DNA or RNA sequence from the user.
- Check that the sequence contains only valid nucleotides.
- Divide the sequence into groups of three nucleotides (codons).
- Translate each complete codon.
- Identify start and stop codons.
- Warn about one or two leftover nucleotides at the end.
- Display the complete codon table and translation results.

## 3. Requirements
- Python 3.8 or later
- No external Python packages are required.

## 4. How to run
1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python codon_table_generator.py
   ```

   On some systems, use `python3 codon_table_generator.py`.

4. Choose `DNA` or `RNA`.
5. Enter a sequence, for example `ATGGCTTTTTAA`.

## 5. Example
Input:
- Sequence type: `DNA`
- Sequence: `ATGGCTTTTTAA`

Expected translation:
- Codons: `ATG - GCT - TTT - TAA`
- Amino acids: `Methionine - Alanine - Phenylalanine - Stop`
- Start codon: `ATG`
- Stop codon: `TAA`

The program prints a table containing all 64 DNA codons before showing the sequence translation.

## 6. Biological background
A codon is a group of three nucleotides. In the standard genetic code, each codon specifies an amino acid or a translation stop signal. `ATG` is the standard DNA start codon and codes for methionine. The DNA stop codons are `TAA`, `TAG`, and `TGA`. For RNA, the corresponding letters use `U` instead of `T`; this program converts RNA `U` to DNA `T` internally before translation.

This is a simple translation exercise. It translates codons from the first nucleotide in the entered sequence and does not search for a reading frame or stop translation at the first stop codon.

## 7. Input validation and incomplete codons
DNA input may contain only `A`, `T`, `G`, and `C`. RNA input may contain only `A`, `U`, `G`, and `C`. Lowercase input is accepted because the program converts it to uppercase. Spaces at the beginning or end are removed. If the sequence length is not divisible by three, the final one or two nucleotides are reported as an incomplete codon and are not translated.

## 8. Main Python concepts used
- **Dictionary:** stores each codon and its meaning.
- **Set:** stores allowed nucleotides and start/stop codons.
- **Function:** separates the program into reusable tasks.
- **Loop:** processes every codon.
- **Conditional statement:** checks input and identifies start/stop codons.
- **String methods:** `strip()` and `upper()` clean user input; `replace()` converts RNA to DNA notation.
- **List:** stores codons and amino-acid names for display.

## 9. Testing checklist
- [ ] DNA example: `ATGGCTTTTTAA`
- [ ] RNA example: `AUGGCUUUUUAA`
- [ ] Invalid DNA character: `ATGX`
- [ ] Incomplete sequence: `ATGGCTA`
- [ ] Empty input
- [ ] Sequence with no start codon
- [ ] Sequence containing each stop codon: `TAA`, `TAG`, and `TGA`

## 10. Comparison with an online codon table
Compare the dictionary in `codon_table_generator.py` with a custom codon table in a GitHub repository or a reliable standard genetic-code reference. Check that:
1. There are exactly 64 unique codons.
2. Each codon is made of three DNA bases.
3. Each codon maps to the correct amino acid or `Stop`.
4. `ATG` maps to Methionine.
5. `TAA`, `TAG`, and `TGA` map to Stop.

Record the repository URL, date checked, and any differences found here before submission:

- Repository/reference checked: **[add URL]**
- Date checked: **[add date]**
- Result: **[write what you found; do not claim a comparison until you have actually done it]**

## 11. Limitations
- Uses the standard genetic code.
- Assumes the entered sequence begins in the reading frame to be translated.
- Does not identify open reading frames or predict a complete protein.
- Treats a stop codon as a displayed translation result rather than stopping the display at that point.

## 12. Author
Add your name and course details here before submitting.
