from flask import Flask
from flask import request
from time import strftime

from services.games import *

# CloudWatch - Imports
import watchtower
import logging

# Honeycomb - Imports
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Honeycomb - Initialize Tracing
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Initialize Flask App
app = Flask(__name__)

# CloudWatch - Configuration
#TODO: get log_group from flask config
console_handler = logging.StreamHandler()
cloudwatch_handler = watchtower.CloudWatchLogHandler(log_group='nba-squeeze-api')
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cloudwatch_handler)

# Honeycomb - Instrumentation
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route("/api/games", methods=['GET'])
def data_games():
    data = Games.run()
    return data, 200

@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%m-%d %H:%M]')
    LOGGER.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

if __name__ == "__main__":
    app.run(debug=True)