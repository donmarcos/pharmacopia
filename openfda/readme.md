## Run Notebook in Local Machine

### AWS Configuration

- Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

- Setting up aws creds

```
$ vim ~/.aws/credentials
```

- Add the following information with respective keys

```
[rearc]
aws_access_key_id = ""
aws_secret_access_key = ""
```
### Create Environment

```
$ conda create -n myenv
$ conda activate myenv
```

### Install dependencies in project directory

```
$ conda install
or 
$ pip install
```

### Run the jupyter notebook

```
$ jupyter notebook
```

### Reference

Refer to [AWS Docs](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
