from analyzers.eml_parser import parse_eml_file

with open("sample.eml", "rb") as f:

    result = parse_eml_file(f)

    print(result)