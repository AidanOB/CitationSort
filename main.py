import init
import load_citations
import compare_citations
import save_citations

__author__ = "Aidan O'Brien"


def main():
    """Load the files, first by filename from init, then the xml files. Then compare the two and save the outputted
    files"""
    files = init.file_list
    citations = load_citations.load_files(files)
    citations_a = citations[0]
    citations_b = citations[1]

    common_citations, num_common = compare_citations.common_citations(citations_a, citations_b)
    save_citations.save_citations(common_citations)


if __name__ == "__main__":
    main()
