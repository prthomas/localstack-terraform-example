resource "aws_lambda_function" "example" {
  filename         = "${local.code_path}/example.zip"
  function_name    = "lambda_example"
  role             = "${aws_iam_role.role.arn}"
  handler          = "example.s3_to_dynamodb"
  source_code_hash = "${base64sha256(file("${local.code_path}/example.zip"))}"
  runtime          = "python3.7"
}

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.example.arn}"
  principal     = "s3.amazonaws.com"
  source_arn    = "${aws_s3_bucket.bucket_for_trigger.arn}"
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = "${aws_s3_bucket.bucket_for_trigger.id}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.example.arn}"
    events              = ["s3:ObjectCreated:*"]
  }
}
