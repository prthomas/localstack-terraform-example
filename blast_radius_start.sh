cwd=`pwd`
cd $cwd/tf
terraform init
terraform validate
cd $cwd
blast-radius --serve ./tf
