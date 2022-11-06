- Terraform deployment
```
cd tf
terraform init
terraform plan
terraform apply -auto-approve

```

- Invoke lambda
```
{
  "object_name": "print.pbm"
}
```

- Function call

curl -X POST https://REPLACE_ME_LAMBDA_URL.lambda-url.us-east-1.on.aws \
-H 'content-type: application/json' \
--data '{"object_name":"print.pbm"}'