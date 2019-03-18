resource "aws_dynamodb_table" "gdata" {
  name           = "gdata"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "sales"
  range_key      = "business"

  attribute = [{
    name = "sales"
    type = "S"
  },
    {
      name = "business"
      type = "S"
    },
  ]

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }
}
