import os

def parse_edi_file(edi_file_path):
    with open(edi_file_path, 'r') as file:
        edi_content = file.read().strip()
        
    segments = edi_content.split('~')
    parsed_segments = [segment.split('*') for segment in segments]
    
    return parsed_segments

def extract_edi_data(segments, transaction_set):
    extracted_data = []
    
    if transaction_set == "810":
        # 810 - Invoice specific segments
        for segment in segments:
            if segment[0] in ("BIG", "ITD", "IT1", "TDS"):
                extracted_data.append(segment)
                
    elif transaction_set == "850":
        # 850 - Purchase Order specific segments
        for segment in segments:
            if segment[0] in ("BEG", "REF", "PO1", "CTT"):
                extracted_data.append(segment)
    
    return extracted_data

def print_edi_data(data, transaction_set):
    print(f"\nExtracted {transaction_set} Data:")
    for segment in data:
        print(f"{segment[0]}: {' | '.join(segment[1:])}")

if __name__ == "__main__":
    edi_file_path = "sample_edi_file.txt"  # Replace with your EDI file path
    
    if not os.path.exists(edi_file_path):
        print(f"File not found: {edi_file_path}")
    else:
        segments = parse_edi_file(edi_file_path)
        
        # Extract and print 810 data
        edi_810_data = extract_edi_data(segments, "810")
        print_edi_data(edi_810_data, "810")
        
        # Extract and print 850 data
        edi_850_data = extract_edi_data(segments, "850")
        print_edi_data(edi_850_data, "850")
