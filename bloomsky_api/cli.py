import click
import json

from .bloomsky_api import BloomSkyAPIClient

@click.command(help='Retrieve data from the BloomSky API and output it as JSON.')
@click.option('--api-key', envvar='BLOOMSKY_API_KEY',
        help='BloomSky API key (can be set via env var BLOOMSKY_API_KEY).')
@click.option('--api-url', help='Override BloomSky API endpoint URL.')
@click.option('--json-indent', type=int, default=None,
help='Number of spaces to indent nested JSON levels.')
def cli(api_key, api_url, json_indent):
    client = BloomSkyAPIClient(api_key=api_key, api_url=api_url)
    data = client.get_data()
    click.echo(json.dumps(data, indent=json_indent))

if __name__ == '__main__':
    cli()
