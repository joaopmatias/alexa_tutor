import sys
import boto3
from botocore import UNSIGNED
from botocore.client import Config 


def update_student():
	s3_student = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
	s3_student.Bucket('alexatutor').download_file('all.txt', 'all.txt')


if __name__ == '__main__':
	update_student()