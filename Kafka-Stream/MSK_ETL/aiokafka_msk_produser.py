import asyncio
from aiokafka import AIOKafkaProducer
from aiokafka.abc import AbstractTokenProvider
import os
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
    async def token(self):
        return await asyncio.get_running_loop().run_in_executor(None, self._token)

    def _token(self):
        # AWS_REGION = os.getenv('AWS_REGION')
        AWS_REGION = 'us-east-1'
        token, _ = MSKAuthTokenProvider.generate_auth_token(AWS_REGION)
        return token
tp =AWSTokenProvider()

async def produce():
    # Create Kafka producer
    producer = AIOKafkaProducer(
        bootstrap_servers='b-3.democluster1.olzziq.c18.kafka.us-east-1.amazonaws.com:9098',
        security_protocol="SASL_SSL",
        ssl_context=create_ssl_context(),
        sasl_mechanism="OAUTHBEARER",
        sasl_oauth_token_provider=tp,
        client_id="my-client-id",
        api_version="0.11.5"
    )

    # Start the producer
    await producer.start()
    try:
        # Produce messages
        for i in range(10):
            value = f"message-{i}".encode('utf-8')
            await producer.send_and_wait("awskafkatopic1", value=value)
            print(f"Produced: {value.decode('utf-8')}")
    finally:
        # Stop the producer
        await producer.stop()

# To run the produce function
if __name__ == "__main__":
    asyncio.run(produce())