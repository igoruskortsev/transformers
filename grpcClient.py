import grpc
import MessageService_pb2_grpc
import MessageService_pb2

def run():
    with grpc.insecure_channel('localhost:8086') as channel:
        stub = MessageService_pb2_grpc.MessageServiceStub(channel)

        response = stub.sendMessage(MessageService_pb2.MessageRequest(text = 'Hi!!!'))

    print('answer')
    print(response)

run()