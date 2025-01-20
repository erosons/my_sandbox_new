from Engineering.aws_developer_assoc.core.aws_Glue.awsGlue_jobs import glueConn
import logging
import json


logging.basicConfig(filename='new.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def job_devEndpoint():
    logging.info("creating a pyspark endpoint")
    try:
        response = glueConn.create_dev_endpoint(
            EndpointName='marwen_Analytics',
            RoleArn='',
            # NumberOfNodes=4,
            WorkerType='Standard',
            GlueVersion='1.0',
            NumberOfWorkers=2,

        )
        print(json.dumps(response, indent=4, sort_keys=True, default=str))

    except glueConn.exceptions.InvalidInputException:
        logging.debug("The input provided was not valid.")
    except glueConn.exceptions.AlreadyExistsException:
        logging.debug("A resource to be created or added already exists")
    except glueConn.exceptions.OperationTimeoutException:
        logging.debug("Operation could not be completed,operation timed out.")
    except glueConn.exceptions.ResourceNumberLimitExceededException:
        logging.debug("A resource numerical limit was exceeded..")
    except glueConn.exceptions.AccessDeniedException:
        logging.debug("A credentials errors, check access keys and secrets..")
    except glueConn.exceptions.InternalServiceException:
        logging.debug("AWS internal sevices error..")
    except glueConn.exceptions.ValidationException:
        logging.debug("A credentials could not be validated")


if __name__ == "__main__":
    job_devEndpoint()
