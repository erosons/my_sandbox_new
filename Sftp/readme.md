pip install mocksftp

mocksftp - Easily test your sftp client code
In-process SFTP server for testing your SFTP related client code.

Usage example
For pytest, use the sftp_server and sftp_client fixtures:

from contextlib import closing
import py.path


def test_open_file(sftp_server, sftp_client):
    # Write directly in the server root.
    root_path = py.path.local(sftp_server.root)
    root_path.join('file.txt').write('content')

    # Access the folder via the client
    sftp = sftp_client.open_sftp()
    assert sftp.listdir('.') == ['file.txt']

    with closing(sftp.open('file.txt', 'r')) as data:
        assert data.read() == b'content'