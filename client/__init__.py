#!python3

"""
Very simple HTTP server in python

"""

from http.server import BaseHTTPRequestHandler
import json

# Server Configuration
HOST_NAME = '0.0.0.0'
HOST_NAME_TEST = HOST_NAME
PORT_NUMBER = 8080
PORT_NUMBER_TEST = PORT_NUMBER + 10


class ServerHandler(BaseHTTPRequestHandler):

    def __write_response(self, body_html_, code):
        self.send_response(code)
        self.end_headers()
        self.wfile.write(body_html_.encode("utf_8"))

    def __get_object(self):
        length = int(self.headers['content-length'])
        content = self.rfile.read(length).decode("utf-8")
        return json.loads(content)

    def __feedback(self):
        object = self.__get_object()

        print("LOG in Feedback >> " , object)
        self.__write_response(json.dumps(object), 204)
        return object

    def __your_path(self):
        object = self.__get_object()

        # log
        print("LOG in PATH >> " , object)
        # Only for test
        #total = calculate(object)
        self.__write_response((json.dumps({'total': 1000})), 200)

    def do_GET(self):
        self.__write_response('hello world', 200)

    def respondOrder(self, body_html_, code):
        taxes = []

        # 1. explode js

        # 2. mutliply qty and price

        # 3. apply taxes

        ## Taxes
        tax_rates = {
            "DE": 0.20,  # Germany
            "UK": 0.21,  # United Kingdom
            "FR": 0.20,  # France
            "IT": 0.25,  # Italy
            "ES": 0.19,  # Spain
            "PL": 0.21,  # Poland
            "RO": 0.20,  # Romania
            "NL": 0.20,  # Netherlands
            "BE": 0.24,  # Belgium
            "EL": 0.20,  # Greece
            "CZ": 0.19,  # Czech Republic
            "PT": 0.23,  # Portugal
            "HU": 0.27,  # Hungary
            "SE": 0.23,  # Sweden
            "AT": 0.22,  # Austria
            "BG": 0.21,  # Bulgaria
            "DK": 0.21,  # Denmark
            "FI": 0.17,  # Finland
            "SK": 0.18,  # Slovakia
            "IE": 0.21,  # Ireland
            "HR": 0.23,  # Croatia
            "LT": 0.23,  # Lithuania
            "SI": 0.24,  # Slovenia
            "LV": 0.20,  # Latvia
            "EE": 0.22,  # Estonia
            "CY": 0.21,  # Cyprus
            "LU": 0.25,  # Luxembourg
            "MT": 0.20   # Malta
        }

        def reduction(type,money):
            if type == "STANDARD":
                if money >= 50000:
                    money = money * 0.85
                elif money >= 10000:
                    money = money * 0.9
                elif money >= 7000:
                    money = money * 0.93
                elif money >= 5000:
                    money = money * 0.95
                elif money >= 1000:
                    money = money * 0.97
                else:
                    money = money
            else: 
                money = 0
            return money

        x = '{"prices":[15.99,2],"quantities":[1,2],"country":"ES","reduction":"STANDARD"}'
        y = json.loads(x)
        taxd_total = 0

        for x in range(len(y["prices"] )):
            taxed = y["prices"][x] * y["quantities"][x] 
            taxed = taxed + taxed * tax_rates[y["country"]]
            taxed = reduction(y["reduction"],taxed)
            taxd_total = taxd_total + taxed
    
        print(taxd_total)



        # 4. create response formated json

        # 5. send response



    def do_POST(self):
        {
            '/ping': lambda: self.__write_response('pong', 200),
            '/feedback': self.__feedback,
            '/path': self.__your_path,
            #'/order': self.__

        }.get(self.path, lambda: self.__write_response('Unknown', 404))()


def start_server(testMode=False):
    global server
    from http.server import HTTPServer

    if testMode:
        host_name = HOST_NAME_TEST
        port_number = PORT_NUMBER_TEST
    else:
        host_name = HOST_NAME
        port_number = PORT_NUMBER

    server = HTTPServer((host_name, port_number), ServerHandler)
    print('Starting server %s:%s use <Ctrl-C> to stop' % (host_name, port_number))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
    print('Server interrupted')


def shutdown_server():
    global server
    server.server_close()
    print('Shutdown server %s:%s ' % (HOST_NAME, PORT_NUMBER))

if __name__ == '__main__':
    start_server()
