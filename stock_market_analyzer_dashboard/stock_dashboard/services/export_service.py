def dataframe_csv_bytes(df):
    return df.to_csv(index=True, index_label="Date").encode("utf-8")

def dataframe_excel_bytes(df):
    from io import BytesIO
    output = BytesIO()
    with __import__("pandas").ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Price History", index=True, index_label="Date")
    return output.getvalue()
