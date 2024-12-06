from io import BytesIO
import tempfile

def upload_data_to_s3(s3_client, dataframe, object_name:str, bucket_name:str):
    buffer = BytesIO()
    dataframe.to_parquet(buffer, engine="pyarrow", index=False)
    buffer.seek(0)

    s3_client.put_object(Bucket=bucket_name, Key=object_name, Body=buffer.getvalue())
    
def download_files_from_s3(s3_client, bucket_name:str, object_name:str):
    file_buffer = BytesIO()
    s3_client.download_fileobj(Bucket=bucket_name, Key=object_name, Fileobj = file_buffer)
    file_buffer.seek(0)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.parquet') as temp_file:
        temp_file.write(file_buffer.read())
        return temp_file.name
    