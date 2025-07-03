# aiokafka==0.10.0
# aws-msk-iam-sasl-signer-python==1.0.1

import asyncio
import os, sys
from aiokafka import AIOKafkaConsumer
from aiokafka.abc import AbstractTokenProvider
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider
import ssl

def create_ssl_context():
    _ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    _ssl_context.options |= ssl.OP_NO_SSLv2
    _ssl_context.options |= ssl.OP_NO_SSLv3
    _ssl_context.check_hostname = False
    _ssl_context.verify_mode = ssl.CERT_NONE
    _ssl_context.load_default_certs()

    return _ssl_context

class AWSTokenProvider(AbstractTokenProvider):
    """
    Returns a token which used OAuth along the Access credentials.
    """
    async def token(self):
        return await asyncio.get_running_loop().run_in_executor(None, self._token)

    def _token(self):
        AWS_REGION = AWS_REGION = 'us-east-1'
        token, _ = MSKAuthTokenProvider.generate_auth_token(AWS_REGION)
        return token

async def consume():
    KAFKA_TOPIC = "awskafkatopic1"
    #KAFKA_GROUP_ID = os.getenv('KAFKA_GROUP_ID', 'demo-group')
    KAFKA_SERVER = 'b-3.democluster1.olzziq.c18.kafka.us-east-1.amazonaws.com:9098'

    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        #group_id=KAFKA_GROUP_ID,
        security_protocol='SASL_SSL',
        ssl_context=create_ssl_context(),
        sasl_mechanism="OAUTHBEARER",
        sasl_oauth_token_provider=AWSTokenProvider()
    )

    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


def main():
    try:
        asyncio.run(consume())
    except KeyboardInterrupt:
        print("Bye!")
        sys.exit(0)


if __name__ == "__main__":
    main()