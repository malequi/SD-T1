import grpc
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import json


class SearchClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        #print(f'{message}')
        return self.stub.GetServerResponse(message)

def funcion(nombreproducto):
    client = SearchClient()
    result = client.get_url(message=nombreproducto)
    return(result)

#if __name__ == '__main__':
    #print(json.loads(str(funcion("cpu"))))
    #client = SearchClient()
    #result = client.get_url(message="cpu")
    #print(result.product[0].name + "*******")
    #print(f'{result}')
