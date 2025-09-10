from flask import Flask
import logging
""" from azure.monitor.opentelemetry import configure_azure_monitor

configure_azure_monitor(connection_string="InstrumentationKey=f36037ba-2352-4962-bc52-643c2ef91d14;IngestionEndpoint=https://centralindia-0.in.applicationinsights.azure.com/;LiveEndpoint=https://centralindia.livediagnostics.monitor.azure.com/;ApplicationId=4d3c3dd2-f143-4011-82ea-46c0045326f5",
                        enable_live_metrics=True) """

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is a demo endpoint'


@app.route('/demoerror')
def demoerror():
    raise ValueError('A very specific bad thing happened.')
    #return 'This endpoint will throw an error'

if __name__ == '__main__':
    app.run(debug=True) 