from flask import Flask

from services.games import *

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

# Honeycomb - Instrumentation
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route("/api/games", methods=['GET'])
def data_games():
    data = Games.run()
    return data, 200

if __name__ == "__main__":
    app.run(debug=True)