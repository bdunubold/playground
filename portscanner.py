

"""
port scanner

-host=localhost -port=5000
Scanning host: localhost port: 5000
Port: 5000 is open

"""

import click
import socket
@click.command()
@click.option("-host")
@click.option("-port")
def port_scanner(host, port):
    click.echo(f"scanning host: {host} port: {port}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, int(port)))
    status = "open" if result == 0 else "not open"
    msg = f"Port: {port} is {status}"
    click.echo(msg)

if __name__ == "__main__":
    port_scanner()