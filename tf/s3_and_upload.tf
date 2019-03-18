resource "aws_s3_bucket" "bucket_for_trigger" {
  bucket = "bucket_for_trigger"
  acl    = "private"
}

resource "aws_s3_bucket_object" "data_file" {
  bucket = "bucket_for_trigger"
  key    = "gdata.csv"
  source = "gdata.csv"
  etag   = "${md5(file("gdata.csv"))}"

  depends_on = [
    "aws_s3_bucket_notification.bucket_notification",
    "aws_lambda_permission.allow_bucket",
  ]
}
