import boto3
import requests


bucket_name = 'my-first-bucket-yez9pj' 
object_name = 'steph_curry.gif'  
url_to_download = "https://i.pinimg.com/originals/f0/52/0c/f0520ca3cf50836182ecefef1d75084b.gif"
expires_in = 60

response = requests.get(url_to_download)
with open(object_name, 'wb') as f:
    f.write(response.content)

s3 = boto3.client('s3', region_name='us-east-1')
with open(object_name, 'rb') as data:
    s3.put_object(Bucket=bucket_name, Key=object_name, Body=data, ContentType='image/gif')

presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print("Presigned URL:")
print(presigned_url)
