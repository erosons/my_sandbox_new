{
  "Comment": "A state machine that triggers an AWS Glue job",
  "StartAt": "StartGlueJob",
  "States": {
    "StartGlueJob": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun.sync",
      "Parameters": {
        "JobName": "YourGlueJobName"
      },
      "Next": "CheckGlueJobStatus"
    },
    "CheckGlueJobStatus": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.JobRunState",
          "StringEquals": "SUCCEEDED",
          "Next": "SuccessState"
        },
        {
          "Variable": "$.JobRunState",
          "StringEquals": "FAILED",
          "Next": "FailState"
        }
      ],
      "Default": "WaitState"
    },
    "WaitState": {
      "Type": "Wait",
      "Seconds": 30,
      "Next": "GetGlueJobStatus"
    },
    "GetGlueJobStatus": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:getJobRun",
      "Parameters": {
        "JobName": "YourGlueJobName",
        "RunId.$": "$.JobRunId"
      },
      "Next": "CheckGlueJobStatus"
    },
    "SuccessState": {
      "Type": "Succeed"
    },
    "FailState": {
      "Type": "Fail"
    }
  }
}
