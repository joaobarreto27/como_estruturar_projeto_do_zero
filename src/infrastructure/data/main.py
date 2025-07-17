from pipeline import extract, load, transform

if __name__ == "__main__":
    data_frame_list = extract.extract_from_excel(
        folder_name="input", extension_type="xlsx"
    )
    df = transform.contact_data_frames(data_frame_list=data_frame_list)
    load.load_excel(df, "output", "output_etl")
