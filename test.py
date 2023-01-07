from aws_cdk import App, Stack
from aws_cdk.assertions import Template
from jsii_demo import SecureBucket


def test_secure_bucket():
    # GIVEN
    app = App()

    # WHEN
    stack = Stack(app, 'test-stack', env={
        "account": "111111111111",
        "region": "eu-west-1"
    })

    # THEN
    SecureBucket(stack, "my-bucket", bucket_name="helloworld")

    template = Template.from_stack(stack)

    template.has_resource_properties("AWS::S3::Bucket",
                          {
                              "BucketEncryption": {
                                  "ServerSideEncryptionConfiguration": [
                                      {
                                          "ServerSideEncryptionByDefault": {
                                              "SSEAlgorithm": "aws:kms"
                                          }
                                      }
                                  ]
                              }
                          }
    )
    template.resource_count_is("AWS::S3::Bucket", 1)

