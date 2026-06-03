def create_records(sentences):

    records = []

    for idx, sentence in enumerate(sentences):

        records.append({
            "id": idx + 1,
            "sentence": sentence
        })

    return records