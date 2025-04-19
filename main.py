import pandas as pd
import argparse
from pgeocode import Nominatim

def get_state(zipcode, geo):
    if zipcode and pd.notna(zipcode):
        result = geo.query_postal_code(zipcode)
        if result is not None:
            state_code = result.get('state_code', '')
            state_name = result.get('state_name', '')
            return state_code, state_name
    return None, None

def main(country, input_file, output_file, zipcode_col, state_code_col, state_col):
    df = pd.read_csv(input_file)
    df[zipcode_col] = df[zipcode_col].astype(str).str.zfill(5)

    geo = Nominatim(country)
    df[[state_code_col, state_col]] = df[zipcode_col].apply(get_state, geo=geo).apply(pd.Series)

    df.to_csv(output_file, index=False)
    print(f"Updated file saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process zip codes and add state information.")

    parser.add_argument('--country', default='US', type=str, help="Country code to process zip codes (default: US)")
    parser.add_argument('--input_file', default='Data/dfZip.csv', type=str, help="Path to the input CSV file (default: Data/dfZip.csv)")
    parser.add_argument('--output_file', default='Data/outputZip.csv', type=str, help="Path to save the output CSV file (default: Data/outputZip.csv)")
    parser.add_argument('--zipcode_col', default='zipcode', type=str, help="Name of the column containing zip codes (default: zipcode)")
    parser.add_argument('--state_code_col', default='state_code', type=str, help="Name of the column to store state codes (default: state_code)")
    parser.add_argument('--state_col', default='state', type=str, help="Name of the column to store state names (default: state)")

    args = parser.parse_args()

    print('Processing ...')
    
    main(args.country, args.input_file, args.output_file, args.zipcode_col, args.state_code_col, args.state_col)

