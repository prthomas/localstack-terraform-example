provider "aws" {
  region                      = "${var.config["region"]}"
  skip_requesting_account_id  = "${local.mock}"
  skip_credentials_validation = "${local.mock}"
  skip_metadata_api_check     = "${local.mock}"
  s3_force_path_style         = "${local.mock}"
  profile                     = "${var.config["profile"]}"

  endpoints {
    dynamodb = "http://localhost:4569"
    lambda   = "http://localhost:4574"
    s3       = "http://localhost:4572"
    iam      = "http://localhost:4593"
  }
}
