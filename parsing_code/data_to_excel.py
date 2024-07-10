import pandas as pd
from openpyxl.styles import Alignment


def write_to_excel(contract_data, file_path, sheet_name):

    try:
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
            contract_data.to_excel(writer, sheet_name=sheet_name, header=False)

            sheet = writer.sheets[sheet_name]

            for column in sheet.columns:
                max_length = 0
                for cell in column:
                    cell.alignment = Alignment(wrap_text=True)
                    cell_value = str(cell.value)
                    cell_length = max(len(line) for line in cell_value.split('\n'))
                    if cell_length > max_length:
                        max_length = cell_length
                adjusted_width = (max_length + 2)
                sheet.column_dimensions[column[0].column_letter].width = adjusted_width

    except FileNotFoundError:
        contract_data.to_excel(file_path, sheet_name=sheet_name, header=False)

        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as writer:
            sheet = writer.sheets[sheet_name]

            for column in sheet.columns:
                max_length = 0
                for cell in column:
                    cell.alignment = Alignment(wrap_text=True)
                    cell_value = str(cell.value)
                    cell_length = max(len(line) for line in cell_value.split('\n'))
                    if cell_length > max_length:
                        max_length = cell_length
                adjusted_width = (max_length + 2)
                sheet.column_dimensions[column[0].column_letter].width = adjusted_width