from Bio import SeqIO


def extract_protein_sequences(input_file):
    for record in SeqIO.parse(input_file, "genbank"):

        for feature in record.features:
            if feature.type == "CDS":

                protein_id = record.id
                description = record.description
                location = feature.location
                translation = feature.qualifiers.get('translation', [''])[0]

                print(f"{protein_id}: {description}")
                print(f"Coding sequence location = [{location.start}:{location.end}]({location.strand})")
                print("Translation =")
                print(translation)
                print()


if __name__ == "__main__":
    input_file ="D:/first\pythonProject\combined_species.gb"
    extract_protein_sequences(input_file)