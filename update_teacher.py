import sys
import boto3
from botocore import UNSIGNED
from botocore.client import Config 

# teacher should sign-in with their credentials through awscli

def update_teacher():
	s3_teacher = boto3.resource('s3')
	data = open('all.txt', 'rb')
	s3_teacher.Bucket('alexatutor').put_object(ACL='public-read',Key='all.txt', Body=data)
	data.close()



if __name__ == '__main__':
	update_teacher() 
