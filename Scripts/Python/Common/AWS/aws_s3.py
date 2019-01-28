import boto3

s3 = boto3.resource('s3')

def s3_list_all_buckets() :
    buckets = []
    for bucket in s3.buckets.all() :
        buckets.append(bucket.name)
    return buckets

def s3_list_objects (bucketname) :
    objects = []
    bucket = s3.Bucket(bucketname)
    for object in bucket.objects.all() :
        objects.append(object.key)
    return objects
