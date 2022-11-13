export type AmplifyDependentResourcesAttributes = {
    "function": {
        "pharmavuec5407e92": {
            "Name": "string",
            "Arn": "string",
            "Region": "string",
            "LambdaExecutionRole": "string"
        },
        "pharmavueproxy": {
            "Name": "string",
            "Arn": "string",
            "Region": "string",
            "LambdaExecutionRole": "string"
        }
    },
    "auth": {
        "pharmavue": {
            "IdentityPoolId": "string",
            "IdentityPoolName": "string",
            "UserPoolId": "string",
            "UserPoolArn": "string",
            "UserPoolName": "string",
            "AppClientIDWeb": "string",
            "AppClientID": "string"
        }
    },
    "api": {
        "pharmaRest": {
            "RootUrl": "string",
            "ApiName": "string",
            "ApiId": "string"
        }
    }
}