from factory_method.json_data_extractor import JSONDataExtractor
from factory_method.xml_data_extractor import XMLDataExtactor
from factory_method.sqlite_data_extractor import SQLiteDataExtractor


def data_extraction_factory(filepath: str):
    if filepath.endswith('.json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('.xml'):
        extractor = XMLDataExtactor
    elif filepath.endswith('.sq3'):
        extractor = SQLiteDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    sqlite_factory = extract_data_from('my_file.sq3')


if __name__ == '__main__':
    main()
