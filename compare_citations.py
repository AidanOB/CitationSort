__author__ = "Aidan O'Brien"


def common_citations(citation_list_a, citation_list_b):
    """
    Compares two lists of citations and returns the ones in common
    :param citation_list_a: List of citations
    :param citation_list_b: List of citations
    :return: list of citations
    """
    common = []
    match = 0
    for record in citation_list_a[0]:
        for article in record:
            if article.findtext("title") is not None:
                for record_b in citation_list_b[0]:
                    for article_b in record_b:
                        if article_b.findtext("title") is not None:
                            if article.findtext("title") == article_b.findtext("title"):
                                common.append(record)
                                match += 1

    return common, match
