#!/usr/bin/env python3
import pandas as pd
import sys

try:
    # Read the Excel file
    xl_file = pd.ExcelFile('Solutions_Exchange_Functional_Requirements.xlsx')
    print("Available sheets:", xl_file.sheet_names)
    
    # Read each sheet and display content
    for sheet_name in xl_file.sheet_names:
        print(f"\n{'='*50}")
        print(f"SHEET: {sheet_name}")
        print(f"{'='*50}")
        
        df = pd.read_excel('Solutions_Exchange_Functional_Requirements.xlsx', sheet_name=sheet_name)
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        # Display all content for smaller sheets, or first 20 rows for larger ones
        if len(df) <= 20:
            print("\nAll content:")
            for i, row in df.iterrows():
                print(f"Row {i+1}:")
                for col in df.columns:
                    if pd.notna(row[col]):
                        print(f"  {col}: {row[col]}")
                print()
        else:
            print("\nFirst 20 rows:")
            for i, row in df.head(20).iterrows():
                print(f"Row {i+1}:")
                for col in df.columns:
                    if pd.notna(row[col]):
                        print(f"  {col}: {row[col]}")
                print()
        
except Exception as e:
    print(f"Error reading Excel file: {e}")
    import traceback
    traceback.print_exc()
