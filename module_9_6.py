def all_variants(text):
    for length in range(0, len(text)):
        for sequences in range(len(text)):
            if sequences + length < len(text):
                yield text[sequences: length + sequences + 1]

a = all_variants("abc")
for i in a:
    print(i)
