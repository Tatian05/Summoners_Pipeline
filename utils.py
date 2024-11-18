from pyspark.sql.types import IntegerType, StringType, FloatType
from io import BytesIO
import tempfile

def map_from_pandas_to_spark(dtype):
    if dtype in ['int64', 'int32']:
        return IntegerType()
    elif dtype == 'float64':
        return FloatType()
    elif dtype in ['string', 'object']:
        return StringType()
    else:
        return ValueError(f'Type not soported: {dtype}')
    

def upload_dataframe_to_s3(s3_client, dataframe, object_name:str, bucket_name:str):
    csv_buffer = BytesIO()
    dataframe.to_csv(csv_buffer, index=False)

    s3_client.put_object(Bucket=bucket_name, Key=object_name, Body=csv_buffer.getvalue())
    
def download_files_from_s3(s3_client, bucket_name:str, object_name:str):
    file_buffer = BytesIO()
    s3_client.download_fileobj(Bucket=bucket_name, Key=object_name, Fileobj = file_buffer)
    file_buffer.seek(0)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_file:
        temp_file.write(file_buffer.read())
        return temp_file.name
    