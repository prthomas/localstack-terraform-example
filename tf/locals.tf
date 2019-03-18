locals {
  mock      = "${var.config["env"] == "production" ? false : true}"
  code_path = "${path.cwd}/../zip"
}
